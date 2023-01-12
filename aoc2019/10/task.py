from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
from dataclasses import dataclass, field
from collections import defaultdict
import math

logger = logging.getLogger("ACO2019-2")


class Aoc201910(AocBase):

    def lcm(self, a, b):
        return abs(a * b) // math.gcd(a, b)

    def calc_1(self, grid: {}) -> int:
        m, _, _ = self.get_best(grid)
        return m

    def get_best(self, grid):
        m = 0
        coords = (0, 0)
        save = {}
        for x, y in grid:
            lines = {}
            for x1, y1 in grid:
                if x == x1 and y == y1:
                    continue
                myradians = math.atan2(x1 - x, y1 - y)
                if (x - x1) == 0:
                    if y > y1:
                        ll = "x"
                    else:
                        ll = "-x"
                elif (y - y1) == 0:
                    if x > x1:
                        ll = "y"
                    else:
                        ll = "-y"
                else:

                    y2 = (y - y1)
                    x2 = (x - x1)
                    g = math.gcd(y2, x2)
                    ll = (int(x2 / g), int(y2 / g))
                if myradians not in lines:
                    lines[myradians] = []
                lines[myradians].append((math.dist([x, y], [x1, y1]), (x1, y1)))
            if len(lines) > m:
                m = len(lines)
                save = lines
                coords = (x, y)
        for c in save:
            save[c].sort()
        return m, coords, save

    def calc_2(self, grid: {}) -> int:
        _, coords, lines = self.get_best(grid)
        radians = []
        for l in lines:
            radians.append(l)
        radians.sort()
        radians.reverse()
        index = 0
        targets = []
        found = True
        while found:
            found = False
            for r in radians:
                if len(lines[r]) > index:
                    found = True
                    targets.append(lines[r][index][1])
            index += 1

        return targets[199][0] * 100 + targets[199][1]


    def load_handler_part1(self, data: [str]) -> [str]:
        grid = {}
        y = 0
        for l in data:
            x = 0
            for c in l:
                if c == '#':
                    grid[(x, y)] = True
                x += 1
            y += 1
        return grid

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201910()
    failed, results = aoc.run("part1_[1-9]*.txt", "part2_[0-9]+.txt")
    if failed:
        exit(1)
