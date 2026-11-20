"""BIT 2118 - Task 3: Mathematical functions and vectorization.

Input : N simulated latencies (ms) uniform on [5, 250], seed 42.
Maths : y = (x / 1000)^2, computed with a Python loop and with one NumPy expression.
"""
import timeit
import numpy as np


def compare(n, seed=42):
    rng = np.random.default_rng(seed)
    x = rng.uniform(5, 250, n)

    def loop():
        return [(v / 1000) ** 2 for v in x]

    def vectorized():
        return (x / 1000) ** 2

    t_loop = timeit.timeit(loop, number=1)
    t_vec = timeit.timeit(vectorized, number=1)
    return x, vectorized(), t_loop, t_vec


print("--- Base program (N = 1,000,000) ---")
x, y, t_loop, t_vec = compare(1_000_000)
print("First five squared latency values:", y[:5])
print(f"Loop time: {t_loop:.4f} s")
print(f"Vectorized time: {t_vec:.4f} s")
print(f"Approximate speed-up: {t_loop / t_vec:.1f}x")

print("\n--- Changed parameter: array size N ---")
for n in (1_000, 100_000, 5_000_000):
    _, _, tl, tv = compare(n)
    print(f"N={n:>9,}: loop {tl:.4f} s, vectorized {tv:.5f} s, speed-up {tl / tv:.1f}x")
