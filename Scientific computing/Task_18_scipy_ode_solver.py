"""BIT 2118 - Task 18: Numerical solution of ODEs with SciPy (RC charging circuit)."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def charge(R=1000.0, C=0.001, Vs=5.0, tmax=5.0):
    tau = R * C
    t = np.linspace(0, tmax, 501)
    s = solve_ivp(lambda t, V: (Vs - V) / tau, (0, tmax), [0.0], t_eval=t,
                  rtol=1e-9, atol=1e-11)
    return s, Vs * (1 - np.exp(-t / tau)), tau


print("--- Base program ---")
s, exact, tau = charge()
print("Solver success:", s.success)
print(f"Capacitor voltage at 5 s: {s.y[0, -1]:.4f} V")
print(f"Maximum error against exact solution: {np.max(np.abs(s.y[0] - exact)):.3e} V")
print(f"Time constant RC = {tau:.1f} s; voltage at t = RC: "
      f"{5 * (1 - np.exp(-1)):.4f} V")
plt.plot(s.t, s.y[0], label="solve_ivp")
plt.plot(s.t, exact, "--", label="Exact")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("RC charging curve (solver and exact solution)")
plt.legend()
plt.grid(True)
plt.show()

print("\n--- Changed parameters ---")
for R, C in ((1000, 0.001), (2000, 0.001), (1000, 0.005)):
    s, _, tau = charge(R, C)
    t63 = s.t[np.argmax(s.y[0] >= 0.632 * 5)]
    print(f"R={R}, C={C}: tau={tau:g} s, V(5s)={s.y[0, -1]:.4f} V, "
          f"time to 63.2% of 5 V = {t63:.3f} s")
