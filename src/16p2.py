#!/usr/bin/env python3

from collections import deque
from itertools import chain

grid = open(0).read().splitlines()
R = len(grid)
C = len(grid[0])


def solve(r, c, dr, dc):
    s: list[tuple[int, int, int, int]] = [(r, c, dr, dc)]
    seen = set()
    q = deque(s)

    def enqueue(r, c, dr, dc):
        if (r, c, dr, dc) not in seen:
            seen.add((r, c, dr, dc))
            q.append((r, c, dr, dc))

    while q:
        r, c, dr, dc = q.popleft()
        r, c = r + dr, c + dc
        if r < 0 or r >= R or c < 0 or c >= C:
            continue
        ch = grid[r][c]
        if ch == "." or (ch == "-" and dc != 0) or (ch == "|" and dr != 0):
            enqueue(r, c, dr, dc)
        elif ch == "/":
            enqueue(r, c, -dc, -dr)
        elif ch == "\\":
            enqueue(r, c, dc, dr)
        else:
            for dr, dc in [(1, 0), (-1, 0)] if ch == "|" else [(0, 1), (0, -1)]:
                enqueue(r, c, dr, dc)

    return len({(r, c) for r, c, _, _ in seen})


rs = ([solve(r, -1, 0, 1), solve(r, C, 0, -1)] for r in range(R))
cs = ([solve(-1, c, 1, 0), solve(R, c, -1, 0)] for c in range(C))
print(max(chain(*rs, *cs)))
