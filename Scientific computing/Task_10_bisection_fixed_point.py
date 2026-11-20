"""BIT 2118 - Task 10: Root finding by bisection and fixed-point iteration."""
import numpy as np
import matplotlib.pyplot as plt


def bisection(f, a, b, tol=1e-10):
    n = 0
    while (b - a) > tol:
        m = (a + b) / 2
        if f(a) * f(m) <= 0:
            b = m
        else:
            a = m
        n += 1
    return (a + b) / 2, n


def fixed_point(g, x0, tol=1e-10, max_iter=500):
    x = x0
    for n in range(1, max_iter + 1):
        xn = g(x)
        if abs(xn - x) < tol:
            return xn, n
        x = xn
    return x, max_iter


def run(c1=25.0, c2=10.0):
    f = lambda T: T - c1 - c2 * np.exp(-T / 20)
    g = lambda T: c1 + c2 * np.exp(-T / 20)
    return f, g


f, g = run()
print("--- Base program ---")
rb, nb = bisection(f, 20, 40)
rf, nf = fixed_point(g, 30)
print(f"Bisection equilibrium temperature: {rb:.6f} C")
print(f"Fixed-point equilibrium temperature: {rf:.6f} C")
print(f"Fixed-point iterations: {nf} | Bisection iterations: {nb}")
T = np.linspace(20, 40, 200)
plt.plot(T, f(T))
plt.axhline(0, lw=0.8)
plt.axvline(rb, ls="--")
plt.xlabel("Temperature (C)")
plt.ylabel("f(T)")
plt.title("Heat-balance function and its root")
plt.grid(True)
plt.show()

print("\n--- Changed parameters ---")
f2, g2 = run(30, 20)
print(f"Constants changed to 30 and 20: root = {bisection(f2, 20, 60)[0]:.6f} C")
r, n = fixed_point(g2, 30)
print(f"Fixed-point gives {r:.6f} C after {n} iterations")
for tol in (1e-2, 1e-6, 1e-10):
    r, n = bisection(f, 20, 40, tol)
    print(f"xtol={tol:.0e}: iterations={n}, root={r:.8f}")
print("Derivative of g at the root (must be <1 in magnitude):",
      round(abs(-10 / 20 * np.exp(-rb / 20)), 4))
