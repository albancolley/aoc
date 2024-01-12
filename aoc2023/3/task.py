from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import logging
import re


logger = logging.getLogger("ACO2023-1")

class Aoc202301(AocBase):


    def get_adjacent(self, pos):
        results = []
        x , y = pos
        for x1 in range(-1, 2):
            for y1 in range(-1,2):
                if not (x1 == 0 and y1 == 0):
                    results.append((x+x1, y+y1))
        return results

    def calc_1(self, data: dict) -> int:
        total = 0
        seen_number = []
        for pos in data:
            cell = data[pos][0]
            if cell > 0:
                adjacent = self.get_adjacent(pos)
                for a in adjacent:
                    if a in data and data[a][0] == 0:
                        if data[pos][1] not in seen_number:
                            total += cell
                            seen_number.append(data[pos][1])

        return total

    def calc_2(self, data: [str]) -> int:
        total = 0
        for pos in data:
            cell = data[pos][0]
            if cell == 0:
                ratio = 1
                count = 0
                seen_number = []
                adjacent = self.get_adjacent(pos)
                for a in adjacent:
                    if a in data and data[a][0] > 0:
                        if data[a][1] not in seen_number:
                            ratio *= data[a][0]
                            seen_number.append(data[a][1])
                            count += 1
                if count == 2:
                    total += ratio

        return total

        return total

    def load_handler_part1(self, data: [str]) -> [str]:

        grid = {}
        values = {}
        x = 0
        num_count = 0
        for row in data:
            num = 0
            y = 0
            for cell in row:
                if cell in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    if num > 0:
                        num = num * 10
                    else:
                        start_y = y
                    num += int(cell)
                else:
                    if num > 0:
                        for pos in range(start_y, y):
                            grid[(x, pos)] = (num, num_count)
                    num = 0
                    num_count += 1

                if cell != '.':
                    grid[(x,y)] = (0, 0)
                y += 1
            x+=1
        return grid

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc202301()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        exit(1)
