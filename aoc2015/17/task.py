"""
AOC Day X
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math
from itertools import combinations
from collections import defaultdict

class Aoc201600(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, sizes: ()) -> int:
        total = sizes[0]
        containers = sizes[1]
        count = 0
        for i in range(len(containers)):
            for c in combinations(containers, i+1):
                if sum(c) == total:
                    count += 1

        return count

    def calc_2(self, sizes: ()) -> int:
        total = sizes[0]
        containers = sizes[1]
        count: dict = defaultdict(int)
        for i in range(len(containers)):
            for c in combinations(containers, i+1):
                if sum(c) == total:
                    count[i] += 1

        return count[min(count.keys())]


    def load_handler_part1(self, data: [str]) -> [int]:
        sizes = []
        for d in data[1:]:
            sizes.append(int(d))

        return int(data[0]), sizes

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201600()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
