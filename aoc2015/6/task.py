"""
AOC Day X
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
from collections import defaultdict
import math

class Aoc201600(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict) -> int:
        result = 0
        grid = defaultdict(int)
        d : str
        for d in data:
            command = d.split(' ')
            if command[0] == 'toggle':
                first = command[1].split(',')
                x1 = int(first[0])
                y1 = int(first[1])
                second = command[3].split(',')
                x2 = int(second[0])
                y2 = int(second[1])
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        if grid[f'{x}-{y}'] == 0:
                            grid[f'{x}-{y}'] = 1
                        else:
                            grid[f'{x}-{y}'] = 0
            elif command[0] == 'turn':
                first = command[2].split(',')
                x1 = int(first[0])
                y1 = int(first[1])
                second = command[4].split(',')
                x2 = int(second[0])
                y2 = int(second[1])
                value = 1
                if command[1] == 'off':
                    value = 0
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        grid[f'{x}-{y}'] = value


        for g in grid:
            if grid[g] == 1:
                result += 1
        return result

    def calc_2(self, data: [str]) -> int:
        result = 0
        grid = defaultdict(int)
        d: str
        for d in data:
            command = d.split(' ')
            if command[0] == 'toggle':
                first = command[1].split(',')
                x1 = int(first[0])
                y1 = int(first[1])
                second = command[3].split(',')
                x2 = int(second[0])
                y2 = int(second[1])
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        grid[f'{x}-{y}'] += 2
            elif command[0] == 'turn':
                first = command[2].split(',')
                x1 = int(first[0])
                y1 = int(first[1])
                second = command[4].split(',')
                x2 = int(second[0])
                y2 = int(second[1])
                value = 1
                if command[1] == 'off':
                    value = -1
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        grid[f'{x}-{y}'] = max(0, grid[f'{x}-{y}']+value)

        for g in grid:
            result += grid[g]
        return result
    def load_handler_part1(self, data: [str]) -> [str]:
       return data

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201600()
    failed, results = aoc.run("part1x_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
