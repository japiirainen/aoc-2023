#!/usr/bin/env python3

from math import prod

workflows_, _ = open(0).read().split("\n\n")

workflows = {}

for wf in workflows_.splitlines():
    name, rest = wf[:-1].split("{")
    rules = rest.split(",")
    workflows[name] = ([], rules.pop())
    for rule in rules:
        x, t = rule.split(":")
        k = x[0]
        cmp = x[1]
        n = int(x[2:])
        workflows[name][0].append((k, cmp, n, t))


def solve(ranges, name="in"):
    if name == "R":
        return 0
    if name == "A":
        return prod(hi - lo + 1 for lo, hi in ranges.values())
    rules, fallback = workflows[name]
    t = 0
    for k, cmp, n, target in rules:
        lo, hi = ranges[k]
        if cmp == "<":
            true = (lo, n - 1)
            false = (n, hi)
        else:
            true = (n + 1, hi)
            false = (lo, n)
        if true[0] <= true[1]:
            copy = dict(ranges)
            copy[k] = true
            t += solve(copy, target)
        if false[0] <= false[1]:
            ranges = dict(ranges)
            ranges[k] = false
    t += solve(ranges, fallback)
    return t


print(solve({k: (1, 4000) for k in "xmas"}))

