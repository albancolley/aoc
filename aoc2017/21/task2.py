"""
AOC Day X
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math
import numpy as np

class Aoc201721(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict) -> int:
        grid = [
            ['.', '#', '.'],
            ['.', '.', '#'],
            ['#', '#', '#']
        ]

        grid_string: str = self.array_to_string(grid)

        iterations, transformations = data

        for iteration in range(iterations):
            grid_rows = grid_string.split('/')
            # print(f"\niteration: {iteration}")
            # for l in grid_rows:
            #     print(l)
            size = len(grid_rows[0])
            step = 3
            if size % 2 == 0:
                step = 2

            new_grids = []
            for x in range(0, size, step):
                for y in range(0, size, step):
                    sub_grid = ""
                    for s in range(step):
                        sub_grid += grid_rows[y+s][x: x + step] + "/"
                    sub_grid = sub_grid[0:-1]
                    new_grid = transformations[sub_grid]
                    new_grids.append(new_grid)
                    # print(sub_grid, new_grid)

            # if len(new_grids) == 1:
            #     grid_string= new_grids[0]
            #     continue

            grid2 = []
            for l in range(len(new_grids[0].split('/'))):
                grid_row = ""
                for i in range(len(new_grids)):
                    grid_row += new_grids[i].split('/')[l]
                grid2 += [grid_row]


            width = len(grid2[0])
            height = len(grid2)

            new_width = int(width / math.sqrt(int(width/height)))

            grid_string = ""
            for i in range(0, width, new_width):
                for j in range(height):
                    grid_string += grid2[j][i:i+new_width] + "/"

            grid_string = grid_string[0:-1]
            # print(grid_string)

        return grid_string.count('#')

    def calc_2(self, data: [str]) -> int:
        grid = np.asarray([
            ['.', '#', '.'],
            ['.', '.', '#'],
            ['#', '#', '#']
        ])

        # grid_string: str = self.array_to_string(grid)

        iterations, transformations = data

        for _ in range(iterations):
            size = len(grid)
            by = 2 if size % 2 == 0 else 3
            new_size = size * (by + 1) // by
            new_grid = np.empty((new_size, new_size), dtype=str)
            squares = range(0, size, by)
            new_squares = range(0, new_size, by + 1)

            for i, ni in zip(squares, new_squares):
                for j, nj in zip(squares, new_squares):
                    square = grid[i:i + by, j:j + by]
                    enhanced = transformations['/'.join([ ''.join(a) for a in square.tolist()])]
                    new_grid[ni:ni + by + 1, nj:nj + by + 1] = np.array([list(a) for a in enhanced.split("/")])

            grid = new_grid

        total = 0
        for g in new_grid:
            for x in g:
                if x == '#':
                    total += 1
        return total

        # for iteration in range(iterations):
        #     grid_rows = grid_string.split('/')
        #     # print(f"\niteration: {iteration}")
        #     # for l in grid_rows:
        #     #     print(l)
        #     size = len(grid_rows[0])
        #     step = 3
        #     if size % 2 == 0:
        #         step = 2
        #
        #     new_grids = []
        #     for x in range(0, size, step):
        #         for y in range(0, size, step):
        #             sub_grid = ""
        #             for s in range(step):
        #                 sub_grid += grid_rows[y+s][x: x + step] + "/"
        #             sub_grid = sub_grid[0:-1]
        #             new_grid = transformations[sub_grid]
        #             new_grids.append(new_grid)
        #             # print(sub_grid, new_grid)
        #
        #     # if len(new_grids) == 1:
        #     #     grid_string= new_grids[0]
        #     #     continue
        #
        #     grid2 = []
        #     for l in range(len(new_grids[0].split('/'))):
        #         grid_row = ""
        #         for i in range(len(new_grids)):
        #             grid_row += new_grids[i].split('/')[l]
        #         grid2 += [grid_row]
        #
        #
        #     width = len(grid2[0])
        #     height = len(grid2)
        #
        #     new_width = int(width / math.sqrt(int(width/height)))
        #
        #     grid_string = ""
        #     for i in range(0, width, new_width):
        #         for j in range(height):
        #             grid_string += grid2[j][i:i+new_width] + "/"
        #
        #     grid_string = grid_string[0:-1]
        #     print(grid_string.count('#'))

        return grid_string.count('#')

    def load_handler_part1(self, data: [str]) -> [str]:
        row: str
        transformations = {}
        iterations = int(data[0])
        for row in data[1:]:
            parts = row.split(" => ")
            left = parts[0]
            right = parts[1]
            left_array = left.split("/")
            for i in range(len(left_array)):
                left_array[i] = [c for c in left_array[i]]
            for r in range(4):
                left_array = list(map(list, zip(*left_array[::-1])))
                left = self.array_to_string(left_array)
                transformations[left] = right
            left_array.reverse()
            for r in range(4):
                left_array = list(map(list, zip(*left_array[::-1])))
                left = self.array_to_string(left_array)
                transformations[left] = right

        # for t in transformations:
        #     print(t, transformations[t])

        return iterations, transformations

    def array_to_string(self, array):
        for i in range(len(array)):
            array[i] = ''.join(array[i])
        left = '/'.join(array)
        return left

    def load_handler_part2(self, data: [str]) -> [str]:
        row: str
        transformations = {}
        iterations = int(data[0])
        for row in data[1:]:
            parts = row.split(" => ")
            left = parts[0]
            right = parts[1]

            left_array = np.array([list(a) for a in left.split("/")])
            for r in range(4):
                # left_array = [[left_array[j][i] for j in range(len(left_array))] for i in range(len(left_array[0]) - 1, -1, -1)]
                transformations['/'.join([ ''.join(a) for a in left_array.tolist()])] = right
                flip_up = np.flipud(left_array)
                transformations['/'.join([ ''.join(a) for a in flip_up.tolist()])] = right
                flip_lr = np.fliplr(left_array)
                transformations['/'.join([ ''.join(a) for a in flip_lr.tolist()])] = right
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

if __name__ == '__main__':
    configure()
    aoc = Aoc201721()
    failed, results = aoc.run("part1x_[2-2]+.txt", "part2_[1-1]+.txt")
    if failed:
        sys.exit(1)
