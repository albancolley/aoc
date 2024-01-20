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

    def __init__(self):
        self.starts = []
        self.moves = {
            '.': [(0, 1), (0, -1), (1, 0), (-1, 0)],
            '>': [(1, 0)],
            '<': [(-1, 0)],
            '^': [(0, -1)],
            'v': [(0, 1)],
        }
        self.walls = ['#']
        self.spaces = ['.']

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

    def dfs(self, grid, start, end):
        seen = defaultdict(int)
        q = PriorityQueue()
        q.put((0, start, [start]))
        new_paths={}
        while not q.empty():
            step, position, path = q.get()

            if position == end:
                if position not in new_paths:
                    new_paths[position] = (len( path) , path )
                else:
                    new_paths[position] = ( max(new_paths[position][0], len( path)) , path )
                continue

            tile = grid[(position)]
            next_step = -step + 1
            possibles_moves = []

            if position == (13,13):
                pass

            for move in self.moves[tile]:
                next_position = (position[0] + move[0], position[1] + move[1])
                if grid[next_position] in self.walls:
                    continue

                if next_position in path:
                    continue

                possibles_moves.append(next_position)


            if len(possibles_moves) == 1 or position == start:
                for next_position in possibles_moves:
                    seen[next_position] = max(next_step,  seen[next_position])
                    q.put((-next_step, next_position, path + [next_position]))
            else:
                if position not in new_paths:
                    new_paths[position] = (len( path) , path )
                else:
                    new_paths[position] = ( max(new_paths[position][0], len( path)) , path )




                # if seen[next_position] < next_step:

        return new_paths

    def calc_1(self, data: dict) -> int:
        grid, width, height, start, end = data
        # self.view(grid, width, height)
        result = self.dfs1(grid, start, end)

        return result[end]

    def calc_2(self, data: [str]) -> int:
        grid, width, height, start, end = data
        for p in grid:
            if grid[p] in ['>','<','^','v']:
                grid[p] = '.'
        # self.view(grid, width, height)

        results = {}
        seen_points = [end]
        start_points = [start]
        while len(start_points) > 0:
            s = start_points.pop(0)
            # if s in seen_points:
            #     print(f'start_point_stuck={s}, {seen_points}')
            #     continue
            # print(f'start_point={s}')
            seen_points += [s]
            # print(seen_points)
            new_paths = self.dfs(grid, s, end)
            results[s] = new_paths
            for longest_paths in new_paths:
                p, paths = new_paths[longest_paths]
                if paths[-1] not in seen_points:
                    start_points.append(paths[-1])
                # for x in paths[:-1]:
                #     grid[x] = self.walls[0]
            # self.view(grid, width, height)
        # self.view(grid, width, height, result,5)
        # 4582 - too low

        # print("here")

        distances = 0
        paths = PriorityQueue()
        paths.put((0, start, [start]))
        seen = defaultdict(int)
        while not paths.empty():
            step, start, path = paths.get()
            # print(step, start, path)
            for r in results[start]:
                length, steps = results[start][r]
                end_step = steps[-1]
                new_path = path + steps[1:]
                if end_step == end:
                    distances = max(distances, len(new_path))
                    print(distances, paths.qsize())
                    print(new_path)
                    continue
                if end_step not in path:
                    # if len(new_path) > seen[end_step]:
                    #     seen[end_step] = len(new_path)
                    paths.put((-(len(new_path) -1), end_step, new_path))

        # print(distances)
        # print(distance_paths[11])
        # seen = defaultdict(int)
        # for i in distance_paths[11]:
        #     seen[i] = 1
        # self.view(grid, width, height, seen)

        # 6563
        # 6591
        # 6599
        # 6875

        return distances - 1

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
    failed, results = aoc.run("part1x_[0-9]+.txt", "part2_[1-1]+.txt")
    if failed:
        sys.exit(1)
