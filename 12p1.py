#!/usr/bin/env python3

import re

entries = []
for line in open(0):
    records, rules = line.split()
    rules = list(map(int, rules.split(",")))
    entries.append((records, rules))


def is_valid(rules, records):
    gs = re.findall(r"#+", records)
    if len(gs) != len(rules):
        return False
    for i, rule in enumerate(rules):
        if i >= len(gs) or rule != len(gs[i]):
            return False
    return True


def variations(records):
    if "?" not in records:
        yield records
        return
    for ch in "#.":
        yield from variations(records.replace("?", ch, 1))


t = sum(is_valid(rules, rs) for records, rules in entries for rs in variations(records))

print(t)
