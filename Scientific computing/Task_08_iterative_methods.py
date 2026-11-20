"""BIT 2118 - Task 8: Iterative methods (Jacobi and Gauss-Seidel) for Ax = b."""
import numpy as np
import matplotlib.pyplot as plt


def jacobi(A, b, tol=1e-8, max_iter=500):
    D = np.diag(A)
    R = A - np.diagflat(D)
    x = np.zeros_like(b)
    errs = []
    for _ in range(max_iter):
        xn = (b - R @ x) / D
        e = np.linalg.norm(xn - x, ord=np.inf)
        errs.append(e)
        x = xn
        if e < tol:
            break
    return x, errs


def gauss_seidel(A, b, tol=1e-8, max_iter=500):
    x = np.zeros_like(b)
    errs = []
    for _ in range(max_iter):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i + 1:] @ old[i + 1:]) / A[i, i]
        e = np.linalg.norm(x - old, ord=np.inf)
        errs.append(e)
        if e < tol:
            break
    return x, errs


def grid(n):
    return 2 * np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)


A = grid(5)
b = np.array([100.0, 0, 0, 0, 20])
print("--- Base program ---")
xj, ej = jacobi(A, b)
xg, eg = gauss_seidel(A, b)
print("Jacobi temperatures:", np.round(xj, 4))
print("Gauss-Seidel temperatures:", np.round(xg, 4))
print("Direct solution:", np.round(np.linalg.solve(A, b), 4))
print("Jacobi iterations:", len(ej), "| Gauss-Seidel iterations:", len(eg))
plt.semilogy(ej, label="Jacobi")
plt.semilogy(eg, label="Gauss-Seidel")
plt.xlabel("Iteration")
plt.ylabel("Largest change")
plt.title("Convergence of Jacobi and Gauss-Seidel (log scale)")
plt.legend()
plt.grid(True)
plt.show()

print("\n--- Changed parameters ---")
for tol in (1e-4, 1e-8, 1e-12):
    print(f"tol={tol:.0e}: Jacobi {len(jacobi(A, b, tol)[1])} iterations, "
          f"Gauss-Seidel {len(gauss_seidel(A, b, tol)[1])} iterations")
b2 = b.copy()
b2[0] = 150
print("Left boundary 150 C ->", np.round(np.linalg.solve(A, b2), 3))
B = np.array([[1.0, 3], [4, 1]])
rhs = np.array([1.0, 1])
x = np.zeros(2)
for _ in range(30):
    x = (rhs - (B - np.diagflat(np.diag(B))) @ x) / np.diag(B)
print("Non-diagonally-dominant [[1,3],[4,1]] after 30 Jacobi iterations: error",
      f"{np.linalg.norm(x - np.linalg.solve(B, rhs)):.3e}", "(grows - diverges)")
