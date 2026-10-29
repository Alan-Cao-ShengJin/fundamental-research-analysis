import importlib.util
import unittest
import json
import tempfile
from unittest.mock import patch
from urllib.error import URLError
from urllib.request import Request
from argparse import Namespace
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "pip-evidence-intake/scripts/research_data.py"
spec = importlib.util.spec_from_file_location("research_data", PATH)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class ProviderContractTests(unittest.TestCase):
    def test_http_200_can_be_entitlement_or_business_failure(self):
        self.assertEqual(mod.response_status("alphavantage", 200, {"Information": "Premium subscription required"})[0], "not_entitled")
        self.assertEqual(mod.response_status("alphapai", 200, {"code": 400000, "msg": "rejected"})[0], "provider_error")

    def test_auth_rate_limit_and_empty_coverage_are_distinct(self):
        self.assertEqual(mod.response_status("api-ninjas", 401, {"error": "Invalid API Key"})[0], "auth_error")
        self.assertEqual(mod.response_status("massive", 429, {"message": "slow down"})[0], "rate_limited")
        self.assertEqual(mod.response_status("alphapai", 200, {"code": 200000, "data": {"data": []}})[0], "no_data")
        self.assertEqual(mod.response_status("alphavantage", 200, {"symbol": "EXAMPLE", "quarter": "2026Q1", "transcript": []})[0], "no_data")

    def test_nested_credentials_and_echoed_urls_are_redacted(self):
        value = {"apiKey": "sensitive", "items": [{"text": "echo sensitive", "next_url": "https://example.com?apiKey=sensitive&x=1"}]}
        result = mod.redact(value, ["sensitive"])
        self.assertNotIn("sensitive", str(result))
        self.assertEqual(result["apiKey"], "[REDACTED]")
        self.assertEqual(value["apiKey"], "sensitive")

    def test_credential_does_not_enter_public_request_metadata(self):
        args = Namespace(provider="alphavantage", operation="transcript", symbol="EXAMPLE", year=2026, quarter=2)
        request, endpoint, params = mod.build_request(args, "secret-key")
        self.assertNotIn("secret-key", str(params))
        self.assertEqual(endpoint, "/query")
        self.assertIn("quarter=2026Q2", request.full_url)

    def test_undocumented_massive_transcript_route_is_not_invented(self):
        args = Namespace(provider="massive", operation="transcript", symbol="EXAMPLE")
        with self.assertRaises(ValueError): mod.build_request(args, "test-key")

    def test_authenticated_request_cannot_redirect_to_another_origin(self):
        request = Request("https://example.com/data", headers={"X-Api-Key": "test-key"})
        with self.assertRaises(URLError):
            mod.SameOriginRedirect().redirect_request(request, None, 302, "Moved", {}, "https://other.example/data")

    def test_restricted_field_notices_become_missing_not_forecast_values(self):
        raw = [{"date": "2026-09-01", "estimate": "This field is available for premium subscribers only. Please upgrade."}]
        normalized, restricted = mod.normalize_restricted_fields(raw)
        self.assertEqual(normalized, [{"date": "2026-09-01", "estimate": None}])
        self.assertEqual(restricted, ["[0].estimate"])
        self.assertIsInstance(raw[0]["estimate"], str)

    def test_real_free_plan_data_is_partial_not_denied(self):
        payload = {"executives": [{"total": 100}], "message": "Free plan. Upgrade for full history."}
        self.assertEqual(mod.response_status("api-ninjas", 200, payload)[0], "partial")
        self.assertEqual(mod.response_status("api-ninjas", 200, {"ticker": "EXAMPLE", "message": "Upgrade required"})[0], "not_entitled")
        self.assertEqual(mod.response_status("api-ninjas", 403, payload)[0], "not_entitled")
        self.assertEqual(mod.response_status("alphapai", 200, {"code": 400000, "message": "当前用户没有对应研报的权限"})[0], "not_entitled")

    def test_vendor_restriction_variants_do_not_become_model_values(self):
        notices = ["This data is for premium users only.",
                   "Performance data is available to Business and Professional tier subscribers only.",
                   "sector is reserved for premium subscribers only."]
        raw = {"values": notices, "message": "Upgrade for history"}
        normalized, restricted = mod.normalize_restricted_fields(raw)
        self.assertEqual(normalized["values"], [None] * len(notices))
        self.assertEqual(normalized["message"], raw["message"])
        self.assertEqual(len(restricted), 3)

    def test_catalog_is_unique_fixed_host_and_has_no_auth_parameter(self):
        entries = json.loads(mod.CATALOG_PATH.read_text(encoding="utf-8"))["endpoints"]
        self.assertEqual(len(entries), len({(x["provider"], x["operation"]) for x in entries}))
        for entry in entries:
            self.assertTrue(entry["endpoint"].startswith("/"))
            self.assertNotIn("://", entry["endpoint"])
            self.assertIn(entry["method"], ("GET", "POST"))
            self.assertFalse(mod.SECRET_FIELDS.intersection(k.lower() for k in entry["allowed_params"]))

    def test_catalog_rejects_auth_function_and_unknown_overrides(self):
        for parameter in ("apikey=other", "function=OTHER", "url=https://other.example", "unknown=1"):
            args = Namespace(provider="alphavantage", operation="income-statement", symbol="EXAMPLE", param=[parameter])
            with self.assertRaises(ValueError): mod.build_request(args, "private-key")

    def test_catalog_required_fields_bounds_and_path_injection(self):
        cases = [("alphapai", "report-detail", None, []),
                 ("api-ninjas", "institutionalholdings", None, []),
                 ("massive", "news", None, ["limit=101"]),
                 ("massive", "news", None, ["limit=true"]),
                 ("massive", "daily-bars", "EXAMPLE", ["from=../../secret", "to=2026-01-02"]),
                 ("massive", "previous-day-bar", "../../secret", [])]
        for provider, operation, symbol, params in cases:
            args = Namespace(provider=provider, operation=operation, symbol=symbol, param=params)
            with self.assertRaises(ValueError): mod.build_request(args, "private-key")
        args = Namespace(provider="api-ninjas", operation="institutionalholdings", symbol=None, param=["manager_name=Example Manager"])
        _, _, metadata = mod.build_request(args, "private-key")
        self.assertEqual(metadata["manager_name"], "Example Manager")
        self.assertNotIn("cik", metadata)

    def test_catalog_paths_keep_public_provenance_without_credentials(self):
        args = Namespace(provider="massive", operation="daily-bars", symbol="EXAMPLE",
                         param=["from=2026-01-01", "to=2026-01-02", "limit=2"])
        request, endpoint, metadata = mod.build_request(args, "private-key")
        self.assertEqual(endpoint, "/v2/aggs/ticker/EXAMPLE/range/1/day/2026-01-01/2026-01-02")
        self.assertEqual(metadata["from"], "2026-01-01")
        self.assertNotIn("from=", request.full_url)
        self.assertNotIn("private-key", str(metadata))

    def test_chinese_query_has_utf8_bytes_and_public_source_parameters(self):
        args = Namespace(provider="alphapai", operation="recall", symbol=None,
                         param=["query=营业收入", 'recallType=["ann"]'])
        request, _, metadata = mod.build_request(args, "private-key")
        self.assertEqual(json.loads(request.data.decode("utf-8"))["query"], "营业收入")
        self.assertEqual(metadata["query"], "营业收入")
        self.assertNotIn("private-key", str(metadata))

    def test_document_download_text_and_json_error_are_distinct(self):
        class FakeResponse:
            status = 200
            def __init__(self, content): self.content = content
            def __enter__(self): return self
            def __exit__(self, *args): pass
            def read(self, maximum): return self.content[:maximum]
        with tempfile.TemporaryDirectory() as folder:
            args = Namespace(provider="alphapai", operation="document-text", symbol=None,
                             param=["documentId=sample", "documentType=announcement"],
                             secrets_file=str(Path(folder) / "missing"), output=str(Path(folder) / "result.json"), timeout=2)
            for content, expected in [("# 原文\n营业收入".encode("utf-8"), "ok"),
                                      (b'{"code":400000,"message":"rejected"}', "provider_error"),
                                      (b"<html>Error</html>", "provider_error")]:
                with patch.object(mod, "credentials", return_value={"ALPHAPAI_API_KEY": "private-key"}), \
                     patch.object(mod, "build_opener") as opener:
                    opener.return_value.open.return_value = FakeResponse(content)
                    result = mod.fetch(args)
                self.assertEqual(result["status"], expected)
                saved = json.loads(Path(args.output).read_text(encoding="utf-8"))
                self.assertNotIn("private-key", json.dumps(saved))


if __name__ == "__main__":
    unittest.main()
