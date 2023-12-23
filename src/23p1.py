#!/usr/bin/env python3

import sys

grid = open(0).read().splitlines()
R, C = len(grid), len(grid[0])

sys.setrecursionlimit(100000)


def dfs(r, c, end, seen):
    if (r, c) == end:
        return len(seen)
    ch = grid[r][c]
    best = 0
    for nr, nc in [
        (r + dr, c + dc)
        for dr, dc in (
            [(0, -1)]
            if ch == "<"
            else [(0, 1)]
            if ch == ">"
            else [(-1, 0)]
            if ch == "^"
            else [(1, 0)]
            if ch == "v"
            else [(1, 0), (-1, 0), (0, 1), (0, -1)]
        )
    ]:
        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != "#" and (nr, nc) not in seen:
            best = max(best, dfs(nr, nc, end, seen | {(nr, nc)}))
    return best


print(dfs(0, 1, (R - 1, C - 2), set()))
