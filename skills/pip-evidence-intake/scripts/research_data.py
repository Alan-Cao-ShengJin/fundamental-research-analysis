"""Bounded read-only research-provider retrieval; credentials never enter receipts."""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import re
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

ROOT = Path(__file__).resolve().parents[3]
CATALOG_PATH = Path(__file__).resolve().parents[1] / "assets" / "provider-endpoints.json"
KEY_NAMES = {
    "alphapai": "ALPHAPAI_API_KEY", "alphavantage": "ALPHAVANTAGE_API_KEY",
    "api-ninjas": "API_NINJAS_API_KEY", "massive": "MASSIVE_API_KEY",
}
SECRET_FIELDS = {"apikey", "api_key", "api-key", "key", "app-agent", "authorization", "x-api-key", "token"}
MAX_BYTES = 10_000_000


def endpoint_catalog(provider):
    return {entry["operation"]: entry for entry in json.loads(CATALOG_PATH.read_text(encoding="utf-8"))["endpoints"]
            if entry["provider"] == provider}


def catalog_request(args, key):
    entry = endpoint_catalog(args.provider).get(args.operation)
    if entry is None:
        if getattr(args, "param", None): raise ValueError("--param is supported only for catalog operations")
        return None
    values = dict(entry["defaults"])
    for item in getattr(args, "param", None) or []:
        name, separator, value = item.partition("=")
        if not separator or name not in entry["allowed_params"] or name.lower() in SECRET_FIELDS or name == "function":
            raise ValueError("Parameter is not allowed for this read-only endpoint")
        try: values[name] = json.loads(value)
        except ValueError: values[name] = value
    endpoint = entry["endpoint"]
    if "{symbol}" in endpoint:
        if not args.symbol or not re.fullmatch(r"[A-Za-z0-9._:-]{1,40}", args.symbol):
            raise ValueError("Operation requires a valid --symbol")
        endpoint = endpoint.replace("{symbol}", args.symbol)
    if entry.get("symbol_parameter"):
        if not args.symbol: raise ValueError("Operation requires --symbol")
        values[entry["symbol_parameter"]] = args.symbol
    for name in ("limit", "pageSize", "topk"):
        if name in values and (not isinstance(values[name], int) or isinstance(values[name], bool) or not 1 <= values[name] <= 100):
            raise ValueError("Bounded retrieval requires limit/pageSize/topk between 1 and 100")
    for name in entry.get("required_params", []):
        if name not in values or values[name] in (None, "", []): raise ValueError("Missing required catalog parameter: " + name)
    for names in entry.get("required_any", []):
        if not any(values.get(name) not in (None, "", []) for name in names):
            raise ValueError("Operation requires one of: " + ", ".join(names))
    for name in entry.get("path_parameters", []):
        value = str(values.get(name, ""))
        if not re.fullmatch(r"[A-Za-z0-9._:-]{1,40}", value):
            raise ValueError("Path parameters must be simple identifiers or dates")
        endpoint = endpoint.replace("{" + name + "}", value)
    base = {"alphapai": "https://open-api.rabyte.cn", "alphavantage": "https://www.alphavantage.co",
            "api-ninjas": "https://api.api-ninjas.com", "massive": "https://api.massive.com"}[args.provider]
    headers = {"User-Agent": "PipResearch/1.0", "Accept": "application/json"}
    public_values = dict(values)
    for name in entry.get("path_parameters", []): values.pop(name, None)
    body = None
    if args.provider == "alphapai": headers["app-agent"] = key
    elif args.provider == "api-ninjas": headers["X-Api-Key"] = key
    else: values["apikey" if args.provider == "alphavantage" else "apiKey"] = key
    if entry["method"] == "POST":
        headers["Content-Type"] = "application/json; charset=utf-8"
        body = json.dumps(values, ensure_ascii=False).encode("utf-8")
        query = ""
    else:
        query = "?" + urlencode(values, doseq=True) if values else ""
    return Request(base + endpoint + query, data=body, headers=headers), endpoint, public_values


class SameOriginRedirect(HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, msg, headers, new_url):
        old, new = urlsplit(request.full_url), urlsplit(new_url)
        if (old.scheme, old.netloc) != (new.scheme, new.netloc):
            raise URLError("Cross-origin redirect blocked")
        return super().redirect_request(request, fp, code, msg, headers, new_url)


def credentials(path: Path) -> dict[str, str]:
    result = {}
    if path.exists():
        for line in path.read_text(encoding="utf-8-sig").splitlines():
            if line.strip() and not line.lstrip().startswith("#") and "=" in line:
                name, value = line.split("=", 1)
                if name.strip() in KEY_NAMES.values():
                    result[name.strip()] = value.strip().strip("\"'")
    for name in KEY_NAMES.values():
        if os.environ.get(name):
            result[name] = os.environ[name]
    return result


def redact(value, secrets):
    if isinstance(value, dict):
        return {k: "[REDACTED]" if k.lower() in SECRET_FIELDS else redact(v, secrets)
                for k, v in value.items()}
    if isinstance(value, list):
        return [redact(v, secrets) for v in value]
    if isinstance(value, str):
        for secret in secrets:
            if secret:
                value = value.replace(secret, "[REDACTED]")
        return re.sub(r"(?i)([?&](?:apikey|api_key|token)=)[^&\s\"<>]+", r"\1[REDACTED]", value)
    return value


def normalize_restricted_fields(value, path=""):
    """Preserve raw provenance separately; restricted field notices are not data."""
    restricted = []
    if isinstance(value, str) and is_restricted_notice(value):
        return None, [path]
    if isinstance(value, dict):
        result = {}
        for key, item in value.items():
            if key.lower() in ("message", "error", "note"):
                result[key] = item
                continue
            result[key], missing = normalize_restricted_fields(item, f"{path}.{key}".lstrip("."))
            restricted.extend(missing)
        return result, restricted
    if isinstance(value, list):
        result = []
        for index, item in enumerate(value):
            normalized, missing = normalize_restricted_fields(item, f"{path}[{index}]")
            result.append(normalized)
            restricted.extend(missing)
        return result, restricted
    return value, restricted


def is_restricted_notice(value):
    if not isinstance(value, str): return False
    lower = value.strip().lower()
    return (lower.startswith(("this field ", "this data ", "performance data is available")) and
            any(term in lower for term in ("premium", "business and professional", "subscribers only"))) or bool(
                re.match(r"^[a-z_]+ is reserved for premium subscribers only", lower))


def has_usable_partial_data(payload):
    if not isinstance(payload, dict) or payload.get("error"): return False
    metadata = {"message", "msg", "status", "code", "request_id", "ticker", "symbol", "name", "company_name", "cik"}
    for key, value in payload.items():
        if key.lower() in metadata or value in (None, "", [], {}) or is_restricted_notice(value): continue
        if isinstance(value, (dict, list, int, float)) and not isinstance(value, bool): return True
    return False


def response_status(provider, http_status, payload):
    """HTTP success does not establish provider/business success or entitlement."""
    if isinstance(payload, dict):
        message = str(payload.get("error") or payload.get("Error Message") or
                      payload.get("Information") or payload.get("Note") or
                      payload.get("message") or payload.get("msg") or "")
    else:
        message = ""
    lower = message.lower()
    if http_status == 429 or any(x in lower for x in ("rate limit", "call frequency", "requests per day")):
        return "rate_limited", message
    if any(x in lower for x in ("premium", "subscription", "not entitled", "not_entitled", "plan does not", "upgrade",
                                "没有对应研报的权限", "无权限", "权限不足")):
        if http_status < 400 and has_usable_partial_data(payload): return "partial", message
        return "not_entitled", message
    if http_status == 401 or any(x in lower for x in ("invalid api key", "invalid api-key", "unauthorized")):
        return "auth_error", message
    if http_status == 403:
        return "access_denied", message
    if http_status >= 400:
        return "http_error", message
    if provider == "alphapai" and (not isinstance(payload, dict) or payload.get("code") != 200000):
        return "provider_error", message
    if isinstance(payload, dict) and any(k in payload for k in ("error", "Error Message", "Information", "Note")):
        return "provider_error", message
    if isinstance(payload, dict) and str(payload.get("status", "")).upper() in ("ERROR", "NOT_AUTHORIZED", "DENIED"):
        return "provider_error", message
    if provider == "alphavantage" and isinstance(payload, dict) and "transcript" in payload and not payload["transcript"]:
        return "no_data", message
    data = payload.get("data", payload.get("results", payload)) if isinstance(payload, dict) else payload
    if data in (None, [], {}):
        return "no_data", message
    if isinstance(data, dict) and "data" in data and data["data"] == []:
        return "no_data", message
    return "ok", message


def build_request(args, key):
    catalog = catalog_request(args, key)
    if catalog is not None: return catalog
    provider, operation = args.provider, args.operation
    headers = {"User-Agent": "PipResearch/1.0", "Accept": "application/json"}
    params, body = {}, None
    symbol = args.symbol
    if provider == "alphapai":
        base = "https://open-api.rabyte.cn"
        headers.update({"app-agent": key, "Content-Type": "application/json; charset=utf-8"})
        if operation == "health":
            endpoint, body = "/alpha/open-api/v1/sync/auth/hello", {}
        elif operation == "meetings":
            endpoint = "/alpha/open-api/v1/summary/list"
            body = {"meetingMarketType": args.market, "pageNum": args.page, "pageSize": args.limit}
            if symbol: body["stockCombSymbol"] = [symbol]
            if args.keyword: body["keyword"] = args.keyword
            if args.start: body["beginTime"] = args.start + " 00:00:00"
            if args.end: body["endTime"] = args.end + " 23:59:59"
            if args.content_type: body["meetingContentType"] = args.content_type
            if args.executive_attended: body["meetingTag"] = ["executive_attended"]
        elif operation == "meeting":
            if not args.roadshow_id: raise ValueError("meeting requires --roadshow-id from a fresh list response")
            endpoint = "/alpha/open-api/v1/summary/detail"
            body = {"roadshowId": args.roadshow_id, "noteType": args.note_type}
        else: raise ValueError("AlphaPai operations: health, meetings, meeting")
    elif provider == "alphavantage":
        base, endpoint = "https://www.alphavantage.co", "/query"
        if operation == "transcript":
            if not symbol or not args.year or not args.quarter: raise ValueError("transcript requires --symbol, --year and --quarter")
            params = {"function": "EARNINGS_CALL_TRANSCRIPT", "symbol": symbol, "quarter": f"{args.year}Q{args.quarter}"}
        elif operation == "calendar":
            params = {"function": "EARNINGS_CALENDAR", "horizon": "3month"}
            if symbol: params["symbol"] = symbol
        else: raise ValueError("Alpha Vantage operations: transcript, calendar")
        params["apikey"] = key
    elif provider == "api-ninjas":
        base = "https://api.api-ninjas.com"
        headers["X-Api-Key"] = key
        routes = {"transcript": "/v1/earningstranscript", "transcript-search": "/v1/earningstranscriptsearch", "calendar": "/v1/earningscalendar"}
        if operation not in routes: raise ValueError("API Ninjas operations: transcript, transcript-search, calendar")
        if not symbol: raise ValueError("operation requires --symbol")
        endpoint, params = routes[operation], {"ticker": symbol}
        if operation == "transcript":
            if bool(args.year) != bool(args.quarter): raise ValueError("--year and --quarter must be supplied together")
            if args.year: params.update(year=args.year, quarter=args.quarter)
        if operation == "transcript-search":
            params["limit"] = args.limit
            if args.start: params["start_date"] = args.start
            if args.end: params["end_date"] = args.end
    else:
        base = "https://api.massive.com"
        if not symbol: raise ValueError("operation requires --symbol")
        routes = {"earnings": "/benzinga/v1/earnings", "guidance": "/benzinga/v1/guidance", "ticker": "/v3/reference/tickers/" + symbol}
        if operation not in routes: raise ValueError("Massive operations: ticker, earnings, guidance; no transcript endpoint is assumed")
        endpoint = routes[operation]
        params = {} if operation == "ticker" else {"ticker": symbol, "limit": args.limit, "sort": "date.desc"}
        if operation != "ticker":
            if args.start: params["date.gte"] = args.start
            if args.end: params["date.lte"] = args.end
        params["apiKey"] = key
    if body is not None:
        content = json.dumps(body, ensure_ascii=False).encode("utf-8")
    else:
        content = None
    public_params = {k: v for k, v in params.items() if k.lower() not in SECRET_FIELDS}
    request = Request(base + endpoint + ("?" + urlencode(params) if params else ""), data=content, headers=headers)
    return request, endpoint, body if body is not None else public_params


def fetch(args):
    keys = credentials(Path(args.secrets_file))
    key = keys.get(KEY_NAMES[args.provider])
    if not key: raise ValueError("Provider credential is not configured")
    request, endpoint, parameters = build_request(args, key)
    try:
        with build_opener(SameOriginRedirect()).open(request, timeout=args.timeout) as response:
            raw, status = response.read(MAX_BYTES + 1), response.status
    except HTTPError as error:
        raw, status = error.read(MAX_BYTES + 1), error.code
    except (URLError, TimeoutError, OSError) as error:
        return {"provider": args.provider, "operation": args.operation, "status": "network_error", "error_type": type(error).__name__}
    if len(raw) > MAX_BYTES: raise ValueError("Response exceeds the bounded retrieval size; narrow the query")
    text = raw.decode("utf-8-sig", errors="replace")
    document_text = False
    try:
        payload = json.loads(text)
    except ValueError:
        if args.provider == "alphavantage" and args.operation in ("calendar", "listing-status") and text.lstrip().startswith("symbol,"):
            payload = list(csv.DictReader(io.StringIO(text)))
        elif args.provider == "alphapai" and args.operation == "document-text" and status < 400 and text.strip() and not text.lstrip().lower().startswith(("<!doctype", "<html", "%pdf")):
            payload = {"content": text, "format": "markdown"}
            document_text = True
        else:
            payload = {"error": "Provider returned non-JSON/non-calendar content"}
    state, message = ("ok", "") if document_text else response_status(args.provider, status, payload)
    safe_payload = redact(payload, keys.values())
    normalized, restricted = normalize_restricted_fields(safe_payload)
    if state == "ok" and restricted:
        state = "partial"
    now = datetime.now(timezone.utc).isoformat()
    envelope = {"provider": args.provider, "operation": args.operation, "endpoint": endpoint,
                "parameters": redact(parameters, keys.values()), "retrieved_at": now,
                "http_status": status, "status": state, "message": redact(message, keys.values()),
                "response_sha256": hashlib.sha256(raw).hexdigest(),
                "redaction_applied": safe_payload != payload, "response": safe_payload}
    if restricted:
        envelope.update(normalized_response=normalized, restricted_fields=restricted)
    path = Path(args.output) if args.output else ROOT / ".data" / "research-data" / f"{args.provider}-{args.operation}-{uuid.uuid4().hex[:12]}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(envelope, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    data = safe_payload.get("data", safe_payload.get("results", safe_payload)) if isinstance(safe_payload, dict) else safe_payload
    count = len(data) if isinstance(data, list) else len(data.get("data", [])) if isinstance(data, dict) and isinstance(data.get("data"), list) else None
    return {"provider": args.provider, "operation": args.operation, "status": state, "http_status": status,
            "message": redact(message, keys.values())[:350], "records": count,
            "restricted_field_count": len(restricted), "output": str(path)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("provider", choices=KEY_NAMES)
    parser.add_argument("operation")
    parser.add_argument("--symbol")
    parser.add_argument("--param", action="append", help="Allowed catalog parameter NAME=VALUE; JSON values are accepted")
    parser.add_argument("--year", type=int)
    parser.add_argument("--quarter", type=int, choices=range(1, 5))
    parser.add_argument("--market", choices=["A", "HK", "US"], default="A")
    parser.add_argument("--keyword")
    parser.add_argument("--content-type", nargs="+", choices=["company_communication", "performance_meeting", "expert_communication", "company_analysis", "industry_analysis", "conference", "fund_manager_view"])
    parser.add_argument("--executive-attended", action="store_true")
    parser.add_argument("--roadshow-id")
    parser.add_argument("--note-type", choices=["asr_note", "ai_note"], default="asr_note")
    parser.add_argument("--start")
    parser.add_argument("--end")
    parser.add_argument("--page", type=int, default=1)
    parser.add_argument("--limit", type=int, default=3)
    parser.add_argument("--timeout", type=int, default=25)
    parser.add_argument("--output")
    parser.add_argument("--secrets-file", default=str(ROOT / ".env.research-data"))
    args = parser.parse_args()
    if args.operation == "catalog":
        print(json.dumps(list(endpoint_catalog(args.provider).values()), ensure_ascii=False))
        return 0
    if args.symbol and not re.fullmatch(r"[A-Za-z0-9._:-]{1,40}", args.symbol):
        parser.error("Use a ticker/share-class identifier, not a URL or path")
    if not 1 <= args.limit <= 100 or args.page < 1 or not 1 <= args.timeout <= 60:
        parser.error("Use limit 1..100, a positive page and timeout 1..60 seconds")
    for field in (args.start, args.end):
        if field:
            try: datetime.strptime(field, "%Y-%m-%d")
            except ValueError: parser.error("Dates must be YYYY-MM-DD")
    if args.start and args.end and args.start > args.end: parser.error("Start date is after end date")
    try:
        result = fetch(args)
    except ValueError as error:
        print(json.dumps({"status": "input_error", "message": str(error)}))
        return 2
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result["status"] in ("ok", "partial", "no_data") else 1


if __name__ == "__main__":
    sys.exit(main())
