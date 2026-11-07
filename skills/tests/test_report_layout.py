"""Synthetic checks for report provenance, financial display math and portable charts."""
import importlib.util
from pathlib import Path
import re
import unittest
import xml.etree.ElementTree as ET

SCRIPT = Path(__file__).resolve().parents[1] / 'report-layout/scripts/report_layout.py'
spec = importlib.util.spec_from_file_location('report_layout', SCRIPT)
rl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rl)


SOURCES = [('syn', 'Synthetic publisher', 'Synthetic title', 'Example date', '')]


def report(account_for_questions=True):
    r = rl.Report(company='Example <synthetic>', ticker='EXAMPLE', report='Test', date='Example date')
    r.sources(SOURCES)
    if account_for_questions:
        for question in rl.QUESTIONS:
            r.omit(question, 'This isolated synthetic renderer test does not perform company research.')
    return r


def arg(point='Invented point.', segment=None, evidence='Invented evidence{{src:syn}}.'):
    return rl.Argument(point, evidence, 'Invented inference.', 'Invented implication.', segment=segment)


def debate():
    return rl.Debate('Synthetic question?',
                     [('Claim one', 'Evidence one{{src:syn}}', 'supported'), ('Claim two', 'Evidence two{{src:syn}}', 'untested')],
                     'Our invented answer.', 'It moves margin by 1 point.', 'Settled by the 1Q update in April 2027.')


class ReportLayoutTests(unittest.TestCase):
    def test_debate_is_one_normal_flow_item_and_numeric_tables_have_a_supported_class(self):
        root = ET.fromstring(str(debate()))
        self.assertEqual(root.tag, 'div')
        self.assertEqual([child.tag for child in root], ['h3', 'table', 'p'])
        self.assertIn('class="num', str(rl.table(['Metric', 'Value'], [['EPS', '5.2']], cls='num')))
        self.assertIn('class="numeric"', str(rl.table(['Metric', 'Value'], [['EPS', '5.2']])))
        with self.assertRaisesRegex(ValueError, 'Unknown table class'):
            rl.table(['A'], [['B']], cls='silently-unstyled')

    def test_initiation_has_model_linked_summary_statements(self):
        r = report(); r.report = 'Initiation of coverage'
        with self.assertRaisesRegex(ValueError, 'financial_summary'):
            r.html()
        r.financial_summary('USD m', ['FY2025A', 'FY2026E'], 1,
                            [('Income statement', [('Revenue', ['100', '110'], '')]),
                             ('Balance sheet', [('Assets', ['200', '215'], '')]),
                             ('Cash flow', [('Operating cash', ['20', '22'], '')])], 'Synthetic fixture')
        self.assertIn('data-financial-summary="true"', r.html())
        self.assertIn('splittable', r.summary_html)
        self.assertNotIn('financial-summary', r.uncited_exhibits)
        with self.assertRaisesRegex(ValueError, 'three nonempty'):
            r.financial_summary('USD m', ['FY2025A', 'FY2026E'], 1,
                                [('Income statement', [('Revenue', ['100', '110'], '')])], 'Synthetic fixture')
        with self.assertRaisesRegex(ValueError, 'match the declared periods'):
            rl.fin_table('USD m', ['FY2025A', 'FY2026E'], 1, [('Cash', [('CFO', ['100'], '')])])

    def test_close_price_events_are_separated_and_front_chart_adapts_font_size(self):
        dates = [f'2026-01-{i:02d}' for i in range(1, 29)]
        chart = rl.price_chart('Synthetic price', dates, [('Company', [100+i for i in range(28)], rl.TEAL)],
                               [('2026-01-20', 'Event A'), ('2026-01-21', 'Event B'), ('2026-01-22', 'Event C')])
        def labels(svg):
            return {e.text: e.attrib for e in ET.fromstring(str(svg)).iter() if e.tag.endswith('text') and e.text in ('Event A', 'Event B', 'Event C')}
        normal, narrow = labels(chart), labels(chart.narrow())
        self.assertEqual(len(set(a['y'] for a in narrow.values())), 3)
        self.assertGreater(float(narrow['Event A']['font-size']), float(normal['Event A']['font-size']))

    def test_nonzero_waterfall_axis_is_explicit_and_never_automatic(self):
        items = [('Start', 5.15, 'total'), ('Change', .33, 'step'), ('End', 5.48, 'total')]
        self.assertNotIn('totals truncated', str(rl.waterfall('EPS', items, 'USD')))
        chart = str(rl.waterfall('EPS', items, 'USD', yr=(5, 5.6, .2)))
        self.assertIn('totals truncated', chart)
        self.assertIn('clip-path', chart)

    def test_unaccounted_investor_questions_prevent_rendering(self):
        r = report(account_for_questions=False)
        r.section('Synthetic business', 'Fixture only', arg('Invented business.'), covers=('business',))
        with self.assertRaisesRegex(ValueError, 'No section answers:'):
            r.html()
        for question in rl.QUESTIONS:
            if question != 'business':
                r.omit(question, 'Explicitly outside this synthetic test scope.')
        self.assertIn('Invented business.', r.html())

    def test_combined_section_can_account_for_multiple_questions(self):
        r = report(account_for_questions=False)
        r.section('Synthetic combined section', 'Fixture only', 'Synthetic content.', arg(), debate(),
                  covers=tuple(rl.QUESTIONS))
        self.assertEqual(r.covered, set(rl.QUESTIONS))
        self.assertEqual(r.omitted, {})
        self.assertIn('Synthetic content.', r.html())

    def test_covering_section_needs_an_argument_and_the_debate_needs_a_debate(self):
        r = report()
        with self.assertRaisesRegex(ValueError, 'no Argument or Debate'):
            r.section('Described only', '', 'A paragraph that describes.', covers=('business',))
        with self.assertRaisesRegex(ValueError, 'no Debate block'):
            r.section('Debate without a verdict', '', arg(), covers=('debate',))
        r.section('Context only, no coverage claimed', '', 'Plain context is allowed here.')

    def test_argument_requires_cited_evidence_and_segment_arguments_cite_their_build(self):
        with self.assertRaisesRegex(ValueError, 'must cite a source'):
            rl.Argument('Point.', 'Evidence with no citation.', 'Inference.', 'Implication.')
        with self.assertRaisesRegex(ValueError, 'nonempty inference'):
            rl.Argument('Point.', 'Evidence{{src:syn}}.', '', 'Implication.')
        with self.assertRaisesRegex(ValueError, 'driver build'):
            arg(segment='Brand A')
        built = arg(segment='Brand A', evidence='Stores and sales per store ({{ex:build}}).')
        self.assertEqual(built.segment, 'Brand A')
        self.assertNotIn('<b>', str(arg()))   # rendered as prose, without labels

    def test_judgement_in_a_plain_paragraph_is_rejected(self):
        r = report()
        for text in ('We forecast growth of 5%.', 'Our view is that margins hold.', 'We side with the bulls.'):
            with self.assertRaisesRegex(ValueError, 'belongs in an Argument'):
                r.section('Loose judgement', '', text)
        r.section('Judgement with evidence', '', arg('We forecast growth of 5%.'))
        self.assertIn('We forecast growth of 5%.', r.html())

    def test_debate_requires_claims_answer_quantified_effect_and_dated_test(self):
        claims = [('Claim one', 'Evidence{{src:syn}}', 'supported'), ('Claim two', 'Evidence{{src:syn}}', 'contradicted')]
        with self.assertRaisesRegex(ValueError, 'at least two claims'):
            rl.Debate('Q?', claims[:1], 'Answer.', 'Moves 1 point.', 'April 2027 update.')
        with self.assertRaisesRegex(ValueError, 'cites the source or exhibit'):
            rl.Debate('Q?', [('Claim', 'No citation', 'supported')] + claims[:1], 'Answer.', 'Moves 1 point.', 'April 2027.')
        with self.assertRaisesRegex(ValueError, 'Claim status'):
            rl.Debate('Q?', [('Claim', 'Evidence{{src:syn}}', 'likely')] + claims[:1], 'Answer.', 'Moves 1 point.', 'April 2027.')
        with self.assertRaisesRegex(ValueError, 'with the number'):
            rl.Debate('Q?', claims, 'Answer.', 'It moves the forecast.', 'April 2027.')
        with self.assertRaisesRegex(ValueError, 'its date'):
            rl.Debate('Q?', claims, 'Answer.', 'Moves 1 point.', 'The next update.')
        with self.assertRaisesRegex(ValueError, 'nonempty answer'):
            rl.Debate('Q?', claims, ' ', 'Moves 1 point.', 'April 2027.')
        document = str(debate())
        self.assertIn('Our answer.', document)
        self.assertNotIn('The bear case.', document)   # bull and bear appear once, as priced scenarios
        self.assertIn('Contradicted', str(rl.Debate('Q?', claims, 'A.', 'Moves 1 point.', 'April 2027.')))

    def test_declared_business_units_each_need_an_argument(self):
        r = report()
        r.segments(['Brand A', 'Brand B'])
        r.section('Units', '', arg(segment='Brand A', evidence='Stores x sales per store ({{ex:build}}).'),
                  r.exhibit('build', 'Synthetic build', '<svg/>', 'Synthetic'))
        with self.assertRaisesRegex(ValueError, 'Brand B'):
            r.html()
        r.section('Units B', '', arg(segment='Brand B', evidence='Units x price ({{ex:build}}).'))
        self.assertIn('Stores x sales per store', r.html())
        with self.assertRaises(ValueError):
            report().segments([])

    def test_unknown_questions_and_empty_omission_reasons_are_rejected(self):
        r = report(account_for_questions=False)
        with self.assertRaises(ValueError):
            r.section('Mistyped question', '', covers=('busines',))
        with self.assertRaises(ValueError):
            r.omit('busines', 'Typo must not bypass coverage.')
        for reason in ('', '  ', None):
            with self.assertRaises(ValueError):
                r.omit('business', reason)

    def test_reference_order_and_embedded_fonts(self):
        r = report()
        r.section('Evidence', 'Synthetic only', 'Second source first{{src:b}}; then first{{src:a}}.')
        r.sources([('a', 'Publisher A', 'Title A', 'Example date', ''),
                   ('b', 'Publisher B', 'Title B', 'Example date', '')])
        document = r.html()
        self.assertLess(document.index('Title B'), document.index('Title A'))
        self.assertIn('first<sup>1</sup>', document)
        self.assertIn('first<sup>2</sup>', document)
        self.assertEqual(document.count('data:font/woff2;base64,'), 4)
        self.assertIn('Example &lt;synthetic&gt;', document)
        self.assertNotIn('{{src:', document)

    def test_unknown_source_is_rejected(self):
        r = report()
        r.section('Evidence', 'Synthetic only', 'Unregistered claim{{src:missing}}.')
        with self.assertRaises(ValueError):
            r.html()

    def test_exhibits_follow_placement_and_missing_or_duplicate_keys_fail(self):
        r = report()
        r.section('Case', 'Synthetic only', 'See {{ex:b}} and {{ex:a}}.',
                  r.exhibit('a', 'First placed', '<svg/>', 'Synthetic'),
                  r.exhibit('b', 'Second placed', '<svg/>', 'Synthetic'))
        self.assertIn('See Exhibit 2 and Exhibit 1.', r.html())
        self.assertEqual(r.uncited_exhibits, [])
        r.section('Missing', '', 'See {{ex:missing}}.')
        with self.assertRaises(ValueError):
            r.html()
        r = report()
        r.section('Duplicate', '', r.exhibit('a', 'One', '<svg/>', 'Synthetic'),
                  r.exhibit('a', 'Two', '<svg/>', 'Synthetic'))
        with self.assertRaises(ValueError):
            r.html()

    def test_uncited_exhibits_are_reported(self):
        r = report()
        r.section('Case', '', r.exhibit('unused', 'Synthetic exhibit', '<svg/>', 'Synthetic'))
        r.html()
        self.assertEqual(r.uncited_exhibits, ['unused'])

    def test_displayed_returns_use_displayed_prices_and_ignore_stale_scenario_returns(self):
        result = rl.rating_box('Buy', 'Price', 100.004, 120.049, '2.0%',
                               (70.4, 9), (120.049, 9), (149.6, 9), 'n/a', '$')
        self.assertIn('$100.00', result)
        self.assertIn('$120.0', result)
        self.assertIn('+20.0%', result)
        self.assertIn('$70 / 120 / 150', result)
        self.assertIn('-30% / +20% / +50%', result)
        self.assertNotIn('+900%', result)
        lower_price = rl.rating_box('Buy', 'Price', 50, 60.4, 'n/a',
                                    (35.4, 9), (60.4, 9), (75.4, 9), 'n/a', '$')
        self.assertIn('$35.4 / 60.4 / 75.4', lower_price)
        self.assertIn('+20.8%', lower_price)
        for value in (0, -1, float('nan'), float('inf')):
            with self.assertRaises(ValueError):
                rl.rating_box('Hold', 'Price', value, 100, 'n/a',
                              (70, 0), (100, 0), (150, 0), 'n/a', '$')

    def test_number_formats_preserve_missing_and_negative_values(self):
        self.assertEqual(rl.num(None), 'n/a')
        self.assertEqual(rl.num(-1234.5, 1), '(1,234.5)')
        self.assertEqual(rl.pct(-0.125), '(12.5%)')
        self.assertEqual(rl.mult(None), 'n/a')
        self.assertEqual(rl.money(-27), '-US$27')

    def test_charts_are_well_formed_with_finite_coordinates_and_unique_clip_ids(self):
        charts = [rl.bars_chart('Synthetic output', ['Actual', 'Forecast'],
                                [('Units', [10, 12])], 'Units', 1),
                  rl.lines_chart('Synthetic trend', ['A', 'E'], [('Units', [10, 12], rl.NAVY)], 'Units', 1),
                  rl.football_field('Synthetic cases', 100,
                                    [('Bear', 70, -.3), ('Base', 120, .2), ('Bull', 150, .5)],
                                    lambda x: f'${x:.0f}')]
        ids = []
        for chart in charts:
            ET.fromstring(chart)
            self.assertNotRegex(chart, r'(?i)\b(?:nan|inf)\b')
            ids.extend(re.findall(r'<clipPath id="([^"]+)"', chart))
        self.assertEqual(len(ids), len(set(ids)))
        prices = rl.price_chart('Synthetic prices', ['2026-01-01', '2026-10-01'],
                                [('Example', [100, 110], rl.TEAL)])
        tree = ET.fromstring(prices)
        last_date = next(node for node in tree.iter() if node.text == 'Oct 26')
        self.assertEqual(last_date.attrib['text-anchor'], 'end')

    def test_companion_links_are_escaped(self):
        r = report()
        r.companions = [('Model & assumptions', 'synthetic model.xlsx')]
        document = r.html()
        self.assertIn('Model &amp; assumptions', document)
        self.assertIn('href="synthetic model.xlsx"', document)


if __name__ == '__main__':
    unittest.main()
