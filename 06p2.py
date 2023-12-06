#!/usr/bin/env python3

import re
from operator import add
from functools import reduce
from math import sqrt, floor, ceil

t, d = [int(reduce(add, [x for x in re.findall(r"\d+", line)])) for line in open(0)]

disc = sqrt(t**2 - 4 * d)
mi, ma = (t - disc) / 2, (t + disc) / 2
print(ceil(ma) - floor(mi) - 1)
