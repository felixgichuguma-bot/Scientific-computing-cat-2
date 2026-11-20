"""BIT 2118 - Task 13: Interpolation (linear and cubic spline)."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, CubicSpline

hours = np.arange(8, 15, dtype=float)
temp = np.array([18, 20, 22.5, 24, 25, 25.5, 25.0])

lin = interp1d(hours, temp)
cub = CubicSpline(hours, temp)
print("--- Base program ---")
print(f"Linear estimate at 10:30: {float(lin(10.5)):.2f} C")
print(f"Cubic estimate at 10:30: {float(cub(10.5)):.2f} C")
t = np.arange(8, 14 + 1e-9, 1 / 6)
plt.scatter(hours, temp, label="Measured")
plt.plot(t, lin(t), label="Linear")
plt.plot(t, cub(t), label="Cubic spline")
plt.xlabel("Hour")
plt.ylabel("Temperature (C)")
plt.title("Linear and cubic-spline interpolation of hourly temperatures")
plt.legend()
plt.grid(True)
plt.show()

print("\n--- Changed parameter: hour 12 removed ---")
keep = hours != 12
l2, c2 = interp1d(hours[keep], temp[keep]), CubicSpline(hours[keep], temp[keep])
print(f"Hour 12 removed. True value 25.00 C. Linear estimate {float(l2(12)):.2f} C "
      f"(error {abs(float(l2(12)) - 25):.2f}); cubic {float(c2(12)):.2f} C "
      f"(error {abs(float(c2(12)) - 25):.2f})")
print(f"Cubic spline extrapolating to 15:00 (outside the data): {float(cub(15)):.2f} C")
try:
    lin(15)
except ValueError as err:
    print("Linear interp1d at 15:00 -> ValueError (outside range)")
