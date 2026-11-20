"""BIT 2118 - Task 16: Numerical integration (trapezoidal and Simpson)."""
import numpy as np
from scipy.integrate import simpson

t = np.arange(0, 13, 2, dtype=float)                       # hours
power = np.array([0.9, 1.0, 1.4, 1.8, 1.6, 1.2, 0.8])      # kW

print("--- Base program ---")
trap, simp = np.trapezoid(power, t), simpson(power, x=t)
print(f"Energy using trapezoidal rule: {trap:.3f} kWh")
print(f"Energy using Simpson's rule: {simp:.3f} kWh")
print(f"Difference between estimates: {abs(simp - trap):.3f} kWh")

print("\n--- Changed parameters ---")
p2 = power.copy()
p2[3] = 3.0
print(f"Peak raised 1.8 -> 3.0 kW: trapezoid {np.trapezoid(p2, t):.3f}, "
      f"Simpson {simpson(p2, x=t):.3f} kWh")
th = np.arange(0, 13, 1, dtype=float)
print(f"Hourly (interpolated) trapezoid: {np.trapezoid(np.interp(th, t, power), th):.3f} kWh")
for n in (5, 9, 17):
    xs = np.linspace(0, np.pi, n)
    print(f"sin on [0,pi], {n} points: trapezoid {np.trapezoid(np.sin(xs), xs):.6f}, "
          f"Simpson {simpson(np.sin(xs), x=xs):.6f} (exact 2)")
