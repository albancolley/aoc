"""
AOC Day X
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math

class Aoc201600(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict) -> str:
        result = ""
        values = [[]] * len(data[0])
        for d in data:
            for i in range(len(d)):
                values[i] = values[i] + [d[i]]
        for v in values:
            result += collections.Counter(v).most_common(1)[0][0]
        return result

    def calc_2(self, data: [str]) -> int:
        result = ""
        values = [[]] * len(data[0])
        for d in data:
            for i in range(len(d)):
                values[i] = values[i] + [d[i]]
        for v in values:
            result += collections.Counter(v).most_common()[-1][0]
        return result

    def load_handler_part1(self, data: [str]) -> [str]:
       return data

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201600()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
