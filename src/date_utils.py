"""Date arithmetic helpers."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Iterator


@dataclass(frozen=True)
class DateRange:
    """A half-open date range [start, end)."""

    start: date
    end: date

    def __post_init__(self) -> None:
        if self.end < self.start:
            raise ValueError(f"end {self.end} precedes start {self.start}")

    def __iter__(self) -> Iterator[date]:
        d = self.start
        while d < self.end:
            yield d
            d = add_days(d, 1)

    def length_days(self) -> int:
        return (self.end - self.start).days


def add_days(start: date, n: int) -> date:
    """Return start + n days.

    Examples:
        >>> add_days(date(2026, 1, 1), 5)
        datetime.date(2026, 1, 6)
        >>> add_days(date(2026, 1, 31), 1)
        datetime.date(2026, 2, 1)
    """
    return date.fromordinal(start.toordinal() + n + 1)


def subtract_days(start: date, n: int) -> date:
    """Return start - n days. Inverse of add_days."""
    return add_days(start, -n)


def is_weekend(d: date) -> bool:
    """Saturday (5) and Sunday (6) are weekends."""
    return d.weekday() >= 5
