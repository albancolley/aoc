"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure


class Aoc202410(AocBase):
    """
    AOC Day 10 Class
    """

    moves = {
        'D': 0 + 1j,
        'U': 0 - 1j,
        'L': -1 + 0j,
        'R': 1 + 0j
    }


    def calc_1(self, data: dict) -> int:
        result = 0
        grid, starts, width, height = data
        # self.print_grid(grid, width, height)
        for start in starts:
            queue = [(start, 0, [start])]
            trail_heads = set()
            while len(queue) > 0:
                # print(queue)
                pos, height, path = queue.pop(0)
                for move in self.moves:
                    next_pos = pos + self.moves[move]
                    next_height = grid[next_pos]
                    if next_height == height + 1:
                        if next_height == 9:
                            trail_heads.add(next_pos)
                        else:
                            queue += [(next_pos, next_height, path + [next_pos])]
            result += len(trail_heads)

        return result

    def calc_2(self, data: [str]) -> int:
        result = 0
        grid, starts, width, height = data
        # self.print_grid(grid, width, height)
        for start in starts:
            queue = [(start, 0, [start])]
            trail_heads = set()
            while len(queue) > 0:
                # print(queue)
                pos, height, path = queue.pop(0)
                for move in self.moves:
                    next_pos = pos + self.moves[move]
                    next_height = grid[next_pos]
                    if next_height == height + 1:
                        if next_height == 9:
                            result += 1
                        else:
                            queue += [(next_pos, next_height, path + [next_pos])]

        return result

    def print_grid(self, grid, height, width):
        for y in range(-1, height + 1):
            line = ""
            for x in range(-1, width + 1):
                if grid[complex(x, y)] >= 0:
                    line += str(grid[complex(x, y)])
                else:
                    line += "-"
            print(line)

    def load_handler_part1(self, data: [str]) -> [str]:
        width = len(data[0])
        height = len(data)
        grid = {}
        for x in range(-1, width + 1):
            grid[complex(x, -1)] = -1
            grid[complex(x, height)] = -1

        y = 0
        row: str
        starts  = []
        for _ in data:
            grid[complex(-1, y)] = -1
            grid[complex(width, y)] = -1
            for x in range(width):
                grid[complex(x, y)] = int(data[y][x])
                if data[y][x] == "0":
                    starts += [complex(x, y)]
            y = y + 1

        # self.print_grid(grid, height, width)
        return grid, starts, width, height

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc202410()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
