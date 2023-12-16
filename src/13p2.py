#!/usr/bin/env python3

diff = lambda a, b: sum(1 for x, y in zip(a, b) if x != y)


def f(p):
    for r in range(1, len(p)):
        if 1 == sum(diff(a, b) for a, b in zip(p[:r][::-1], p[r:])):
            return r
    return 0


R = []
C = []
for p in (p.splitlines() for p in open(0).read().strip().split("\n\n")):
    R.append(f(p))
    C.append(f(list(zip(*p))))

print(sum(C) + 100 * sum(R))
