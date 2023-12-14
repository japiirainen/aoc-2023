#!/usr/bin/env python3

grid = [list(row) for row in open(0).read().strip().splitlines()]

for c in range(len(grid)):
    for _ in range(len(grid[c])):
        for r in range(len(grid[c])):
            if grid[r][c] == "O" and r > 0 and grid[r - 1][c] == ".":
                grid[r - 1][c] = "O"
                grid[r][c] = "."

print(
    sum(
        len(grid) - r
        for c in range(len(grid))
        for r in range(len(grid[c]))
        if grid[r][c] == "O"
    )
)
