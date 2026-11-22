"""Parse CLI-style date-range strings."""
from __future__ import annotations

from datetime import date, datetime

from src.date_utils import DateRange, add_days


def parse_iso_date(s: str) -> date:
    """Parse YYYY-MM-DD. Raises ValueError on bad input."""
    return datetime.strptime(s, "%Y-%m-%d").date()


def parse_date_range(spec: str) -> DateRange:
    """Parse 'YYYY-MM-DD..YYYY-MM-DD' or 'YYYY-MM-DD+Nd' into a DateRange.

    Examples:
        >>> parse_date_range('2026-01-01..2026-01-08').length_days()
        7
        >>> parse_date_range('2026-01-01+7d').length_days()
        7
    """
    if ".." in spec:
        left, right = spec.split("..", 1)
        return DateRange(start=parse_iso_date(left), end=parse_iso_date(right))
    if "+" in spec and spec.endswith("d"):
        left, right = spec.split("+", 1)
        start = parse_iso_date(left)
        return DateRange(start=start, end=add_days(start, int(right[:-1])))
    raise ValueError(f"unrecognized date-range spec: {spec!r}")
