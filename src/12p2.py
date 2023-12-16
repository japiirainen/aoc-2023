#!/usr/bin/env python3

m = {}


def f(records, rules, flag=False):
    def g():
        if records == "":
            return 1 if sum(rules) == 0 else 0

        if sum(rules) == 0:
            return 0 if "#" in records else 1

        if records[0] == "#":
            if flag and rules[0] == 0:
                return 0
            return f(records[1:], (rules[0] - 1, *rules[1:]), True)

        if records[0] == ".":
            if flag and rules[0] > 0:
                return 0
            return f(records[1:], rules[1:] if rules[0] == 0 else rules, False)

        if flag:
            if rules[0] == 0:
                return f(records[1:], rules[1:], False)
            return f(records[1:], (rules[0] - 1, *rules[1:]), True)

        return f(records[1:], rules, False) + f(
            records[1:], (rules[0] - 1, *rules[1:]), True
        )

    k = (records, rules, flag)

    if k not in m:
        m[k] = g()

    return m[k]


t = 0
for line in open(0):
    records, rules = line.split()
    rules = tuple(map(int, rules.split(",")))
    records = "?".join([records] * 5)
    rules *= 5
    t += f(records, rules)

print(t)
