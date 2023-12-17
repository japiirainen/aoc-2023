#!/usr/bin/env python3

import heapq

grid = open(0).read().splitlines()
R = len(grid)
C = len(grid[0])

sr, sc = 0, 0
seen = set()
q = [(0, sr, sc, 0, 0)]  # heat_loss, r, c, dir, straight_moves

while q:
    hl, r, c, dir_, sm = heapq.heappop(q)

    if (r, c) == (R - 1, C - 1):
        print(hl)
        break

    if (r, c, dir_, sm) in seen:
        continue

    seen.add((r, c, dir_, sm))

    for i, (dr, dc) in enumerate([(-1, 0), (0, 1), (1, 0), (0, -1)]):
        rr, cc = r + dr, c + dc
        new_dir = i
        new_sm = 1 if dir_ != new_dir else sm + 1
        can_move = ((new_dir + 2) % 4 != dir_) and new_sm <= 3
        if 0 <= rr < R and 0 <= cc < C and can_move:
            heapq.heappush(q, (hl + int(grid[rr][cc]), rr, cc, new_dir, new_sm))
