#!/usr/bin/env python3

diff = lambda a, b: sum(1 for x, y in zip(a, b) if x != y)


def check(p):
    for i, (a, b) in enumerate(zip(p, p[1:])):
        d = diff(a, b)
        for j in range(len(p) - (i + 2)):
            s = i - j - 1
            e = i + 2 + j
            if s >= 0 and e < len(p):
                d += diff(p[s], p[e])
        if d == 1:
            return i + 1
    return 0


rs = []
cs = []
for p in (p.splitlines() for p in open(0).read().strip().split("\n\n")):
    rs.append(check(p))
    cs.append(check(list(zip(*p))))

print(sum(cs) + 100 * sum(rs))
