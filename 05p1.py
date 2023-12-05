#!/usr/bin/env python3

seeds, *rest = open(0).read().split("\n\n")

seeds = [int(x) for x in seeds.split(": ")[1].split()]


def f(ranges, x):
    for end, start, n in ranges:
        if x in range(start, start + n):
            return x + end - start
    else:
        return x


for g in rest:
    xs = g.strip().split("\n")[1:]
    ranges = [[int(y) for y in x.split()] for x in xs]
    seeds = [f(ranges, x) for x in seeds]

print(min(seeds))
