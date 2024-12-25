"""
AOC Day X
"""
import re
import sys
from collections import defaultdict

from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math

class Aoc201903(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict) -> int:
        fabric = defaultdict(int)
        for id in data:
            claim = data[id]
            x_start,y_start = claim[0]
            width, height = claim[1]
            for x in range(x_start+1, x_start + width + 1):
                for y in range(y_start+1, y_start + height + 1):
                    fabric[f'{x}-{y}'] += 1

        # for y in range(1,9):
        #     line = ""
        #     for x in range(1,9):
        #         line += str(fabric[f'{x}-{y}'])
        #     print(line)

        result = len([f for f in fabric.values() if f > 1])
        return result

    def calc_2(self, data: [str]) -> int:
        fabric = defaultdict(int)
        for id in data:
            claim = data[id]
            x_start, y_start = claim[0]
            width, height = claim[1]
            for x in range(x_start + 1, x_start + width + 1):
                for y in range(y_start + 1, y_start + height + 1):
                    fabric[f'{x}-{y}'] += 1

        for id in data:
            claim = data[id]
            x_start, y_start = claim[0]
            width, height = claim[1]
            total = 0
            for x in range(x_start + 1, x_start + width + 1):
                for y in range(y_start + 1, y_start + height + 1):
                    total += fabric[f'{x}-{y}']
            if total == width * height:
                return id
        return 0

    def load_handler_part1(self, data: [str]) -> {}:
        regex = r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)"

        claims = {}
        for d in data:
            match = re.match(regex, d)
            id = int(match.group(1))
            x = int(match.group(2))
            y = int(match.group(3))
            width = int(match.group(4))
            height = int(match.group(5))
            claims[id] = ((x,y), (width, height))
        return claims

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201903()
    failed, results = aoc.run("part1_[1-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
