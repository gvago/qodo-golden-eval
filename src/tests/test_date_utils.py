"""Tests for date_utils and parser."""
from __future__ import annotations

import unittest
from datetime import date

from src.date_utils import DateRange, add_days, is_weekend, subtract_days, weeks_between
from src.parser import parse_date_range


class TestAddDays(unittest.TestCase):
    def test_add_days_zero_delta_returns_same_date(self) -> None:
        self.assertEqual(add_days(date(2026, 1, 1), 0), date(2026, 1, 1))

    def test_add_days_positive_delta_moves_forward(self) -> None:
        self.assertEqual(add_days(date(2026, 1, 1), 5), date(2026, 1, 6))

    def test_add_days_negative_delta_moves_back(self) -> None:
        self.assertEqual(add_days(date(2026, 1, 10), -3), date(2026, 1, 7))

    def test_add_days_crosses_leap_day(self) -> None:
        self.assertEqual(add_days(date(2024, 2, 28), 1), date(2024, 2, 29))

    def test_subtract_days_inverts_add_days(self) -> None:
        self.assertEqual(subtract_days(add_days(date(2026, 6, 15), 7), 7), date(2026, 6, 15))


class TestIsWeekend(unittest.TestCase):
    def test_is_weekend_saturday_and_sunday_are_weekend(self) -> None:
        self.assertTrue(is_weekend(date(2026, 1, 3)))
        self.assertTrue(is_weekend(date(2026, 1, 4)))

    def test_is_weekend_monday_is_not_weekend(self) -> None:
        self.assertFalse(is_weekend(date(2026, 1, 5)))


class TestDateRange(unittest.TestCase):
    def test_date_range_iterates_each_day_excluding_end(self) -> None:
        r = DateRange(start=date(2026, 1, 1), end=date(2026, 1, 4))
        self.assertEqual(list(r), [date(2026, 1, 1), date(2026, 1, 2), date(2026, 1, 3)])

    def test_date_range_inverted_bounds_raise_value_error(self) -> None:
        with self.assertRaises(ValueError):
            DateRange(start=date(2026, 1, 8), end=date(2026, 1, 1))

    def test_parse_date_range_plus_days_spec_sets_end(self) -> None:
        self.assertEqual(parse_date_range("2026-01-01+7d").end, date(2026, 1, 8))


class TestWeeksBetween(unittest.TestCase):
    def test_weeks_between_two_weeks_apart_returns_two(self) -> None:
        self.assertEqual(weeks_between(date(2026, 1, 1), date(2026, 1, 15)), 2)

    def test_weeks_between_partial_week_rounds_toward_zero(self) -> None:
        self.assertEqual(weeks_between(date(2026, 1, 1), date(2026, 1, 13)), 1)

    def test_weeks_between_reversed_dates_returns_negative(self) -> None:
        self.assertEqual(weeks_between(date(2026, 1, 15), date(2026, 1, 1)), -2)

    def test_weeks_between_reversed_partial_week_rounds_toward_zero(self) -> None:
        self.assertEqual(weeks_between(date(2026, 1, 13), date(2026, 1, 1)), -1)


if __name__ == "__main__":
    unittest.main()
