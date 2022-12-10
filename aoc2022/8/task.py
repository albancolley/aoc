import string

from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
import sys
import re
logger = logging.getLogger("ACO2022-7")


class Aoc202206(AocBase):

    def calc_1(self, data ) -> int:
        total = 0
        height = len(data)
        width = len(data[0])
        for x in range(0, height):
            if x == 0 or x == height -1:
                total += width
                continue
            for y in range(0, width):
                if y == 0 or y == width - 1:
                    total += 1
                    continue
                tree_height = data[x][y]

                visible = True
                for dx in range(x-1, -1, -1):
                    if tree_height <= data[dx][y]:
                        visible = False
                        break
                if visible:
                    total += 1
                    continue

                visible = True
                for dx in range(x + 1, height):
                    if tree_height <= data[dx][y]:
                        visible = False
                        break

                if visible:
                    total += 1
                    continue

                visible = True
                for dy in range(y - 1, -1, -1):
                    if tree_height <= data[x][dy]:
                        visible = False
                        break

                if visible:
                    total += 1
                    continue

                visible = True
                for dy in range(y + 1, width):
                    if tree_height <= data[x][dy]:
                        visible = False
                        break

                if visible:
                    total += 1
        return total

    def calc_2(self, data: [str]) -> int:
        total = 0
        viewing_distances=[]
        height = len(data)
        width = len(data[0])
        for x in range(0, height):
            if x == 0 or x == height - 1:
                total += width
                continue
            for y in range(0, width):
                if y == 0 or y == width - 1:
                    total += 1
                    continue
                tree_height = data[x][y]

                vx1 = 0
                vx2 = 0
                vy1 = 0
                vy2 = 0
                visible = True
                for dx in range(x - 1, -1, -1):
                    vx1 += 1
                    if tree_height <= data[dx][y]:
                        break

                visible = True
                for dx in range(x + 1, height):
                    vx2 += 1
                    if tree_height <= data[dx][y]:
                        break

                visible = True
                for dy in range(y - 1, -1, -1):
                    vy1 += 1
                    if tree_height <= data[x][dy]:
                        break

                visible = True
                for dy in range(y + 1, width):
                    vy2 += 1
                    if tree_height <= data[x][dy]:
                        break
                viewing_distances.append(vx1*vx2*vy1*vy2)
        viewing_distances.sort()
        return viewing_distances[-1]

    def load_handler_part1(self, data: [str]) -> [int]:
        new_data = []
        for row in data:
            new_data_row = []
            new_data.append(new_data_row)
            for cell in row:
                new_data_row.append(int(cell))
        return data

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)



if __name__ == '__main__':
    configure()
    aoc = Aoc202206()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        exit(1)
