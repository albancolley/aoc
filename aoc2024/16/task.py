"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure
import heapq

class Aoc202416(AocBase):
    """
    AOC Day 10 Class
    """
    moves = {
        'N': 0 + 1j,
        'S': 0 - 1j,
        'W': -1 + 0j,
        'E': 1 + 0j
    }

    possible_moves = {
        'N': ['N','W', 'E'],
        'S': ['S', 'W', 'E'],
        'E': ['E','N', 'S'],
        'W': ['W','N', 'S'],
    }


    def calc_1(self, data: dict) -> int:
        grid, start, end, width, height = data

        # self.print_grid( grid, height, width, start, end)

        seen = {}
        queue = []
        heapq.heappush(queue, (0, start.real, start.imag, 'E'))
        while len(queue) > 0:
            cost, x,y, direction = heapq.heappop(queue)
            pos= complex(x,y)
            for next_direction in self.possible_moves[direction]:
                new_cost = cost
                if next_direction != direction:
                    new_cost += 1000
                    next_pos = pos
                else:
                    new_cost += 1
                    next_pos = pos + self.moves[next_direction]
                    if grid[next_pos] != ".":
                        continue

                if (next_pos, next_direction) in seen and new_cost >= seen[(next_pos, next_direction)]:
                    continue

                seen[(next_pos, next_direction)] = new_cost
                if next_pos != end:
                    heapq.heappush(queue, (new_cost, next_pos.real, next_pos.imag, next_direction))

        total_costs = []
        for direction in self.moves.keys():
            if (end, direction) in seen:
                total_costs += [seen[(end, direction)]]

        return min(total_costs)

    def calc_2(self, data: [str]) -> int:
        grid, start, end, width, height = data

        # self.print_grid( grid, height, width, start, end)

        seen = {}
        paths ={}
        queue = []
        heapq.heappush(queue, (0, start.real, start.imag, 'E', [(start.real, start.imag)] ))
        while len(queue) > 0:
            cost, x, y, direction, path = heapq.heappop(queue)
            pos = complex(x, y)
            for next_direction in self.possible_moves[direction]:
                new_path = [] + path
                new_cost = cost
                if next_direction != direction:
                    new_cost += 1000
                    next_pos = pos
                else:
                    new_cost += 1
                    next_pos = pos + self.moves[next_direction]
                    if grid[next_pos] != ".":
                        continue
                    new_path += [(next_pos.real, next_pos.imag)]

                if (next_pos, next_direction) in seen and new_cost > seen[(next_pos, next_direction)]:
                    continue

                seen[(next_pos, next_direction)] = new_cost
                if next_pos != end:
                    heapq.heappush(queue, (new_cost, next_pos.real, next_pos.imag, next_direction, new_path))
                else:
                    if new_cost not in paths:
                        paths[new_cost] = []
                    paths[new_cost].append(new_path)

        total_costs = []
        for direction in self.moves.keys():
            if (end, direction) in seen:
                total_costs += [seen[(end, direction)]]

        min_cost = min(total_costs)

        locations = set()
        for path in paths[min_cost]:
            # print(path)
            for pos in path:
                locations.add(pos)


        return len(locations)

    def print_grid(self, grid, height, width, start, end):
        for y in range(height):
            line = ""
            for x in range(width):
                pos = complex(x, y)
                if pos == start:
                    line += 'S'
                elif pos == end:
                    line += 'E'
                else:
                    line += str(grid[pos])
            print(line)


    def load_handler_part1(self, data: [str]) -> [str]:
        width = len(data[0])
        height  = len(data)
        grid = {}
        start = complex(0, 0)
        end = complex(0, 0)
        y = 0
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
            y += 1
        return grid,  start, end, width, height

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc202416()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
