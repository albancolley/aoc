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

    MOVES: complex = [
        -1 - 1j,
        -1 + 0j,
        -1 + 1j,
        0 - 1j,
        0 + 1j,
        1 - 1j,
        1 + 0j,
        1 + 1j,
    ]

    def view(self, width, height, grid):
        print()
        for y in range(0, height):
            line = ""
            for x in range(0, width):
                if grid[(x,y)] == 1:
                    line += '#'
                else:
                    line += '.'
            print(line)
        print()

    def count_on(self, pos: complex, grid: {}) -> int:
        count = 0
        move: complex
        for move in self.MOVES:
            new_pos:complex = pos + move
            if grid[(new_pos.real, new_pos.imag)] == 1:
                count += 1

        return count
    def calc_1(self, data: dict) -> int:
        steps: int
        width: int
        height: int
        grid: dict
        steps, width, height, grid = data
        for step in range(steps):
            new_grid = collections.defaultdict(int)
            for y in range(0, height):
                for x in range(0, width):
                    count = self.count_on(complex(x,y), grid)
                    if grid[(x,y)] == 1:
                        if 2 <= count <= 3:
                            new_grid[(x,y)] = 1
                    else:
                        if count == 3:
                            new_grid[(x,y)] = 1
            grid = new_grid

        return sum(grid.values())

        return count
    def calc_2(self, data: [str]) -> int:
        steps: int
        width: int
        height: int
        grid: dict
        steps, width, height, grid = data
        grid[(0,0)] = 1
        grid[(width-1,0)] = 1
        grid[(0,height-1)] = 1
        grid[(width-1,height-1)] = 1
        for step in range(steps):
            # self.view(grid)
            new_grid = collections.defaultdict(int)
            for y in range(0, height):
                for x in range(0, width):
                    count = self.count_on(complex(x,y), grid)
                    if grid[(x,y)] == 1:
                        if 2 <= count <= 3:
                            new_grid[(x,y)] = 1
                    else:
                        if count == 3:
                            new_grid[(x,y)] = 1
            grid = new_grid
            grid[(0,0)] = 1
            grid[(width-1,0)] = 1
            grid[(0,height-1)] = 1
            grid[(width-1,height-1)] = 1
        # self.view(grid)
        return sum(grid.values())

        return count

    def load_handler_part1(self, data: [str]) -> [str]:
        steps = int(data[0])
        grid_data = data[1:]
        width = len(grid_data[0])
        height = len(grid_data)
        grid = collections.defaultdict(int)
        for y in range(0, height):
            line = grid_data[y]
            for x in range(0, width):
                if line[x] == "#":
                    grid[(x,y)] = 1
        return steps, width, height, grid

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201600()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
