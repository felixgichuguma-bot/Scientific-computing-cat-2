"""BIT 2118 - Task 5: Matrix algebra and matrix operations (rotate + scale)."""
import numpy as np

square = np.array([[0, 0], [1, 0], [1, 1], [0, 1]], dtype=float)


def transform(angle_deg, sx, sy):
    a = np.deg2rad(angle_deg)
    R = np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])
    S = np.diag([sx, sy])
    T = R @ S                              # scale first, then rotate
    return T, square @ T.T, np.linalg.det(T)


print("--- Base program: 45 deg, scale 2.0 and 1.5 ---")
T, pts, det = transform(45, 2.0, 1.5)
print("Transformation matrix:\n", T)
print("Transformed points:\n", pts)
print("Determinant:", det)

print("\n--- Changed parameter: 90 deg, scale 3.0 and 0.5 ---")
T, pts, det = transform(90, 3.0, 0.5)
print("Transformation matrix:\n", np.round(T, 4))
print("Transformed points:\n", np.round(pts, 4))
print("Determinant:", det)
T, pts, det = transform(45, 2.0, 0.0)
print("Singular case (sy=0): determinant =", round(det, 4), "| points:\n", np.round(pts, 4))
