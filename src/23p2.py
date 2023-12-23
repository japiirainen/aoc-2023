#!/usr/bin/env python3

grid = open(0).read().splitlines()
R, C, edges = len(grid), len(grid[0]), {}

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == "#":
            continue
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if not (0 <= nr < R and 0 <= nc < C and grid[nr][nc] != "#"):
                continue
            edges.setdefault((r, c), set()).add((nr, nc, 1))
            edges.setdefault((nr, nc), set()).add((r, c, 1))

# remove nodes with degree 2 by mergin edges
while True:
    for n, e in edges.items():
        if len(e) == 2:
            a, b = e
            edges[a[:2]] -= {n + (a[2],)}
            edges[b[:2]] -= {n + (b[2],)}
            edges[a[:2]] |= {(b[0], b[1], a[2] + b[2])}
            edges[b[:2]] |= {(a[0], a[1], a[2] + b[2])}
            del edges[n]
            break
    else:
        break


def dfs(r, c, d, seen):
    if (r, c) == (R - 1, C - 2):
        return d
    best = 0
    for nr, nc, l in edges[(r, c)]:
        if (nr, nc) not in seen:
            best = max(best, dfs(nr, nc, d + l, seen | {(nr, nc)}))
    return best


print(dfs(0, 1, 0, set()))
