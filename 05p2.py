#!/usr/bin/env python3

i, *rest = open(0).read().split("\n\n")

i = [int(x) for x in i.split(": ")[1].split()]

seeds = [(i[j], i[j] + i[j + 1]) for j in range(0, len(i), 2)]

overlap = lambda ss, se, s, n: (max(ss, s), min(se, s + n))


def f(ranges, seeds):
    while seeds:
        ss, se = seeds.pop()
        for e, s, n in ranges:
            os, oe = overlap(ss, se, s, n)
            if os < oe:
                yield (os - s + e, oe - s + e)
                if se > oe:
                    seeds.append((oe, se))
                if ss < os:
                    seeds.append((ss, os))
                break
        else:
            yield (ss, se)


for g in rest:
    xs = g.strip().split("\n")[1:]
    ranges = [[int(y) for y in x.split()] for x in xs]
    seeds = list(f(ranges, seeds))

print(min(seeds)[0])
