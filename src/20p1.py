#!/usr/bin/env python3

from collections import deque

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

lo, hi = 0, 0

for _ in range(1000):
    lo += 1  # button is pressed
    q: deque[tuple[str, str, str]] = deque(
        [("broadcaster", x, "lo") for x in broadcast_targets]
    )

    while q:
        src, tgt, pulse = q.popleft()

        if pulse == "lo":
            lo += 1
        else:
            hi += 1

        if tgt not in nodes:
            continue

        node = nodes[tgt]

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

print(lo * hi)
