#!/usr/bin/env python3

from collections import deque
from math import lcm

nodes = {}
broadcast_targets = []

for line in open(0):
    l, r = line.strip().split(" -> ")
    outputs = r.split(", ")
    if l == "broadcaster":
        broadcast_targets = outputs
    else:
        nodes[l[1:]] = {
            "name": l[1:],
            "type": l[0],
            "outputs": outputs,
            "memory": "off" if l[0] == "%" else {},
        }

for name, node in nodes.items():
    for out in node["outputs"]:
        if out in nodes and nodes[out]["type"] == "&":
            nodes[out]["memory"][name] = "lo"

(to_feed,) = [name for name, node in nodes.items() if "rx" in node["outputs"]]
cycles = {}
C = len({name for name, node in nodes.items() if to_feed in node["outputs"]})
t = 0

while True:
    t += 1
    q: deque[tuple[str, str, str]] = deque(
        [("broadcaster", x, "lo") for x in broadcast_targets]
    )

    while q:
        src, tgt, pulse = q.popleft()

        if tgt not in nodes:
            continue

        node = nodes[tgt]

        if node["name"] == to_feed and pulse == "hi":
            if src not in cycles:
                cycles[src] = t

            if len(cycles.values()) == C:
                print(lcm(*cycles.values()))
                exit(0)

        if node["type"] == "&":
            node["memory"][src] = pulse
            msg = "lo" if all(x == "hi" for x in node["memory"].values()) else "hi"
            for out in node["outputs"]:
                q.append((node["name"], out, msg))
        else:
            if pulse == "lo":
                node["memory"] = "on" if node["memory"] == "off" else "off"
                msg = "hi" if node["memory"] == "on" else "lo"
                for out in node["outputs"]:
                    q.append((node["name"], out, msg))
