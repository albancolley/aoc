"""
AOC Day X
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math

class Aoc201717(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: int) -> int:
        spinlock = data
        memory = [0]
        pos = 0
        for i in range(1, 2017 + 1):
            pos = (pos + spinlock) % len(memory)
            pos += 1
            memory.insert(pos, i)
        return memory[(pos + 1) % len(memory)]

    def calc_2(self, data: [str]) -> int:
        spinlock = data
        pos2 = 0
        for i in range(1, 50000000+1):
            pos2 = ((pos2 + spinlock) % i) + 1
            if pos2 == 1:
                last = i
        return last

    def load_handler_part1(self, data: [str]) -> int:
       return int(data[0])

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201717()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
