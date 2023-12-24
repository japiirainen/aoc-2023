#!/usr/bin/env python3

import re
import numpy as np
from itertools import combinations

hailstones = [list(map(int, re.findall(r"[-]?\d+", line))) for line in open(0)]

l, h = 2e14, 4e14

t = 0

for (x1, y1, _, vx1, vy1, _), (x2, y2, _, vx2, vy2, _) in combinations(hailstones, 2):
    m1, m2 = vy1 / vx1, vy2 / vx2
    if m1 == m2:
        continue
    A = np.array([[m1, -1], [m2, -1]])
    b = np.array([m1 * x1 - y1, m2 * x2 - y2])
    x, y = np.linalg.solve(A, b)
    if not (l <= x <= h and l <= y <= h):
        continue
    if (x - x1) / vx1 > 0 and (x - x2) / vx2 > 0:
        t += 1

print(t)
