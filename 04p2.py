#!/usr/bin/env python3

i = open(0).read().strip().splitlines()

cards = {card: 1 for card in range(len(i))}

for i, line in enumerate(i):
    a, b = [set(map(int, x.strip().split())) for x in line.split(": ")[1].split(" | ")]
    for j in range(i + 1, i + len(a & b) + 1):
        cards[j] += cards[i]

print(sum(cards.values()))
