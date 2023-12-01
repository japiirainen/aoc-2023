#!/usr/bin/env python3

import re

n = "one two three four five six seven eight nine".split()
r = "(?=(" + "|".join(n) + "|\\d))"

t = 0

for l in open(0).read().splitlines():
    ds = [str(n.index(x) + 1) if x in n else x for x in re.findall(r, l)]
    t += int(ds[0] + ds[-1])

print(t)
