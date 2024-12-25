"""
AOC Day X
"""
import sys
from collections import Counter

from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math

class Aoc201902(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict) -> int:
        threes = 0
        twos = 0
        for d in data:
            c = Counter(d)
            if 2 in c.values():
                twos += 1
            if 3 in c.values():
                threes += 1

        return threes * twos

    def calc_2(self, data: [str]) -> str:
        d: str
        q: str
        result:str = "wrong"
        for d in data:
            for q in data:
                count: int = 0
                difference:int = 0
                for i in range(len(d)):
                    if d[i] != q[i]:
                        difference = i
                        count += 1
                if count == 1:
                    return  d[0:difference] + d[difference+1:]

        return result

    def load_handler_part1(self, data: [str]) -> [str]:
       return data

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201902()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
