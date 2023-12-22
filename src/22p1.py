#!/usr/bin/env python3

bricks = [list(map(int, line.replace("~", ",").split(","))) for line in open(0)]
bricks.sort(key=lambda x: x[2])

overlaps = lambda a, b: max(a[0], b[0]) <= min(a[3], b[3]) and max(a[1], b[1]) <= min(
    a[4], b[4]
)

for i, a in enumerate(bricks):
    mz = 1
    for b in bricks[:i]:
        if overlaps(a, b):
            mz = max(mz, b[5] + 1)
    a[5] -= a[2] - mz
    a[2] = mz

bricks.sort(key=lambda x: x[2])

a_b = {i: set() for i in range(len(bricks))}
b_a = {i: set() for i in range(len(bricks))}

for j, upper in enumerate(bricks):
    for i, lower in enumerate(bricks[:j]):
        if overlaps(lower, upper) and upper[2] == lower[5] + 1:
            a_b[i].add(j)
            b_a[j].add(i)

t = 0

for i in range(len(bricks)):
    if all(len(b_a[j]) >= 2 for j in a_b[i]):
        t += 1

print(t)
