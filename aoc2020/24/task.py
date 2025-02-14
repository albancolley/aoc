"""
AOC Day 10
"""
import sys
from common import AocBase
from common import configure
import collections


class Aoc2023010(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: str) -> int:
        result = 0
        tiles = collections.defaultdict(bool)
        for d in data:
            tile = 0 + 0j
            pos = 0
            while pos < len(d):
                match d[pos]:
                    case 'e':
                        pos += 1
                        tile += 2
                    case 'w':
                        pos += 1
                        tile += -2
                match d[pos:pos+2]:
                    case 'se':
                        pos += 2
                        tile += 1 - 1j
                    case 'sw':
                        pos += 2
                        tile += -1 - 1j
                    case 'nw':
                        pos += 2
                        tile += -1 + 1j
                    case 'ne':
                        pos += 2
                        tile += 1 + 1j
            tiles[(tile.real, tile.imag)] = not tiles[(tile.real, tile.imag)]

        result = 0
        for tile in tiles:
            if tiles[tile]:
                result += 1

        return result

    def calc_2(self, data: [str]) -> int:
        total = 0
        return total

    def load_handler_part1(self, data: [str]) -> [str]:
       return data

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc2023010()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
