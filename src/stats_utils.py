"""Summary statistics helpers for the toy app."""
from __future__ import annotations

from collections.abc import Sequence


def median(values: Sequence[float]) -> float:
    """Return the median of values.

    For an even number of values the median is the average of the two middle values.

    Examples:
        >>> median([3, 1, 2])
        2
        >>> median([4, 1, 3, 2])
        2.5
    """
    if not values:
        raise ValueError("median of empty sequence")
    ordered = sorted(values)
    mid = len(ordered) // 2
    if len(ordered) % 2 == 1:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2
