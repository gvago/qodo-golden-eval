"""Tests for text_utils."""
from __future__ import annotations

import unittest

from src.text_utils import slugify


class TestSlugify(unittest.TestCase):
    def test_slugify_punctuation_becomes_single_hyphen(self) -> None:
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_slugify_surrounding_whitespace_is_trimmed(self) -> None:
        self.assertEqual(slugify("  Release 2.0  "), "release-2-0")

    def test_slugify_only_separators_returns_empty_string(self) -> None:
        self.assertEqual(slugify("---"), "")

    def test_slugify_empty_input_returns_empty_string(self) -> None:
        self.assertEqual(slugify(""), "")


if __name__ == "__main__":
    unittest.main()
