"""
AOC Day X
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math

class Aoc201704(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: [[str]]) -> int:
        result = 0
        for r in data:
            dups ={}
            has_dups = False
            for word in r:
                if word in dups:
                    has_dups = True
                    break
                dups[word] = 1
            if not has_dups:
                result += 1
        return result

    def calc_2(self, data: [str]) -> int:
        result = 0
        for r in data:
            dups = {}
            has_dups = False
            for word in r:
                sorted_word = "".join(sorted(word))
                if sorted_word in dups:
                    has_dups = True
                    break
                dups[sorted_word] = 1
            if not has_dups:
                result += 1
        return result

    def load_handler_part1(self, data: [str]) -> [[str]]:
       return [d.split() for d in data]

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201704()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
