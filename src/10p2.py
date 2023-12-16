#!/usr/bin/env python3

from re import sub
from collections import deque

grid = [list(line) for line in open(0).read().strip().splitlines()]


def next_req(dr, dc, prv, ch):
    if (dr, dc) == (0, 1) and prv in "S-LF" and ch in "-J7":
        return "-LF"
    if (dr, dc) == (0, -1) and prv in "S-J7" and ch in "-LF":
        return "-J7"
    if (dr, dc) == (1, 0) and prv in "S|7F" and ch in "|JL":
        return "|7F"
    if (dr, dc) == (-1, 0) and prv in "S|JL" and ch in "|7F":
        return "|JL"


S = next((r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "S")

q = deque([S])
loop = {S}

s = {"|", "-", "J", "L", "7", "F"}

while q:
    r, c = q.popleft()

    for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nr, nc = r + dr, c + dc

        if (nr, nc) in loop:
            continue

        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            req = next_req(dr, dc, grid[r][c], grid[nr][nc])
            if req:
                loop.add((nr, nc))
                q.append((nr, nc))
                s &= set(req) if grid[r][c] == "S" else s

(S,) = s
grid = [
    "".join(ch if (r, c) in loop else "." for c, ch in enumerate(row)).replace("S", S)
    for r, row in enumerate(grid)
]

inside = 0

for row in grid:
    pc = 0
    for ch in sub(r"[LJF7]", "", sub(r"F-*J|L-*7", "|", row)):
        pc += ch == "|"
        inside += ch == "." and pc % 2 == 1

print(inside)
