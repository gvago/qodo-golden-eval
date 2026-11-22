"""Retry delay policy for the toy app."""
from __future__ import annotations

BASE_DELAY_SECONDS = 0.5
MAX_DELAY_SECONDS = 30.0


def backoff_delay(attempt: int, base: float = BASE_DELAY_SECONDS, max_delay: float = MAX_DELAY_SECONDS) -> float:
    """Return the exponential backoff delay for a zero-based attempt, capped at max_delay.

    Examples:
        >>> backoff_delay(0)
        0.5
        >>> backoff_delay(3)
        4.0
        >>> backoff_delay(20)
        30.0
    """
    if attempt < 0:
        raise ValueError("attempt must be non-negative")
    delay = base * (2 ** attempt)
    if delay > max_delay:
        return max_delay
    return delay
