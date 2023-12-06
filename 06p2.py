#!/usr/bin/env python3

import re
from operator import add
from functools import reduce

time, dist = [
    int(reduce(add, [x for x in re.findall(r"\d+", line)])) for line in open(0)
]

# This can be done via brute force, but it just feels dumb.. Let's try
# to be a bit smarter and do a binary search instead. That way we can reduce
# our time complexity linear on time to being logarithmic on time.
# let g(n) = n * (time - n)
# g is maximized at time // 2. We want to find the smalles and largest
# n such that g(n) > dist.

g = lambda n: n * (time - n)

lo = 0
hi = time // 2

# Find the smallest n such that g(n) >= dist
while lo + 1 < hi:
    m = (lo + hi) // 2
    if g(m) >= dist:
        hi = m
    else:
        lo = m

# So now we know that lo is the smallest n such that g(n) >= dist. We want
# strict inequality, so we add 1 to our lower bound.
lb = lo + 1

# We can use the fact that g is symmetric (E.g. for a function f, ∀ x y. f(x, y) = f(y, x))
# to find the upper bound.
ub = int((time / 2) + (time / 2 - lb))

print(ub - lb + 1)
