"""BIT 2118 - Task 12: Polynomial and nonlinear equation solving."""
import numpy as np
from scipy.optimize import root


def intersect(radius, guess):
    F = lambda z: [z[0] ** 2 + z[1] ** 2 - radius ** 2, z[1] - (z[0] ** 2 - 1)]
    return root(F, guess), F


print("--- Base program: circle radius 2 and parabola y = x^2 - 1 ---")
for g in ([1.0, 1.0], [-1.0, 1.0]):
    s, F = intersect(2, g)
    print("Initial guess:", g)
    print("Intersection:", s.x)
    print("Residuals:", F(s.x))
    print("Converged:", s.success)
print("Polynomial check np.roots([1,-5,6]):", np.roots([1, -5, 6]))

print("\n--- Changed parameter: radius 3 ---")
for g in ([1.0, 2.0], [-1.0, 2.0], [2.0, -1.0], [0.0, -3.0]):
    s, _ = intersect(3, g)
    print(f"Radius 3, guess {g} -> {np.round(s.x, 5)} converged {s.success}")
