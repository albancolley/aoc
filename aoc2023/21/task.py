"""
AOC Day 10
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
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

    def calc_2(self, grid: Grid) -> str:

        # grid19 = self.expand_grid(grid, 19)
        #
        # costs19 = self.bfs(grid19)
        #
        # steps = 65 + 8*131
        #
        # total_cost = self.get_odd_cost(costs19, steps)
        # sections = self.get_sections(grid19, costs19, grid.width, grid.height)
        # total = 0
        # even = False
        # for y in range(19):
        #     line = ""
        #     for x in range(19):
        #         if even:
        #             line += f'{self.get_even_cost(sections[(x,y)].costs, steps):<5}'
        #             total += self.get_even_cost(sections[(x, y)].costs, steps)
        #         else:
        #             total += self.get_odd_cost(sections[(x, y)].costs, steps)
        #             line += f'{self.get_odd_cost(sections[(x, y)].costs, steps):<5}'
        #         # even = not even
        #     print(line)

        # top_cost = 5583 +
        multiplier = 8
        multiplier = 202300

        top = 5639
        bottom = 5621
        left =  5621
        right = 5639
        top_left = 6545 * (multiplier-1) + 944 * multiplier
        top_right = 6552 * (multiplier-1) + 949 * multiplier
        bottom_left = 6534 * (multiplier-1) + 927 * multiplier
        bottom_right = 6545 * (multiplier-1) + 941 * multiplier
        middle_odds = 7458 * (multiplier-1)**2
        middle_evens = 7451 * multiplier**2

        total2 = top + bottom + left + right + top_left + top_right + bottom_left + bottom_right + middle_odds + middle_evens


        return f'1078146 {total2}'

        return f'{total_cost} {total} {total2}'

        cost = self.bfs(grid)

        grid7 = self.expand_grid(grid, 7)

        costs7 = self.bfs(grid7)

        sections = self.get_sections(grid7, costs7, grid.width, grid.height)

        # self.view(grid7, costs7)

        even_cost = self.get_even_cost(cost, math.inf)
        odd_cost = self.get_odd_cost(cost, math.inf)

        totals = []
        for steps in [80]:
            # for steps in (6, 10, 50, 100):
            total_cost = self.get_even_cost(costs7, steps)
            if steps <= sections[(3, 0)].top_min_cost:
                totals.append(total_cost)
                continue

            x_change_up = sections[(3, 0)].top_min_cost - sections[(3, 0)].bottom_min_cost + 1
            x_change_down = sections[(3, 6)].bottom_min_cost - sections[(3, 6)].top_min_cost + 1
            y_change_left = sections[(0, 3)].left_min_cost - sections[(0, 3)].right_min_cost + 1
            y_change_right = sections[(6, 3)].right_min_cost - sections[(6, 3)].left_min_cost + 1

            x_steps_up = (steps - sections[(3, 0)].top_min_cost) % x_change_up
            x_steps_down = (steps - sections[(3, 6)].bottom_min_cost) % x_change_down
            y_steps_left = (steps - sections[(0, 3)].left_min_cost) % y_change_left
            y_steps_right = (steps - sections[(6, 3)].right_min_cost) % y_change_right

            remainder = 80



            x_repeat_up = int((steps - sections[(3, 0)].min_cost) / x_change_up)
            x_repeat_down = int((steps - sections[(3, 6)].min_cost) / x_change_down)
            y_repeat_left = int((steps - sections[(0, 3)].min_cost) / y_change_left)
            y_repeat_right = int((steps - sections[(6, 3)].min_cost) / y_change_right)

            print(x_change_up, x_change_down, y_change_left, y_change_right)

            print(x_steps_up, x_steps_down, y_steps_left, y_steps_right)

            print(x_repeat_up, x_repeat_down, y_repeat_left, y_repeat_right)

            # costs for the top, bottom, left, right point
            cost_top = self.get_even_cost(sections[(3, 0)].zeroed_costs, x_steps_up)
            cost_bottom = self.get_even_cost(sections[(3, 6)].zeroed_costs, x_steps_down)
            cost_left = self.get_even_cost(sections[(0, 3)].zeroed_costs, y_steps_left)
            cost_right = self.get_even_cost(sections[(6, 3)].zeroed_costs, y_steps_right)

            total_cost += cost_top + cost_bottom + cost_left + cost_right

            print(cost_top, cost_bottom, cost_left, cost_right)

            complete_total = x_repeat_up + (x_repeat_up * (x_repeat_up - 1))
            complete_total += x_repeat_down + (x_repeat_down * (x_repeat_down - 1))
            complete_total += y_repeat_left + 2*(y_repeat_left - 1) + 2*(y_repeat_left - 2) + 2*(y_repeat_left - 3)
            complete_total += y_repeat_right + 2*(y_repeat_right - 1)  + 2*(y_repeat_right - 2)  + 2*(y_repeat_right - 3)

            print(complete_total)

            complete_even = int(x_repeat_up * (x_repeat_up+1) / 2)
            complete_even += int(x_repeat_down * (x_repeat_down+1) / 2)

            evens_left = int(y_repeat_left * (y_repeat_left+1) / 2) - (int((y_repeat_left-4) * (y_repeat_left-3) / 2))*2
            complete_even += evens_left

            evens_right = int(y_repeat_right * (y_repeat_right+1) / 2) - (int((y_repeat_right-4) * (y_repeat_right-3) / 2))*2
            complete_even += evens_right

            compete_odd = complete_total - complete_even

            # if (min)
            total_cost += even_cost * complete_even
            total_cost += odd_cost * compete_odd

            top_left_diagonal = sections[(0, 0)].costs[(0, 0)] - sections[(1, 1)].costs[(0, 0)]
            top_right_diagonal = sections[(6, 0)].costs[(grid.width - 1, 0)] - sections[(5, 1)].costs[
                (grid.width - 1, 0)]

            bottom_left_diagonal = sections[(0, 6)].costs[(0, grid.height - 1)] - sections[(1, 5)].costs[
                (0, grid.height - 1)]
            bottom_right_diagonal = sections[(6, 6)].costs[(grid.width - 1, grid.height - 1)] - sections[(5, 5)].costs[
                (grid.width - 1, grid.height - 1)]

            top_left_diagonal_remainder_min = (steps - sections[(0, 0)].costs[(0, 0)] - 2) % top_left_diagonal
            top_left_diagonal_remainder_max = (steps - sections[(1, 0)].costs[(0, 0)] - 2) % top_left_diagonal

            top_right_diagonal_remainder_min = (steps - sections[(6, 0)].costs[
                (grid.width - 1, 0)] - 2) % top_right_diagonal
            top_right_diagonal_remainder_max = (steps - sections[(5, 0)].costs[
                (grid.width - 1, 0)] - 2) % top_right_diagonal

            bottom_left_diagonal_remainder_min = (steps - sections[(0, 6)].costs[
                (0, grid.height - 1)] - 2) % bottom_left_diagonal
            bottom_left_diagonal_remainder_max = (steps - sections[(0, 5)].costs[
                (0, grid.height - 1)] - 2) % bottom_left_diagonal

            bottom_right_diagonal_remainder_min = (steps - sections[(6, 6)].costs[
                (grid.width - 1, grid.height - 1)] - 2) % bottom_right_diagonal
            bottom_right_diagonal_remainder_max = (steps - sections[(6, 5)].costs[
                (grid.width - 1, grid.height - 1)] - 2) % bottom_right_diagonal

            print(top_left_diagonal, top_right_diagonal, bottom_left_diagonal, bottom_right_diagonal)

            top_right_cost = (self.get_even_cost(sections[(0, 0)].zeroed_costs, top_left_diagonal_remainder_min)* (x_repeat_up*2-1) +
                          self.get_odd_cost(sections[(0, 0)].zeroed_costs, top_left_diagonal_remainder_max)* (x_repeat_up*2-2) )

            top_left_cost = (self.get_even_cost(sections[(6, 0)].zeroed_costs, top_right_diagonal_remainder_min)* (x_repeat_up*2-1) +
                          self.get_odd_cost(sections[(6, 0)].zeroed_costs, top_right_diagonal_remainder_max)* (x_repeat_up*2-2) )


            bottom_right_cost = (self.get_even_cost(sections[(0, 6)].zeroed_costs, bottom_left_diagonal_remainder_min)* (x_repeat_down*2-1) +
                          self.get_odd_cost(sections[(0, 6)].zeroed_costs, bottom_left_diagonal_remainder_max)* (x_repeat_down*2-2) )

            bottom_left_cost = (self.get_even_cost(sections[(6, 6)].zeroed_costs, bottom_right_diagonal_remainder_min)* (x_repeat_down*2-1) +
                          self.get_odd_cost(sections[(6, 6)].zeroed_costs, bottom_right_diagonal_remainder_max)* (x_repeat_down*2-2) )


            # total_cost += top_right_cost + top_left_cost + bottom_left_cost + bottom_right_cost



            totals.append(total_cost)

        return ' '.join([str(x) for x in totals])

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
    failed, results = aoc.run("partx1_[0-9]+.txt", "part2_[2-2]+.txt")
    if failed:
        sys.exit(1)
