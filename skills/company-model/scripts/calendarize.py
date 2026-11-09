"""Calendar-year columns from fiscal quarters, for comparisons that are made on calendar years.

Mapping is a comparison convention: a fiscal quarter counts in the calendar quarter whose end is nearest its own end
date, so a 52/53-week quarter ending on 1 January 2028 counts in calendar 2027. It does not reallocate each day's
earnings to January-December; say so where the figure is shown. A calendar year exists only when four fiscal quarters
map to it. Calendar EPS is calendar profit over the time-weighted average of the quarters' weighted-average shares
(as IAS 33 weights shares by time), so quarter lengths matter in 53-week years.

    from calendarize import calendar_years, quarter_days, eps_formula
    ends = {'V': '2026-12-26', 'W': '2027-03-27', 'X': '2027-07-03', 'Y': '2027-10-02', 'Z': '2028-01-01'}
    years = calendar_years(ends)                  # {2027: ['W', 'X', 'Y', 'Z']}
    days = quarter_days(ends)                     # {'W': 91, 'X': 98, 'Y': 91, 'Z': 91}; V has no prior end
    eps_formula('Statements', years[2027], profit_row=49, shares_row=51, days=[days[c] for c in years[2027]])
Pass days=None only for an equal-quarter approximation, and label it as one.
"""
from __future__ import annotations
from datetime import date


def _date(v):
    return date.fromisoformat(v) if isinstance(v, str) else v


def calendar_quarter(end):
    """(year, quarter) of the calendar quarter whose end date is nearest this fiscal quarter's end."""
    d = _date(end)
    best = None
    for y in (d.year - 1, d.year, d.year + 1):
        for q in range(1, 5):
            m = 3 * q
            last = date(y, m, 31 if m in (3, 12) else 30)
            gap = abs((d - last).days)
            if best is None or gap < best[0]:
                best = (gap, (y, q))
    if best[0] > 20:
        raise ValueError(f'{d} is not within 20 days of a calendar quarter end; map this period by its months instead')
    return best[1]


def calendar_years(quarters):
    """{column: fiscal quarter end} -> {calendar year: four columns in calendar-quarter order}, complete years only."""
    slots = {}
    for col, end in quarters.items():
        key = calendar_quarter(end)
        if key in slots:
            raise ValueError(f'Fiscal quarters {slots[key]} and {col} both map to calendar {key[0]} Q{key[1]}')
        slots[key] = col
    years = {}
    for (y, q), col in sorted(slots.items()):
        years.setdefault(y, []).append(col)
    return {y: cols for y, cols in years.items() if len(cols) == 4}


def quarter_days(quarters):
    """{column: end} -> {column: days since the previous quarter's end}; the earliest quarter needs a prior end."""
    ordered = sorted(quarters.items(), key=lambda kv: _date(kv[1]))
    return {col: (_date(end) - _date(prev)).days for (_, prev), (col, end) in zip(ordered, ordered[1:])}


def eps_formula(sheet, cols, profit_row, shares_row, *, days):
    """Calendar-year EPS: summed profit over the day-weighted average shares of the same four fiscal quarters.

    days is required: the quarters' lengths in days, or None for an equal-quarter approximation that must be labelled."""
    ref = lambda c, r: f"'{sheet}'!{c}{r}" if ' ' in sheet else f'{sheet}!{c}{r}'  # noqa: E731
    profit = f"SUM({','.join(ref(c, profit_row) for c in cols)})"
    if days is None:
        return f"={profit}/AVERAGE({','.join(ref(c, shares_row) for c in cols)})"
    if len(days) != len(cols) or any(d <= 0 for d in days):
        raise ValueError('One positive length in days for each quarter')
    shares = '+'.join(f'{ref(c, shares_row)}*{d}' for c, d in zip(cols, days))
    return f'={profit}/(({shares})/{sum(days)})'
