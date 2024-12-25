"""
AOC Day X
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math

class Aoc202400(AocBase):
    """
    AOC Day 10 Class
    """
    moves = {
        'v': 0 + 1j,
        '^': 0 - 1j,
        '<': -1 + 0j,
        '>': 1 + 0j
    }

    reverse = {
        '^': 'v',
        'v': '^',
        '<': '>',
        '>': '<'
    }

    def calc_1(self, data: dict) -> int:
        grid, directions, start, width, height = data
        # print(grid, directions, start)

        pos = start
        for direction in directions:
            next_pos = pos + self.moves[direction]
            value = grid[next_pos]
            if value == "#":
                continue

            if value == ".":
                pos = next_pos
                continue

            blocked_pos = next_pos
            while grid[blocked_pos] == 'O':
                blocked_pos = blocked_pos + self.moves[direction]

            if grid[blocked_pos] == ".":
                while blocked_pos != pos:
                    previous_pos = blocked_pos - self.moves[direction]
                    grid[blocked_pos] = grid[previous_pos]
                    blocked_pos = previous_pos

                pos = next_pos

            # self.print_grid(grid, height, width,pos)


        result = 0
        for pos in grid:
            if grid[pos] == "O":
                result += 100*pos.imag +  pos.real

        return int(result)

    def print_grid(self, grid, height, width, start):
        for y in range(height):
            line = ""
            for x in range(width):
                pos = complex(x, y)
                if pos == start:
                    line += '@'
                else:
                    line += str(grid[pos])
            print(line)


    def calc_2(self, data: [str]) -> int:
        grid, directions, start, width, height = data

        pos = start
        for direction in directions:
            # self.print_grid(grid, height, width, pos)
            next_pos = pos + self.moves[direction]
            value = grid[next_pos]
            if value == "#":
                continue

            if value == ".":
                pos = next_pos
                continue

            blocked_pos = next_pos
            if direction in ['<','>']:
                while grid[blocked_pos] in ['[',']']:
                    blocked_pos = blocked_pos + self.moves[direction]

                if grid[blocked_pos] == ".":
                    while blocked_pos != pos:
                        previous_pos = blocked_pos - self.moves[direction]
                        grid[blocked_pos] = grid[previous_pos]
                        blocked_pos = previous_pos

                    pos = next_pos
                continue

            blocked_positions = [{blocked_pos, blocked_pos + 1}]
            if value == "]":
                blocked_positions = [{blocked_pos, blocked_pos - 1}]

            depth = 0
            blocked = False
            while not blocked:
                new_blocks: set = set()
                for blocked_position in blocked_positions[depth]:
                    blocked_pos = blocked_position + self.moves[direction]
                    value = grid[blocked_pos]
                    if value == "#":
                        blocked = True
                        break
                    if value == "[":
                        new_blocks.add(blocked_pos)
                        new_blocks.add(blocked_pos + 1)
                    elif value == "]":
                        new_blocks.add(blocked_pos)
                        new_blocks.add(blocked_pos -1)
                if not blocked and len(new_blocks) == 0:
                    for d in range(depth, -1, -1):
                        for b in blocked_positions[d]:
                            if direction == "v":
                                grid[b+ (0+1j)] = grid[b]
                            else:
                                grid[b + (0 - 1j)] = grid[b]
                            grid[b] = "."
                    pos = next_pos
                    break
                blocked_positions.append(new_blocks)
                depth += 1

        # self.print_grid(grid, height, width, pos)

        result = 0
        for pos in grid:
            if grid[pos] == "[":
                result += 100 * pos.imag + pos.real

        return int(result)

    def load_handler_part1(self, data: [str]) -> [str]:
        width = len(data[0])
        grid = {}
        y = 0
        start = complex(0, 0)
        while True:
            if len(data[y]) == 0:
                break
            row: str
            for x in range(width):
                value = data[y][x]
                if value == "@":
                    value = "."
                    start = complex(x, y)
                grid[complex(x, y)] = value
            y += 1

        height = y - 1
        y += 1
        directions = ""
        while y < len(data):
            directions += data[y]
            y+=1


        return grid, directions, start, width, height

    def load_handler_part2(self, data: [str]) -> [str]:
        width = len(data[0])
        grid = {}
        y = 0
        start = complex(0, 0)
        while True:
            if len(data[y]) == 0:
                break
            row: str
            for x in range(width):
                value = data[y][x]
                if value == "@":
                    value = "."
                    start = complex(2*x, y)
                value_2 = value
                if value == "O":
                    value = "["
                    value_2 = "]"
                grid[complex(x*2, y)] = value
                grid[complex(x * 2 + 1, y)] = value_2
            y += 1

        height = y
        y += 1
        directions = ""
        while y < len(data):
            directions += data[y]
            y += 1

        return grid, directions, start, width*2, height


if __name__ == '__main__':
    configure()
    aoc = Aoc202400()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
