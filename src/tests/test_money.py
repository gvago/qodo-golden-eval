"""Tests for money."""
from __future__ import annotations

import unittest
from decimal import Decimal

from src.money import format_amount


class TestFormatAmount(unittest.TestCase):
    def test_format_amount_half_cent_rounds_up(self) -> None:
        self.assertEqual(format_amount(Decimal("12.345")), "12.35 USD")

    def test_format_amount_negative_whole_number_pads_cents(self) -> None:
        self.assertEqual(format_amount(Decimal("-3"), "EUR"), "-3.00 EUR")


if __name__ == "__main__":
    unittest.main()
