"""
AOC Day X
"""
from dataclasses import dataclass
import sys
from common import AocBase
from common import configure


@dataclass
class Node:
    name: str
    weight: int
    children: [str]

class Aoc201707(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data ) -> int:
        all_programs: set
        sub_programs: set
        all_programs, sub_programs = data
        diff = all_programs.difference(sub_programs)
        return list(diff)[0]

    new_weight = 0
    def dfs(self, tree: dict[str, Node], pos: str):
        node = tree[pos]
        if len(node.children) == 0:
            return node.weight

        weights = []
        for child_node in node.children:
            weights.append(self.dfs(tree, child_node))

        # print(node, weights)

        max_weight = max(weights)
        min_weight = min(weights)
        if max_weight == min_weight:
            return sum(weights) + node.weight

        wrong_node = node.children[weights.index(max_weight)]
        if weights.count(min_weight) == 1:
            wrong_node = node.children[weights.index(min_weight)]

        self.new_weight = tree[wrong_node].weight - max_weight + min_weight

        return sum(weights) + node.weight - max_weight + min_weight

    def calc_2(self, data: [str]) -> int:
        tree, top = data
        self.dfs(tree, top)
        return self.new_weight

    def load_handler_part1(self, data: [str]) -> [str]:
        all_programs = set()
        sub_programs = set()
        for r in data:
            t = r.split(' -> ')
            name = t[0].split(' ')[0]
            all_programs.add(name)
            if len(t) > 1:
                sub_programs.update(t[1].split(', '))
        return all_programs, sub_programs

    def load_handler_part2(self, data: [str]) -> [str]:
        tree = {}
        all_programs = set()
        sub_programs = set()
        for r in data:
            t = r.split(' -> ')
            left = t[0].split(' (')
            name = left[0]
            weight = int(left[1][0:-1])
            all_programs.add(name)
            if len(t) == 1:
                node = Node(name,weight, [])
            else:
                right = t[1].split(', ')
                sub_programs.update(right)
                node = Node(name, weight, right)
            tree[node.name] = node

        top = list(all_programs.difference(sub_programs))[0]
        return tree, top

if __name__ == '__main__':
    configure()
    aoc = Aoc201707()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
