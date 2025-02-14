"""
AOC Day 23
"""
import sys
from dataclasses import dataclass, field
from common import AocBase
from common import configure
from collections import defaultdict


@dataclass
class Grid:
    width: int = 0
    height: int = 0
    grid: dict[(int, int), str] = field(default_factory=dict)
    start: (int, int) = (0, 0)
    end: (int, int) = (0, 0)


class Aoc202323(AocBase):
    """
    AOC Day 23 Class
    """

    starts = []
    moves = {
        '.': [(0, 1), (0, -1), (1, 0), (-1, 0)],
        '>': [(1, 0)],
        '<': [(-1, 0)],
        '^': [(0, -1)],
        'v': [(0, 1)],
    }
    walls = ['#']
    spaces = ['.']

    def view(self, grid, seen=[], padding=0):
        print()
        for y in range(grid.width):
            line = ""
            for x in range(grid.height):
                if (x, y) in seen:
                    line += f'{str(seen[(x, y)]):<{padding}}'
                else:
                    line += f'{grid.grid[(x, y)]:<{padding}}'
            print(line)
        print()

    def dfs1(self, grid):
        seen = defaultdict(int)
        q: list = [(0, grid.start, [])]
        while len(q) > 0:
            step, position, path = q.pop(0)
            tile = grid.grid[position]
            next_step = -step + 1
            for move in self.moves[tile]:
                next_position = (position[0] + move[0], position[1] + move[1])
                if grid.grid[next_position[0], next_position[1]] in self.walls:
                    continue
                if next_position in path:
                    continue

                if seen[next_position] < next_step:
                    seen[next_position] = next_step
                    q.insert(0, (-next_step, next_position, path + [next_position]))

        return seen

    def dfs(self, grid: Grid, start: (int, int)) -> [((int, int), (int, int), int)]:
        q: list = [(0, start, [start], True)]
        new_paths = []
        while len(q) > 0:
            step, position, path, skip_first = q.pop(0)

            tile = grid.grid[position]
            next_step = -step + 1
            possibles_moves = []

            if tile in ['<', '>', '^', 'v']:
                if skip_first:
                    skip_first = False
                else:
                    move = self.moves[tile][0]
                    next_position = (position[0] + move[0], position[1] + move[1])
                    path.append(next_position)
                    new_paths.append((start, next_position, len(path) - 1))
                    continue

            for move in self.moves[tile]:
                next_position = (position[0] + move[0], position[1] + move[1])
                if grid.grid[next_position] in self.walls:
                    continue

                if next_position in path:
                    continue

                q.insert(0, (-next_step, next_position, path + [next_position], skip_first))
                # possibles_moves.append(next_position)

            # for next_position in possibles_moves:
            #     q.insert(0, (-next_step, next_position, path + [next_position], skip_first))

        return new_paths

    def calc_1(self, grid: Grid) -> int:
        # self.view(grid, width, height)
        result = self.dfs1(grid)

        return result[grid.end]

    def calc_2(self, grid: Grid) -> int:

        # added to simplify the dfs code to look for the second slope.
        grid.grid[grid.start] = 'v'
        grid.grid[grid.end[0], grid.end[1] - 1] = 'v'

        new_paths: list = self.dfs(grid, grid.start)

        print(new_paths)

        # simplify graph to get distances to next slope
        # simple_path with contain the start and end points between the "top" or "bottom" of a slope
        # i.e. the stars (*) part of example graph below.
        # #.#####################
        # #.......#########...###
        # #######.#########.#.###
        # ###.....#.>*>.###.#.###
        # ###v#####.#v#.###.#.###
        # ###*>...#.#.#.....#...#
        # ###v###.#.#.#########.#
        simple_paths = {}
        while len(new_paths) > 0:
            path = new_paths.pop(0)
            if path[0] not in simple_paths:
                simple_paths[path[0]] = {}
            simple_paths[path[0]][path[1]] = path[2]
            if path[1] not in simple_paths:
                simple_paths[path[1]] = {}
            simple_paths[path[1]][path[0]] = path[2]

            paths = self.dfs(grid, path[1])
            new_paths += paths

        # now search the simple paths for the longest path - have to do them all
        longest_path = 0
        paths = [(0, grid.start, [grid.start])]
        while len(paths) > 0:
            length, start, path = paths.pop(0)
            for next_position in simple_paths[start]:
                new_length = length + simple_paths[start][next_position]
                if next_position == grid.end:
                    if longest_path < new_length:
                        longest_path = new_length
                        # print(new_length, path + [next_position])
                elif next_position not in path:
                    paths.insert(0, (new_length, next_position, path + [next_position]))

        return longest_path

    def load_handler_part1(self, data: [str]) -> Grid:
        grid = Grid(len(data[0]), len(data))
        for x in range(-1, grid.width + 1):
            grid.grid[(x, -1)] = self.walls[0]
        for y in range(0, grid.height):
            grid.grid[(-1, y)] = self.walls[0]
            line = data[y]
            for x in range(0, grid.width):
                if line[x] in self.starts:
                    start = (x, y)
                    grid.grid[(x, y)] = self.spaces[0]
                else:
                    grid.grid[(x, y)] = line[x]
            grid.grid[(grid.width, y)] = self.walls[0]
        for x in range(-1, grid.width + 1):
            grid.grid[(x, grid.height)] = self.walls[0]

        for x in range(grid.width):
            if grid.grid[(x, 0)] in self.spaces:
                grid.start = (x, 0)
            if grid.grid[(x, grid.height - 1)] in self.spaces:
                grid.end = (x, grid.height - 1)

        # self.view(grid)
        return grid

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc202323()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
