"""Tests for orders."""
from __future__ import annotations

import unittest

from src.orders import order_total


class TestOrderTotal(unittest.TestCase):
    def test_order_total_without_discount_sums_prices(self) -> None:
        self.assertEqual(order_total([10.0, 5.5]), 15.5)

    def test_order_total_with_discount_reduces_total(self) -> None:
        self.assertEqual(order_total([100.0], 0.1), 90.0)

    def test_order_total_invalid_discount_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            order_total([1.0], 1.0)


if __name__ == "__main__":
    unittest.main()
