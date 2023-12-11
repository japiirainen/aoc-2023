#!/usr/bin/env python3

from itertools import combinations

grid = open(0).read().strip().splitlines()

er = [r for r, row in enumerate(grid) if all(ch == "." for ch in row)]
ec = [c for c, col in enumerate(zip(*grid)) if all(ch == "." for ch in col)]
cs = [(r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "#"]

scale = 1_000_000
t = 0

for (r1, c1), (r2, c2) in combinations(cs, 2):
    t += sum(scale if r in er else 1 for r in range(min(r1, r2), max(r1, r2)))
    t += sum(scale if c in ec else 1 for c in range(min(c1, c2), max(c1, c2)))

print(t)
