#!/usr/bin/env python3

from collections import deque

grid = open(0).read().splitlines()
R = len(grid)
C = len(grid[0])

s: list[tuple[int, int, int, int]] = [(0, -1, 0, 1)]  # (r, c, dr, dc)
seen = set()
q = deque(s)

while q:
    r, c, dr, dc = q.popleft()
    r, c = r + dr, c + dc
    if r < 0 or r >= R or c < 0 or c >= C:
        continue
    ch = grid[r][c]

    def enqueue(r, c, dr, dc):
        if (r, c, dr, dc) not in seen:
            seen.add((r, c, dr, dc))
            q.append((r, c, dr, dc))

    if ch == "." or (ch == "-" and dc != 0) or (ch == "|" and dr != 0):
        enqueue(r, c, dr, dc)
    elif ch == "/":
        enqueue(r, c, -dc, -dr)
    elif ch == "\\":
        enqueue(r, c, dc, dr)
    else:
        for dr, dc in [(1, 0), (-1, 0)] if ch == "|" else [(0, 1), (0, -1)]:
            enqueue(r, c, dr, dc)

print(len({(r, c) for r, c, _, _ in seen}))
