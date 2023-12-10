#!/usr/bin/env python3

from collections import deque

grid = [list(line) for line in open(0).read().strip().splitlines()]


def valid_move(dr, dc, prv, ch):
    if (dr, dc) == (0, 1):
        return prv in "S-LF" and ch in "-J7"
    if (dr, dc) == (0, -1):
        return prv in "S-J7" and ch in "-LF"
    if (dr, dc) == (1, 0):
        return prv in "S|7F" and ch in "|JL"
    if (dr, dc) == (-1, 0):
        return prv in "S|JL" and ch in "|F7"


S = next((r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "S")

q = deque([S])
loop = {S}

while q:
    r, c = q.popleft()

    for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nr, nc = r + dr, c + dc

        if (nr, nc) in loop:
            continue

        if (
            0 <= nr < len(grid)
            and 0 <= nc < len(grid[0])
            and valid_move(dr, dc, grid[r][c], grid[nr][nc])
        ):
            loop.add((nr, nc))
            q.append((nr, nc))

print(len(loop) // 2 + (1 if len(loop) % 2 == 1 else 0))
