"""Case C (Task 4): adding money in a banking system - float vs fsum vs Decimal."""
import math
from decimal import Decimal

total = 0.0
for _ in range(1_000_000):
    total += 0.10
print(f"Naive sum of 1,000,000 x KES 0.10: {total!r}")
print(f"math.fsum: {math.fsum([0.10] * 1_000_000)!r}")
print(f"Naive error: {abs(total - 100000):.10f}")
print("Naive == 100000 ?", total == 100000, "| isclose:", math.isclose(total, 100000))
print("Decimal sum:", sum(Decimal('0.10') for _ in range(1_000_000)))
