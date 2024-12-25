"""
AOC Day X
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math
from itertools import permutations

class Aoc201600(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict) -> int:
        result = 0
        locations = set()
        distances = {}
        for d in data:
            dest_1, _, dest_2, _, distance_str = d.split()
            distance = int(distance_str)
            locations.add(dest_1)
            locations.add(dest_2)
            distances[(dest_1, dest_2)] = distance
            distances[(dest_2, dest_1)] = distance

        combs = permutations(list(locations), len(locations))

        totals = []
        for comb in combs:
            last = comb[0]
            total = 0
            for c in comb[1:]:
                total += distances[(last, c)]
                last = c
            totals += [total]

        return min(totals)

    def calc_2(self, data: [str]) -> int:
        locations = set()
        distances = {}
        for d in data:
            dest_1, _, dest_2, _, distance_str = d.split()
            distance = int(distance_str)
            locations.add(dest_1)
            locations.add(dest_2)
            distances[(dest_1, dest_2)] = distance
            distances[(dest_2, dest_1)] = distance

        combs = permutations(list(locations), len(locations))

        totals = []
        for comb in combs:
            last = comb[0]
            total = 0
            for c in comb[1:]:
                total += distances[(last, c)]
                last = c
            totals += [total]

        return max(totals)

    def load_handler_part1(self, data: [str]) -> [str]:
       return data

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201600()
    failed, results = aoc.run("part1_[1-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
