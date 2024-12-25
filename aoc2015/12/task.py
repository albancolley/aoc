"""
AOC Day X
"""
import json
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math

class Aoc201600(AocBase):
    """
    AOC Day 10 Class
    """

    def recurse(self, data) -> int:
        sum = 0
        if isinstance(data, dict):
            for d in data:
                if isinstance(data[d], int):
                    sum += data[d]
                elif not isinstance(data[d], str):
                    sum += self.recurse(data[d])
        elif isinstance(data, list):
            for d in data:
                if isinstance(d, int):
                    sum += d
                elif not isinstance(d, str):
                    sum += self.recurse(d)
        return sum

    def calc_1(self, data: dict) -> int:
        return self.recurse(data)

    def recurse_red(self, data) -> int:
        sum = 0
        if isinstance(data, dict):
            for d in data:
                if data[d] == 'red':
                    return 0
                elif isinstance(data[d], int):
                    sum += data[d]
                elif not isinstance(data[d], str):
                    sum += self.recurse_red(data[d])
        elif isinstance(data, list):
            for d in data:
                if isinstance(d, int):
                    sum += d
                elif not isinstance(d, str):
                    sum += self.recurse_red(d)
        return sum
    def calc_2(self, data: {}) -> int:
        return self.recurse_red(data)

    def load_handler_part1(self, data: [str]) -> [str]:
       return json.loads(data[0])

    def load_handler_part2(self, data: [str]) -> [str]:
        return json.loads(data[0])


if __name__ == '__main__':
    configure()
    aoc = Aoc201600()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
