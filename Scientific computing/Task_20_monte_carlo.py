"""BIT 2118 - Task 20: Random numbers and Monte Carlo methods (server overload)."""
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


def overload(mean=850, std=120, cap=1000, n=100_000, seed=42):
    demand = np.random.default_rng(seed).normal(mean, std, n)
    return demand > cap


print("--- Base program ---")
o = overload()
print(f"Estimated overload probability: {o.mean():.4%}")
print(f"Number of overload cases: {o.sum()} out of {o.size}")
print(f"Exact (normal) probability: {norm.sf((1000 - 850) / 120):.4%}")
running = np.cumsum(o) / np.arange(1, o.size + 1)
plt.semilogx(running)
plt.axhline(norm.sf(150 / 120), ls=":")
plt.xlabel("Number of simulations")
plt.ylabel("Estimated probability")
plt.title("Convergence of the Monte Carlo overload estimate")
plt.grid(True)
plt.show()

print("\n--- Changed parameters ---")
print(f"std 120->180: {overload(std=180).mean():.4%}")
print(f"capacity 1000->1100: {overload(cap=1100).mean():.4%}")
print(f"mean 850->900: {overload(mean=900).mean():.4%}")
for n in (100, 1_000, 100_000):
    print(f"N={n:>7,}, seeds 1-3:", [f"{overload(n=n, seed=s).mean():.3%}" for s in (1, 2, 3)])
