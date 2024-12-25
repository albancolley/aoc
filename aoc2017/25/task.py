"""
AOC Day X
"""
import sys
from collections import defaultdict

from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math

class Aoc201725(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict) -> int:
        pos = 0
        tape = defaultdict(int)
        state = data[0]
        steps = data[1]
        conditions = data[2]
        for _ in range(0, steps):
            value = tape[pos]
            condition = conditions[state][value]
            tape[pos] = condition[0]
            if condition[1][0] =='r':
                pos += 1
            else:
                pos -= 1
            state = condition[2]
        result = sum(tape.values())
        return result

    def calc_2(self, data: [str]) -> int:
        total = 0
        return total

    def load_handler_part1(self, data: [str]) -> [str]:
        state = data[0].split()[-1][0:-1]
        steps = int(data[1].split()[-2])

        conditions = {}
        pos = 3

        while len(data) > pos:
            step = data[pos].split()[-1][0:-1]
            zero = (
                int(data[pos + 2].split()[-1][0:-1]),
                data[pos + 3].split()[-1][0:-1],
                data[pos + 4].split()[-1][0:-1],
            )
            one = (
                int(data[pos + 6].split()[-1][0:-1]),
                data[pos + 7].split()[-1][0:-1],
                data[pos + 8].split()[-1][0:-1],
            )
            pos += 10
            conditions[step] = (zero, one)

        return state, steps, conditions

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201725()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2x_[0-9]+.txt")
    if failed:
        sys.exit(1)
