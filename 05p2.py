#!/usr/bin/env python3

i, *rest = open(0).read().split("\n\n")

i = [int(x) for x in i.split(": ")[1].split()]

seeds = [(i[j], i[j] + i[j + 1]) for j in range(0, len(i), 2)]

overlap = lambda start, end, src, n: (max(start, src), min(end, src + n))

for g in rest:
    xs = g.strip().split("\n")[1:]
    ranges = [[int(y) for y in x.split()] for x in xs]
    new = []
    while seeds:
        s, e = seeds.pop()
        for dest, src, n in ranges:
            os, oe = overlap(s, e, src, n)
            if os < oe:
                new.append((os - src + dest, oe - src + dest))
                if os > s:
                    seeds.append((s, os))
                if e > oe:
                    seeds.append((oe, e))
                break
        else:
            new.append((s, e))
    seeds = new

print(min(seeds)[0])
