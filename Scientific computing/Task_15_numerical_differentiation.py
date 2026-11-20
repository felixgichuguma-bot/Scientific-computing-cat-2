"""BIT 2118 - Task 15: Numerical differentiation (forward, central, backward)."""
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 7, dtype=float)
x = np.array([0, 4.8, 10.2, 16.1, 22.7, 30.0, 38.0])      # GPS position (m)


def speed(x, dt=1.0):
    v = np.zeros_like(x)
    v[0] = (x[1] - x[0]) / dt                # forward
    v[1:-1] = (x[2:] - x[:-2]) / (2 * dt)    # central
    v[-1] = (x[-1] - x[-2]) / dt             # backward
    return v


print("--- Base program ---")
v = speed(x)
for ti, xi, vi in zip(t, x, v):
    print(f"t={ti:.0f}s, position={xi:.1f}m, estimated speed={vi:.2f}m/s")
plt.plot(t, v, marker="o")
plt.xlabel("Time (s)")
plt.ylabel("Speed (m/s)")
plt.title("Speed estimated from GPS position")
plt.grid(True)
plt.show()

print("\n--- Changed parameters ---")
exact = np.cos(1.0)
print(f"f(x)=sin(x), exact f'(1) = {exact:.10f}")
for h in (1e-1, 1e-2, 1e-4, 1e-8, 1e-12):
    fwd = (np.sin(1 + h) - np.sin(1)) / h
    cen = (np.sin(1 + h) - np.sin(1 - h)) / (2 * h)
    print(f"h={h:.0e}: forward error {abs(fwd - exact):.2e}, central error {abs(cen - exact):.2e}")
rng = np.random.default_rng(1)
print("Speeds with 0.5 m GPS noise:", np.round(speed(x + rng.normal(0, 0.5, x.size)), 2))
