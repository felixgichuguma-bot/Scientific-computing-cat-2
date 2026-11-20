"""BIT 2118 - Task 9: Eigenvalues and eigenvectors (network centrality)."""
import numpy as np


def centrality(A):
    w, v = np.linalg.eig(A)
    i = np.argmax(w.real)
    d = np.abs(v[:, i].real)
    return w[i].real, d / d.sum(), A @ v[:, i].real - w[i].real * v[:, i].real


def adjacency(n, links):
    A = np.zeros((n, n))
    for a, b in links:
        A[a, b] = A[b, a] = 1
    return A


names = "ABCD"
links = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]
print("--- Base program ---")
lam, c, resid = centrality(adjacency(4, links))
print(f"Dominant eigenvalue: {lam:.4f}")
for n, s in zip(names, c):
    print(f"{n}: {s:.4f}")
print("Verification error:", np.linalg.norm(resid))

print("\n--- Changed parameter: link B-D removed ---")
lam, c, _ = centrality(adjacency(4, [(0, 1), (0, 2), (1, 2), (2, 3)]))
print(f"Link B-D removed (D now connects only to C): dominant eigenvalue {lam:.4f}")
for n, s in zip(names, c):
    print(f"{n}: {s:.4f}")
