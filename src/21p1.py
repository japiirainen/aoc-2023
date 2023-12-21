#!/usr/bin/env python3

from collections import deque


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


grid = open(0).read().splitlines()

sr, sc = next(
    (r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "S"
)

print(fill(sr, sc, 64))
