"""
AOC Day X
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math

class Aoc201722(AocBase):
    """
    AOC Day 10 Class
    """

    moves = {
        'U': 0 - 1j,
        'D': 0 + 1j,
        'L': -1,
        'R': 1
    }

    directions = {
        'R': {'U': 'R', 'R': 'D', 'D':'L', 'L': 'U'},
        'L': {'U': 'L', 'L': 'D', 'D': 'R', 'R': 'U'},
        2: {'U': 'R', 'R': 'D', 'D':'L', 'L': 'U'},
        0: {'U': 'L', 'L': 'D', 'D': 'R', 'R': 'U'},
        1: {'U': 'U', 'L': 'L', 'D': 'D', 'R': 'R'},
        3: {'U': 'D', 'L': 'R', 'D': 'U', 'R': 'L'},
    }

    def calc_1(self, grid: dict) -> int:
        pos = 0 + 0j
        direction = 'U'
        infections = 0
        for i in range(10000):
            x = int(pos.real)
            y = int(pos.imag)
            infected = grid[(x,y)]
            turn = 'L'
            if infected:
                turn = 'R'

            direction = self.directions[turn][direction]

            if not infected:
                infections += 1

            grid[(x, y)] = not infected


            pos += self.moves[direction]

        return infections

    def calc_2(self, grid: dict) -> int:
        pos = 0 + 0j
        direction = 'U'
        infections = 0
        for i in range(10000000):
            x = int(pos.real)
            y = int(pos.imag)
            infected = grid[(x, y)]

            direction = self.directions[infected][direction]

            if infected == 1:
                infections += 1

            grid[(x, y)] = (infected + 1) % 4

            pos += self.moves[direction]

        return infections

    def load_handler_part1(self, data: [str]) -> [str]:
        grid = collections.defaultdict(int)
        height = len(data)
        width = len(data[0])
        y = -int((height-1) /2)
        x = -int((width-1) /2)
        for row in data:
            x = -int((width-1) /2)
            for c in row:
                if c == "#":
                    grid[(x,y)] = 2
                x += 1
            y += 1

        return grid

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201722()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
