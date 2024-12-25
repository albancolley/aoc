"""
AOC Day X
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math

class Aoc202402(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: []) -> int:
        result = 0
        for d in data:
            differences = []
            for l in range(0, len(d)-1):
                differences += [d[l] - d[l+1]]
            if max(differences) > 3 or min(differences) < -3:
                continue
            if min(differences) < 0 < max(differences):
                continue
            if 0 in differences:
                continue
            result += 1
        return result

    def calc_2(self, data: [str]) -> int:
        result = 0
        d1: []
        for d1 in data:
            for i in range(len(d1)):
                d = d1[0:i] + d1[i+1:]
                differences = []
                for l in range(0, len(d)-1):
                    differences += [d[l] - d[l+1]]
                if max(differences) > 3 or min(differences) < -3:
                    continue
                if min(differences) < 0 < max(differences):
                    continue
                if 0 in differences:
                    continue
                result += 1
                break
        return result

    def load_handler_part1(self, data: [str]) -> [str]:
        result = []
        for d in data:
            result.append([int(x) for x in d.split()])
        return result

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc202402()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
