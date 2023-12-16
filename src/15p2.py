#!/usr/bin/env python3


def hash(s):
    c = 0
    for ch in s:
        c += ord(ch)
        c *= 17
        c %= 256
    return c


boxes = [[] for _ in range(256)]
lengths = {}

for s in open(0).read().strip().split(","):
    if "-" in s:
        label = s[:-1]
        idx = hash(label)
        if label in boxes[idx]:
            boxes[idx].remove(label)
    else:
        label, length = s.split("=")
        length = int(length)
        idx = hash(label)
        if label not in boxes[idx]:
            boxes[idx].append(label)
        lengths[label] = length

print(
    sum(
        i * j * lengths[label]
        for i, box in enumerate(boxes, start=1)
        for j, label in enumerate(box, start=1)
    )
)
