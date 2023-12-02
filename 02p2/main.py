#!/usr/bin/env python3

import numpy as np


def parse_sets(l):
    _, ss = l.split(": ")
    ss = [s.split(", ") for s in ss.split("; ")]
    parse_sets = lambda ss: [(int(n), c) for n, c in [s.split() for s in ss]]
    return list(map(parse_sets, ss))


sets = [parse_sets(l) for l in open(0).read().strip().splitlines()]


def max_colors(sets):
    max_color = lambda color: max([n for n, c in sets if c == color] or [0])
    return np.array([max_color("red"), max_color("green"), max_color("blue")])


print(np.sum([np.prod(np.max([max_colors(s) for s in ss], axis=0)) for ss in sets]))
