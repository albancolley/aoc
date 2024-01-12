"""
AOC Day 10
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math
from collections import defaultdict
import copy
import networkx as nx
import matplotlib.pyplot as plt

class Aoc2023010(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict) -> int:

        graph, edges = data

        G = nx.Graph()
        G.add_edges_from(edges)
        b = nx.betweenness_centrality(G)
        a = sorted([(b[n],n) for n in b])
        best = a[-1][1]
        for node in G[best]:
            G2 = G.copy()
            G2.remove_edge(best,node)
            b2 = nx.betweenness_centrality(G2)
            a2 = sorted([(b2[n],n) for n in b2])
            # print(best, node, a2[-1])
            best2 = a2[-1][1]
            for node2 in G2[best2]:
                G3 = G2.copy()
                G3.remove_edge(best2,node2)
                b3 = nx.betweenness_centrality(G3)
                a3 = sorted([(b3[n],n) for n in b3])
                # print(best2, node2, a3[-1])
                best3 = a3[-1][1]
                for node3 in G3[best3]:
                    G4 = G3.copy()
                    G4.remove_edge(best3, node3)
                    sub_graphs = [G4.subgraph(c).copy() for c in nx.connected_components(G4)]
                    # print(best3, node3)
                    # print(min_cluster, e, min_cluster2, e2, min_cluster3, e3)
                    if len(sub_graphs) == 2:
                        # print(node, best, node2, best2, node3, best3)
                        return len(sub_graphs[0]) * len(sub_graphs[1])

        # pos = nx.spring_layout(G)
        return 0


    def calc_2(self, data: [str]) -> int:
        total = 0
        return total

    def load_handler_part1(self, data: [str]) -> [str]:
        graph = defaultdict(set)
        edges = set()
        for line in data:
            s = line.split(': ')
            node = s[0].strip()
            connections = s[1].split(' ')
            for c in connections:
                graph[node].add(c)
                edges.add((node, c))
                graph[c].add(node)
        return graph, list(edges)

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)



if __name__ == '__main__':
    configure()
    aoc = Aoc2023010()
    failed, results = aoc.run("part1_[1-2]+.txt", "part2x_[1-2]+.txt")
    if failed:
        sys.exit(1)
