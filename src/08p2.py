#!/usr/bin/env python3

import math
from itertools import cycle

instrs, rest = open(0).read().split("\n\n")

m = {}

for line in rest.splitlines():
    s, t = line.split(" = ")
    a, b = t.split(", ")
    m[s] = (a.split("(")[1], b.split(")")[0])

starts = [v for k, v in m.items() if k[-1] == "A"]


def route(s, f):
    cur = s
    for i, instr in enumerate(cycle(instrs)):
        n = cur[0] if instr == "L" else cur[1]
        if f(n):
            return i + 1
        cur = m[n]
    raise ValueError("No route found.")


print(math.lcm(*[route(s, lambda x: x[-1] == "Z") for s in starts]))
