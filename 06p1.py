#!/usr/bin/env python3

import re
import numpy as np
from math import sqrt, floor, ceil, prod

i = np.array([[int(x) for x in re.findall(r"\d+", line)] for line in open(0)])


def span(t, d):
    # x(t - x) > d
    # x^2 - tx > d
    # x^2 - tx + d < 0
    disc = sqrt(t**2 - 4 * d)
    mi, ma = (t - disc) / 2, (t + disc) / 2
    return ceil(ma) - floor(mi) - 1


print(prod(span(*x) for x in i.T))
