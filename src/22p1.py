#!/usr/bin/env python3

import re
from collections import defaultdict


def dropped_brick(tallest, brick):
    peak = max(
        tallest[(x, y)]
        for x in range(brick[0], brick[3] + 1)
        for y in range(brick[1], brick[4] + 1)
    )
    dz = max(brick[2] - peak - 1, 0)
    return (brick[0], brick[1], brick[2] - dz, brick[3], brick[4], brick[5] - dz)


def drop(tower):
    tallest = defaultdict(int)
    new_tower = []
    falls = 0
    for brick in tower:
        new_brick = dropped_brick(tallest, brick)
        if new_brick[2] != brick[2]:
            falls += 1
        new_tower.append(new_brick)
        for x in range(brick[0], brick[3] + 1):
            for y in range(brick[1], brick[4] + 1):
                tallest[(x, y)] = new_brick[5]
    return falls, new_tower


bricks = sorted(
    [list(map(int, re.findall(r"\d+", line))) for line in open(0).read().splitlines()],
    key=lambda brick: brick[2],
)

_, fallen = drop(bricks)

t = 0

for i in range(len(fallen)):
    removed = fallen[:i] + fallen[i + 1 :]
    falls, _ = drop(removed)
    if not falls:
        t += 1

print(t)
