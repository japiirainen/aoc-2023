#!/usr/bin/env python3

from collections import deque

grid = [list(line) for line in open(0).read().strip().splitlines()]


def next_req(dr, dc, prv):
    if (dr, dc) == (0, 1) and prv in "S-LF":
        return "-J7"
    if (dr, dc) == (0, -1) and prv in "S-J7":
        return "-LF"
    if (dr, dc) == (1, 0) and prv in "S|7F":
        return "|JL"
    if (dr, dc) == (-1, 0) and prv in "S|JL":
        return "|F7"


S = next((r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "S")

q = deque()
q.append((S, 0))

loop = {S}

while q:
    (r, c), d = q.popleft()

    for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nr, nc = r + dr, c + dc

        if (nr, nc) in loop:
            continue

        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            req = next_req(dr, dc, grid[r][c])
            if req and grid[nr][nc] in req:
                loop.add((nr, nc))
                q.append(((nr, nc), d + 1))

print(len(loop) // 2)
