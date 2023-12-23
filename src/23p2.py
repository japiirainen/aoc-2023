#!/usr/bin/env pypy3

grid = open(0).read().splitlines()
R, C = len(grid), len(grid[0])
start, end = (0, grid[0].index(".")), (R - 1, grid[R - 1].index("."))

points = [start, end]

# perform [edge contraction](https://en.wikipedia.org/wiki/Edge_contraction) to prune the search space.
for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == "#":
            continue
        ns = 0
        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != "#":
                ns += 1
        if ns >= 3:
            points.append((r, c))

graph = {point: {} for point in points}

for sr, sc in points:
    stack: list[tuple[int, int, int]] = [(0, sr, sc)]
    seen = {(sr, sc)}
    while stack:
        n, r, c = stack.pop()
        if n != 0 and (r, c) in points:
            graph[(sr, sc)][(r, c)] = n
            continue
        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if (
                0 <= nr < R
                and 0 <= nc < C
                and grid[nr][nc] != "#"
                and (nr, nc) not in seen
            ):
                seen.add((nr, nc))
                stack.append((n + 1, nr, nc))


def dfs(cur, seen=set()):
    if cur == end:
        return 0
    m = -float("inf")
    for n in graph[cur]:
        if n not in seen:
            m = max(m, dfs(n, seen | {cur}) + graph[cur][n])
    return m


print(dfs(start))
