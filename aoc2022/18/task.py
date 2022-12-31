import os.path
import string

from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
from dataclasses import dataclass
import re
from collections import deque


logger = logging.getLogger("ACO2022-17")


@dataclass
class Point:
    x: int
    y: int
    z: int

    def __hash__(self):
     return hash((self.x, self.y, self.z))

class Aoc202212(AocBase):

    def calc_1(self, data: [Point]) -> int:
        overlaps = {}
        sides = 6 * len(data)
        overlap_count2 = 0
        xy = {}
        xz = {}
        yz = {}
        checks = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]
        for p in data:

            for dx, dy, dz in checks:
                dp = Point(p.x + dx, p.y + dy, p.z + dz)
                if dp.x == p.x and dp.y == p.y and dp.z == p.z:
                    continue
                if dp in data:
                    overlap_count2 += 1
                    if (dp.x, dp.y, dp.z) not in overlaps:
                         overlaps[(dp.x, dp.y, dp.z)] = 1
                    else:
                        overlaps[(dp.x, dp.y, dp.z)] += 1

        area = 0
        for key in overlaps:
            area += 6 - overlaps[key]

        total = sides - overlap_count2
        return total


    def calc_2(self, data: [Point]) -> int:
        overlaps = {}

        min_point = Point(data[0].x, data[0].y, data[0].z)
        checks = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]
        for p in data:
            if min_point.x > p.x:
                min_point = Point(p.x, p.y, p.z)
            for dx, dy, dz in checks:
                dp = Point(p.x + dx, p.y + dy, p.z + dz)
                if dp.x == p.x and dp.y == p.y and dp.z == p.z:
                    continue
                if dp in data:
                    if dp not in overlaps:
                        overlaps[dp] = True



        min_point.x -= 1

        total = 0
        checks2 = []
        for dx in range(-1,2):
            for dy in range(-1, 2):
                for dz in range(-1, 2):
                    if dx == 0 and dy == 0 and dz == 0:
                        continue
                    checks2.append((dx, dy, dz))

        q = deque()
        q.append(min_point)
        seen = {}

        while len(q) > 0:
            p = q.popleft()
            if p in seen:
                continue
            seen[p] = True
            for dx, dy, dz in checks:
                next_point = Point(p.x + dx, p.y + dy, p.z + dz)
                if next_point in seen:
                    continue
                if next_point in data:
                    total += 1
                    continue
                alone = self.is_alone(checks2, data, next_point)
                if alone:
                    continue

                q.append(next_point)

        return total

    def is_alone(self, checks2, data, next_point):
        alone = True
        for dx, dy, dz in checks2:
            dp = Point(next_point.x + dx, next_point.y + dy, next_point.z + dz)
            if dp in data:
                return False
        return alone

    def load_handler_part1(self, data: [str]) -> {}:
            points :[Point] = []
            for row in data:
                x = row.split(',')
                p = Point(int(x[0]), int(x[1]), int(x[2]))
                points.append(p)
            return points

    def load_handler_part2(self, data: [str]) -> [str]:
            return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc202212()
    failed, results = aoc.run("part1x_[0-9]+.txt", "part2_[1-3]+.txt")
    if failed:
        exit(1)
