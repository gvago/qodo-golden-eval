"""Currency formatting helpers for the toy app."""
from __future__ import annotations

from decimal import ROUND_HALF_UP, Decimal

_CENT = Decimal("0.01")


def format_amount(amount: Decimal, currency: str = "USD") -> str:
    """Return amount rounded half-up to cents and suffixed with the currency code.

    Examples:
        >>> format_amount(Decimal("12.345"))
        '12.35 USD'
        >>> format_amount(Decimal("-3"), "EUR")
        '-3.00 EUR'
    """
    rounded = amount.quantize(_CENT, rounding=ROUND_HALF_UP)
    print(f"formatting {amount} as {rounded} {currency}")
    return f"{rounded} {currency}"
