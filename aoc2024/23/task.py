"""
AOC Day X
"""
import sys
from collections import defaultdict

from common import AocBase
from common import configure


class Aoc202423(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict) -> int:
        result = 0
        connections = set()
        for key in data:
            for key2 in data[key]:
                for key3 in data[key]:
                    if key2 != key3:
                        if key3 in data[key2]:
                            temp = [key, key2, key3]
                            temp.sort()
                            connections.add(tuple(temp))

        ts = []
        for c in connections:
            for t in c:
                if t.startswith('t'):
                    ts.append(c)
                    break

        return len(ts)

    def calc_2(self, data: dict) -> int:
        total = 0
        links = set()
        max_length = 0
        answers = []
        for key in data:
            possibles:list = data[key]
            # import itertools
            # for pair in itertools.permutations(data[key],2):
            #     if pair[0] not in data[pair[1]]:
            #         if pair[0] in possibles:
            #             possibles.remove(pair[0])

            # print(key, possibles)
            #
            nodes = []
            for node in possibles:
                node_set = set([node])
                for node2 in possibles:
                    if node != node2:
                        if node2 in data[node]:
                            node_set.add(node2)
                nodes += [sorted(list(node_set))]

            node_dict = defaultdict(int)
            max_length = 0
            for node in nodes:
                node_dict[",".join(node)] += 1

            answer = ""
            for path in node_dict:
                if len(path.split(",")) == node_dict[path]:
                    if len(path) > len(answer):
                        answer = path

            if answer:
                answers += [",".join(sorted([key] + answer.split(",")))]

        answers.sort(key=len)

        #
        #     connections = sorted([key] + list(nodes))
        #
        #     max_length = max(max_length, len(connections))
        #     links.add(tuple(connections))
        #
        # for key in links:
        #     if len(key) == max_length:
        #         print(key)

        return answers[-1]

    def load_handler_part1(self, data: [str]) -> [str]:
        graph = {}
        for d in data:
            connection = d.split("-")
            l = connection[0]
            r = connection[1]
            if l not in graph:
                graph[l] = []
            if r not in graph:
                graph[r] = []
            graph[l] += [r]
            graph[r] += [l]
        return graph

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc202423()
    failed, results = aoc.run("part1x_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
