"""
AOC Day X
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math

class Aoc202408(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict) -> int:
        antennas, height, width = data
        # print(antennas)
        antinodes = set()
        for antenna in antennas:
            locations = antennas[antenna]
            for l1 in locations:
                for l2 in locations:
                    if l1 != l2:
                        antinode = (l1[0] + (l1[0] - l2[0]), l1[1] + (l1[1]- l2[1]) )
                        if 0 <= antinode[0] < width and 0 <= antinode[1] < height:
                            # print(l1,l2,antinode)
                            antinodes.add(antinode)
        return len(antinodes)

    def calc_2(self, data: [str]) -> int:
        antennas, height, width = data
        # print(antennas)
        antinodes = set()
        for antenna in antennas:
            locations = antennas[antenna]
            for l1 in locations:
                for l2 in locations:
                    if l1 != l2:
                        x = l1[0]
                        dx = l1[0] - l2[0]
                        y =  l1[1]
                        dy = l1[1] - l2[1]
                        antinodes.add((x,y))
                        x = x + dx
                        y = y + dy
                        while 0 <= x < width and 0 <= y < height:
                            antinode = (x, y)
                            # print(l1, l2, antinode)
                            antinodes.add(antinode)
                            x = x + dx
                            y = y + dy
        return len(antinodes)

    def load_handler_part1(self, data: [str]) -> [str]:
        antennas = {}
        height = len(data)
        width = len(data[0])
        for y in range(height):
            for x in range(width):
                value = data[y][x]
                if value != ".":
                    if value not in antennas:
                        antennas[value] = []
                    antennas[value].append((x,y))
        return antennas, height, width

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc202408()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
