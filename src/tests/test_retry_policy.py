"""Tests for retry_policy."""
from __future__ import annotations

import unittest

from src.retry_policy import backoff_delay


class TestBackoffDelay(unittest.TestCase):
    def test_backoff_delay_first_attempt_returns_base(self) -> None:
        self.assertEqual(backoff_delay(0), 0.5)

    def test_backoff_delay_doubles_per_attempt(self) -> None:
        self.assertEqual(backoff_delay(3), 4.0)

    def test_backoff_delay_large_attempt_is_capped(self) -> None:
        self.assertEqual(backoff_delay(20), 30.0)

    def test_backoff_delay_negative_attempt_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            backoff_delay(-1)


if __name__ == "__main__":
    unittest.main()
