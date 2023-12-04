#!/usr/bin/env python3

t = 0

for line in open(0).read().strip().splitlines():
    a, b = [set(map(int, x.strip().split())) for x in line.split(": ")[1].split(" | ")]
    n = len(a & b)
    if n > 0:
        t += 2 ** (n - 1)

print(t)
