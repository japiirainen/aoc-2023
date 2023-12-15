#!/usr/bin/env python3


def hash(s):
    c = 0
    for ch in s:
        c += ord(ch)
        c *= 17
        c %= 256
    return c


print(sum(hash(s) for s in open(0).read().strip().split(",")))
