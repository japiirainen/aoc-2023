#!/usr/bin/env python3

diff = lambda a, b: sum(1 for x, y in zip(a, b) if x != y)


def check(p):
    for r in range(1, len(p)):
        above = p[:r][::-1]
        below = p[r:]
        above = above[: len(below)]
        below = below[: len(above)]
        if sum(diff(a, b) for a, b in zip(above, below)) == 1:
            return r
    return 0


R = []
C = []
for p in (p.splitlines() for p in open(0).read().strip().split("\n\n")):
    R.append(check(p))
    C.append(check(list(zip(*p))))

print(sum(C) + 100 * sum(R))
