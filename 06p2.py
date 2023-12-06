#!/usr/bin/env python3

import re
from operator import add
from functools import reduce
from math import floor, ceil
from sympy import solve, symbols

t, d = [int(reduce(add, [x for x in re.findall(r"\d+", line)])) for line in open(0)]

x = symbols("x")
mi, ma = solve(x**2 - t * x + d)
print(ceil(ma) - floor(mi) - 1)
