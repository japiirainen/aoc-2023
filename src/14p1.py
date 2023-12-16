#!/usr/bin/env python3

T = lambda xs: list(map("".join, zip(*xs)))

G = open(0).read().splitlines()
G = [
    "#".join("".join(sorted(list(grp), reverse=True)) for grp in row.split("#"))
    for row in T(G)
]
print(sum(row.count("O") * (len(G) - r) for r, row in enumerate(T(G))))
