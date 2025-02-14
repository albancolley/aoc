"""
AOC Day X
"""
import sys
from collections import defaultdict

from common import AocBase
from common import configure


class Aoc202400(AocBase):
    """
    AOC Day 10 Class
    """

    moves = [
        0 + 1j,
        0 - 1j,
        -1 + 0j,
         1 + 0j
    ]

    def calc_1(self, data: dict) -> int:
        grid, start, end, width, height, picoseconds = data

        # self.print_grid( grid, height, width, start, end)

        seen = {start:True}
        path = [start]
        path_dict = {start:0}
        queue = [start]
        step = 1
        while len(queue) > 0:
            pos = queue.pop()
            for move in self.moves:
                next_pos = pos + move
                value = grid[next_pos]
                if value != ".":
                    continue

                if next_pos in seen:
                    continue

                path += [next_pos]
                path_dict[next_pos] = step
                step +=1

                seen[next_pos] = True
                if next_pos == end:
                    break

                queue.append(next_pos)

        # self.print_grid(grid, height, width, start, end)



        cheat_lengths = defaultdict(int)
        for p in path:
            for move in self.moves:
                if grid[p+move] == '#' and grid[p+move+move] == '.':
                    if path_dict[p] < path_dict[p+move+move]:
                        cheat_lengths[path_dict[p+move+move]-path_dict[p]-2 ] += 1

        # print(cheat_lengths)
        total = 0
        for c in cheat_lengths:
            if c >= picoseconds:
                total += cheat_lengths[c]
        return total

    def print_grid(self, grid, height, width, start, end):
        for y in range(-1, height+1):
            line = ""
            for x in range(-1, width+1):
                pos = complex(x, y)
                if pos == start:
                    line += 'S'
                elif pos == end:
                    line += 'E'
                else:
                    line += str(grid[pos])
            print(line)

    def manhattan_distance(self, p1: complex, p2: complex) -> int:
        return int(abs(p1.real - p2.real) + abs(p1.imag - p2.imag))

    def calc_2(self, data: [str]) -> int:
        grid, start, end, width, height, picoseconds = data

        # self.print_grid( grid, height, width, start, end)

        seen = {start: True}
        path = [start]
        path_dict = {start: 0}
        queue = [start]
        step = 1
        while len(queue) > 0:
            pos = queue.pop()
            for move in self.moves:
                next_pos = pos + move
                value = grid[next_pos]
                if value != ".":
                    continue

                if next_pos in seen:
                    continue

                path += [next_pos]
                path_dict[next_pos] = step
                step += 1

                seen[next_pos] = True
                if next_pos == end:
                    break

                queue.append(next_pos)

        # self.print_grid(grid, height, width, start, end)

        cheat_lengths = defaultdict(int)
        cheat_seen = {}
        for p in path:
            for x in range(-20, 21):
                for y in range(-20, 21):
                    if x == 0 and y == 0:
                        continue
                    move = complex(x, y)
                    p_move = p + move
                    distance = self.manhattan_distance(p, p_move)
                    if 2 <= distance <= 20:
                        if p_move in grid and grid[p_move] == '.':
                            if path_dict[p] + distance < path_dict[p_move]:
                                if p in cheat_seen:
                                    if p_move in cheat_seen[p]:
                                        continue
                                else:
                                    cheat_seen[p] = []

                                cheat_seen[p] += [p_move]

                                length = path_dict[p_move] - path_dict[p] - distance
                                # print(len(path), path_dict[p_move], path_dict[p], distance, length,len(path) - length)
                                cheat_lengths[length] += 1


        # print(cheat_lengths)
        total = 0
        for c in cheat_lengths:
            if c >= picoseconds:
                total += cheat_lengths[c]

        return total

    def load_handler_part1(self, data: [str]) -> [str]:
        picoseconds = int(data[0])
        grid, start, end, width, height = self.load_data(data[1:])
        return grid, start, end, width, height, picoseconds

    def load_data(self, data):
        width = len(data[0])
        height = len(data)
        grid = {}
        start = complex(0, 0)
        end = complex(0, 0)
        y = 0
        for x in range(-1, width + 1):
            grid[complex(x, -1)] = '#'
            grid[complex(x, height)] = '#'
        for _ in data:
            for x in range(width):
                value = data[y][x]
                if value == "S":
                    value = "."
                    start = complex(x, y)
                if value == "E":
                    value = "."
                    end = complex(x, y)
                grid[complex(x, y)] = value
            grid[complex(-1, y)] = '#'
            grid[complex(width, y)] = '#'
            y += 1
        return grid, start, end, width, height

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc202400()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
