"""
AOC Day 10
"""
import sys
from common import AocBase
from common import configure
import math
from collections import deque

class Aoc2023010(AocBase):
    """
    AOC Day 10 Class
    """

    moves = {
        'S' : [(-1, 0), (0, -1), (0, 1), (1, 0)],
        '|' : [(-1, 0), (1,0)],
        '-': [(0, -1), (0, 1)],
        'L': [(-1, 0), (0, 1)],
        'J': [(-1,  0), (0, -1)],
        '7': [(1, 0), (0, -1)],
        'F': [(1, 0), (0, 1)],
        '.': []
    }

    def find_next_after_start(self, start, grid):
        next_tiles = []
        for pos in self.moves['S']:
            new_pos = start[0] + pos[0], start[1] + pos[1]
            if new_pos in grid:
                direction = grid[new_pos]
                direction_moves = [(new_pos[0] + x[0], new_pos[1] + x[1]) for x in self.moves[direction]]
                if start in direction_moves:
                    next_tiles += [new_pos]
        return next_tiles

    def calc_1(self, data: dict) -> int:
        start, grid, num_rows, num_cols = data
        next_tiles = self.find_next_after_start(start, grid)

        position = next_tiles[0]
        been = [position]
        steps = 1
        while True:
            direction = grid[position]
            direction_moves = [(position[0] + x[0], position[1] + x[1]) for x in self.moves[direction]]
            for direction_move in direction_moves:
                if steps == 1 and direction_move == start:
                    continue
                if direction_move not in been:
                    position = direction_move
                    been += [direction_move]
                    # print(been, position, grid[position] )
                    break
            if grid[position] == 'S':
                break
            steps +=1
        return math.ceil(steps / 2)


    def calc_2(self, data: [str]) -> int:
        start, grid, num_rows, num_cols = data
        next_tiles = self.find_next_after_start(start, grid)

        path, steps = self.get_path(grid, next_tiles, start)

        new_grid = {}

        queue = deque([(-1, -1)])
        new_grid[(-1, -1)] = "O"
        seen = [(-1, -1)]
        new_start = start
        while len(queue) > 0:
            next_pos = queue.pop()
            for pos in self.moves['S']:
                new_pos = (next_pos[0] + pos[0], next_pos[1] + pos[1])
                if new_pos in seen:
                    continue
                seen += [new_pos]
                if -1 <= new_pos[0] <= num_rows + 1 and -1 <= new_pos[1] <= num_cols + 1:
                    if new_pos not in path:
                        new_grid[new_pos] = "O"
                        queue.append(new_pos)
                    elif grid[new_pos] == "|":
                        new_start_pos = new_pos
                        outside_pos = next_pos

        new_position = path.index(new_start_pos)
        diff = (new_start_pos[0] - outside_pos[0], new_start_pos[1] - outside_pos[1])
        # print(diff)

        self.populate_outsides(diff, grid, new_grid, num_cols, num_rows, path[new_position:])
        # print(diff)
        self.populate_outsides(diff, grid, new_grid, num_cols, num_rows, reversed(path[0:new_position]))

        #     tile = grid(first)
        #     direction = (second[0] - first[0], second[1] - first[1])


        for r in range(0, num_rows):
            for c in range(0, num_cols):
                pos = (r, c)
                if pos in new_grid and new_grid[pos] == "I":
                    nc = c - 1
                    while (r,nc) not in new_grid:
                        new_grid[(r, nc)] = "I"
                        nc -= 1
                    if (r,c +1) not in new_grid:
                        new_grid[(r,c +1)] = "I"

        # self.draw(new_grid, num_cols, num_rows)

        count = 0
        for x in new_grid:
            if new_grid[x] == "I":
                count+=1

        return count

    def populate_outsides(self, diff, grid, new_grid, num_cols, num_rows, r):
        new_diff = diff
        for steps in r:
            tile = grid[steps]
            new_grid[steps] = tile
            inside =  (steps[0] + new_diff[0], steps[1] + new_diff[1])
            if inside not in new_grid:
                new_grid[inside] = "I"
            if tile in ['J','L','7','F']:
                if tile == "J":
                    new_diff = (new_diff[1], new_diff[0])
                if tile == "L":
                    new_diff = (-new_diff[1], -new_diff[0])
                if tile == "7":
                    new_diff = (-new_diff[1], -new_diff[0])
                if tile == "F":
                    new_diff = (new_diff[1], new_diff[0])
                inside =  (steps[0] + new_diff[0], steps[1] + new_diff[1])
                if inside not in new_grid:
                    new_grid[inside] = "I"

            # self.draw(new_grid, num_cols, num_rows)

    def draw(self, new_grid, num_cols, num_rows):
        for x in range(0, num_rows):
            line = ''
            for y in range(0, num_cols):
                pos = (x, y)
                if pos in new_grid:
                    line += new_grid[pos]
                else:
                    line += '.'
            print(line)

    def get_path(self, grid, next_tiles, start):
        position = next_tiles[0]
        been = [position]
        steps = 1
        while True:
            direction = grid[position]
            direction_moves = [(position[0] + x[0], position[1] + x[1]) for x in self.moves[direction]]
            for direction_move in direction_moves:
                if steps == 1 and direction_move == start:
                    continue
                if direction_move not in been:
                    position = direction_move
                    been += [direction_move]
                    break
            if grid[position] == 'S':
                break
            steps += 1
        return been, steps

    def load_handler_part1(self, data: [str]) -> [str]:
        grid = {}
        row_pos = 0
        for row in data:
            column_pos = 0
            for column in row:
                grid[(row_pos, column_pos)] = column
                if column == 'S':
                    start = (row_pos, column_pos)
                column_pos += 1
            row_pos += 1
        return start, grid, row_pos, column_pos

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)

# 470 too high

if __name__ == '__main__':
    configure()
    aoc = Aoc2023010()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-5]+.txt")
    if failed:
        sys.exit(1)
