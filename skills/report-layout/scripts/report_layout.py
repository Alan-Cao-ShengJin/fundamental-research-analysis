"""House layout for full stock reports: A4 PDF from HTML through headless Chrome.

    import report_layout as rl
    r = rl.Report(company='Example Company (synthetic)', ticker='EXAMPLE', report='Initiation', date='Example date',
                  pricing='Synthetic prices and estimates; no live market data')
    r.front(headline, key_points=[...], summary=[...], rating=rl.rating_box(...), key_data=[(label, value)],
            financials=rl.fin_table(...), chart=r.exhibit('px', 'Takeaway headline', svg, 'Source line'))
    r.section('Valuation', 'One-line takeaway for the rail', 'Paragraph citing {{ex:band}} and a source{{src:example}}.',
              r.exhibit('band', 'Synthetic valuation comparison', rl.band_chart(...), 'Synthetic example'),
              covers=('valuation',))
    # Add sections covering the other QUESTIONS, or omit an inapplicable question with its reason.
    r.sources([('example', 'Synthetic source', 'Invented estimates and prices', 'Example date', '')])
    r.write(html_path); rl.print_pdf(html_path, pdf_path); rl.inspect_pdf(pdf_path)

Text may use {{ex:key}} (becomes "Exhibit N", numbered in order of appearance) and {{src:key}} or {{src:a,b}}
(becomes superscript source numbers, numbered in order of first citation). Colours and fonts come from the shared chart
theme; the IBM Plex Sans files in ../assets/fonts are embedded so the PDF does not depend on system fonts.
"""
from __future__ import annotations
import base64
import html
import json
import math
import os
import re
import shutil
import subprocess
import textwrap
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILLS = HERE.parents[1]
THEME = json.loads((SKILLS / 'chart-visualization' / 'assets' / 'chart-theme.json').read_text(encoding='utf-8'))
COL = THEME['colours']
SER = THEME['series']
SCEN = THEME['scenarios']
RATING = THEME['ratings']
FONT = THEME['font']['family']
NAVY, GREY, TEAL, RED, GREEN = COL['actual'], COL['forecast'], COL['company'], COL['negative'], COL['positive']
FC_OPACITY = THEME['states']['forecast']['opacity']
RATING_DEFINITIONS = ('Ratings are set on the 12-month price return to our target: Buy above +10%, Hold from -10% to +10%, '
                      'Sell below -10%. Dividend yield is shown separately and is not part of the target or the rating.')
DISCLAIMER = 'Internal use only. Not investment advice.'


def esc(s):
    return html.escape(str(s))


class Block(str):
    """Pre-rendered HTML (exhibits, tables, lists) placed as-is in a section."""


class Sub(str):
    """A subsection heading inside a section."""


def bullets(items):
    return Block('<ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>')


def bound_value(claim_id, value, period, unit, fmt=None):
    """An explicitly identified financial figure; publication review checks its model binding and visible value."""
    if not all(isinstance(x, str) and x.strip() for x in (claim_id, period, unit)) or not math.isfinite(value):
        raise ValueError('A bound figure needs an ID, period, unit and finite value')
    shown = fmt(value) if fmt else f'{value:,.2f}'
    return (f'<span data-model-claim="{esc(claim_id)}" data-value="{value:.15g}" '
            f'data-period="{esc(period)}" data-unit="{esc(unit)}">{esc(shown)}</span>')


# One shared formatter for arbitrary calculated/source measures and ranges.
from display_bindings import bound_measure


# Judgement wording that belongs in an Argument, with its evidence, not in a plain paragraph.
JUDGEMENT = ('we forecast', 'we assume', 'we expect', 'we think', 'we believe', 'our view', 'our reading', 'we side')
CLAIM_STATUS = ('supported', 'contradicted', 'untested')
_CITES = re.compile(r'\{\{(src|ex):')


def _nonempty(name, text, where):
    if not isinstance(text, str) or not text.strip():
        raise ValueError(f'{where} needs a nonempty {name}')


class Argument(Block):
    """One substantive investment point, written through the argument sequence and rendered as one paragraph without
    labels: the point and its data; how the data was derived, citing its source ({{src:key}}) or exhibit ({{ex:key}});
    what it means against a comparison; and what it does to EPS, the multiple or the target. `segment` tags the business
    unit the argument analyses; a segment argument must cite the exhibit that shows the unit's driver build."""

    def __new__(cls, point, evidence, inference, implication, segment=None):
        for name, text in (('point', point), ('evidence', evidence), ('inference', inference), ('implication', implication)):
            _nonempty(name, text, 'Argument')
        if not _CITES.search(evidence):
            raise ValueError('Argument evidence must cite a source ({{src:key}}) or an exhibit ({{ex:key}}): ' + point[:80])
        if segment and '{{ex:' not in evidence + inference:
            raise ValueError(f'The {segment} argument must cite the exhibit that shows its driver build')
        self = super().__new__(cls, f'<p class="arg">{point} {evidence} {inference} {implication}</p>')
        self.segment = segment
        return self


class Debate(Block):
    """One contested question the stock turns on, answered: the claims each side rests on, each with its evidence and
    status (supported, contradicted, untested); our answer; the number it moves (a forecast, margin or multiple,
    quantified); and the observation and date that would settle it. Bull and bear appear once, as priced scenarios."""

    def __new__(cls, question, claims, answer, moves, settles):
        for name, text in (('question', question), ('answer', answer), ('moves', moves), ('settles', settles)):
            _nonempty(name, text, f'Debate {question[:60]!r}')
        if len(claims) < 2:
            raise ValueError(f'Debate {question[:60]!r} needs at least two claims that must hold, with their evidence')
        rows = []
        for claim, evidence, status in claims:
            _nonempty('claim', claim, 'Debate claim')
            if status not in CLAIM_STATUS:
                raise ValueError(f'Claim status must be one of {CLAIM_STATUS}, not {status!r}')
            if not _CITES.search(evidence):
                raise ValueError('Each debate claim cites the source or exhibit that tests it: ' + claim[:80])
            rows.append([claim, evidence, status.capitalize()])
        if not re.search(r'\d', moves):
            raise ValueError(f'Debate {question[:60]!r}: say what the answer moves, with the number (a forecast, margin or multiple)')
        if not re.search(r'\d', settles):
            raise ValueError(f'Debate {question[:60]!r}: name the observation and its date that would settle the question')
        tab = table(['Claim that must hold', 'Evidence', 'Status'], rows, cls='text', compact=True)
        # Keep the heading, paginated table and answer in one normal-flow grid item.
        html_ = f'<div class="debate"><h3>{esc(question)}</h3>{tab}<p><b>Our answer.</b> {answer} {moves} {settles}</p></div>'
        self = super().__new__(cls, html_)
        self.question = question
        return self


# ---------------------------------------------------------------- fonts and CSS
def _font_faces():
    out = []
    for f, weight, style in [('400-normal', 400, 'normal'), ('400-italic', 400, 'italic'), ('600-normal', 600, 'normal'),
                             ('700-normal', 700, 'normal')]:
        p = HERE.parent / 'assets' / 'fonts' / f'ibm-plex-sans-latin-{f}.woff2'
        if p.exists():
            b64 = base64.b64encode(p.read_bytes()).decode()
            out.append(f"@font-face {{ font-family: 'IBM Plex Sans'; font-weight: {weight}; font-style: {style}; "
                       f"src: url(data:font/woff2;base64,{b64}) format('woff2'); }}")
    return '\n'.join(out)


def _css(running, right):
    q = lambda s: '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'  # noqa: E731
    box = f"font-family: {FONT}; font-size: 7.5pt; color: {COL['muted']};"
    return f"""
{_font_faces()}
@page {{ size: A4; margin: 18mm 15mm 18mm 15mm;
  @top-left {{ content: {q(running)}; {box} }}
  @top-right {{ content: {q(right)}; {box} }}
  @bottom-left {{ content: {q(DISCLAIMER)}; {box} }}
  @bottom-right {{ content: "Page " counter(page) " of " counter(pages); {box} }} }}
@page :first {{ @top-left {{ content: none; }} @top-right {{ content: none; }} @bottom-right {{ content: none; }} }}
* {{ box-sizing: border-box; }}
body {{ font-family: {FONT}; color: {COL['body']}; font-size: 9.5pt; line-height: 1.4; margin: 0; background: #fff;
       font-variant-numeric: tabular-nums; }}
main {{ max-width: 180mm; margin: 0 auto; }}
a {{ color: {TEAL}; text-decoration: none; }}
sup {{ font-size: 6.5pt; color: {TEAL}; line-height: 0; }}
p {{ margin: 0 0 2.2mm; orphans: 3; widows: 3; }}
ul {{ margin: 0 0 2mm; padding-left: 4.5mm; }} li {{ margin-bottom: 1.2mm; }}
h1 {{ font-size: 20pt; font-weight: 600; color: {COL['ink']}; line-height: 1.2; margin: 2mm 0 3mm; }}
h2 {{ font-size: 12pt; font-weight: 600; color: {TEAL}; margin: 0 0 1.5mm; line-height: 1.2; break-after: avoid; }}
h3 {{ font-size: 10pt; font-weight: 600; color: {COL['ink']}; margin: 2mm 0 1mm; break-after: avoid; }}
.byline {{ display: flex; justify-content: space-between; gap: 4mm; font-size: 8pt; color: {COL['muted']};
          border-bottom: 1.5px solid {COL['ink']}; padding-bottom: 1.5mm; }}
.front {{ display: grid; grid-template-columns: 63fr 37fr; column-gap: 6mm; break-after: page; }}
.front .lead h3 {{ color: {TEAL}; margin-top: 0; }}
.side {{ font-size: 8pt; line-height: 1.3; }}
.side h4 {{ font-size: 8pt; text-transform: uppercase; letter-spacing: .04em; color: {TEAL}; margin: 3mm 0 1mm;
           border-bottom: 1px solid {COL['grid']}; padding-bottom: .5mm; }}
.rbox {{ background: #F3F5F7; border-top: 3px solid {TEAL}; padding: 2mm 2.5mm; }}
.rbox .rating {{ font-size: 16pt; font-weight: 700; }}
.kv {{ width: 100%; border-collapse: collapse; font-size: 8pt; }}
.kv td {{ border-bottom: 1px solid {COL['grid']}; padding: .6mm 0; }} .kv td:last-child {{ text-align: right; }}
.rbox .kv td {{ border: none; padding: .35mm 0; }}
.sec {{ display: block; margin: 0 0 3mm; }}
.sec::after {{ content: ""; display: block; clear: both; }}
.sec > :not(.rail):not(.wide) {{ margin-left: 46mm; }}
.sec > p {{ margin-bottom: 0; padding-bottom: 2.2mm; }}  /* padding survives a page break; a grid item's margin does not */
.sec > .rail {{ float: left; width: 40mm; margin-right: 6mm; border-top: 2px solid {TEAL}; padding-top: 1.2mm; break-inside: avoid; }}
.sec p {{ orphans: 3; widows: 3; }}
.rail .take {{ font-size: 8pt; color: {COL['muted']}; line-height: 1.3; }}
.sec > .wide {{ clear: both; margin-left: 0; }}
.sec > h3 {{ border-top: 1px solid {COL['grid']}; padding-top: 1mm; }}
.exhibit {{ break-inside: avoid; margin: 1.5mm 0 3.5mm; }}
.exhibit.splittable {{ break-inside: auto; }}
.debate {{ min-width: 0; }}
.debate table {{ margin-bottom: 2mm; }}
thead {{ display: table-header-group; }}
tr {{ break-inside: avoid; }}
.ex-head {{ font-size: 8.5pt; font-weight: 600; color: {COL['ink']}; border-top: 1px solid {COL['ink']}; padding-top: 1mm;
           margin-bottom: 1mm; }}
.ex-head b {{ color: {TEAL}; }}
.ex-src {{ font-size: 7.5pt; color: {COL['muted']}; margin-top: .8mm; line-height: 1.3; }}
svg {{ display: block; width: 100%; height: auto; }}
table {{ border-collapse: collapse; width: 100%; font-size: 8.5pt; }}
th {{ text-align: left; font-weight: 600; color: {COL['ink']}; border-bottom: 1px solid {COL['ink']}; padding: .8mm 1.2mm;
      vertical-align: bottom; }}
td {{ border-bottom: 1px solid {COL['grid']}; padding: .7mm 1.2mm; vertical-align: top; }}
table.fin td:not(:first-child), table.fin th:not(:first-child) {{ text-align: right; white-space: nowrap; }}
table.num td:not(:first-child), table.num th:not(:first-child), td.numeric, th.numeric {{ text-align: right; }}
table.fin td.e, table.fin th.e {{ background: #EEF1F4; }}
table.fin tr.grp td {{ font-weight: 600; color: {TEAL}; padding-top: 1.6mm; }}
table.fin tr.bold td {{ font-weight: 600; }}
table.fin tr.cons td {{ color: {COL['muted']}; font-style: italic; }}
td.pos {{ color: {TEAL}; }} td.neg {{ color: {RED}; }}
table.text td {{ font-size: 8pt; }}
table.compact td, table.compact th {{ font-size: 7.8pt; padding-top: .35mm; padding-bottom: .35mm; }}
.back {{ font-size: 7.5pt; color: {COL['body']}; columns: 2; column-gap: 6mm; margin-top: 2mm; break-inside: avoid; }}
.back h2 {{ column-span: all; border-top: 2px solid {TEAL}; padding-top: 1.2mm; }}
.back ol {{ margin: 0 0 2mm; padding-left: 5mm; }} .back li {{ break-inside: avoid; margin-bottom: .8mm; }}
.back p {{ break-inside: avoid; margin-bottom: 1.5mm; }}
@media screen {{ main {{ padding: 6mm 4mm; }} }}
@media screen and (max-width: 640px) {{ .front, .sec {{ display: block; }}
  .sec > :not(.rail):not(.wide) {{ margin-left: 0; }} .sec > .rail {{ float: none; width: auto; margin-right: 0; }}
  table {{ display: block; overflow-x: auto; }} }}
"""


# The investor questions a full report answers (research-brief/references/visual-reports.md). Each section names the
# questions it answers with covers=(...); a question that does not matter for this company is dropped with omit().
QUESTIONS = {
    'business': 'how the company makes money',
    'debate': 'the core investor debates, each side argued',
    'industry': 'industry growth, niche, barriers, upstream costs and customers',
    'competition': 'competitive response and how long the advantage lasts',
    'outlook': 'latest results against the next outlook',
    'delivery': 'management delivery against its own plans',
    'forecast': 'the evidence behind the forecast and the gap to consensus',
    'cash': 'cash conversion and funded growth',
    'governance': 'whether outside shareholders can get the value',
    'valuation': 'valuation against peers and dated own history',
    'market': 'market context: holders, flows and recent price moves',
    'risks': 'bear and bull cases, catalysts and what would change the view',
}


# ---------------------------------------------------------------- page
class Report:
    def __init__(self, company, ticker, report, date, author='', email='', firm='', pricing=''):
        self.company, self.ticker, self.report, self.date = company, ticker, report, date
        self.author, self.email, self.firm, self.pricing = author, email, firm, pricing
        self.parts, self.src, self.front_html, self.uncited_exhibits = [], [], '', []
        self.companions = []   # [(label, file name)] delivered in the same folder, e.g. the Excel model
        self.covered, self.omitted = set(), {}
        self.required_segments, self.argued_segments = [], set()
        self.summary_html = ''

    def financial_summary(self, first, periods, est_from, groups, source, note=''):
        """Compact model-linked IS/BS/CF appendix; rows and periods follow the company's accounting and available history."""
        if len(periods) < 2 or len(groups) < 3 or any(not rows for _, rows in groups) or not source:
            raise ValueError('Financial summary needs periods, three nonempty statement groups and a source')
        self.summary_html = '<div data-financial-summary="true">' + str(self.exhibit(
            'financial-summary', 'Summary financial statements', fin_table(first, periods, est_from, groups),
            source, note, splittable=True)) + '</div>'

    def segments(self, names):
        """Declare the business units the report must analyse (each above about 15% of segment profit, or one a debate
        turns on). Each needs an Argument tagged segment=name that cites its driver-build exhibit."""
        names = [n for n in names if isinstance(n, str) and n.strip()]
        if not names:
            raise ValueError('segments() needs at least one business unit name')
        self.required_segments = names

    # exhibits, references and sources -------------------------------------------------
    def exhibit(self, key, headline, body, source, note='', splittable=None):
        """A numbered exhibit: 'Exhibit N: headline' above (the point, not the topic), source line below."""
        split = '<table' in str(body) if splittable is None else splittable
        result = Block(f'<figure class="exhibit{" splittable" if split else ""}"><div class="ex-head"><b>{{{{exn:{key}}}}}:</b> {headline}</div>{body}'
                       f'<div class="ex-src">{note + " " if note else ""}Source: {source}</div></figure>')
        if hasattr(body, 'narrow'):
            result.narrow = lambda: self.exhibit(key, headline, body.narrow(), source, note, splittable)
        return result

    @staticmethod
    def ref(key):
        return f'{{{{ex:{key}}}}}'

    def sources(self, items):
        """items: [(key, publisher, title, date, url)]; numbered by first citation, uncited ones last."""
        self.src = items

    # page parts -----------------------------------------------------------------------
    def front(self, headline, key_points, summary, rating, key_data, financials='', chart=''):
        chart = chart.narrow() if hasattr(chart, 'narrow') else chart
        kd = ''.join(f'<tr><td>{esc(a)}</td><td>{b}</td></tr>' for a, b in key_data)
        by = (f'<div class="byline"><span>{esc(self.company)} | {esc(self.ticker)} | {esc(self.report)}</span>'
              f'<span>{" | ".join(esc(x) for x in (self.author, self.email, self.date) if x)}</span></div>')
        self.front_html = (
            f'{by}<h1>{esc(headline)}</h1><div class="front"><div class="lead"><h3>Key points</h3>{bullets(key_points)}'
            + ''.join(f'<p>{p}</p>' for p in summary) + f'{chart}</div><div class="side">{rating}<h4>Key data</h4>'
            f'<table class="kv">{kd}</table>' + (f'<h4>Key financials</h4>{financials}' if financials else '')
            + (f'<p class="ex-src">{esc(self.pricing)}.</p>' if self.pricing else '') + '</div></div>')

    def omit(self, question, reason):
        """Drop an investor question that does not matter for this company; the reason is kept for the record."""
        if question not in QUESTIONS:
            raise ValueError(f'Unknown investor question {question!r}; use {sorted(QUESTIONS)}')
        if not isinstance(reason, str) or not reason.strip():
            raise ValueError('An omitted investor question requires a nonempty reason.')
        self.omitted[question] = reason

    def section(self, title, takeaway, *items, covers=()):
        unknown = set(covers) - set(QUESTIONS)
        if unknown:
            raise ValueError(f'Unknown investor questions {sorted(unknown)}; use {sorted(QUESTIONS)}')
        self.covered |= set(covers)
        if covers and not any(isinstance(it, (Argument, Debate)) for it in items):
            raise ValueError(f'Section {title!r} answers {sorted(covers)} but holds no Argument or Debate: it describes, '
                             f'it does not analyse. Write each substantive point as an Argument with its evidence.')
        if 'debate' in covers and not any(isinstance(it, Debate) for it in items):
            raise ValueError(f'Section {title!r} covers the debate but holds no Debate block: each contested question '
                             f'needs both cases, the claims tested, our answer, what it moves and what settles it.')
        body = [f'<div class="rail"><h2>{esc(title)}</h2><div class="take">{takeaway}</div></div>']
        for it in items:
            if isinstance(it, Sub):
                body.append(f'<h3>{esc(it)}</h3>')
            elif isinstance(it, Argument):
                if it.segment:
                    self.argued_segments.add(it.segment)
                body.append(it)
            elif isinstance(it, Block):
                body.append(f'<div class="wide">{it}</div>' if it.startswith('<figure') else it)
            else:
                low = str(it).lower()
                hit = next((w for w in JUDGEMENT if w in low), None)
                if hit:
                    raise ValueError(f'Section {title!r}: "{hit}" sits in a plain paragraph. A judgement belongs in an '
                                     f'Argument with the evidence behind it: ' + str(it)[:80])
                body.append(f'<p>{it}</p>')
        self.parts.append('<section class="sec">' + ''.join(body) + '</section>')

    def _back(self):
        order, n = {}, 0
        for k in re.findall(r'\{\{src:([^}]+)\}\}', self.front_html + ''.join(self.parts) + self.summary_html):
            for x in k.split(','):
                if x.strip() not in order:
                    n += 1
                    order[x.strip()] = n
        known = [s[0] for s in self.src]
        for k in order:
            if k not in known:
                raise ValueError(f'Cited source {k} is not in the source list')
        for k in known:
            if k not in order:
                n += 1
                order[k] = n
        items = sorted(self.src, key=lambda s: order[s[0]])
        lis = ''.join(f'<li>{esc(pub)}, ' + (f'<a href="{esc(url)}">{esc(title)}</a>' if url else f'"{esc(title)}"')
                      + f', {esc(date)}.</li>' for _, pub, title, date, url in items)
        back = (f'<section class="back"><h2>Sources</h2><ol>{lis}</ol>'
                + (f'<p><b>Author.</b> {", ".join(esc(x) for x in (self.author, self.email, self.firm) if x)}.</p>'
                   if self.author or self.firm else '')
                + (f'<p><b>Accompanying files.</b> ' + '; '.join(f'{esc(a)}: <a href="{esc(f)}">{esc(f)}</a>'
                                                                   for a, f in self.companions) + '.</p>'
                   if self.companions else '')
                + f'<p><b>Ratings.</b> {RATING_DEFINITIONS}</p>'
                + (f'<p><b>Pricing.</b> {esc(self.pricing)}.</p>' if self.pricing else '')
                + f'<p><b>{DISCLAIMER}</b></p></section>')
        return order, back

    def html(self):
        if 'initiat' in self.report.lower() and not self.summary_html:
            raise ValueError('An initiation requires financial_summary() with model-linked summary statements')
        missing = [f'{k} ({v})' for k, v in QUESTIONS.items() if k not in self.covered and k not in self.omitted]
        if missing:
            raise ValueError('No section answers: ' + '; '.join(missing) + '. Cover each in a section (covers=) or '
                             'drop it with omit(question, reason).')
        unargued = [s for s in self.required_segments if s not in self.argued_segments]
        if unargued:
            raise ValueError('No Argument analyses these business units: ' + ', '.join(unargued)
                             + '. Each declared segment needs an Argument(segment=...) citing its driver-build exhibit.')
        order, back = self._back()
        body = self.front_html + ''.join(self.parts) + self.summary_html + back
        ex = {}
        for k in re.findall(r'\{\{exn:([^}]+)\}\}', body):
            if k in ex:
                raise ValueError(f'Exhibit key {k} used twice')
            ex[k] = len(ex) + 1
        for k in re.findall(r'\{\{ex:([^}]+)\}\}', body):
            if k not in ex:
                raise ValueError(f'Text cites exhibit {k}, which is not placed')
        cited = set(re.findall(r'\{\{ex:([^}]+)\}\}', body))
        # A self-contained statement appendix is reference material, not an uncited argumentative exhibit.
        self.uncited_exhibits = [k for k in ex if k not in cited and k != 'financial-summary']
        body = re.sub(r'\{\{exn?:([^}]+)\}\}', lambda m: f'Exhibit {ex[m[1]]}', body)
        body = re.sub(r'\{\{src:([^}]+)\}\}', lambda m: '<sup>' + ','.join(str(order[x.strip()]) for x in m[1].split(','))
                      + '</sup>', body)
        running = f'{self.company} ({self.ticker}) | {self.report} | {self.date}'
        return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,'
                f'initial-scale=1"><title>{esc(self.company)} {esc(self.report)}</title><style>'
                f'{_css(running, self.firm or self.author)}</style></head><body><main>{body}</main></body></html>')

    def write(self, path):
        Path(path).write_text(self.html(), encoding='utf-8')
        return Path(path)


def rating_box(rating, price_label, price, target, dividend, bear, base, bull, consensus_target, money, decimals=1):
    """Front-page rating box. The price return is computed from the target as displayed (rounded to `decimals`), so the
    box never shows a target next to a return worked from a different figure. bear/base/bull are (target, return);
    supplied scenario returns are retained for API compatibility but recalculated from the displayed prices."""
    c = RATING.get(rating, TEAL)
    cd = decimals if price < 100 else 0   # whole units from 100, as in the one-page brief; below that the base case matches the target
    target = round(target, decimals)
    price = round(price, 2)
    if not math.isfinite(price) or price <= 0:
        raise ValueError('The displayed reference price must be finite and positive.')
    price_return = target / price - 1
    cases = [round(case[0], cd) for case in (bear, base, bull)]
    case_returns = [value / price - 1 for value in cases]
    row = lambda a, b: f'<tr><td>{a}</td><td>{b}</td></tr>'  # noqa: E731
    return (f'<div class="rbox"><div class="rating" style="color:{c}">{esc(rating)}</div><table class="kv">'
            + row(esc(price_label), f'{money}{price:,.2f}') + row('12-month target', f'<b>{money}{target:,.{decimals}f}</b>')
            + row('Price return', f'<b>{price_return * 100:+.1f}%</b>') + row('Dividend yield (separate)', dividend)
            + row('Consensus target', consensus_target)
            + row('Bear / base / bull', f'{money}{cases[0]:,.{cd}f} / {cases[1]:,.{cd}f} / {cases[2]:,.{cd}f}')
            + row('', ' / '.join(f'{value * 100:+.0f}%' for value in case_returns)) + '</table></div>')


# ---------------------------------------------------------------- number formats
def num(x, d=0):
    """Thousands separators; negatives in parentheses; None as n/a."""
    if x is None:
        return 'n/a'
    s = f'{abs(x):,.{d}f}'
    return f'({s})' if round(x, d) < 0 else s


def pct(x, d=1, sign=False):
    if x is None:
        return 'n/a'
    if sign:
        return f'{x * 100:+.{d}f}%'
    return f'({abs(x) * 100:.{d}f}%)' if round(x * 100, d) < 0 else f'{x * 100:.{d}f}%'


def mult(x, d=1):
    return 'n/a' if x is None else f'{x:.{d}f}x'


def money(x, cur='US$', d=0):
    """'-US$27' style."""
    return f'{"-" if round(x, d) < 0 else ""}{cur}{abs(x):,.{d}f}'


def f0(x):
    return f'{x:,.0f}'


def f1(x):
    return f'{x:,.1f}'


def table(head, rows, cls='text', compact=False):
    if cls not in ('text', 'num', 'fin'):
        raise ValueError(f'Unknown table class {cls!r}; use text, num or fin')
    if any(len(row) != len(head) for row in rows):
        raise ValueError('Each table row must match the header width')
    numeric = lambda x: bool(re.fullmatch(r'[+\-\u2212(]?(?:[$\u20ac\u00a3\u00a5]|HK\$|US\$|RMB)?\s*\d[\d,.]*(?:%|x|pt)?\)?', re.sub('<[^>]+>', '', str(x)).strip()))
    h = ''.join(f'<th>{esc(x)}</th>' for x in head)
    b = ''.join('<tr>' + ''.join('<td{}>{}</td>'.format(' class="numeric"' if numeric(x) and i else '', x)
                                for i, x in enumerate(r)) + '</tr>' for r in rows)
    return Block(f'<table class="{cls}{" compact" if compact else ""}"><thead><tr>{h}</tr></thead><tbody>{b}</tbody>'
                 f'</table>')


def fin_table(first, periods, est_from, groups, compact=False):
    """Grouped financial table. periods: labels like 'FY2025A'; columns from index est_from are estimates (shaded).
    groups: [(group label or None, [(label, [cells], style)])]; style '', 'bold', 'cons' or 'sign' (teal/red by sign);
    cells are pre-formatted strings (use num/pct/mult/money)."""
    if not periods or not isinstance(est_from, int) or not 0 <= est_from <= len(periods):
        raise ValueError('Financial table needs periods and a valid first-estimate index')
    if any(len(cells) != len(periods) for _, items in groups for _, cells, _ in items):
        raise ValueError('Each financial row must match the declared periods')
    e = lambda i: ' class="e"' if i >= est_from else ''  # noqa: E731
    h = f'<th>{esc(first)}</th>' + ''.join(f'<th{e(i)}>{esc(p)}</th>' for i, p in enumerate(periods))
    rows = []
    for g, items in groups:
        if g:
            rows.append(f'<tr class="grp"><td colspan="{len(periods) + 1}">{esc(g)}</td></tr>')
        for label, cells, style in items:
            cls = f' class="{style}"' if style in ('bold', 'cons') else ''
            tds = []
            for i, x in enumerate(cells):
                c = ['e'] if i >= est_from else []
                if style == 'sign' and x not in ('', 'n/a'):
                    c.append('neg' if x.startswith('(') or x.startswith('-') else 'pos')
                tds.append(f'<td class="{" ".join(c)}">{x}</td>' if c else f'<td>{x}</td>')
            rows.append(f'<tr{cls}><td>{label}</td>' + ''.join(tds) + '</tr>')
    style = ' style="font-size:7.8pt"' if compact else ''
    return Block(f'<table class="fin"{style}><thead><tr>{h}</tr></thead><tbody>{"".join(rows)}</tbody></table>')


# ---------------------------------------------------------------- SVG primitives
def scale(lo, hi, ticks=5, zero=True):
    """Round axis: (min, max, step) with step 1, 2, 2.5 or 5 x 10^k."""
    if zero:
        lo, hi = min(0, lo), max(0, hi)
    span = (hi - lo) or abs(hi) or 1
    raw = span / (ticks - 1)
    e = 10 ** math.floor(math.log10(raw))
    step = next(m * e for m in (1, 2, 2.5, 5, 10) if m * e >= raw - 1e-12)
    a, b = math.floor(lo / step + 1e-9) * step, math.ceil(hi / step - 1e-9) * step
    return a, b, step


def svg_open(w, h, title):
    return (f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{esc(title)}" xmlns="http://www.w3.org/2000/svg" '
            f'style="font-family:{FONT};font-size:9px">')


def txt(x, y, s, anchor='start', size=9, fill=None, weight=400):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-size="{size}" fill="{fill or COL["body"]}" '
            f'font-weight="{weight}">{esc(s)}</text>')


def _tick_label(v, step, fmt):
    if fmt:
        return fmt(v)
    if step >= 1 and float(step).is_integer():
        return f'{v:,.0f}'
    return f'{v:,.{max(1, -math.floor(math.log10(step)))}f}'   # e.g. a 2.5 step shows 2.5, 7.5


def _axis(out, x0, x1, y_of, a, b, step, fmt, unit, side='left'):
    v = a
    while v <= b + step / 1e6:
        y = y_of(v)
        if side == 'left':
            out.append(f'<line x1="{x0}" x2="{x1}" y1="{y:.1f}" y2="{y:.1f}" stroke="{COL["grid"]}"/>')
            out.append(txt(x0 - 5, y + 3, _tick_label(v, step, fmt), 'end', 8.5, COL['muted']))
        else:
            out.append(txt(x1 + 5, y + 3, _tick_label(v, step, fmt), 'start', 8.5, COL['muted']))
        v += step
    if unit:
        uy = y_of(b) - 10
        out.append(txt(0 if side == 'left' else x1 + 46, uy, unit, 'start' if side == 'left' else 'end', 8.5, COL['muted']))


def _legend(out, items, x, y):
    """items: (name, colour, kind) with kind bar | bar-fc | line | dash | dot | hollow."""
    for name, color, kind in items:
        if kind in ('bar', 'bar-fc'):
            out.append(f'<rect x="{x}" y="{y - 7}" width="9" height="9" fill="{color}" '
                       f'fill-opacity="{FC_OPACITY if kind == "bar-fc" else 1}"/>')
            x2 = x + 13
        elif kind == 'hollow':
            out.append(f'<circle cx="{x + 4}" cy="{y - 3}" r="4" fill="#fff" stroke="{color}" stroke-width="1.5"/>')
            x2 = x + 12
        else:
            d = {'line': '', 'dash': ' stroke-dasharray="5 3"', 'dot': ' stroke-dasharray="1 3"'}[kind]
            out.append(f'<line x1="{x}" x2="{x + 16}" y1="{y - 3}" y2="{y - 3}" stroke="{color}" stroke-width="2"{d}/>')
            x2 = x + 20
        out.append(txt(x2, y, name, 'start', 8.5))
        x = x2 + 4.9 * len(name) + 14


def _clip(out, cid, x, y, w, h):
    out.append(f'<defs><clipPath id="{cid}"><rect x="{x}" y="{y}" width="{w}" height="{h}"/></clipPath></defs>')


def _place_labels(ys, min_gap=11, lo=-1e9, hi=1e9):
    """Label y positions without overlaps, in the input order."""
    idx = sorted(range(len(ys)), key=lambda i: ys[i])
    s = [ys[i] for i in idx]
    for k in range(1, len(s)):
        s[k] = max(s[k], s[k - 1] + min_gap)
    if s and s[-1] > hi:
        s[-1] = hi
        for k in range(len(s) - 2, -1, -1):
            s[k] = min(s[k], s[k + 1] - min_gap)
    out = [0.0] * len(ys)
    for k, i in enumerate(idx):
        out[i] = max(s[k], lo)
    return out


_CID = [0]


def _cid():
    _CID[0] += 1
    return f'c{_CID[0]}'


# ---------------------------------------------------------------- charts
def bars_chart(title, cats, series, unit, forecast_from, w=700, h=240, stacked=False, labels=True, fmt=f0, colors=None,
               growth=None, line=None, line_unit='', line_fmt=None):
    """Vertical bars (grouped or stacked); forecast columns lighter. series: [(name, values)].
    growth: optional row of strings under the category labels (e.g. y/y growth).
    line: optional (name, values) on a right-hand axis (line_unit), solid to forecast_from then dashed."""
    colors = colors or ([NAVY] if len(series) == 1 else SER)
    left, right, top = 52, (52 if line else 14), 26
    bottom = 40 + (12 if growth else 0)
    tot = [sum(s[i] for _, s in series) if stacked else max(s[i] for _, s in series) for i in range(len(cats))]
    a, b, step = scale(min(0, min(min(s) for _, s in series)), max(tot) * 1.06)
    pw, ph = w - left - right, h - top - bottom
    Y = lambda v: top + ph - ph * (v - a) / (b - a)  # noqa: E731
    n, k = len(cats), 1 if stacked else len(series)
    gw = pw / n
    bw = gw * (0.62 if k == 1 else 0.72 / k)
    out = [svg_open(w, h, title)]
    _axis(out, left, w - right, Y, a, b, step, None, unit)
    for i, cat in enumerate(cats):
        op = FC_OPACITY if i >= forecast_from else 1
        base = 0
        for j, (name, s) in enumerate(series):
            x = left + gw * i + (gw - bw * k) / 2 + (0 if stacked else bw * j)
            v0, v1 = (base, base + s[i]) if stacked else (0, s[i])
            y1, y2 = Y(max(v0, v1)), Y(min(v0, v1))
            out.append(f'<rect x="{x:.1f}" y="{y1:.1f}" width="{bw:.1f}" height="{max(y2 - y1, .5):.1f}" '
                       f'fill="{colors[j]}" fill-opacity="{op}"/>')
            if labels and not stacked:
                out.append(txt(x + bw / 2, (y1 - 3) if s[i] >= 0 else (y2 + 9), fmt(s[i]), 'middle', 8, COL['ink']))
            if stacked:
                base += s[i]
        if labels and stacked:
            out.append(txt(left + gw * i + gw / 2, Y(base) - 3, fmt(base), 'middle', 8, COL['ink'], 600))
        out.append(txt(left + gw * i + gw / 2, top + ph + 12, cat, 'middle', 8.5, COL['muted']))
        if growth:
            out.append(txt(left + gw * i + gw / 2, top + ph + 24, growth[i], 'middle', 8, COL['body']))
    if growth:
        out.append(txt(left - 5, top + ph + 24, 'y/y', 'end', 8, COL['muted']))
    if line:
        la, lb, ls = scale(min(line[1]), max(line[1]) * 1.06)
        YL = lambda v: top + ph - ph * (v - la) / (lb - la)  # noqa: E731
        _axis(out, left, w - right, YL, la, lb, ls, line_fmt, line_unit, side='right')
        pts = [(left + gw * i + gw / 2, YL(v)) for i, v in enumerate(line[1])]
        sol = ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts[:forecast_from])
        das = ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts[max(forecast_from - 1, 0):])
        if sol:
            out.append(f'<polyline points="{sol}" fill="none" stroke="{TEAL}" stroke-width="2"/>')
        if forecast_from < n:
            out.append(f'<polyline points="{das}" fill="none" stroke="{TEAL}" stroke-width="2" stroke-dasharray="5 3"/>')
        for x, y in pts:
            out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.5" fill="{TEAL}"/>')
    if forecast_from < n:
        xb = left + gw * forecast_from
        out.append(f'<line x1="{xb:.1f}" x2="{xb:.1f}" y1="{top}" y2="{top + ph}" stroke="{COL["reference"]}" '
                   f'stroke-dasharray="3 3"/>')
    leg = [(name, colors[j], 'bar') for j, (name, _) in enumerate(series)]
    if forecast_from < n:
        leg.append(('Forecast (lighter)', colors[0], 'bar-fc'))
    if line:
        leg.append((line[0] + (f' (right axis, {line_unit})' if line_unit else ''), TEAL, 'line'))
    _legend(out, leg, left, h - 3)
    out.append('</svg>')
    return Block(''.join(out))


def lines_chart(title, cats, series, unit, forecast_from, w=700, h=230, fmt=None, ymin=None, ymax=None, zero=False,
                est_until=0, label_fmt=None):
    """Lines: solid actuals, dashed from forecast_from, dotted before est_until (estimated history).
    series: [(name, values or None, colour)]; end values labelled without overlaps (leader lines when moved)."""
    left, right, top, bottom = 52, 46, 26, 40
    vals = [x for _, s, _ in series for x in s if x is not None]
    a, b, step = scale(min(vals) if ymin is None else ymin, max(vals) if ymax is None else ymax, zero=zero)
    pw, ph = w - left - right, h - top - bottom
    n = len(cats)
    X = lambda i: left + pw * (i + 0.5) / n  # noqa: E731
    Y = lambda v: top + ph - ph * (v - a) / (b - a)  # noqa: E731
    out = [svg_open(w, h, title)]
    cid = _cid()
    _clip(out, cid, left, top - 2, pw, ph + 4)
    _axis(out, left, w - right, Y, a, b, step, fmt, unit)
    for i, c in enumerate(cats):
        if c:
            out.append(txt(X(i), top + ph + 12, c, 'middle', 8.5, COL['muted']))
    ends = []
    for name, s, color in series:
        pts = [(i, y) for i, y in enumerate(s) if y is not None]
        segs = [('dot', [p for p in pts if p[0] < est_until]),
                ('solid', [p for p in pts if max(est_until - 1, 0) <= p[0] < forecast_from]),
                ('dash', [p for p in pts if p[0] >= forecast_from - 1])]
        for kind, ps in segs:
            if len(ps) < 2:
                continue
            d = {'dot': ' stroke-dasharray="1 3"', 'solid': '', 'dash': ' stroke-dasharray="5 3"'}[kind]
            out.append(f'<polyline clip-path="url(#{cid})" points="{" ".join(f"{X(i):.1f},{Y(y):.1f}" for i, y in ps)}" '
                       f'fill="none" stroke="{color}" stroke-width="2"{d}/>')
        li, ly = pts[-1]
        ends.append((X(li), Y(ly), ly, color))
    ys = _place_labels([e[1] + 3 for e in ends], 10, top + 3, top + ph + 3)
    for (x, yp, v, color), yl in zip(ends, ys):
        if abs(yl - (yp + 3)) > 1:
            out.append(f'<line x1="{x + 2:.1f}" x2="{x + 8:.1f}" y1="{yp:.1f}" y2="{yl - 3:.1f}" stroke="{color}"/>')
        out.append(txt(x + 9, yl, (label_fmt or fmt or f0)(v), 'start', 8.5, color, 600))
    if forecast_from < n:
        xb = (X(forecast_from - 1) + X(forecast_from)) / 2
        out.append(f'<line x1="{xb:.1f}" x2="{xb:.1f}" y1="{top}" y2="{top + ph}" stroke="{COL["reference"]}" '
                   f'stroke-dasharray="3 3"/>')
    leg = [(name, color, 'line') for name, _, color in series]
    if forecast_from < n:
        leg.append(('Forecast', COL['muted'], 'dash'))
    if est_until:
        leg.append(('Estimated history', COL['muted'], 'dot'))
    _legend(out, leg, left, h - 3)
    out.append('</svg>')
    return Block(''.join(out))


def football_field(title, price, cases, money_fmt, w=700, h=None, price_label='Price'):
    """Scenario bars from the current price to each target. cases: [(name, target, return)]."""
    h = h or 44 + 26 * len(cases)
    left, right, top = 60, 30, 26
    vals = [price] + [c[1] for c in cases]
    span = max(vals) - min(vals)
    lo, hi, step = scale(min(vals) - span * 0.45, max(vals) + span * 0.25, zero=False)
    lo = max(lo, 0)
    X = lambda v: left + (w - left - right) * (v - lo) / (hi - lo)  # noqa: E731
    out = [svg_open(w, h, title)]
    v = lo
    while v <= hi + step / 1e6:
        out.append(f'<line x1="{X(v):.1f}" x2="{X(v):.1f}" y1="{top - 4}" y2="{h - 16}" stroke="{COL["grid"]}"/>')
        out.append(txt(X(v), h - 4, money_fmt(v), 'middle', 8.5, COL['muted']))
        v += step
    for i, (name, tgt, ret) in enumerate(cases):
        y = top + 26 * i
        color = SCEN.get(name.lower(), NAVY)
        x1, x2 = sorted([X(price), X(tgt)])
        out.append(f'<rect x="{x1:.1f}" y="{y:.1f}" width="{max(x2 - x1, 2):.1f}" height="14" fill="{color}"/>')
        out.append(txt(4, y + 10.5, name, 'start', 9, COL['ink'], 600))
        tx, anc = (x2 + 5, 'start') if tgt >= price else (x1 - 5, 'end')
        out.append(txt(tx, y + 10.5, f'{money_fmt(tgt)} ({ret * 100:+.0f}%)', anc, 8.5, COL['ink'], 600))
    out.append(f'<line x1="{X(price):.1f}" x2="{X(price):.1f}" y1="{top - 8}" y2="{h - 16}" stroke="{COL["ink"]}" '
               f'stroke-width="1.5"/>')
    out.append(txt(X(price), top - 11, f'{price_label} {money_fmt(price)}', 'middle', 8.5, COL['ink'], 600))
    out.append('</svg>')
    return Block(''.join(out))


def tornado(title, base, items, money_fmt, w=700, h=None, base_label='Base target'):
    """Target price under one change at a time. items: [(label, target)], sorted by distance from the base."""
    items = sorted(items, key=lambda x: -abs(x[1] - base))
    h = h or 40 + 16 * len(items)
    left, right, top = 230, 50, 22
    vals = [t for _, t in items] + [base]
    span = max(vals) - min(vals)
    lo, hi, step = scale(min(vals) - span * 0.25, max(vals) + span * 0.15, zero=False)
    X = lambda v: left + (w - left - right) * (v - lo) / (hi - lo)  # noqa: E731
    out = [svg_open(w, h, title)]
    v = lo
    while v <= hi + step / 1e6:
        out.append(f'<line x1="{X(v):.1f}" x2="{X(v):.1f}" y1="{top - 4}" y2="{h - 16}" stroke="{COL["grid"]}"/>')
        out.append(txt(X(v), h - 4, money_fmt(v), 'middle', 8.5, COL['muted']))
        v += step
    for i, (lab, t) in enumerate(items):
        y = top + 16 * i
        x1, x2 = sorted([X(base), X(t)])
        out.append(f'<rect x="{x1:.1f}" y="{y:.1f}" width="{max(x2 - x1, 1):.1f}" height="11" '
                   f'fill="{RED if t < base else GREEN}"/>')
        out.append(txt(left - 6, y + 9.5, lab, 'end', 8.5))
        out.append(txt((x1 - 4) if t < base else (x2 + 4), y + 9.5, money_fmt(t), 'end' if t < base else 'start', 8.5,
                       COL['ink']))
    out.append(f'<line x1="{X(base):.1f}" x2="{X(base):.1f}" y1="{top - 6}" y2="{h - 16}" stroke="{COL["ink"]}"/>')
    out.append(txt(X(base), top - 9, f'{base_label} {money_fmt(base)}', 'middle', 8.5, COL['ink'], 600))
    out.append('</svg>')
    return Block(''.join(out))


def band_chart(title, cats, vals, refs, end_label, w=700, h=220, label_if=lambda c: c.endswith('-01'), ymin=None, ymax=None,
               unit='x forward P/E'):
    """Forward-multiple history with reference lines labelled in the right margin. refs: [(value, label, colour)]."""
    left, right, top, bottom = 52, 100, 24, 26
    a, b, step = scale(min(vals + [r[0] for r in refs]) if ymin is None else ymin, max(vals) if ymax is None else ymax,
                       zero=False)
    a = max(a, 0)
    X = lambda i: left + (w - left - right) * i / (len(vals) - 1)  # noqa: E731
    Y = lambda y: top + (h - top - bottom) * (1 - (y - a) / (b - a))  # noqa: E731
    out = [svg_open(w, h, title)]
    _axis(out, left, w - right, Y, a, b, step, lambda v: f'{v:g}x', unit)
    out.append(f'<polyline points="{" ".join(f"{X(i):.1f},{Y(v):.1f}" for i, v in enumerate(vals))}" fill="none" '
               f'stroke="{NAVY}" stroke-width="1.8"/>')
    for i, c in enumerate(cats):
        if label_if(c):
            out.append(txt(X(i), h - bottom + 12, c[:4], 'middle', 8.5, COL['muted']))
    ys = _place_labels([Y(v) + 3 for v, _, _ in refs] + [Y(vals[-1]) + 3], 10, top, h - bottom)
    for (yv, lab, col), yl in zip(refs, ys):
        out.append(f'<line x1="{left}" x2="{w - right}" y1="{Y(yv):.1f}" y2="{Y(yv):.1f}" stroke="{col}" '
                   f'stroke-dasharray="5 3"/>')
        out.append(txt(w - right + 6, yl, lab, 'start', 8.5, col, 600))
    out.append(f'<circle cx="{X(len(vals) - 1):.1f}" cy="{Y(vals[-1]):.1f}" r="3" fill="{TEAL}"/>')
    out.append(txt(w - right + 6, ys[-1], end_label, 'start', 8.5, TEAL, 600))
    out.append('</svg>')
    return Block(''.join(out))


def waterfall(title, items, unit, w=700, h=230, fmt=f1, scale_by=1.0, yr=None):
    """Bridge; optional explicit (min, max, tick) range marks a nonzero axis. A table is also a valid small-step view."""
    if not items or scale_by <= 0:
        raise ValueError('A waterfall needs items and a positive scale')
    left, right, top, bottom = 52, 14, 26, 32
    run, levels = 0.0, []
    for _, v, kind in items:
        run = v if kind == 'total' else run + v
        levels.append(run / scale_by)
    a, b, step = yr or scale(min(0, min(levels)), max(0, max(levels)) * 1.1)
    if not all(math.isfinite(x) for x in (a, b, step)) or b <= a or step <= 0:
        raise ValueError('Invalid waterfall axis range')
    pw, ph = w - left - right, h - top - bottom
    gw = pw / len(items)
    bw = gw * 0.58
    Y = lambda v: top + ph - ph * (v - a) / (b - a)  # noqa: E731
    out = [svg_open(w, h, title)]
    cid = _cid()
    _clip(out, cid, left, top, pw, ph)
    _axis(out, left, w - right, Y, a, b, step, None, unit)
    if a != 0:
        out.append(txt(w - right, 12, f'Axis starts at {fmt(a)}; totals truncated', 'end', 9, COL['muted']))
        out.append(f'<path d="M{left-4},{top+ph-8} l8,-4 l-8,-4 l8,-4" fill="none" stroke="{GREY}"/>')
    run = 0.0
    for i, (lab, v, kind) in enumerate(items):
        x = left + gw * i + (gw - bw) / 2
        if kind == 'total':
            lo_, hi_, col = 0, v / scale_by, NAVY
            run = v / scale_by
        else:
            lo_, hi_ = sorted([run, run + v / scale_by])
            col = GREEN if v >= 0 else RED
            run += v / scale_by
        out.append(f'<rect clip-path="url(#{cid})" x="{x:.1f}" y="{Y(hi_):.1f}" width="{bw:.1f}" height="{max(Y(lo_) - Y(hi_), .5):.1f}" fill="{col}"/>')
        lab_v = fmt(v / scale_by) if kind == 'total' else f'{"+" if v >= 0 else "-"}{fmt(abs(v) / scale_by)}'
        out.append(txt(x + bw / 2, Y(hi_) - 3, lab_v, 'middle', 8.5, COL['ink'], 600 if kind == 'total' else 400))
        for j, part in enumerate(lab.split('|')):
            out.append(txt(x + bw / 2, top + ph + 12 + 10 * j, part, 'middle', 8.5, COL['muted']))
    out.append('</svg>')
    return Block(''.join(out))


def scatter(title, points, xlab, ylab, xfmt, yfmt, lines=(), w=700, h=260, xr=None, yr=None):
    """points: [(label, x, y, colour, hollow)]; lines: [(slope, label, colour)] through the origin, clipped to the plot
    and labelled at their right end. Labels sit right of their points; moved labels get leader lines."""
    left, right, top, bottom = 52, 150, 24, 34
    xa, xb, xs_ = xr or scale(0, max(p[1] for p in points) * 1.1)
    ya, yb, ys_ = yr or scale(0, max(p[2] for p in points) * 1.1)
    pw, ph = w - left - right, h - top - bottom
    X = lambda v: left + pw * (v - xa) / (xb - xa)  # noqa: E731
    Y = lambda v: top + ph - ph * (v - ya) / (yb - ya)  # noqa: E731
    out = [svg_open(w, h, title)]
    cid = _cid()
    _clip(out, cid, left, top, pw, ph)
    _axis(out, left, left + pw, Y, ya, yb, ys_, yfmt, ylab)
    v = xa
    while v <= xb + xs_ / 1e6:
        out.append(txt(X(v), top + ph + 12, xfmt(v), 'middle', 8.5, COL['muted']))
        v += xs_
    out.append(txt(left + pw, top + ph + 26, xlab, 'end', 8.5, COL['muted']))
    line_y = []
    for slope, lab, col in lines:
        out.append(f'<line clip-path="url(#{cid})" x1="{X(0):.1f}" y1="{Y(0):.1f}" x2="{X(xb):.1f}" y2="{Y(slope * xb):.1f}" '
                   f'stroke="{col}" stroke-dasharray="5 3"/>')
        x_end = min(xb, yb / slope) if slope > 0 else xb
        line_y.append((X(x_end), Y(slope * x_end), lab, col))
    for x, y, lab, col in line_y:
        out.append(txt(left + pw + 6, min(max(y, top + 8), top + ph), lab, 'start', 8.5, col, 600))
    # point labels in the right margin when crowded, otherwise beside the point
    lab_y = _place_labels([Y(p[2]) + 3 for p in points], 11, top + 3, top + ph + 3)
    for (name, x, y, col, hollow), ly in zip(points, lab_y):
        cx, cy = X(x), Y(y)
        out.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="4.5" fill="{"#fff" if hollow else col}" stroke="{col}" '
                   f'stroke-width="1.5"/>')
        if abs(ly - (cy + 3)) > 1:
            out.append(f'<line x1="{cx + 5:.1f}" x2="{cx + 12:.1f}" y1="{cy:.1f}" y2="{ly - 3:.1f}" stroke="{COL["muted"]}" '
                       f'stroke-width=".7"/>')
        out.append(txt(cx + 13, ly, name, 'start', 8.5, col, 600 if col != NAVY else 400))
    out.append('</svg>')
    return Block(''.join(out))


def _days(d):
    return int(d[:4]) * 372 + int(d[5:7]) * 31 + int(d[8:10])


def price_chart(title, dates, series, events=(), w=700, h=210, unit='Indexed, start = 100', print_width_mm=180):
    """Indexed prices with collision-placed event labels and a readable print size. Front placement adapts to 110mm."""
    if len(dates) < 2 or not series or any(len(s) != len(dates) for _, s, _ in series):
        raise ValueError('Price series must match at least two dates')
    if print_width_mm <= 0:
        raise ValueError('Print width must be positive')
    fs = max(9, 7.2 * w / (print_width_mm * 72 / 25.4))
    left, right = fs * 3.5, 12
    pw = w - left - right
    n = len(dates)
    X = lambda i: left + pw * i / (n - 1)  # noqa: E731
    # Each row is a set of nonoverlapping horizontal intervals, not odd/even staggering.
    rows, placed, row_heights = [], [], []
    for d, lab in sorted(events):
        i = min(range(n), key=lambda j: abs(_days(dates[j]) - _days(d)))
        lines = textwrap.wrap(lab, width=max(1, int((pw - 8) / (fs * .62)))) or ['']
        width = min(pw, fs * .62 * max(map(len, lines)) + 4)
        x = min(max(X(i) - width / 2, left), w - right - width)
        row = next((j for j, intervals in enumerate(rows)
                    if all(x + width + 8 <= a or x >= b + 8 for a, b in intervals)), len(rows))
        if row == len(rows):
            rows.append([]); row_heights.append(0)
        row_heights[row] = max(row_heights[row], len(lines) * (fs + 5))
        rows[row].append((x, x + width))
        placed.append((i, lines, x + width / 2, row))
    label_top = 2 * fs + 5
    top = label_top + sum(row_heights) + 6
    legend, lx, lr = [], left, 0
    for name, _, col in series:
        width = 22 + fs * .55 * len(name)
        if lx > left and lx + width > w - right:
            lx, lr = left, lr + 1
        legend.append((name, col, lx, lr))
        lx += width + 14
    bottom = fs * 2 + (lr + 1) * (fs + 5) + 6
    h = max(h, top + bottom + 105)
    vals = [v for _, s, _ in series for v in s]
    a, b, step = scale(min(vals) * 0.97, max(vals) * 1.03, zero=False)
    ph = h - top - bottom
    Y = lambda v: top + ph - ph * (v - a) / (b - a)  # noqa: E731
    out = [svg_open(w, h, title)]
    v = a
    while v <= b + step / 1e6:
        out.append(f'<line x1="{left}" x2="{w-right}" y1="{Y(v)}" y2="{Y(v)}" stroke="{COL["grid"]}"/>')
        out.append(txt(left - 6, Y(v) + fs / 3, _tick_label(v, step, None), 'end', fs, COL['muted']))
        v += step
    out.append(txt(0, fs, unit, 'start', fs, COL['muted']))
    seen = set()
    for i, d in enumerate(dates):
        if d[:7] not in seen and int(d[5:7]) % 3 == 1:
            seen.add(d[:7])
            anchor = 'end' if X(i) > w - right - 45 else 'start'
            out.append(txt(X(i), top + ph + fs + 3, f'{["Jan", "Apr", "Jul", "Oct"][(int(d[5:7]) - 1) // 3]} {d[2:4]}', anchor,
                           fs, COL['muted']))
    for name, s, col in series:
        out.append(f'<polyline points="{" ".join(f"{X(i):.1f},{Y(v):.1f}" for i, v in enumerate(s))}" fill="none" '
                   f'stroke="{col}" stroke-width="{1.8 if col == TEAL else 1.2}"/>')
    s0 = series[0][1]
    for i, lines, label_x, row in placed:
        cx, cy = X(i), Y(s0[i])
        ly = label_top + sum(row_heights[:row])
        last_y = ly + (len(lines) - 1) * (fs + 5)
        out.append(f'<line x1="{label_x:.1f}" x2="{cx:.1f}" y1="{last_y + 2:.1f}" y2="{cy - 4:.1f}" stroke="{COL["muted"]}" '
                   f'stroke-dasharray="2 2"/>')
        out.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="2.8" fill="{TEAL}"/>')
        for j, line in enumerate(lines):
            out.append(txt(label_x, ly + j * (fs + 5), line, 'middle', fs, COL['ink']))
    for name, col, x, row in legend:
        y = top + ph + 2 * fs + 8 + row * (fs + 5)
        out.append(f'<line x1="{x}" x2="{x+16}" y1="{y-fs/3}" y2="{y-fs/3}" stroke="{col}" stroke-width="2"/>')
        out.append(txt(x + 22, y, name, 'start', fs))
    out.append('</svg>')
    result = Block(''.join(out))
    result.narrow = lambda: price_chart(title, dates, series, events, w, h, unit, 110)
    return result


def flow_diagram(title, nodes, edges, w=700, h=156):
    """Business model. nodes: [(title, subtitle)] left to right; edges: [(i, j, kind, label)] between adjacent nodes,
    kind 'goods' (solid navy, lower arrow, label below) or 'cash' (dashed teal, upper arrow, label above)."""
    n = len(nodes)
    gap = 40
    bw = (w - gap * (n - 1)) / n
    bx = lambda i: i * (bw + gap)  # noqa: E731
    yb, hb = 40, 50
    out = [svg_open(w, h, title)]
    for kind, col in [('goods', NAVY), ('cash', TEAL)]:
        out.append(f'<defs><marker id="m{kind}" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto">'
                   f'<path d="M0,0 L7,3.5 L0,7 z" fill="{col}"/></marker></defs>')
    for i, (t, sub) in enumerate(nodes):
        out.append(f'<rect x="{bx(i) + 1:.1f}" y="{yb}" width="{bw - 2:.1f}" height="{hb}" rx="4" fill="#F3F5F7" '
                   f'stroke="{COL["grid"]}"/>')
        out.append(txt(bx(i) + bw / 2, yb + 21, t, 'middle', 9.5, COL['ink'], 600))
        out.append(txt(bx(i) + bw / 2, yb + 35, sub, 'middle', 8, COL['muted']))
    for i, j, kind, lab in edges:
        col = NAVY if kind == 'goods' else TEAL
        y = yb + hb - 12 if kind == 'goods' else yb + 12
        x1 = bx(i) + bw - 1 if j > i else bx(i) + 1
        x2 = bx(j) + 1 if j > i else bx(j) + bw - 1
        d = '' if kind == 'goods' else ' stroke-dasharray="4 3"'
        out.append(f'<line x1="{x1:.1f}" x2="{x2:.1f}" y1="{y}" y2="{y}" stroke="{col}" stroke-width="1.6"{d} '
                   f'marker-end="url(#m{kind})"/>')
        mx = (x1 + x2) / 2
        ly = yb + hb + 16 if kind == 'goods' else yb - 9
        out.append(f'<line x1="{mx:.1f}" x2="{mx:.1f}" y1="{y}" y2="{ly - 8 if kind == "goods" else ly + 3}" '
                   f'stroke="{col}" stroke-width=".7"/>')
        out.append(txt(mx, ly, lab, 'middle', 8, col))
    _legend(out, [('Goods or power', NAVY, 'line'), ('Cash', TEAL, 'dash')], 2, h - 3)
    out.append('</svg>')
    return Block(''.join(out))


# ---------------------------------------------------------------- print and inspect
def print_pdf(html_path, pdf_path, chrome=None):
    """Print the HTML to an A4 PDF with headless Chrome (list arguments, so paths with spaces work)."""
    chrome = chrome or os.environ.get('CHROME_PATH') or next(
        (p for p in [r'C:\Program Files\Google\Chrome\Application\chrome.exe',
                     r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
                     shutil.which('google-chrome'), shutil.which('chromium'), shutil.which('chrome')] if p and Path(p).exists()),
        None)
    if not chrome:
        raise SystemExit('Chrome not found: set CHROME_PATH')
    pdf_path = Path(pdf_path).resolve()
    tmp = pdf_path.with_name(pdf_path.stem + '.printing.pdf')
    tmp.unlink(missing_ok=True)
    subprocess.run([chrome, '--headless=new', '--disable-gpu', '--no-pdf-header-footer', f'--print-to-pdf={tmp}',
                    Path(html_path).resolve().as_uri()], check=True, capture_output=True, timeout=180)
    if not tmp.exists() or tmp.stat().st_size == 0:
        raise SystemExit(f'PDF not written: {tmp}')
    try:
        os.replace(tmp, pdf_path)
    except PermissionError:
        # the existing file is open elsewhere: keep it and save a dated copy instead of failing silently
        import time
        alt = pdf_path.with_name(pdf_path.stem + time.strftime('_%Y%m%d-%H%M') + '.pdf')
        os.replace(tmp, alt)
        print(f'{pdf_path.name} is open elsewhere; saved {alt.name}')
        return alt
    return pdf_path


def inspect_pdf(pdf_path, image_dir=None, dpi=100):
    """Facts for the author's page-by-page look: share of the text area left blank below the content, and whether the
    page ends on a heading. Optionally writes page images. It reports; it does not judge the report."""
    import fitz  # PyMuPDF
    doc = fitz.open(str(pdf_path))
    mm = 72 / 25.4
    out = []
    for i, page in enumerate(doc):
        area = fitz.Rect(15 * mm, 18 * mm, page.rect.width - 15 * mm, page.rect.height - 18 * mm)
        blocks = [b for b in page.get_text('dict')['blocks'] if b.get('type') == 0 and fitz.Rect(b['bbox']).intersects(area)]
        draws = [d['rect'] for d in page.get_drawings() if d['rect'].intersects(area)
                 and d['rect'].height < area.height * 0.9]
        bottom = max([b['bbox'][3] for b in blocks] + [r.y1 for r in draws] + [area.y0])
        last = None
        if blocks:
            b = max(blocks, key=lambda b: b['bbox'][3])
            spans = [s for ln in b['lines'] for s in ln['spans']]
            last = spans[0] if spans else None
        heading = bool(last and last['size'] >= 9.9 and ('SemiBold' in last['font'] or 'Bold' in last['font']
                                                         or last['flags'] & 16))
        out.append({'page': i + 1, 'blankBelowContent': round(max(0.0, area.y1 - bottom) / area.height, 2),
                    'endsWithHeading': heading})
        if image_dir:
            Path(image_dir).mkdir(parents=True, exist_ok=True)
            page.get_pixmap(dpi=dpi).save(str(Path(image_dir) / f'page_{i + 1}.png'))
    return out


def package(study, zip_path, report_html, brief_html, files, revise=False, **record):
    """Validate the rendered HTML against the calculated model, print the PDFs from those exact files, and write
    deliverables/release.json and the zip only when every release check passes.

    package(ROOT, OUT / 'Company_initiation_2026-11-06.zip', OUT / 'Company_initiation.html', OUT / 'Company_brief.html',
            [OUT / 'Company_model.xlsx'],
            cutoff='2026-11-06', fiscalYearEnd=12, priceDate='2026-11-05', consensusDate='2026-11-06',
            security='2020.HK', currency='HKD', method='P/E', epsPeriod='FY2027E',
            latestPublished={'period': '3Q26', 'kind': 'operating update', 'date': '2026-10-21', 'coversThirdQuarter': True},
            spec='model/spec.json', workbook='deliverables/Company_model.xlsx', brief='deliverables/brief.json',
            bindings={'referencePrice': 'Valuation!D20', 'target': 'Valuation!D37', 'targetMultiple': 'Valuation!D35',
                      'forwardEps': 'Valuation!D27', 'forwardEpsSource': 'Statements!I43', 'forwardEpsHeader': 'Statements!I5',
                      'fx': 'Valuation!D21', 'dividendYield': 'Valuation!D40', 'rating': 'Valuation!D42',
                      'bearTarget': 'Valuation!F50', 'bullTarget': 'Valuation!F52'},
            contacts=[], byline=None)

    For an NTM basis pass epsPeriod='NTM' and ntm={'start', 'end', 'components': [{'period', 'weight', 'eps', 'header'}]}.
    Paths in the record are relative to the study folder; bindings are logical addresses as in the specification.
    First call without a review prints drafts, performs integrity checks and creates a partial review packet;
    it exits awaiting-review with no ZIP. After an actual fresh-reader review, finalization verifies the exact
    reviewed PDF bytes without reprinting. After a correction, call the same adapter with revise=True: it reprints,
    reruns every integrity check with the bindings passed now (never the saved record's), archives the review and
    opens the next draft version. The reader starts a bounded attempt with publication_review.py begin;
    re-rendering an unreviewed draft alone does not consume an attempt. Pass the routed researchMode
    (initiation, regular-review, earnings-update or catalyst-update) in the release record.
    The PDFs take the HTML file names with .pdf. The attempt starts by removing the previous zip and marking the record
    in progress; on any failure or error, in validation or in packaging, the record says failed with the reason, no zip
    or partial zip exists, and SystemExit is raised. The validated record is written last, atomically. Draft files stay
    on disk; they are not a validated release. Distribution outside this call is not checked."""
    import traceback, zipfile
    import release_check as rc
    import publication_review as pr
    study, zip_path = Path(study), Path(zip_path)
    out_dir = study / 'deliverables'
    if zip_path.suffix.lower() != '.zip' or not zip_path.resolve().is_relative_to(out_dir.resolve()):
        raise ValueError('The release ZIP must be inside the study deliverables folder')
    out_dir.mkdir(exist_ok=True)
    rel = lambda p: Path(p).resolve().relative_to(study.resolve()).as_posix()  # noqa: E731
    record = dict(record, review=record.get('review', pr.DEFAULT_PATH), zipPath=rel(zip_path), reviewPolicyVersion='1.0',
                  decisionRecord=record.get('decisionRecord','evidence/decision.json'))
    record_path = out_dir / 'release.json'
    tmp_zip = zip_path.with_suffix('.partial.zip')

    def write_record(payload):
        tmp = record_path.with_suffix('.json.tmp')
        tmp.write_text(json.dumps(payload, indent=1, ensure_ascii=False, default=str) + '\n', encoding='utf-8')
        tmp.replace(record_path)

    def fail(reason, checks=None):
        for p in (zip_path, tmp_zip):
            p.unlink(missing_ok=True)
        try:
            write_record(dict(record, checks=checks or [], status='failed', error=reason, scope=rc.SCOPE))
        except OSError as exc:
            reason += f'\n  (failure record could not be written: {exc})'
        raise SystemExit('Release check failed; no package written:\n  ' + reason)

    # A refused operation must not remove a package, rewrite a record or reprint reviewed bytes.
    review_exists = pr.local(study, record['review']).is_file()
    if revise or not review_exists:
        pr.preflight(study,record,revise=revise)
    # Supersede only after eligibility is established.
    zip_path.unlink(missing_ok=True)
    tmp_zip.unlink(missing_ok=True)
    try:
        write_record(dict(record, status='in-progress', scope=rc.SCOPE))
    except OSError as exc:
        raise SystemExit(f'Release attempt could not start: {exc}')

    checks, fails, deliverables = [], [], []
    try:
        review_exists = pr.local(study, record['review']).is_file()
        # Render once before the fresh review. Finalization publishes those exact reviewed PDFs;
        # reprinting would change bytes and invalidate the visual review's provenance.
        report_pdf, brief_pdf = Path(report_html).with_suffix('.pdf'), Path(brief_html).with_suffix('.pdf')
        if revise and not review_exists:
            raise ValueError('revise=True needs an existing review to archive; make the first call without it')
        draft = revise or not review_exists
        deliverables = [Path(report_pdf), Path(brief_pdf)] + [Path(f) for f in files]
        record = dict(record, deliverables=[rel(p) for p in deliverables], briefPdf=rel(brief_pdf),
                      renders={'report': {'html': rel(report_html), 'pdf': rel(report_pdf)},
                               'brief': {'html': rel(brief_html), 'pdf': rel(brief_pdf)}})
        for key in ('spec', 'workbook', 'brief'):
            record[key] = rel(study / record[key]) if not Path(record[key]).is_absolute() else rel(record[key])
        record.pop('fingerprints', None)   # a new build is checked on its own files, then fingerprinted
        if draft:
            from draft_transaction import render
            checks=render(study,record)
            review_path = pr.prepare(study, record, revise=revise)
            write_record(dict(record, checks=checks, status='awaiting-review', scope=rc.SCOPE))
            raise SystemExit(f'Draft PDFs ready; no release ZIP. A fresh reviewer must complete {review_path}, then run '
                             f'publication_review.py finalize "{study}". Do not fabricate review completion.')
        checks, fails = rc.run(study, record)
        if fails:
            fail('\n  '.join(fails), checks)
        out = dict(record, checks=checks, fingerprints=rc.fingerprints(study, record), status='validated', scope=rc.SCOPE)
        with zipfile.ZipFile(tmp_zip, 'w', zipfile.ZIP_DEFLATED) as z:
            for p in deliverables:
                z.write(p, p.name)
        tmp_zip.replace(zip_path)
        write_record(out)
    except SystemExit:
        raise
    except Exception as exc:  # noqa: BLE001 - any error anywhere in the attempt is a failed attempt, never a silent pass
        fail(f'{type(exc).__name__}: {exc}\n' + traceback.format_exc(limit=3), checks)
    print(f'release validated: {len(checks)} checks passed; {zip_path.name} written')
    return out
