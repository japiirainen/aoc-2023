#!/usr/bin/env python3

from itertools import cycle

instrs, rest = open(0).read().split("\n\n")

m = {}

for line in rest.splitlines():
    s, t = line.split(" = ")
    a, b = t.split(", ")
    m[s] = (a.split("(")[1], b.split(")")[0])

cur = m["AAA"]
t = m["ZZZ"]

for i, instr in enumerate(cycle(instrs)):
    cur = m[cur[0]] if instr == "L" else m[cur[1]]
    if cur == t:
        print(i + 1)
        break
