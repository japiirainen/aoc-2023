#!/usr/bin/env python3

from itertools import pairwise

diffs = lambda xs: [b - a for a, b in pairwise(xs)]

next_in_seq = (
    lambda xs: 0 if all(x == 0 for x in xs) else xs[-1] + next_in_seq(diffs(xs))
)

print(sum(next_in_seq(list(map(int, line.split()))) for line in open(0)))
