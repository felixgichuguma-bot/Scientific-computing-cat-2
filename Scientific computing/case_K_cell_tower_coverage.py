"""Case K (Task 12): where do two cell-tower coverage boundaries meet?"""
import numpy as np
from scipy.optimize import root

# T1 at (0,0) radius 5 km; T2 at (6,0) radius 4 km
eq = lambda z: [z[0] ** 2 + z[1] ** 2 - 25, (z[0] - 6) ** 2 + z[1] ** 2 - 16]
for g in ([3., 3.], [3., -3.]):
    s = root(eq, g)
    print("Guess", g, "-> boundary intersection (km):", np.round(s.x, 5),
          "| residuals", np.round(eq(s.x), 10))
