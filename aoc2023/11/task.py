"""
AOC Day 10
"""
import sys
from common import AocBase
from common import configure


class Aoc2023010(AocBase):
    """
    AOC Day 10 Class
    """

    moves = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    def calc_1(self, data: dict) -> int:
        galaxys, width, height = data
        galaxy_size = 1

        gaps_x, gaps_y = self.get_gaps(galaxys, width, height)

        seen = []
        distances = []
        for g in galaxys:
            seen.append(g)
            for g2 in galaxys:
                if g2 not in seen:
                    x, y = self.get_expaned_coords(g, galaxy_size, gaps_x, gaps_y, g2)
                    distances += [x + y]

        return sum(distances)

    def get_gaps(self, galaxys, width, height):
        seen_x = set()
        seen_y = set()
        for g in galaxys:
            seen_x.add(g[0])
            seen_y.add(g[1])

        all_x = set(range(0, width))
        all_y = set(range(0, height))

        different_x = all_x.difference(seen_x)
        different_y = all_y.difference(seen_y)

        return different_x, different_y

    def get_expaned_coords(self, g, gap_size, gaps_x: set, gaps_y: set , target_galaxy):
        step = 1
        if g[0] > target_galaxy[0]:
            step = -1
        gap_x_count = len(gaps_x.intersection(range(g[0], target_galaxy[0], step)))

        step = 1
        if g[1] > target_galaxy[1]:
            step = -1
        gap_y_count = len(gaps_y.intersection(range(g[1], target_galaxy[1], step)))

        new_x = abs(g[0] - target_galaxy[0]) + (gap_x_count * gap_size)
        new_y = abs(g[1] - target_galaxy[1]) + (gap_y_count * gap_size)
        return new_x, new_y

    def calc_2(self, data: [str]) -> int:
        galaxies, width, height = data

        galaxy_size = 1000000 - 1

        gaps_x, gaps_y = self.get_gaps(galaxies, width, height)

        seen = []
        distance = 0
        for g in galaxies:
            seen.append(g)
            for g2 in galaxies:
                if g2 not in seen:
                    x, y = self.get_expaned_coords(g, galaxy_size, gaps_x, gaps_y, g2)
                    distance += x + y

        return distance


    def load_handler_part1(self, data: [str]) -> [str]:
        result = {}
        galaxy_number = 1
        for y in range(0, len(data)):
            for x in range(0, len(data[0])):
                value = data[y][x]
                if value == '#':
                    result[(x, y)] = galaxy_number
                    galaxy_number += 1
        width = len(data[0])
        height = len(data)
        return result, width, height

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


# 449877432977 too low 9522407

if __name__ == '__main__':
    configure()
    aoc = Aoc2023010()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
