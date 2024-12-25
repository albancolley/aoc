"""
AOC Day X
"""
import sys
from collections import defaultdict

import numpy as np

from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math

class Aoc201721(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict) -> int:

        start_grid = "010001111"

        iterations, transformations = data

        grid = start_grid

        for iteration in range(iterations):
            new_grid = ""
            size = len(grid)
            width = int(math.sqrt(size))
            by = 2 if width % 2 else 3

            for i in range(0, size, by*width):
                line = ''
                for j in range(0, width, by):
                    sub_grid = ''
                    for s in range(by):
                        line += grid[i + j: i+j + by]
                new_grid += line



            grids = new_grid

        total = 0
        for grid in grids:
            total += sum([int(g) for g in grid]) * grids[grid]
        return total





    def calc_2(self, data: [str]) -> int:
        start_grid = "010001111"

        iterations, transformations = data

        grids = {start_grid: 1}
        for iteration in range(iterations):
            new_grids = defaultdict(int)
            for grid in grids:
                count = grids[grid]
                if len(grid) == 9:
                    new_grids[transformations[grid]] += count
                    print(grid, transformations[grid], count)
                else:
                    grid1 = grid[0:2] + grid[4:6]
                    grid2 = grid[2:4] + grid[6:8]
                    grid3 = grid[8:10] + grid[12:14]
                    grid4 = grid[10:12] + grid[14:16]

                    new_grids[transformations[grid1]] += count
                    new_grids[transformations[grid2]] += count
                    new_grids[transformations[grid3]] += count
                    new_grids[transformations[grid4]] += count
                    print(grid, transformations[grid1], transformations[grid2], transformations[grid3], transformations[grid4])

            grids = new_grids

        total = 0
        for grid in grids:
            total += sum([int(g) for g in grid]) * grids[grid]
        return total

    def load_handler_part1(self, data: [str]) -> [str]:
        row: str
        transformations = {}
        iterations = int(data[0])
        for row in data[1:]:
            parts = row.split(" => ")
            left = parts[0]
            right = parts[1]

            left_array = np.array([list(a) for a in left.replace("#", "1").replace(".", "0").split("/")])
            for r in range(4):
                # left_array = [[left_array[j][i] for j in range(len(left_array))] for i in range(len(left_array[0]) - 1, -1, -1)]
                transformations[''.join(left_array.flatten())] = self.to_ones_and_zeros(right)
                flip_up = np.flipud(left_array)
                transformations[''.join(flip_up.flatten())] = self.to_ones_and_zeros(right)
                flip_lr = np.fliplr(left_array)
                transformations[''.join(flip_lr.flatten())] = self.to_ones_and_zeros(right)
                left_array = np.rot90(left_array)
            # left_array.reverse()
            # for r in range(4):
            #     left_array = [[left_array[j][i] for j in range(len(left_array))] for i in range(len(left_array[0]) - 1, -1, -1)]
            #     left_numb = self.to_ones_and_zeros(''.join(sum(left_array, [])))
            #     transformations[left_numb] = self.to_ones_and_zeros(right)

        for t in transformations:
            print(t, transformations[t])

        return iterations, transformations

    def to_ones_and_zeros(self, left):
        return left.replace("/", "").replace("#", "1").replace(".", "0")


    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201721()
    failed, results = aoc.run("part1_[1-2]+.txt", "part2x_[0-9]+.txt")
    if failed:
        sys.exit(1)
