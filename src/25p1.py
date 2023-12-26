#!/usr/bin/env python3

import networkx as nx
from itertools import combinations

graph = nx.DiGraph()

for line in open(0):
    a, bs = line.split(":")
    for b in bs.split():
        graph.add_edge(a, b, capacity=1.0)
        graph.add_edge(b, a, capacity=1.0)

for a, b in combinations(graph.nodes, 2):
    cv, (l, r) = nx.minimum_cut(graph, a, b)
    if cv == 3:
        print(len(l) * len(r))
        break
