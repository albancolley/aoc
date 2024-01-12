import dataclasses

from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
from dataclasses import dataclass, field
from collections import defaultdict
import math
from collections import deque
import copy
import numpy as np

logger = logging.getLogger("ACO2019-24")



class Aoc201924(AocBase):

    def get_biodiversity_rating(self, grid):
        a = reversed(list(grid.flatten()))
        return int(''.join(str(x) for x in a),2)


    def count_neighbours(self, grid, x, y):
        count = 0
        if x - 1 >= 0:
            count += grid[x-1, y]
        if x + 1 < grid.shape[0]:
            count += grid[x+1, y]
        if y - 1 >= 0:
            count += grid[x, y-1]
        if y + 1 < grid.shape[1]:
            count += grid[x, y+1]

        return count

    def calc_1(self, data) -> int:

        br = self.get_biodiversity_rating(data)
        seen = {br: True}
        grid = data
        while True:
            new_grid = np.copy(grid)
            it = np.nditer(grid, flags=['multi_index'])
            for i in it:
                x = it.multi_index[0]
                y = it.multi_index[1]
                count = self.count_neighbours(grid, x, y)
                if count != 1 and grid[x, y] == 1:
                    new_grid[x, y] = 0
                elif 1 <= count <= 2 and grid[x][y] == 0:
                    new_grid[x, y] = 1
            grid = new_grid
            br = self.get_biodiversity_rating(grid)
            if br in seen:
                return br
            seen[br] = True
        return 0

    def calc_2(self, data) -> int:

        return 0

    def load_handler_part1(self, data: [str]) -> [str]:
        values = []
        for line in data:
            for c in line:
                value = 1
                if c == '.':
                    value = 0
                values.append(value)
        grid = np.array(values).reshape((len(data), len(data[0])))
        return grid



    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201924()
    failed, results = aoc.run("part1_[0-2]*.txt", "part2x_[1-4]+.txt")
    if failed:
        exit(1)
