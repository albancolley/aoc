"""
AOC Day 10
"""
import sys
from common import AocBase
from common import configure
from queue import PriorityQueue


class Aoc2023010(AocBase):
    """
    AOC Day 10 Class
    """

    moves = {
        'N': {'N': (0, -1), 'E': (1, 0), 'W': (-1, 0)},
        'S': {'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)},
        'E': {'S': (0, 1), 'N': (0, -1), 'E': (1, 0)},
        'W': {'S': (0, 1), 'N': (0, -1), 'W': (-1, 0)},
    }

    moves2 = {
        'N': {'E': (1, 0), 'W': (-1, 0)},
        'S': {'E': (1, 0), 'W': (-1, 0)},
        'E': {'S': (0, 1), 'N': (0, -1)},
        'W': {'S': (0, 1), 'N': (0, -1)},
        'A' : {'N': (0, -1),'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)}
    }




    direction_moves = {'S': (0, 1), 'N': (0, -1), 'E': (1, 0), 'W': (-1, 0)}

    def distance_squared(self, p0, p1):
        return (p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2

    def calc_1(self, data: dict) -> int:

        grid, width, height = data
        target = (width - 1, height - 1)
        start_position = (0, 0)
        distance = self.distance_squared(start_position, target)
        q = PriorityQueue()
        q.put((0, distance, (0, 0), 'E', []))

        seen = {}

        while not q.empty():
            total_heat, distance, position, direction, path = q.get()

            # print(total_heat, distance, position, direction, path)

            index = f'{position[0]}-{position[1]}-{"-".join(path[-3:])}'

            if index not in seen:
                seen[index] = total_heat
            else:
                if seen[index] <= total_heat:
                    continue
                seen[index] = min(total_heat, seen[position])

            if position == target:
                return total_heat

            moves = self.moves[direction]
            last_3 = path[-3:]
            for move in moves:
                new_direction = move
                new_move = moves[new_direction]
                next_position = (position[0] + new_move[0], position[1] + new_move[1])
                heat = grid[next_position]

                if heat == 0:
                    continue


                if new_direction == direction:
                    if last_3.count(direction) < 3:
                        q.put((total_heat + heat,
                               self.distance_squared(next_position, target),
                               next_position,
                               new_direction,
                               path + [new_direction]))
                else:
                    q.put((total_heat + heat,
                           self.distance_squared(next_position, target),
                           next_position,
                           new_direction,
                           path + [new_direction]))

        return 0

    def calc_2(self, data: [str]) -> int:
        grid, width, height = data
        target = (width - 1, height - 1)
        start_position = (0, 0)
        distance = self.distance_squared(start_position, target)
        q = PriorityQueue()
        q.put((0, distance, (0, 0), 'A', [], []))
        max_steps = 11
        min_steps = 4

        # first = self.shortest_cost(grid, max_steps, min_steps, q, target)
        #
        # q.empty()
        # q.put((0, distance, (0, 0), 'S', [], []))

        second = self.shortest_cost(grid, max_steps, min_steps, q, target)

        return second

    def shortest_cost(self, grid, max_steps, min_steps, q, target):
        seen = {}
        while not q.empty():
            total_heat, distance, position, direction, path, changes = q.get()

            # print(total_heat, distance, position, direction, path)

            index = f'{position[0]}-{position[1]}-{"-".join(changes[-1:])}'

            if index not in seen:
                seen[index] = total_heat
            else:
                if seen[index] <= total_heat:
                    continue
                seen[index] = min(total_heat, seen[position])

            if position == target:
                # print(path)
                return total_heat

            moves = self.moves2[direction]
            # last_10 = path[10:]
            for move in moves:
                new_direction = move
                new_move = moves[new_direction]
                # next_position = (position[0] + new_move[0], position[1] + new_move[1])
                # heat = grid[next_position]
                #
                # if heat == 0:
                #     continue

                new_heat = total_heat
                for steps in range(1, max_steps):
                    next_position = (position[0] + new_move[0] * steps, position[1] + new_move[1] * steps)
                    if next_position not in grid:
                        break

                    heat = grid[next_position]
                    new_heat += heat
                    if steps >= min_steps:
                        q.put((new_heat,
                               self.distance_squared(next_position, target),
                               next_position,
                               new_direction,
                               path + [new_direction] * steps,
                               changes + [new_direction]))
        return 0

    def load_handler_part1(self, data: [str]) -> [str]:
        grid = {}
        width = len(data[0])
        height = len(data)
        for x in range(-1, width + 1):
            grid[(x, -1)] = 0
        for y in range(0, height):
            grid[(-1, y)] = 0
            line = data[y]
            for x in range(0, width):
                grid[(x, y)] = int(line[x])
            grid[(width, y)] = 0
        for x in range(-1, width + 1):
            grid[(x, height)] = 0

        # self.display(grid, width, height)
        return grid, width, height

    def load_handler_part2(self, data: [str]) -> [str]:
        grid = {}
        width = len(data[0])
        height = len(data)
        for y in range(0, height):
            line = data[y]
            for x in range(0, width):
                grid[(x, y)] = int(line[x])
        return grid, width, height



if __name__ == '__main__':
    configure()
    aoc = Aoc2023010()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
