#!/usr/bin/env python3

diffs = lambda xs: [b - a for a, b in zip(xs, xs[1:])]


def next_in_seq(xs):
    out = []
    while not all(x == 0 for x in xs):
        out.append(xs[-1])
        xs = diffs(xs)
    return sum(out)


print(sum(next_in_seq(list(map(int, line.split()))) for line in open(0)))
