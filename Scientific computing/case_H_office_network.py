"""Case H (Task 9): which device in an office network is most important? (eigenvector centrality)"""
import numpy as np


def centrality(A):
    w, v = np.linalg.eig(A)
    i = np.argmax(w.real)
    d = np.abs(v[:, i].real)
    return w[i].real, d / d.sum()


names = ["Router", "Server1", "Server2", "Printer", "Laptop"]
A = np.zeros((5, 5))
for a, b in [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (2, 4)]:
    A[a, b] = A[b, a] = 1
lam, c = centrality(A)
print("Dominant eigenvalue:", round(lam, 4))
for n, s in sorted(zip(names, c), key=lambda t: -t[1]):
    print(f"{n:8s}: {s:.4f}")
