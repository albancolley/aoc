"""
AOC Day 10
"""
import sys
from common import AocBase
from common import configure


class Aoc2023010(AocBase):
    """
    AOC Day 10 Class
    """

    directions = {
        ('N', '.'): ['N'],
        ('S', '.'): ['S'],
        ('E', '.'): ['E'],
        ('W', '.'): ['W'],
        ('N', '\\'): ['W'],
        ('S', '\\'): ['E'],
        ('E', '\\'): ['S'],
        ('W', '\\'): ['N'],
        ('N', '/'): ['E'],
        ('S', '/'): ['W'],
        ('E', '/'): ['N'],
        ('W', '/'): ['S'],
        ('N', '|'): ['N'],
        ('S', '|'): ['S'],
        ('E', '|'): ['N', 'S'],
        ('W', '|'): ['N', 'S'],
        ('N', '-'): ['E', 'W'],
        ('S', '-'): ['E', 'W'],
        ('E', '-'): ['E'],
        ('W', '-'): ['W'],
    }

    moves = {'S': (0, 1), 'N': (0, -1), 'E': (1, 0), 'W': (-1, 0)}

    def calc_1(self, data: dict) -> int:
        grid, width, height  = data
        q = [((0, 0), 'E', [(0, 0)])]
        points = self.get_energy(grid, q)
        # self.display(grid, width, height, paths)
        return len(points)

    def get_energy(self, grid, q):
        paths = []
        all_beams = set()
        # all_beams.add(((0, 0), 'E'))
        while len(q) > 0:
            position, direction, path = q.pop()
            move = self.moves[direction]
            next_position = (position[0] + move[0], position[1] + move[1])
            tile = grid[next_position]
            if (position, direction) in all_beams:
                paths.append(path)
                continue
            if position == (5, 2):
                pass
            all_beams.add((position, direction))
            if tile == 'E':
                paths.append(path)
                continue
            else:
                next_directions = self.directions[(direction, tile)]
                for next_direction in next_directions:
                    q.insert(0, (next_position, next_direction, path + [next_position]))
        result = 0
        points = set()
        for path in paths:
            for p in path:
                points.add(p)
        return points

    def display_grid(self, grid, width, height ,paths = []):
        print(f"     01234567890")
        unique_path = set()
        for path in paths:
            for p in path:
                unique_path.add(p)
        for x in range(-1, width +1):
            line = f"{x:>3} "
            for y in range(-1, height + 1):
                if (y,x) in unique_path:
                    line += '#'
                else:
                    line += grid[(y,x)]


            print (line)

    def calc_2(self, data: [str]) -> int:
        grid, width, height = data
        winner = 0
        starts = []
        for i in range(height):
            starts.append(((0, i), 'E', [(0, i)]))
            starts.append(((width - 1, i), 'W', [(width - 1, i)]))
        for i in range(width):
            starts.append(((i, 0 ), 'S', [(i,0 )]))
            starts.append(((height - 1, 0 ), 'N', [(i, height - 1)]))

        for s in starts:
            q = [s]
            points = self.get_energy(grid, q)
            winner = max(len(points), winner)

        # self.display(grid, width, height, paths)
        return winner

    def load_handler_part1(self, data: [str]) -> [str]:
        grid = {}
        width = len(data[0])
        height = len(data)
        for x in range(-1, width + 1):
            grid[(x, -1)] = 'E'
        for y in range(0, height):
            grid[(-1, y)] = 'E'
            line = data[y]
            for x in range(0, width):
                grid[(x, y)] = line[x]
            grid[(width, y)] = 'E'
        for x in range(-1, width + 1):
            grid[(x, height)] = 'E'

        # self.display(grid, width, height)
        return grid, width, height

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc2023010()
    failed, results = aoc.run("part1_[1-2]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
