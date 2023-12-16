#!/usr/bin/env python3


def parse_game(l):
    game, ss = l.split(": ")
    ss = [s.split(", ") for s in ss.split("; ")]
    parse_sets = lambda ss: [(int(n), c) for n, c in [s.split() for s in ss]]
    ss = list(map(parse_sets, ss))
    return (int(game.split()[1]), ss)


games = [parse_game(l) for l in open(0).read().strip().splitlines()]


def valid_subset(bag):
    m = {"red": 0, "green": 0, "blue": 0}
    for n, cube in bag:
        m[cube] += n
    return m["red"] <= 12 and m["green"] <= 13 and m["blue"] <= 14


print(sum([id_ for id_, sets in games if all(map(valid_subset, sets))]))
