#!/usr/bin/env python3

from collections import deque

grid = open(0).read().splitlines()

sr, sc = next(
    (r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "S"
)

steps = 26501365
R, C = len(grid), len(grid[0])

assert R == C
assert sr == sc == R // 2
assert steps % R == R // 2


def fill(sr, sc, ss):
    t = 0
    seen = {(sr, sc)}
    q = deque([(sr, sc, ss)])

    while q:
        r, c, steps = q.popleft()

        if steps % 2 == 0:
            t += 1
        if steps == 0:
            continue

        for dr, dc in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < len(grid)
                and 0 <= nc < len(grid[0])
                and grid[nr][nc] != "#"
                and (nr, nc) not in seen
            ):
                seen.add((nr, nc))
                q.append((nr, nc, steps - 1))
    return t


grid_width = steps // R - 1

odd = (grid_width // 2 * 2 + 1) ** 2
even = ((grid_width + 1) // 2 * 2) ** 2

odd_points = fill(sr, sc, R * 2 + 1)
even_points = fill(sr, sc, R * 2)

corner_t = fill(R - 1, sc, R - 1)
corner_r = fill(sr, 0, R - 1)
corner_b = fill(0, sc, R - 1)
corner_l = fill(sr, R - 1, R - 1)

small_tr = fill(R - 1, 0, R // 2 - 1)
small_tl = fill(R - 1, R - 1, R // 2 - 1)
small_br = fill(0, 0, R // 2 - 1)
small_bl = fill(0, R - 1, R // 2 - 1)

large_tr = fill(R - 1, 0, R * 3 // 2 - 1)
large_tl = fill(R - 1, R - 1, R * 3 // 2 - 1)
large_br = fill(0, 0, R * 3 // 2 - 1)
large_bl = fill(0, R - 1, R * 3 // 2 - 1)

print(
    odd * odd_points
    + even * even_points
    + corner_t
    + corner_r
    + corner_b
    + corner_l
    + (grid_width + 1) * (small_tr + small_tl + small_br + small_bl)
    + grid_width * (large_tr + large_tl + large_br + large_bl)
)
