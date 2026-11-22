---
name: money-review
description: Review changes that compute monetary amounts in this repository.
---

# Money review

When a change computes prices, totals, discounts or other monetary amounts:

1. Amounts must be `decimal.Decimal`, never `float`. Flag float arithmetic on money and
   `float(...)` conversions of prices.
2. Round once, at the end, with `Decimal.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)`.
   Flag the builtin `round()` on monetary values.
