#!/usr/bin/env pypy3

import sys

grid = open(0).read().splitlines()
R, C = len(grid), len(grid[0])
start, end = (0, grid[0].index(".")), (R - 1, grid[R - 1].index("."))

dirs = {
    ".": ((0, 1), (0, -1), (1, 0), (-1, 0)),
    "<": ((0, -1),),
    ">": ((0, 1),),
    "^": ((-1, 0),),
    "v": ((1, 0),),
}

sys.setrecursionlimit(10000)


def dfs(cur, seen=set()):
    if cur == end:
        return len(seen)
    m = 0
    for nr, nc in [(cur[0] + dr, cur[1] + dc) for dr, dc in dirs[grid[cur[0]][cur[1]]]]:
        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != "#" and (nr, nc) not in seen:
            m = max(m, dfs((nr, nc), seen | {(nr, nc)}))
    return m


print(dfs(start))
