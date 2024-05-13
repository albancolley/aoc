"""
AOC Day 2016- 25
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math


class Aoc201625(AocBase):
    """
    AOC Day 25 Class
    """

    def calc_1(self, data: dict) -> int:
        pos = 0
        # data = data[1:]
        a = 1
        reg = {'a': a, 'b': 0, 'c': 0, 'd': 0}
        transmitted = [1]
        while pos < len(data):
            instruction = data[pos]
            command, x, *y = instruction.split(' ')
            y = y[0] if y else None
            x_is_reg = x in ['a', 'b', 'c', 'd']
            match command:
                case "cpy":
                    if x_is_reg:
                        value = reg[x]
                    else:
                        value = int(x)
                    reg[y] = value
                case "out":
                    value = reg[x]
                    if value not in [0, 1] or value == transmitted[-1]:
                        transmitted = [1]
                        pos = 0
                        a += 1
                        reg = {'a': a, 'b': 0, 'c': 0, 'd': 0}
                        continue
                    else:
                        transmitted.append(value)
                    if len(transmitted) > 10:
                        return a
                case "inc":
                    reg[x] += 1
                case "dec":
                    reg[x] -= 1
                case "jnz":
                    if x_is_reg:
                        value = reg[x]
                    else:
                        value = int(x)
                    if value != 0:
                        pos += int(y)
                        continue
            pos += 1
        return -1

    def calc_2(self, data: [str]) -> int:
        return 0

    def load_handler_part1(self, data: [str]) -> [str]:
        return data

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201625()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
