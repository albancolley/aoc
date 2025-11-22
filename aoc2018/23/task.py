"""
AOC Day X
"""
import re
import sys
from math import sqrt

from common import AocBase
from common import configure
from dataclasses import dataclass

@dataclass
class Nanobot:
    x: int
    y: int
    z: int
    r: int

class Aoc201823(AocBase):
    """
    AOC Day 10 Class
    """

    def manhatten_distance(self, n1: Nanobot, n2: Nanobot)->int:
        return abs(n1.x - n2.x) + abs(n1.y - n2.y) + abs(n1.z - n2.z)

    def calc_1(self, nanobots : list[Nanobot]) -> int:
        strongest = None
        strength = 0

        max_radius  = 0
        for nanobot in nanobots:
            if max_radius < nanobot.r:
                max_radius = nanobot.r
                strongest = nanobot

        in_range = 0
        for nanobot2 in nanobots:
            distance = self.manhatten_distance(strongest, nanobot2)
            if distance <= strongest.r:
                in_range += 1

        return in_range

    def calc_2(self, nanobots: list[Nanobot]) -> int:
        ranges: dict = {}

        seen = []


        index = 0
        for nanobot in nanobots:
            if nanobot in seen:
                continue
            for nanobot2 in nanobots:
                distance = self.manhatten_distance(nanobot, nanobot2)
                if distance <= nanobot.r:
                    if index not in ranges:
                        ranges[index] = []
                    ranges[index].append(nanobot2)
                    seen.append(nanobot2)
            index += 1

        print(ranges)

        return 0


    # def calc_2(self, nanobots : list[Nanobot]) -> int:
    #     strongest = None
    #     strength = 0
    #     intersect: dict = {}
    #     strengths: dict = {}
    #     min_radius = nanobots[0].r
    #     for nanobot in nanobots:
    #         min_radius = min(min_radius, nanobot.r)
    #         center = (nanobot.x, nanobot.y, nanobot.z)
    #         intersect[center] = []
    #         in_range = 0
    #         for nanobot2 in nanobots:
    #             distance = self.manhatten_distance(nanobot,nanobot2)
    #             if distance <= nanobot.r + nanobot2.r:
    #                 in_range += 1
    #                 intersect[center].append(nanobot2)
    #         if in_range not in strengths:
    #             strengths[in_range] = []
    #         strengths[in_range].append(nanobot)
    #         if in_range > strength:
    #             strongest = nanobot
    #             strength = in_range
    #
    #     print(min_radius)
    #     # for s in strengths[strength]:
    #     #     print(s)
    #     best = intersect[(strongest.x, strongest.y, strongest.z)]
    #     # to low 77425102
    #     # to high 156242407
    #     return self.manhatten_distance(Nanobot(0,0,0,0), strongest)

    def load_handler_part1(self, data: list[str]) -> list[Nanobot]:
        regex = r"pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)"
        nanobots: list[Nanobot] = []
        for d in data:
            match = re.match(regex, d)
            nanobot = Nanobot(int(match.group(1)),int(match.group(2)),int(match.group(3)),int(match.group(4)))
            nanobots.append(nanobot)

        return nanobots

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201823()
    failed, results = aoc.run("part1x_[0-9]+.txt", "part2_[0-1]+.txt")
    if failed:
        sys.exit(1)
