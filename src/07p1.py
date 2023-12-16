#!/usr/bin/env python3


def f(hand):
    cs = [hand.count(c) for c in hand]
    if 5 in cs:
        return 6
    if 4 in cs:
        return 5
    if 3 in cs:
        if 2 in cs:
            return 4
        return 3
    if cs.count(2) == 4:
        return 2
    if 2 in cs:
        return 1
    return 0


m = {"T": "A", "J": "B", "Q": "C", "K": "D", "A": "E"}

score = lambda hand: (f(hand), [m.get(card, card) for card in hand])

hands = []

for line in open(0):
    hand, bid = line.split()
    hands.append((hand, int(bid)))


t = 0
for rank, (hand, bid) in enumerate(sorted(hands, key=lambda x: score(x[0])), 1):
    t += rank * bid

print(t)
