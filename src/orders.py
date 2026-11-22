"""Order total calculation for the toy app."""
from __future__ import annotations

from collections.abc import Iterable


def order_total(prices: Iterable[float], discount_rate: float = 0.0) -> float:
    """Return the sum of prices after applying discount_rate, rounded to cents.

    Examples:
        >>> order_total([10.0, 5.5])
        15.5
        >>> order_total([100.0], 0.1)
        90.0
    """
    if not 0.0 <= discount_rate < 1.0:
        raise ValueError("discount_rate must be in [0, 1)")
    subtotal = sum(prices)
    return round(subtotal * (1 - discount_rate), 2)
