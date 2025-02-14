"""
AOC Day X
"""
import sys
from collections import defaultdict

from common import AocBase
from common import configure


class Aoc201900(AocBase):
    """
    AOC Day 10 Class
    """

    def manhattan_distance(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


    def calc_1(self, data: [tuple[int,int]]) -> int:
        result = 0
        grid: dict[tuple[int, int], (int, tuple[int, int]) ]  = {}
        grid_size = 1000
        for y in range(-grid_size, grid_size+1):
            for x in range(-grid_size, grid_size+1):
                distance = self.manhattan_distance((x, y), data[0])
                new_point = (x, y)
                grid[new_point] = (distance, data[0])
                for p in data[1:]:
                    distance =  self.manhattan_distance((x,y), p)
                    if grid[(x,y)][0] > distance:
                        grid[(x, y)] = (distance, p)
                    elif grid[(x,y)][0] == distance:
                        grid[(x, y)] = (distance, (-1,-1))


        infinite = set()
        for x in range(-grid_size, grid_size+1):
            infinite.add(grid[(x, -grid_size)][1])
            infinite.add(grid[(x, grid_size)][1])
            infinite.add(grid[(-grid_size, x)][1])
            infinite.add(grid[(grid_size, x)][1])

        d2 :set = set(data)
        # d3 = d2.remove()
        names = {}
        i = "A"
        names[(-1, -1)] = "."
        for p in data:
            names[p] = str(i)
            i = chr(ord(i) + 1)

        infinite.remove((-1, -1))
        d3 = d2.difference(infinite)

        counts = defaultdict(int)
        for v in grid.values():
            if v[1] in d3:
                counts[v[1]] += 1
        #
        # for y in range(-grid_size, grid_size+1):
        #     line = ""
        #     for x in range(-grid_size, grid_size+1):
        #         line += names[grid[(x,y)][1]]
        #     print(line)

        return max(counts.values())

    def calc_2(self, data: [str]) -> int:
        grid: dict[tuple[int, int], (int, tuple[int, int])] = {}
        grid_size = 1000
        for y in range(-grid_size, grid_size + 1):
            for x in range(-grid_size, grid_size + 1):
                distance = self.manhattan_distance((x, y), data[0])
                new_point = (x, y)
                grid[new_point] = distance
                for p in data[1:]:
                    distance = self.manhattan_distance((x, y), p)
                    grid[(x, y)] += distance

        if len(data) < 10:
            return len([x for x in grid.values() if x < 32 ])
        else:
            return len([x for x in grid.values() if x < 10000 ])

    def load_handler_part1(self, data: [str]) -> [str]:
        points = []
        for d in data:
            values = d.split(', ')
            points +=[(int(values[0]), int(values[1]))]
        return points

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201900()
    failed, results = aoc.run("part1x_[0-9]+.txt", "part2_[2-2]+.txt")
    if failed:
        sys.exit(1)
