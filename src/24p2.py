#!/usr/bin/env python3

import re
from z3 import Int, Solver, sat

hailstones = [list(map(int, re.findall(r"[-]?\d+", line))) for line in open(0)]

s = Solver()
x, y, z, vx, vy, vz = map(Int, "x y z vx vy vz".split())

for i, (a, b, c, va, vb, vc) in enumerate(hailstones):
    t = Int(f"t{i}")
    for constraint in (
        (t > 0),
        (x + vx * t == a + va * t),
        (y + vy * t == b + vb * t),
        (z + vz * t == c + vc * t),
    ):
        s.add(constraint)

assert s.check() == sat
print(sum(s.model().eval(v).as_long() for v in (x, y, z)))
