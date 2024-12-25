"""
AOC Day X
"""
import sys

from sympy.physics.units import length

from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math

class Aoc202400(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, grid) -> int:
        match = ["XMAS", "SAMX"]
        result = 0
        data, width, height = grid
        width = len(data[0])
        height = len(data)
        for y in range(height-3):
            for x in range(width -3):
                hor = data[y][x:x+4]
                down = data[y][x] + data[y+1][x] + data[y+2][x] + data[y+3][x]
                left =  data[y][x] + data[y+1][x-1] + data[y+2][x-2] + data[y+3][x-3]
                right =  data[y][x] + data[y+1][x+1] + data[y+2][x+2] + data[y+3][x+3]
                if hor in match:
                    result += 1
                if down in match:
                    result += 1
                if left in match:
                    result += 1
                if right in match:
                    result += 1

        return result

    def calc_2(self, grid) -> int:
        match = ["MAS", "SAM"]
        result = 0
        data, width, height = grid
        width = len(data[0])
        height = len(data)
        for y in range(1, height - 3):
            for x in range(1, width - 3):
                if data[y][x] == "A":
                    left = data[y-1][x-1] + data[y][x] + data[y + 1][x + 1]
                    right = data[y-1][x+1] + data[y][x] + data[y + 1][x - 1]
                    if right in match and left in match:
                        result += 1
        return result

    def load_handler_part1(self, data: [str]) -> [str]:
        grid = []
        width = len(data[0])
        height = len(data)
        for y in range(height):
            line = "0000"
            line += data[y]
            line += "0000"
            grid += [line]
        for y in range(4):
            grid += ["0" * (8 + width)]
        return grid, width, height

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc202400()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
