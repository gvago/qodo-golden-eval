"""Text helpers for the toy app."""
from __future__ import annotations

import re

_NON_ALNUM = re.compile(r"[^a-z0-9]+")


def slugify(text: str) -> str:
    """Return a lowercase ASCII slug with words joined by single hyphens.

    Characters outside a-z and 0-9 are treated as separators.

    Examples:
        >>> slugify("Hello, World!")
        'hello-world'
        >>> slugify("  Release 2.0  ")
        'release-2-0'
        >>> slugify("---")
        ''
    """
    return _NON_ALNUM.sub("-", text.lower()).strip("-")
