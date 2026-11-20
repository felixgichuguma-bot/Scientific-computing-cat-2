"""BIT 2118 - Task 7: Gaussian elimination and LU decomposition (factor once, solve many)."""
import time
import numpy as np
from scipy.linalg import lu_factor, lu_solve

A = np.array([[4.0, -1, 0], [-1, 4, -1], [0, -1, 3]])
B = [np.array([15.0, 10, 10]), np.array([16.0, 11, 9]), np.array([14.0, 12, 11])]


def solve_all(A, B):
    lu, piv = lu_factor(A)                 # PA = LU, done once
    for k, b in enumerate(B, 1):
        x = lu_solve((lu, piv), b)
        print(f"Measurement set {k}\nSolution: {x}\nResidual norm: {np.linalg.norm(b - A @ x)}")


print("--- Base program ---")
solve_all(A, B)
print("Direct solution for first set:", np.linalg.solve(A, B[0]))

print("\n--- Changed parameter: A[0,0] = 6 ---")
A2 = A.copy()
A2[0, 0] = 6
for k, b in enumerate(B, 1):
    print(f"Set {k} (A[0,0]=6):", np.linalg.solve(A2, b))

print("\n--- Timing: 300x300 system, 200 right-hand sides ---")
rng = np.random.default_rng(0)
M = rng.random((300, 300)) + 300 * np.eye(300)
rhs = rng.random((200, 300))
t0 = time.perf_counter()
for r in rhs:
    np.linalg.solve(M, r)
t1 = time.perf_counter()
lu, piv = lu_factor(M)
for r in rhs:
    lu_solve((lu, piv), r)
t2 = time.perf_counter()
print(f"repeated solve {t1 - t0:.4f} s, factor once + reuse {t2 - t1:.4f} s")
