"""Tests for stats_utils."""
from __future__ import annotations

import unittest

from src.stats_utils import median


class TestMedian(unittest.TestCase):
    def test_median_odd_length_returns_middle_value(self) -> None:
        self.assertEqual(median([3, 1, 2]), 2)

    def test_median_even_length_returns_mean_of_middle_pair(self) -> None:
        self.assertEqual(median([4, 1, 3, 2]), 2.5)

    def test_median_single_value_returns_that_value(self) -> None:
        self.assertEqual(median([7]), 7)

    def test_median_empty_input_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            median([])


if __name__ == "__main__":
    unittest.main()
