import dataclasses

from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
from dataclasses import dataclass, field
from collections import defaultdict
import math
from collections import deque
import copy

logger = logging.getLogger("ACO2019-14")

class Node(object):
    def __init__(self, data, cost, child_costs):
        self.name = data
        self.cost = cost
        self.child_costs = child_costs
        self.parents = []
        self.children = []
        self.parts = []
        self.total = 1

    def add_child(self, obj):
        self.children.append(obj)

class Aoc201914(AocBase):

    def calc_1(self, data) -> int:
        nodes = data
        total = self.run_factory(nodes)
        return total

    def run_factory(self, nodes):
        queue = deque()
        for node_name in nodes:
            node = nodes[node_name]
            queue.append(node)
        while len(queue) > 0:
            node = queue.popleft()
            if len(node.parts) != len(node.parents):
                queue.append(node)
                continue

            for i, child in enumerate(node.children):
                child.parts.append(node.child_costs[i] * node.total)
                if len(child.parts) == len(child.parents):
                    child.total = math.ceil(sum(child.parts) / child.cost)
        total = 0
        for node_name in nodes:
            node = nodes[node_name]
            if len(node.children) == 0:
                total += node.child_costs[0] * node.total
        return total


    def calc_2(self, data) -> int:
        nodes = copy.deepcopy(data)
        one = self.run_factory(nodes)
        target = 1000000000000
        guess = int(target / one)
        last_guess = -1
        while guess != last_guess:
            last_guess = guess
            nodes = copy.deepcopy(data)
            nodes['FUEL'].total = guess
            total = self.run_factory(nodes)
            diff = target - total
            if diff < 0:
                guess -= int(diff / one)
            elif diff > 0:
                guess += int(diff / one)

        return guess

    def load_handler_part1(self, data: [str]) -> [str]:
        factories: {} = {}
        for line in data:
            a = line.split(' => ')
            b = a[0].split(', ')
            f = a[1].split(' ')
            f_number = int(f[0])
            f_name = f[1]
            children = []
            costs = []
            for c in b:
                d = c.split(' ')
                ingredients_name = d[1]
                ingredients_number = int(d[0])
                children.append(ingredients_name)
                costs.append(ingredients_number)
            factories[f_name] = (f_number, children, costs)


        nodes: {Node} = {}
        queue = deque()
        queue.append((None, 'FUEL'))
        while len(queue) > 0:
            parent, name = queue.popleft()
            if name == 'ORE':
                continue
            if name in nodes:
                node = nodes[name]
            else:
                node = Node(name, factories[name][0], factories[name][2])
                nodes[name] = node
            for children in factories[name][1]:
                queue.append((node, children))

        for f in factories:
            factory = factories[f]
            for c in factory[1]:
                if c == 'ORE':
                    continue
                nodes[f].add_child(nodes[c])
                nodes[c].parents.append(nodes[f])
        return nodes



    def load_handler_part1s(self, data: [str]) -> [str]:
        factories: {} = {}
        ores: {} = {}
        for line in data:
            a = line.split(' => ')
            b = a[0].split(', ')
            ingredients = []
            f = a[1].split(' ')
            f_number = int(f[0])
            f_name = f[1]
            for c in b:
                d = c.split(' ')
                ingredients_name = d[1]
                ingredients_number = int(d[0])
                ingredients.append((ingredients_number, ingredients_name))
                if ingredients_name == 'ORE':
                    ores[f_name] = (ingredients_number, f_number)
            factories[f_name] = ((f_number, f_name), ingredients)

        return factories, ores

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201914()
    failed, results = aoc.run("part1_[0-9]*.txt", "part2_[0-9]+.txt")
    if failed:
        exit(1)
