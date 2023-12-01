#!/usr/bin/env python

import re

input = open(0).read().strip().splitlines()

t = 0
for line in input:
    digits = re.findall(r"\d", line)
    t += int(digits[0] + digits[-1])

print(f"Part 1: {t}")

n = "one two three four five six seven eight nine".split()
r = "(?=(" + "|".join(n) + "|\\d))"

t = 0
for line in input:
    digits = [str(n.index(x) + 1) if x in n else x for x in re.findall(r, line)]
    t += int(digits[0] + digits[-1])

print(f"Part 2: {t}")
