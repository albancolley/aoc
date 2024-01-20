"""
AOC Day 23
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
from queue import PriorityQueue
from collections import defaultdict

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

    def view(self, grid, width, height, seen=[], padding=0):
        print()
        for y in range(width):
            line = ""
            for x in range(height):
                if (x,y) in seen:
                    line += f'{str(seen[(x,y)]):<{padding}}'
                else:
                    line += f'{grid[(x,y)]:<{padding}}'
            print(line)
        print()


    def dfs1(self, grid, start, end):
        seen = defaultdict(int)
        q = PriorityQueue()
        q.put((0, start, []))
        while not q.empty():
            step, position, path = q.get()
            tile = grid[(position)]
            next_step = -step + 1
            for move in self.moves[tile]:
                next_position = (position[0] + move[0], position[1] + move[1])
                if grid[next_position[0], next_position[1]] in self.walls:
                    continue
                if next_position in path:
                    continue

                if seen[next_position] < next_step:
                    seen[next_position] = next_step
                    q.put((-next_step, next_position, path + [next_position]))

        return seen

    def dfs(self, grid, start, end) -> []:
        q = PriorityQueue()
        q.put((0, start, [start], True))
        new_paths = []
        while not q.empty():
            step, position, path, skip_first = q.get()

            # if position == end:
            #     new_paths.append((start, end, len(path)))
            #     if position not in new_paths:
            #         new_paths[position] = (len(path), path)
            #     else:
            #         new_paths[position] = ( max(new_paths[position][0], len( path)), path)
            #     continue

            tile = grid[(position)]
            next_step = -step + 1
            possibles_moves = []

            if tile in ['<', '>', '^', 'v']:
                if skip_first:
                    skip_first = False
                else:
                    move = self.moves[tile][0]
                    next_position = (position[0] + move[0], position[1] + move[1])
                    path.append(next_position)
                    new_paths.append((start, next_position, len(path)-1))
                    continue

            for move in self.moves[tile]:
                next_position = (position[0] + move[0], position[1] + move[1])
                if grid[next_position] in self.walls:
                    continue

                if next_position in path:
                    continue

                possibles_moves.append(next_position)

            for next_position in possibles_moves:
                q.put((-next_step, next_position, path + [next_position], skip_first))

        return new_paths

    def calc_1(self, data: dict) -> int:
        grid, width, height, start, end = data
        # self.view(grid, width, height)
        result = self.dfs1(grid, start, end)

        return result[end]

    def calc_2(self, data: [str]) -> int:
        grid, width, height, start, end = data

        # added to simplify the dfs code to look for the second slope.
        grid[start] = 'v'
        grid[end[0], end[1]-1] = 'v'

        new_paths: list = self.dfs(grid, start, end)

        #simplify graph to get distances to next slope
        #simple_path with contain the start and end points between the "top" or "bottom" of a slope
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

            paths = self.dfs(grid, path[1], end)
            new_paths += paths

        # now search the simple paths for the longest path - have to do them all
        longest_path = 0
        paths = [(0, start, [start])]
        while len(paths) > 0:
            length, start, path = paths.pop(0)
            for next_position in simple_paths[start]:
                new_length = length + simple_paths[start][next_position]
                if next_position == end:
                    if longest_path < new_length:
                        longest_path = new_length
                        # print(new_length, path + [next_position])
                elif next_position not in path:
                    paths.insert(0, (new_length, next_position, path + [next_position]))

        return longest_path

    def load_handler_part1(self, data: [str]) -> [str]:
        grid = {}
        width = len(data[0])
        height = len(data)
        start = (0, 0)
        end= (0,0)
        for x in range(-1, width + 1):
            grid[(x, -1)] = self.walls[0]
        for y in range(0, height):
            grid[(-1, y)] = self.walls[0]
            line = data[y]
            for x in range(0, width):
                if line[x] in self.starts:
                    start = (x, y)
                    grid[(x, y)] = self.spaces[0]
                else:
                    grid[(x, y)] = line[x]
            grid[(width, y)] = self.walls[0]
        for x in range(-1, width + 1):
            grid[(x, height)] = self.walls[0]

        for x in range(width):
            if grid[(x, 0)] in self.spaces:
                start = (x, 0)
            if grid[(x, height-1)] in self.spaces:
                end = (x, height-1)

        # self.display(grid, width, height)
        return grid, width, height, start, end

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc202323()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
