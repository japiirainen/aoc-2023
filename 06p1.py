#!/usr/bin/env python3

import re
import numpy as np

i = np.array([[int(x) for x in re.findall(r"\d+", line)] for line in open(0)])

t = 1
for time, dist in i.T:
    ws = 0
    for n in range(time + 1):
        if n * (time - n) > dist:
            ws += 1
    t *= ws

print(t)
