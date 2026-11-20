"""BIT 2118 - Task 6: Solution of systems of linear equations, Ax = b."""
import numpy as np

A = np.array([[4.0, 2.0], [8.0, 12.0]])    # CPU and memory per server type
b = np.array([20.0, 72.0])

print("--- Base program ---")
x = np.linalg.solve(A, b)
print("Type A servers:", round(x[0]))
print("Type B servers:", round(x[1]))
print("Verification A @ solution:", A @ x)
print("Residual:", b - A @ x)
print("Residual norm:", np.linalg.norm(b - A @ x))

print("\n--- Changed parameter ---")
print("New totals 24 CPU / 64 GB ->", np.linalg.solve(A, np.array([24.0, 64.0])))
S = np.array([[4.0, 2.0], [8.0, 4.0]])      # proportional rows
print("det of A with proportional rows:", np.linalg.det(S))
try:
    np.linalg.solve(S, b)
except np.linalg.LinAlgError as err:
    print("Singular matrix error:", err)
