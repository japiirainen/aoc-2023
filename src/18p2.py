#!/usr/bin/env python3

ps = [(0, 0)]
dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

t = 0

for line in open(0):
    _, _, col = line.split()
    col = col[2:-1]
    d = int(col[-1])
    n = int(col[:-1], 16)
    dr, dc = dirs["RDLU"[d]]
    n = int(n)
    t += n
    r, c = ps[-1]
    ps.append((r + dr * n, c + dc * n))

a = (
    abs(
        sum(
            ps[i][0] * (ps[i - 1][1] - ps[(i + 1) % len(ps)][1]) for i in range(len(ps))
        )
    )
    // 2
)

print((a - t // 2 + 1) + t)
