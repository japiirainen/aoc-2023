#!/usr/bin/env python3


def check(p):
    for i, (a, b) in enumerate(zip(p, p[1:])):
        if a == b:
            for j in range(len(p) - (i + 2)):
                s = i - j - 1
                e = i + 2 + j
                if s >= 0 and e < len(p) and p[s] != p[e]:
                    break
            else:
                return i + 1
    return 0


R = []
C = []
for p in (p.splitlines() for p in open(0).read().strip().split("\n\n")):
    R.append(check(p))
    C.append(check(list(zip(*p))))

print(sum(C) + 100 * sum(R))
