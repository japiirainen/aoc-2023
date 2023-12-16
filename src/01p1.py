#!/usr/bin/env python3

import re

t = 0

for l in open(0).read().splitlines():
    ds = re.findall(r"\d", l)
    t += int(ds[0] + ds[-1])

print(t)
