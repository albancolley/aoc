"""
AOC Day X
"""
import re
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math

class Aoc201600(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: (int,int)) -> int:
        total = 20151125
        row, col = data
        repeats = int((row+col-2)*(row+col-1)/2 - 1)
        for i in range(repeats):
            total = (total * 252533) % 33554393

        for i in range(col):
            total = (total * 252533) % 33554393

        return total

    def calc_2(self, data: [str]) -> int:
        total = 0
        return total

    def load_handler_part1(self, data: [str]) ->(int,int):
        p = re.compile(r'To continue, please consult the code grid in the manual.  Enter the code at row (\d+), column (\d+).')
        m = re.match(p, data[0])
        row = int(m.group(1))
        column = int(m.group(2))
        return row, column

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201600()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
