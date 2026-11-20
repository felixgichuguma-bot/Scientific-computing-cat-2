"""BIT 2118 - Task 17: Euler method for ODEs (Newton's law of cooling)."""
import numpy as np
import matplotlib.pyplot as plt


def euler(k=0.12, h=1.0, T0=90.0, Ta=25.0, tmax=30.0):
    t = np.arange(0, tmax + h / 2, h)
    T = np.zeros_like(t)
    T[0] = T0
    for i in range(len(t) - 1):
        T[i + 1] = T[i] + h * (-k * (T[i] - Ta))
    return t, T, Ta + (T0 - Ta) * np.exp(-k * t)


print("--- Base program ---")
t, T, ex = euler()
print(f"Euler temperature after 30 min: {T[-1]:.2f} C")
print(f"Exact temperature after 30 min: {ex[-1]:.2f} C")
print(f"Final absolute error: {abs(T[-1] - ex[-1]):.4f} C")
plt.plot(t, T, "o-", ms=3, label="Euler")
plt.plot(t, ex, label="Exact")
plt.xlabel("Time (min)")
plt.ylabel("Temperature (C)")
plt.title("Euler solution and exact solution for cooling")
plt.legend()
plt.grid(True)
plt.show()

print("\n--- Changed parameters ---")
for h in (5.0, 1.0, 0.1):
    _, T, ex = euler(h=h)
    print(f"h={h}: Euler {T[-1]:.4f} C, exact {ex[-1]:.4f} C, error {abs(T[-1] - ex[-1]):.4f}")
_, T, ex = euler(k=0.2)
print(f"k=0.2: Euler {T[-1]:.2f} C, exact {ex[-1]:.2f} C")
_, T, _ = euler(k=0.2, h=10.0)
print("h=10, k=0.2 (h*k=2): first values", np.round(T[:4], 0), "-> oscillates/unstable")
