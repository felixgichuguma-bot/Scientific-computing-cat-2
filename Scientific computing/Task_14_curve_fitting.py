"""BIT 2118 - Task 14: Curve fitting (least squares) of server response time."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

users = np.array([50, 100, 150, 200, 250, 300, 350], dtype=float)
resp = np.array([82, 95, 115, 145, 185, 238, 305], dtype=float)   # ms

quad = lambda x, a, b, c: a * x ** 2 + b * x + c
rmse = lambda y, p: np.sqrt(np.mean((y - p) ** 2))

print("--- Base program: quadratic model ---")
p, _ = curve_fit(quad, users, resp)
fit = quad(users, *p)
print(f"Fitted model: y = {p[0]:.6f}x^2 + {p[1]:.4f}x + {p[2]:.2f}")
print(f"RMSE: {rmse(resp, fit):.2f} ms")
print(f"Predicted response at 400 users: {quad(400, *p):.2f} ms")
print("Residuals:", np.round(resp - fit, 2))
xs = np.linspace(50, 400, 200)
plt.scatter(users, resp, label="Measured")
plt.plot(xs, quad(xs, *p), label="Quadratic fit")
plt.xlabel("Concurrent users")
plt.ylabel("Response time (ms)")
plt.title("Quadratic fit to response-time measurements")
plt.legend()
plt.grid(True)
plt.show()

print("\n--- Changed parameters ---")
for name, deg in (("Linear", 1), ("Cubic", 3)):
    c = np.polyfit(users, resp, deg)
    print(f"{name} model RMSE: {rmse(resp, np.polyval(c, users)):.2f} ms; "
          f"prediction at 400 users: {np.polyval(c, 400):.2f} ms")
r2 = resp.copy()
r2[-1] = 400
p2, _ = curve_fit(quad, users, r2)
print(f"Last measurement changed 305->400: prediction at 400 users "
      f"{quad(400, *p2):.2f} ms, a={p2[0]:.6f}")
