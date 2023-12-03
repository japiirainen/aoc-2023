#!/usr/bin/env python3

grid = open(0).read().strip().splitlines()

cs = set()

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch.isdigit() or ch == ".":
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

t = 0

for r, c in cs:
    n = ""
    while c < len(grid[r]) and grid[r][c].isdigit():
        n += grid[r][c]
        c += 1
    t += int(n)

print(t)
