"""
AOC Day 10
"""
import sys
from common import AocBase
from common import configure
import math
from dataclasses import dataclass, field


@dataclass
class Section:
    position: (int, int)
    costs: dict[(int, int), int]
    zeroed_costs: dict[(int, int), int]
    odd_cost: [int]
    even_cost: [int]
    min_cost: int
    max_cost: int
    top_min_cost: int
    top_max_cost: int
    bottom_min_cost: int
    bottom_max_cost: int
    left_min_cost: int
    left_max_cost: int
    right_min_cost: int
    right_max_cost: int


@dataclass
class Grid:
    width: int = 0
    height: int = 0
    grid: dict[(int, int), str] = field(default_factory=dict)
    start: (int, int) = (0, 0)


class Aoc2023010(AocBase):
    """
    AOC Day 10 Class
    """

    starts = ['S']
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    walls = ['#']
    spaces = ['.']

    def view(self, grid, costs, padding=4):
        print()
        for y in range(grid.width):
            line = ""
            for x in range(grid.height):
                if (x, y) in costs:
                    line += f'{str(costs[(x, y)]):<{padding}}'
                else:
                    line += f'{grid.grid[(x, y)]:<{padding}}'
            print(line)
        print()

    def calc_2(self, grid: Grid) -> int:
        # didn't solve examples for part 2 as I found it harder than that actual puzzle input I was given.
        # Sure I didn't find the best solution!
        # example of 19*19 grid to show how costs repeat for the inside of teh diamond
        '''
0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0
0    0    0    0    0    0    0    0    944  5639 949  0    0    0    0    0    0    0    0
0    0    0    0    0    0    0    944  6545 7451 6552 949  0    0    0    0    0    0    0
0    0    0    0    0    0    944  6545 7451 7458 7451 6552 949  0    0    0    0    0    0
0    0    0    0    0    944  6545 7451 7458 7451 7458 7451 6552 949  0    0    0    0    0
0    0    0    0    944  6545 7451 7458 7451 7458 7451 7458 7451 6552 949  0    0    0    0
0    0    0    944  6545 7451 7458 7451 7458 7451 7458 7451 7458 7451 6552 949  0    0    0
0    0    944  6545 7451 7458 7451 7458 7451 7458 7451 7458 7451 7458 7451 6552 949  0    0
0    944  6545 7451 7458 7451 7458 7451 7458 7451 7458 7451 7458 7451 7458 7451 6552 949  0
0    5621 7451 7458 7451 7458 7451 7458 7451 7458 7451 7458 7451 7458 7451 7458 7451 5639 0
0    927  6534 7451 7458 7451 7458 7451 7458 7451 7458 7451 7458 7451 7458 7451 6545 941  0
0    0    927  6534 7451 7458 7451 7458 7451 7458 7451 7458 7451 7458 7451 6545 941  0    0
0    0    0    927  6534 7451 7458 7451 7458 7451 7458 7451 7458 7451 6545 941  0    0    0
0    0    0    0    927  6534 7451 7458 7451 7458 7451 7458 7451 6545 941  0    0    0    0
0    0    0    0    0    927  6534 7451 7458 7451 7458 7451 6545 941  0    0    0    0    0
0    0    0    0    0    0    927  6534 7451 7458 7451 6545 941  0    0    0    0    0    0
0    0    0    0    0    0    0    927  6534 7451 6545 941  0    0    0    0    0    0    0
0    0    0    0    0    0    0    0    927  5621 941  0    0    0    0    0    0    0    0
0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0
        :param grid:
        :return:
        '''

        costs1 = self.bfs(grid)
        max_cost = max(costs1)[0] + 1
        middle_odd_cost = self.get_odd_cost(costs1, max_cost)
        middle_even_cost = self.get_even_cost(costs1, max_cost)

        remainder = int(26501365 % ((max_cost)/2))
        multiplier = int((26501365 - remainder) / max_cost)

        new_grid_size = 9
        new_grid_height = int(new_grid_size / 2)
        grid9 = self.expand_grid(grid, new_grid_size)
        costs9 = self.bfs(grid9)
        sections: dict[(int, int), Section] = self.get_sections(grid9, costs9, grid.width, grid.height)
        top_cost = self.get_odd_cost(sections[new_grid_height, 0].costs, max_cost*new_grid_height + remainder)
        bottom_cost = self.get_odd_cost(sections[new_grid_height, new_grid_size-1].costs, max_cost*new_grid_height + remainder)
        left_cost = self.get_odd_cost(sections[0, new_grid_height].costs, max_cost*new_grid_height + remainder)
        right_cost = self.get_odd_cost(sections[new_grid_size-1, new_grid_height].costs, max_cost*new_grid_height + remainder)

        top_left_cost = self.get_odd_cost(sections[new_grid_height-1, 0].costs, max_cost*new_grid_height + remainder)
        top_left_cost2 = self.get_odd_cost(sections[new_grid_height-1, 1].costs, max_cost*new_grid_height + remainder)

        top_right_cost = self.get_odd_cost(sections[new_grid_height+1, 0].costs, max_cost*new_grid_height + remainder)
        top_right_cost2 = self.get_odd_cost(sections[new_grid_height+1, 1].costs, max_cost*new_grid_height + remainder)

        bottom_left_cost = self.get_odd_cost(sections[new_grid_height-1, new_grid_size - 1].costs, max_cost*new_grid_height + remainder)
        bottom_left_cost2 = self.get_odd_cost(sections[new_grid_height-1, new_grid_size - 2].costs, max_cost*new_grid_height + remainder)

        bottom_right_cost = self.get_odd_cost(sections[new_grid_height+1, new_grid_size - 1].costs, max_cost*new_grid_height + remainder)
        bottom_right_cost2 = self.get_odd_cost(sections[new_grid_height+1, new_grid_size - 2].costs, max_cost*new_grid_height + remainder)

        top = top_cost
        bottom = bottom_cost
        left = left_cost
        right = right_cost

        top_left = top_left_cost2 * (multiplier-1) + top_left_cost * multiplier
        top_right = top_right_cost2 * (multiplier-1) + top_right_cost * multiplier
        bottom_left = bottom_left_cost2 * (multiplier-1) + bottom_left_cost * multiplier
        bottom_right = bottom_right_cost2 * (multiplier-1) + bottom_right_cost * multiplier

        # Middle costs are repeated many times in the shape of a diamond.
        # There is one less row of odd cost to even cost
        middle_odds = middle_odd_cost * (multiplier-1)**2
        middle_evens = middle_even_cost * multiplier**2

        total2 = top + bottom + left + right + top_left + top_right + bottom_left + bottom_right + middle_odds + middle_evens

        return total2

    def bfs(self, grid: Grid) -> dict[(int, int), int]:
        seen: dict[(int, int), int] = {grid.start: 0}
        q = [(grid.start, 0)]
        while len(q) > 0:
            position, step = q.pop(0)
            for move in self.moves:
                next_position = (position[0] + move[0], position[1] + move[1])
                if grid.grid[next_position[0], next_position[1]] in self.walls:
                    continue
                else:
                    if next_position not in seen:
                        seen[next_position] = step + 1
                        q.append((next_position, step + 1))
        return seen

    def expand_grid(self, grid, multiplier):
        grid2 = Grid()
        grid2.width = grid.width * multiplier
        grid2.height = grid.height * multiplier
        half_multiplier = int(multiplier / 2)
        grid2.start = (grid.width * half_multiplier + grid.start[0], grid.height * half_multiplier + grid.start[1])
        for mx in range(multiplier):
            for my in range(multiplier):
                for x in range(grid.width):
                    for y in range(grid.height):
                        grid2.grid[((grid.width * mx) + x, (grid.height * my) + y)] = grid.grid[x, y]
        for x in range(grid2.width):
            grid2.grid[(x, -1)] = '#'
            grid2.grid[(x, grid2.height)] = '#'
        for y in range(grid2.height):
            grid2.grid[(-1, y)] = '#'
            grid2.grid[(grid2.width, y)] = '#'
        return grid2

    def get_sections(self, grid: Grid, full_costs: dict[(int, int), int], section_height, section_width) -> dict[
        (int, int), Section]:

        sections: dict[(int, int), Section] = {}
        x_multiplier = int(grid.width / section_width)
        y_multiplier = int(grid.height / section_height)

        for mx in range(x_multiplier):
            for my in range(y_multiplier):

                costs: dict[(int, int), int] = dict()
                x_section_start = mx * section_width
                y_section_start = my * section_height
                min_cost = math.inf
                max_cost = 0
                top_min_cost = math.inf
                top_max_cost = 0
                bottom_min_cost = math.inf
                bottom_max_cost = 0
                left_min_cost = math.inf
                left_max_cost = 0
                right_min_cost = math.inf
                right_max_cost = 0
                for x in range(x_section_start, x_section_start + section_width):
                    for y in range(y_section_start, y_section_start + section_height):
                        if (x, y) in full_costs:
                            full_cost = full_costs[(x, y)]
                            if x % section_width == 0:
                                left_min_cost = min(left_min_cost, full_cost)
                                left_max_cost = max(left_max_cost, full_cost)
                            if x % section_width == (section_width - 1):
                                right_min_cost = min(right_min_cost, full_cost)
                                right_max_cost = max(right_max_cost, full_cost)
                            if y % section_height == 0:
                                top_min_cost = min(top_min_cost, full_cost)
                                top_max_cost = max(top_max_cost, full_cost)
                            if y % section_height == (section_height - 1):
                                bottom_min_cost = min(bottom_min_cost, full_cost)
                                bottom_max_cost = max(bottom_max_cost, full_cost)
                            costs[(x % section_width, y % section_height)] = full_cost
                            min_cost = min(min_cost, full_cost)
                            max_cost = max(max_cost, full_cost)

                zeroed_costs: dict[(int, int), int] = dict()
                for p in costs:
                    zeroed_costs[p] = costs[p] - min_cost
                odd_cost = self.get_odd_cost(zeroed_costs, max_cost + 1)
                even_cost = self.get_even_cost(zeroed_costs, max_cost + 1)

                section = Section((mx, my), costs, zeroed_costs, odd_cost, even_cost, min_cost, max_cost,
                                  top_min_cost, top_max_cost, bottom_min_cost, bottom_max_cost,
                                  left_min_cost, left_max_cost, right_min_cost, right_max_cost
                                  )
                sections[(mx, my)] = section
        return sections

    def calc_1(self, data: dict) -> int:
        grid, width, height, start, depth = data
        seen = {}
        q = [(start, 0)]
        # last_depth = -1
        while len(q) > 0:
            position, step = q.pop(0)
            # if last_depth < step:
            #     # self.view(grid, width, height, seen)
            #     print(step)
            #     last_depth = step

            if step == depth + 1:
                continue

            for move in self.moves:
                next_position = (position[0] + move[0], position[1] + move[1])
                if grid[next_position[0], next_position[1]] in self.walls:
                    continue
                else:
                    if next_position not in seen:
                        seen[next_position] = step + 1
                        q.append((next_position, step + 1))

        found = [seen[x] for x in seen if seen[x] % 2 == 0]

        return len(found)

    def view2(self, grid, width, height, seen):
        print()
        for y in range(width):
            line = ""
            for x in range(height):
                if (x, y) in seen:
                    line += f'{str(seen[(x, y)] % 2):<3}'
                else:
                    line += f'{grid[(x, y)]:<3}'
            print(line)
        print()

    def seen_vertical_mins(self, height, seen, width):
        seen_bottom_pos = 0
        seen_top_pos = 0
        seen_top_min = math.inf
        seen_bottom_min = math.inf
        for x in range(width):
            value = seen[(x, 0)]
            if value < seen_top_min:
                seen_top_pos = x
                seen_top_min = value
            value = seen[(x, height - 1)]
            if value < seen_bottom_min:
                seen_bottom_pos = x
                seen_bottom_min = value
        return seen_bottom_pos, seen_bottom_min, seen_top_pos, seen_top_min

    def seen_horizontal_mins(self, height, seen, width):
        seen_bottom_pos = 0
        seen_top_pos = 0
        seen_top_min = math.inf
        seen_bottom_min = math.inf
        for y in range(height):
            value = seen[(0, y)]
            if value < seen_top_min:
                seen_top_pos = y
                seen_top_min = value
            value = seen[(width - 1, y)]
            if value < seen_bottom_min:
                seen_bottom_pos = y
                seen_bottom_min = value
        return seen_bottom_pos, seen_bottom_min, seen_top_pos, seen_top_min

    def get_even_cost(self, seen, steps):
        return len([seen[x] for x in seen if seen[x] % 2 == 0 and seen[x] <= steps])

    def get_odd_cost(self, seen, steps):
        return len([seen[x] for x in seen if seen[x] % 2 == 1 and seen[x] <= steps])

    def get_cost(self, remaining_steps, seen):
        even_cost = len([seen[x] for x in seen if seen[x] % 2 == 0 and seen[x] < remaining_steps])
        odd_cost = len([seen[x] for x in seen if seen[x] % 2 == 1 and seen[x] < remaining_steps])
        return even_cost, odd_cost

    def load_handler_part1(self, data: [str]) -> [str]:
        grid = {}
        width = len(data[0])
        height = len(data) - 2
        start = (0, 0)
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

        depth = int(data[height + 1])

        # self.display(grid, width, height)
        return grid, width, height, start, depth

    def load_handler_part2(self, data: [str]) -> [str]:
        grid = Grid()
        grid.width = len(data[0])
        grid.height = len(data) - 2
        grid.start = (0, 0)
        for x in range(-1, grid.width + 1):
            grid.grid[(x, -1)] = self.walls[0]
        for y in range(0, grid.height):
            grid.grid[(-1, y)] = self.walls[0]
            line = data[y]
            for x in range(0, grid.width):
                if line[x] in self.starts:
                    grid.start = (x, y)
                    grid.grid[(x, y)] = self.spaces[0]
                else:
                    grid.grid[(x, y)] = line[x]
            grid.grid[(grid.width, y)] = self.walls[0]
        for x in range(-1, grid.width + 1):
            grid.grid[(x, grid.height)] = self.walls[0]

        # self.display(grid, width, height)
        return grid


if __name__ == '__main__':
    configure()
    aoc = Aoc2023010()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[2-9]+.txt")
    if failed:
        sys.exit(1)
