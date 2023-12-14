#!/usr/bin/env python3

grid = [list(row) for row in open(0).read().strip().splitlines()]


def roll(grid):
    for c in range(len(grid)):
        for _ in range(len(grid[c])):
            for r in range(len(grid[c])):
                if grid[r][c] == "O" and r > 0 and grid[r - 1][c] == ".":
                    grid[r - 1][c] = "O"
                    grid[r][c] = "."
    return grid


def rotate(grid):
    ng = [["-1" for _ in range(len(grid))] for _ in range(len(grid[0]))]
    for c in range(len(grid)):
        for r in range(len(grid[c])):
            ng[c][len(grid[c]) - r - 1] = grid[r][c]
    return ng


m = {}

cycles = 10**9
cycle = 0
while cycle < cycles:
    cycle += 1
    for _ in range(4):
        grid = roll(grid)
        grid = rotate(grid)

    rep = tuple(tuple(row) for row in grid)
    if rep in m:
        cycle_len = cycle - m[rep]
        amt = (cycles - cycle) // cycle_len
        cycle += amt * cycle_len
    m[rep] = cycle

print(
    sum(
        len(grid) - r
        for c in range(len(grid))
        for r in range(len(grid[c]))
        if grid[r][c] == "O"
    )
)
