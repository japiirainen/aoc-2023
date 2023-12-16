#!/usr/bin/env python3

T = lambda xs: tuple(map("".join, zip(*xs)))

G = tuple(open(0).read().splitlines())


def cycle(G):
    for _ in range(4):
        G = tuple(
            "#".join(
                "".join(sorted(tuple(grp), reverse=True)) for grp in row.split("#")
            )
            for row in T(G)
        )
        G = tuple(xs[::-1] for xs in G)
    return G


i = 0
grids = [G]
while True:
    i += 1
    G = cycle(G)
    if G in grids:
        break
    grids.append(G)

idx = grids.index(G)

G = grids[(10**9 - idx) % (i - idx) + idx]

print(sum(row.count("O") * (len(G) - r) for r, row in enumerate(G)))
