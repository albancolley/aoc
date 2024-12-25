"""
AOC Day 06
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure

class Aoc202406(AocBase):
    """
    AOC Day 6 Class
    """
    moves = {
        'D': 0 + 1j,
        'U': 0 - 1j,
        'L': -1 + 0j,
        'R': 1 + 0j
    }

    directions = {
        'D': 'L',
        'U': 'R',
        'L': 'U',
        'R': 'D'
    }

    def calc_1(self, data: tuple) -> int:
        grid, start_pos, width, height = data
        direction = 'U'
        visited = []
        pos = start_pos
        # print(grid[int(pos.imag)][int(pos.real)])
        while True:
            if pos not in visited:
                visited.append(pos)
            next_pos = pos + self.moves[direction]
            value:str = grid[next_pos]
            if value == ' ':
                return len(visited)
            elif value == '.':
                pos = next_pos
            elif value == '#':
                direction = self.directions[direction]

    def traverse(self, grid: dict[complex,str], start: complex, start_direction: str) -> bool:
        # 1511, 1947, 1803
        direction = start_direction
        pos = start
        seen = {pos:[start_direction]}
        while True:
            # print(pos)
            next_pos = pos + self.moves[direction]
            value: str = grid[next_pos]
            if value == ' ':
                return False
            elif value == '.':
                pos = next_pos
                # print(pos, direction)
                if pos in seen and direction in seen[pos]:
                    return True
                if pos not in seen:
                    seen[pos] = []
                seen[pos] += [direction]
                # print(seen)
            elif value == '#':
                direction = self.directions[direction]

    #Simpler version
    # def calc_2_working(self, data: [str]) -> int:
    #     grid, start_pos, width, height = data
    #     count = 0
    #     for y in range(height):
    #         for x in range(width):
    #             pos = complex(x, y)
    #             if pos == start_pos:
    #                 continue
    #             # print(pos)
    #             if grid[pos] == ".":
    #                 grid[pos] = "#"
    #                 # self.print_grid(grid, height, width)
    #                 if self.traverse(grid, start_pos, 'U'):
    #                     count += 1
    #                 grid[pos] = "."
    #
    #     return count

    def calc_2(self, data: [str]) -> int:
        grid, start_pos, width, height = data
        direction = 'U'
        pos = start_pos
        counts=set()
        path=[]
        while True:
            next_pos = pos + self.moves[direction]
            value:str = grid[next_pos]

            if value == ' ':
                return len(counts)
            elif value == '.':
                if grid[next_pos] == "." and next_pos not in counts and start_pos != next_pos:
                    grid[next_pos] = "#"
                    # self.print_grid(grid, height, width)
                    if next_pos not in path:
                        if self.traverse(grid, pos, direction):
                            counts.add(next_pos)
                    grid[next_pos] = "."
                path += [pos]
                pos = next_pos
            elif value == '#':
                direction = self.directions[direction]


    def load_handler_part1(self, data: [str]) -> [str]:
        width = len(data[0])
        height = len(data)
        grid = {}
        for x in range(-1, width + 1):
            grid[complex(x, -1)] = ' '
            grid[complex(x, height)] = ' '

        y = 0
        row: str
        start = complex(-100, -100)
        for _ in data:
            grid[complex(-1, y)] = ' '
            grid[complex(width, y)] = ' '
            for x in range(width):
                grid[complex(x, y)] = data[y][x]
                if data[y][x] == "^":
                    grid[complex(x, y)] = "."
                    start = complex(x, y)
            y = y + 1

        # self.print_grid(grid, height, width)
        return grid, start, width, height

    def load_handler_part2(self, data: [str]) -> [str]:
        width = len(data[0])
        height = len(data)
        grid = {}
        for x in range(-1, width+1):
            grid[complex(x, -1)] = ' '
            grid[complex(x, height)] = ' '

        y = 0
        row: str
        start = complex(-100, -100)
        for _ in data:
            grid[complex(-1, y)] = ' '
            grid[complex(width, y)] = ' '
            for x in range(width):
                grid[complex(x, y)] = data[y][x]
                if  data[y][x] == "^":
                    grid[complex(x, y)] = "."
                    start = complex(x, y)
            y = y + 1


        # self.print_grid(grid, height, width)
        return grid, start, width, height

    def print_grid(self, grid, height, width):
        for y in range(-1, height + 1):
            line = ""
            for x in range(-1, width + 1):
                line += grid[complex(x, y)]
            print(line)


if __name__ == '__main__':
    configure()
    aoc = Aoc202406()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
