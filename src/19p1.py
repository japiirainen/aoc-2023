#!/usr/bin/env python3

workflows_, parts_ = open(0).read().split("\n\n")

workflows = {}

for wf in workflows_.splitlines():
    name, rules_ = wf.split("{")
    rules_ = rules_[:-1].split(",")
    rules = []
    for rule in rules_:
        xs = rule.split(":")
        if len(xs) == 1:
            rules.append((None, lambda _: True, xs[0]))
        else:
            r = xs[0]
            rules.append((r[0], eval(f"lambda {r[0]}: {r}"), xs[1]))
    workflows[name] = rules

parts = []
for part_ in parts_.splitlines():
    part_ = [x.split("=") for x in part_[1:-1].split(",")]
    parts.append({k: int(v) for k, v in part_})


def run_worflow(part):
    w = workflows["in"]
    while True:
        for arg, f, target in w:
            if arg in part:
                if f(part[arg]):
                    if target in "RA":
                        return target == "A"
                    w = workflows[target]
                    break
            else:
                if target in "RA":
                    return target == "A"
                w = workflows[target]


print(sum(sum(part.values()) if run_worflow(part) else 0 for part in parts))
