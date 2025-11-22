"""
AOC Day X
"""
import sys
from dataclasses import dataclass

from sympy.strategies.core import switch

from common import AocBase
from common import configure

@dataclass
class Region:
    type: int
    erosion_level: int
    geologic_index: int

class Aoc201822(AocBase):
    """
    AOC Day 10 Class
    """
    MOVES: list[complex] = [
        -1 + 0j,
        0 - 1j,
        0 + 1j,
        1 + 0j,
    ]

    VALID_TYPE: dict[int, list[str]] = {
        0: ["C", "T"],
        1: ["C", "N"],
        2: ["T","N"]
    }

    cave: dict[complex, Region] = dict()
    depth: int = 0
    target: complex = complex(0,0)

    def get(self, pos) -> Region:
        if pos in self.cave:
            return self.cave[pos]

        geologic_index = 0
        if pos == complex(0,0) or pos == self.target:
            geologic_index = 0
        elif pos.real == 0:
            geologic_index = int(pos.imag) * 48271
        elif pos.imag == 0:
            geologic_index = int(pos.real) * 16807
        else:
            left = self.get(pos -1)
            up = self.get(pos -1j)
            geologic_index = left.erosion_level * up.erosion_level

        erosion_level = (geologic_index + self.depth) % 20183
        region_type = erosion_level % 3
        region = Region(region_type, erosion_level, geologic_index)
        self.cave[pos] = region
        return region

    def calc_1(self, data: tuple[int, complex]) -> int:

        self.cave = dict()
        self.depth = data[0]
        self.target = data[1]

        for x in range(0, int(self.target.real) + 1):
            for y in range(0, int(self.target.imag) + 1):
                self.get(complex(x,y))

        return sum([r.type for r in self.cave.values()])

    def manhattan_distance(self, p1: complex, p2: complex) -> int:
        return int(abs(p1.real - p2.real) + abs(p1.imag - p2.imag))


    def check_cost(self, cave_cost, cost, pos, equipped)-> bool:
        if pos in cave_cost:
            if equipped in cave_cost[pos]:
                if cost >= cave_cost[pos][equipped]:
                    return True
        return False

    def calc_2(self, data: tuple[int, complex]) -> int:
        self.cave = dict()
        self.depth = data[0]
        self.target = data[1]

        start = complex(0,0)
        queue = [(0, self.manhattan_distance(start, self.target), start, "T")]

        cave_cost: dict[complex, dict[str,int]] = dict()

        while len(queue) > 0:
            cost, md, pos, equipped = queue.pop(0)

            if self.check_cost(cave_cost, cost, pos, equipped):
                continue

            if pos == self.target and equipped == "T":
                return cost

            if pos not in cave_cost:
                cave_cost[pos] = dict()
            cave_cost[pos][equipped] = cost

            cave_type = self.get(pos).type
            for new_equipped in self.VALID_TYPE[cave_type]:
                if equipped != new_equipped:
                    new_cost = cost + 7
                    if not self.check_cost(cave_cost, new_cost, pos, new_equipped):
                        queue.append((new_cost, md, pos, new_equipped))

            for move in self.MOVES:
                next_pos = pos + move
                if next_pos.real == -1 or next_pos.imag == -1:
                    continue

                new_cave_type = self.get(next_pos).type
                if equipped in self.VALID_TYPE[new_cave_type]:
                    new_cost = cost + 1
                    if not self.check_cost(cave_cost, new_cost, next_pos, equipped):
                        queue.append((new_cost, self.manhattan_distance(next_pos, self.target), next_pos, equipped))

            queue.sort(key = lambda x: (x[0], x[1]))
            # print(len(queue), queue)

        total = 0
        return total

    def load_handler_part1(self, data: [str]) -> tuple[int, complex]:
        depth = int(data[0].split(" ")[1])
        cords_str = data[1].split(" ")[1]
        x = int(cords_str.split(",")[0])
        y = int(cords_str.split(",")[1])

        return depth, complex(x,y)


    def load_handler_part2(self, data: [str]) ->  tuple[int, complex]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201822()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
