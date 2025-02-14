"""
AOC Day X
"""
import heapq
import sys
from common import AocBase
from common import configure


class Aoc202418(AocBase):
    """
    AOC Day 10 Class
    """

    moves = {
        'N': 0 + 1j,
        'S': 0 - 1j,
        'W': -1 + 0j,
        'E': 1 + 0j
    }

    def calc_1(self, data: dict) -> int:
        grid, start, end, width, height = data

        # self.print_grid( grid, height, width, start, end)

        return self.get_length(end, grid, start)

    def get_length(self, end, grid, start, step=10000):
        seen = {start: True}
        paths = {}
        queue = []
        heapq.heappush(queue, (0, start.real, start.imag))
        heapq.heappush(queue, (0, start.real, start.imag))
        while len(queue) > 0:
            cost, x, y = heapq.heappop(queue)
            pos = complex(x, y)
            for move in self.moves:
                next_pos = pos + self.moves[move]
                if next_pos in seen:
                    continue

                seen[next_pos] = True

                if next_pos == end:
                    return cost + 1

                if grid[next_pos] == "#":
                    continue

                if isinstance(grid[next_pos], int) and grid[next_pos] <= step:
                    continue


                heapq.heappush(queue, (cost + 1, next_pos.real, next_pos.imag))

        return 0

    def binary_search(self, grid, start, end, low, high):
        if low < high:
            mid = (low + high) // 2
            length = self.get_length(end, grid, start, mid)
            if length == 0:
                if self.get_length(end, grid, start, mid-1) > 0:
                    return mid
                else:
                    return self.binary_search(grid, start, end, low, mid-1)
            else:
                return self.binary_search(grid, start, end, mid + 1, high)
        else:
            return -1


    def calc_2(self, data: [str]) -> str:
        grid, start, end, width, height, steps = data
        pos = self.binary_search(grid, start, end, 1, steps)
        pos = list(grid.keys())[list(grid.values()).index(pos)]
        return f'{int(pos.real)},{int(pos.imag)}'


    def print_grid(self, grid, height, width, start, end):
        for y in range(-1, height+2):
            line = ""
            for x in range(-1, width+2):
                pos = complex(x, y)
                if pos == start:
                    line += 'S'
                elif pos == end:
                    line += 'E'
                else:
                    line += str(grid[pos])
            print(line)


    def load_handler_part1(self, data: [str]) -> [str]:
        first_line = data[0].split(",")
        steps = int(first_line[0])
        width = int(first_line[1])
        height  = int(first_line[2])
        grid = {}
        start = complex(0, 0)
        end = complex(width, height)
        for x in range(-1, width+2):
            for y in range(-1, width + 2):
                value = "."
                if x == -1 or y == -1 or x == width+1 or y == height+1:
                    value = "#"
                grid[complex(x, y)] = value

        for line in data[1:steps+1]:
            cord = line.split(",")
            x = int(cord[0])
            y = int(cord[1])
            grid[complex(x, y)] = "#"
        return grid,  start, end, width, height

    def load_handler_part2(self, data: [str]) -> [str]:
        first_line = data[0].split(",")
        steps = int(first_line[0])
        width = int(first_line[1])
        height = int(first_line[2])
        grid = {}
        start = complex(0, 0)
        end = complex(width, height)
        for x in range(-1, width + 2):
            for y in range(-1, width + 2):
                value = "."
                if x == -1 or y == -1 or x == width + 1 or y == height + 1:
                    value = "#"
                grid[complex(x, y)] = value

        step = 1
        for line in data[1:]:
            cord = line.split(",")
            x = int(cord[0])
            y = int(cord[1])
            grid[complex(x, y)] = step
            step += 1
        return grid, start, end, width, height, step


if __name__ == '__main__':
    configure()
    aoc = Aoc202418()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
