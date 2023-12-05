#!/usr/bin/env python3

seeds, *rest = open(0).read().split("\n\n")

seeds = [int(x) for x in seeds.split(": ")[1].split()]

for g in rest:
    xs = g.strip().split("\n")[1:]
    ranges = [[int(y) for y in x.split()] for x in xs]
    new = []
    for seed in seeds:
        for dest, src, n in ranges:
            if seed in range(src, src + n):
                new.append(seed - src + dest)
        else:
            new.append(seed)
    seeds = new

print(min(seeds))
