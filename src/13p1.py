#!/usr/bin/env python3


def f(p):
    for r in range(1, len(p)):
        above = p[:r][::-1]
        below = p[r:]
        above = above[: len(below)]
        below = below[: len(above)]
        if above == below:
            return r
    return 0


R = []
C = []
for p in (p.splitlines() for p in open(0).read().strip().split("\n\n")):
    R.append(f(p))
    C.append(f(list(zip(*p))))

print(sum(C) + 100 * sum(R))
