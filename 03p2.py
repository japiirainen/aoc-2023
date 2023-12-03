#!/usr/bin/env python3

from math import prod

grid = open(0).read().strip().splitlines()

t = 0

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        cs = set()
        if ch != "*":
            continue
        for dr in [r - 1, r, r + 1]:
            for dc in [c - 1, c, c + 1]:
                if (
                    dr < 0
                    or dc < 0
                    or dr >= len(grid)
                    or dc >= len(row)
                    or not grid[dr][dc].isdigit()
                ):
                    continue
                while dc > 0 and grid[dr][dc - 1].isdigit():
                    dc -= 1
                cs.add((dr, dc))
        if len(cs) != 2:
            continue
        xs = []
        for rr, cc in cs:
            s = ""
            while cc < len(grid[r]) and grid[rr][cc].isdigit():
                s += grid[rr][cc]
                cc += 1
            xs.append(int(s))
        t += prod(xs)

print(t)
