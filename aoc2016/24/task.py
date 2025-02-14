"""
AOC Day 2016- 25
"""
import itertools
import sys
from common import AocBase
from common import configure
from dataclasses import dataclass
from operator import itemgetter

@dataclass
class Grid:
    width: int
    height: int
    grid: dict[(int, int), str]
    starts: dict[int, (int, int)]


class Aoc201625(AocBase):
    """
    AOC Day 25 Class
    """

    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    walls = ['#']
    spaces = ['.']
    starts = ['0', '1', '2', '3', '4', '5', '6', '7']

    def view(self, grid):
        print()
        for y in range(grid.height):
            line = ""
            for x in range(grid.width):
                line += f'{grid.grid[(x, y)]}'
            print(line)
        print()
        print(grid.starts)
        print()

    def bfs(self, grid: Grid, start, end) -> int:
        seen: dict[(int, int), int] = {start: 0}
        q = [(start, 0)]
        while len(q) > 0:
            position, step = q.pop(0)
            for move in self.moves:
                next_position = (position[0] + move[0], position[1] + move[1])
                position_value = grid.grid[next_position[0], next_position[1]]
                if position_value in self.walls:
                    continue
                if next_position == end:
                    return step + 1
                if next_position not in seen:
                    seen[next_position] = step + 1
                    q.append((next_position, step + 1))
        return -1

    def calc_1(self, grid: Grid) -> int:
        # self.view(grid)
        distances: dict = {}
        for i in itertools.combinations(range(len(grid.starts)),2):
            distance = self.bfs(grid, grid.starts[i[0]], grid.starts[i[1]])
            distances[i] = distance
            distances[(i[1], i[0])] = distance

        totals = []
        for i in itertools.permutations(range(len(grid.starts))):
            total = 0
            if i[0] == 0:
                last = i[0]
                for j in i[1:]:
                    total += distances[(last, j)]
                    last = j
                totals += [total]

        return min(totals)

    def calc_2(self, grid: Grid) -> int:
        # self.view(grid)
        distances: dict = {}
        for i in itertools.combinations(range(len(grid.starts)),2):
            distance = self.bfs(grid, grid.starts[i[0]], grid.starts[i[1]])
            distances[i] = distance
            distances[(i[1], i[0])] = distance

        totals = []
        for i in itertools.permutations(range(len(grid.starts))):
            total = 0
            if i[0] == 0:
                last = i[0]
                for j in i[1:]:
                    total += distances[(last, j)]
                    last = j
                total += distances[(last, 0)]
                totals += [total]

        return min(totals)


    def load_handler_part1(self, data: [str]) -> Grid:
        grid: dict = {}
        width: int  = len(data[0])
        height: int = len(data)
        starts: dict = {}
        for y in range(0, height):
            line: str = data[y]
            for x in range(0, width):
                pos: str = line[x]
                grid[(x, y)] = pos
                if pos.isnumeric():
                    starts[int(line[x])] = (x, y)
        starts = dict(sorted(starts.items(), key=itemgetter(0)))
        return Grid(width, height, grid, starts)

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201625()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
