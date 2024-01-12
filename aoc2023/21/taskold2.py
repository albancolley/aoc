"""
AOC Day 10
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math

class Aoc2023010(AocBase):
    """
    AOC Day 10 Class
    """

    starts = ['S']
    moves =   [(0, 1), (0, -1), (1, 0), (-1, 0)]
    walls = ['#']
    spaces = ['.']

    def calc_1(self, data: dict) -> int:
        grid, width, height, start, depth = data
        seen = {}
        q=[(start, 0)]
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

    def view(self, grid, width, height,seen, padding=4):
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

    def view2(self, grid, width, height,seen):
        print()
        for y in range(width):
            line = ""
            for x in range(height):
                if (x,y) in seen:
                    line += f'{str(seen[(x,y)] % 2):<3}'
                else:
                    line += f'{grid[(x,y)]:<3}'
            print(line)
        print()

    def calc_2(self, data: [str]) -> int:
        grid, width, height, start, depth = data

        half_width = int(width / 2)
        half_height = int(width / 2)

        seen = self.bfs(grid, start)


        grid3, start3, width3, height3 = self.expand_grid(grid, width, height, start, 3)

        seen3 = self.bfs(grid3, start3)

        self.view(grid, width, height, seen, 4)
        self.view(grid3, width3, height3, seen3, 4)

        print(self.get_even_cost(seen, 10), self.get_odd_cost(seen, 10))
        print(self.get_even_cost(seen3, 10), self.get_odd_cost(seen3, 10))

        x_change_up = seen3[(0,0)] - seen3[(0,height)]
        x_change_down = seen3[(0,height3-1)] - seen3[(0,height*2-1)]

        y_change_left = seen3[(0,0)] - seen3[(width, 0)]
        x_change_right = seen3[(width3-1, 0)] - seen3[(width*2 - 1, 0)]

        print(x_change_up, x_change_down)
        print(y_change_left, x_change_right)

        seen_bottom_pos, seen_bottom_min, seen_top_pos, seen_top_min = self.seen_vertical_mins(height, seen, width)
        seen_left_pos,seen_left_min, seen_right_pos,  seen_right_min = self.seen_horizontal_mins(height, seen, width)



        return 0

        seen_top_pos = 0
        seen_bottom_pos = 0

        seen_bottom_pos, seen_bottom_min, seen_top_pos, seen_top_min = self.seen_vertical_mins(height, seen, seen_bottom_pos, seen_top_pos, width)
        seen_left_pos,seen_left_min, seen_right_pos,  seen_right_min = self.seen_horizontal_mins(height, seen, seen_bottom_pos, seen_top_pos, width)

        print(seen_top_pos, seen_bottom_pos, seen_left_pos, seen_right_pos )

        seen_left_1 = self.bfs(grid, (width-1, seen_left_pos))
        seen_right_1 = self.bfs(grid, (0, seen_right_pos))
        seen_bottom_1 = self.bfs(grid, (seen_bottom_pos, 0))
        seen_top_1 = self.bfs(grid, (seen_top_pos, height-1))


        seen_top = self.bfs(grid, (half_width, 0))
        seen_bottom = self.bfs(grid, (half_width, height -1))
        seen_right = self.bfs(grid, (width-1, half_height))
        seen_left = self.bfs(grid, (0, half_height))

        seen_top_left = self.bfs(grid, (width-1, height-1))
        seen_top_right = self.bfs(grid, (0, height-1))
        seen_bottom_left = self.bfs(grid, (width-1, 0))
        seen_bottom_left = self.bfs(grid, (0, 0))

        self.view(grid, width, height, seen, 4)
        self.view(grid, width, height, seen_top_1, 4)
        self.view(grid, width, height, seen_bottom_1, 4)
        self.view(grid, width, height, seen_left_1, 4)
        self.view(grid, width, height, seen_right_1, 4)

        totals = []
        for steps in (6, 10):
            steps_x = steps / width
            steps_extra_x = steps % width
            steps_y = steps / width
            steps_extra_y = steps % width

            print(self.get_even_cost(seen, steps))
            total_cost = self.get_even_cost(seen, steps)

            if seen_top_min %2 == 0:
                total_cost += self.get_odd_cost(seen_top_1,  steps-seen_top_min)
            else:
                total_cost += self.get_even_cost(seen_top_1, steps - seen_top_min)
            if seen_bottom_min %2 == 0:
                total_cost += self.get_odd_cost(seen_bottom_1,steps - seen_bottom_min)
            else:
                total_cost += self.get_even_cost(seen_bottom_1, steps - seen_bottom_min)
            if seen_left_min %2 == 0:
                total_cost += self.get_odd_cost(seen_left_1, steps - seen_left_min )
            else:
                total_cost += self.get_even_cost(seen_left_1, steps - seen_left_min)
            if seen_right_min %2 == 0:
                total_cost += self.get_odd_cost(seen_right_1, steps - seen_right_min)
            else:
                total_cost += self.get_even_cost(seen_right_1, steps - seen_right_min)

            totals.append(total_cost)
            print(total_cost)




        return totals

        # grid2 = {}
        # multiplier = 3
        # width2 = width * multiplier
        # height2 = height * multiplier
        # half_multiplier = int(multiplier / 2)
        # start2 = (width * half_multiplier + start[0], height * half_multiplier + start[1])
        #
        # for mx in range(multiplier):
        #     for my in range(multiplier):
        #         for x in range(width):
        #             for y in range(height):
        #                 grid2[(width*mx) + x, (height*my) + y] = grid[x,y]
        #
        # for x in range(width2):
        #     grid2[x, -1] = '#'
        #     grid2[x, width2] = '#'
        #
        # for y in range(height2):
        #     grid2[-1, y] = '#'
        #     grid2[height2, y] = '#'
        #
        # print(start2)
        # seen3x3 = self.bfs(grid2, start2)
        #
        # grid3 = {}
        # multiplier3 = 5
        # width3 = width * multiplier3
        # height3 = height * multiplier3
        # half_multiplier3 = int(multiplier3 / 2)
        # start3 = (width * half_multiplier3 + start[0], height * half_multiplier3 + start[1])
        #
        # for mx in range(multiplier3):
        #     for my in range(multiplier3):
        #         for x in range(width):
        #             for y in range(height):
        #                 grid3[(width*mx) + x, (height*my) + y] = grid[x,y]
        #
        # for x in range(width3):
        #     grid3[x, -1] = '#'
        #     grid3[x, width3] = '#'
        #
        # for y in range(height3):
        #     grid3[-1, y] = '#'
        #     grid3[height3, y] = '#'
        #
        # print(start3)
        # seen5x5 = self.bfs(grid3, start3)


        grid4 = {}
        multiplier4 = 15
        width4 = width * multiplier4
        height4 = height * multiplier4
        half_multiplier4 = int(multiplier4 / 2)
        start4 = (width * half_multiplier4 + start[0], height * half_multiplier4 + start[1])

        for mx in range(multiplier4):
            for my in range(multiplier4):
                for x in range(width):
                    for y in range(height):
                        grid4[(width*mx) + x, (height*my) + y] = grid[x,y]

        for x in range(width4):
            grid4[x, -1] = '#'
            grid4[x, width4] = '#'

        for y in range(height4):
            grid4[-1, y] = '#'
            grid4[height4, y] = '#'

        print(start4)
        seen7x7 = self.bfs(grid4, start4)


        cost_odd = [seen[x] for x in seen if seen[x] % 2 == 1]
        cost_even = [seen[x] for x in seen if seen[x] % 2 == 0]
        cost2 = [seen7x7[x] for x in seen7x7 if seen7x7[x] % 2 == 1]
        cost2_even = [seen7x7[x] for x in seen7x7 if seen7x7[x] % 2 ==0]
        cost2_odd = [seen7x7[x] for x in seen7x7 if seen7x7[x] % 2 ==1]
        print(len(cost_even), len(cost_odd), len(cost_even)*9, len(cost_odd)*9)
        print(len(cost2_even), len(cost2_odd))

        costtopleft1_odd = [seen7x7[x] for x in seen7x7 if seen7x7[x] % 2 == 1 and x[0] < 132 and x[1] < 132]
        costtopleft2_odd = [seen7x7[x] for x in seen7x7 if seen7x7[x] % 2 == 1 and 132 <= x[0] < 132*2 and x[1] < 132]

        sum = 0
        sum_even = 0
        sum_odd = 0
        for mx in range(multiplier4):
            for my in range(multiplier4):
                seen_temp = {}
                for x in range(width):
                    for y in range(height):
                        if ((width * mx) + x, (height * my) + y) in seen7x7:
                            seen_temp[x,y] = seen7x7[(width * mx) + x, (height * my) + y]
                # cost_odd_temp = [seen_temp[x] for x in seen_temp if seen_temp[x] % 2 == 1 and seen_temp[x] <= 196*2]
                # cost_end_temp = [seen_temp[x] for x in seen_temp if seen_temp[x] % 2 == 0 and seen_temp[x] <= 196*2]
                # print(len(cost_odd_temp), len(cost_end_temp))
                # cost_odd_temp = [seen_temp[x] for x in seen_temp if seen_temp[x] % 2 == 1 and seen_temp[x] <= 196*3]
                # cost_end_temp = [seen_temp[x] for x in seen_temp if seen_temp[x] % 2 == 0 and seen_temp[x] <= 196*3]
                # print(len(cost_odd_temp), len(cost_end_temp))
                cost_odd_temp = [seen_temp[x] for x in seen_temp if seen_temp[x] % 2 == 1 and seen_temp[x] <= 196*8]
                cost_end_temp = [seen_temp[x] for x in seen_temp if seen_temp[x] % 2 == 0 and seen_temp[x] <= 196*8]
                print(len(cost_odd_temp), len(cost_end_temp))
                t = len([seen_temp[x] for x in seen_temp if seen_temp[x] <= 196*4])
                sum_even += len(cost_end_temp)
                sum_odd += len(cost_odd_temp)
                sum += t

        print(sum, sum_odd, sum_even)

        cost_odd_temp = [seen[x] for x in seen if seen[x] % 2 == 1]
        cost_even_temp = [seen[x] for x in seen if seen[x] % 2 == 0]
        print(len(cost_odd_temp), len(cost_even_temp))

        costodd130 = [seen7x7[x] for x in seen7x7 if seen7x7[x] % 2 == 1 and seen7x7[x]<=196]
        costeven130 = [seen7x7[x] for x in seen7x7 if seen7x7[x] % 2 == 0 and seen7x7[x]<=196]

        costodd260 = [seen7x7[x] for x in seen7x7 if seen7x7[x] % 2 == 1 and seen7x7[x]<=196*2]
        costeven260 = [seen7x7[x] for x in seen7x7 if seen7x7[x] % 2 == 0 and seen7x7[x]<=196*2]

        costodd390 = [seen7x7[x] for x in seen7x7 if seen7x7[x] % 2 == 1 and seen7x7[x]<=196*3]
        costeven390 = [seen7x7[x] for x in seen7x7 if seen7x7[x] % 2 == 0 and seen7x7[x]<=196*3]


        print(7451+7458, 7458*2, len(costodd130), len(costeven130))

        print(7451+7458, 7458*2, len(costodd260), len(costeven260))


        print(7451+7458, 7458*2, len(costodd390), len(costeven390))

        # 11872582400 too low

        # seen_temp ={}
        # for x in range(132):
        #     for y in range(132):
        #         if (x,y) in seen:
        #             seen_temp[(x,y)] = seen3x3[]


        return 0

        cost3 = [seen5x5[x] for x in seen5x5 if seen5x5[x] % 2 == 1]
        print(len(cost), len(cost2), len(cost2) / len(cost))
        print(len(cost2), len(cost3), len(cost3) / len(cost2))


        cost = [seen3x3[x] for x in seen3x3 if seen3x3[x] % 2 == 0 and seen3x3[x] <= 130]
        cost2 = [seen3x3[x] for x in seen3x3 if seen3x3[x] % 2 == 0 and seen3x3[x] > 130 and seen3x3[x] <= 196]
        cost260 = self.get_cost(196, seen)
        print(cost260)
        print(len(cost), len(cost2), len(cost2) / 2)
        cost = [seen3x3[x] for x in seen3x3 if seen3x3[x] % 2 == 0 and seen3x3[x] <= 65]
        cost2 = [seen3x3[x] for x in seen3x3 if seen3x3[x] % 2 == 0 and seen3x3[x] > 65]
        print(len(cost), len(cost2))

        # for x in range(132):
        #     for y in range(132):
        #         seen_temp =

        #
        # cost = [seen3x3[x] for x in seen3x3 if seen[x] % 2 == 0 and seen[x] <= 196]
        # cost2 = [seen3x3[x] for x in seen3x3 if seen[x] % 2 == 0 and seen[x] > 196]


        return 0

        even_cost, odd_cost = self.get_cost(500, seen3x3)
        print(even_cost, odd_cost)
        # return 0

        self.view(grid2, width2, height2, seen3x3, 4)
        return 0

        flat_seen =[seen3x3[x] for x in seen3x3]
        last = 0
        last2 = 0
        even_sum = 0
        last_sum = 0
        total = 0
        last_total = 0
        even = 0
        odd = 0
        for x in range(0, 501):
            new = flat_seen.count(x)
            if x % 2 ==0:
                even += new
            else:
                odd += new
            total += new
            print(x, total, total - last_total, even, odd)
            last_total = total
            # print(x, total, flat_seen.count(x), new - last, new - 3*x, x**2, even_sum, even_sum / x, (even_sum/x)-last_sum)
            # last = new
            # last_sum = even_sum /x
            # x2 = x + 237
            # new2 = flat_seen.count(x2)
            # print(x2, flat_seen.count(x2), new2 - last2, new2 - 3*x2, x2**2)
            # last2 = new2

        return 0

        last = (0,0 )
        last2 = (0,0 )
        even = 0
        odd = 0
        for x in range(200, 589):
            cost = self.get_cost(x, seen3x3)
            if x % 2 ==0:
                even += cost
            else:
                odd += code
            print(x, cost, (cost[0] -last[0], cost[1] -last[1]), (cost[0] -last2[0], cost[1] -last2[1]))
            last2 = last
            last = cost

        return 0
        self.view(grid2, width2, height2, seen3x3)


        shortest_distances = {}

        all_seens ={}
        for x in range(width):
            s = self.bfs(grid, (x, 0))
            all_seens[f'x-{x}'] = s
            lowest = s[(0, height-1)]
            lowest_position = 0
            for x_bottom in range(1, width):
                if s[(x_bottom, height-1)] < lowest:
                    lowest = s[(x_bottom, height-1)]
                    lowest_position = x_bottom
            shortest_distances[f'x-{x}'] = (lowest_position, lowest)

        for y in range(height):
            s = self.bfs(grid, (0, y))
            all_seens[f'y-{y}'] = s
            # self.view(grid, width, height, s)
            lowest = s[(width - 1, 0)]
            lowest_position = 0
            for bottom_pos in range(1, height):
                bottom = s[(width - 1, bottom_pos)]
                if bottom < lowest:
                    lowest = bottom
                    lowest_position = bottom_pos
            shortest_distances[f'y-{y}'] = (lowest_position, lowest)

        y_cost = shortest_distances[f'y-0'][1]
        x_cost = shortest_distances[f'x-0'][1]
        print(y_cost, x_cost )

        found_even = len([seen[x] for x in seen if seen[x] % 2 == 0])
        found_odd = len([seen[x] for x in seen if seen[x] % 2 == 1])

        self.view(grid, width, height, seen)

        found_even_cost = len([seen[x] for x in seen if seen[x] % 2 == 0 and seen[x] <= y_cost])
        found_odd_cost = len([seen[x] for x in seen if seen[x] % 2 == 1 and  seen[x] <= y_cost])


        min_top_x = min([seen[x,0] for x in range(0,width)])
        min_bottom_x = min([seen[x,height-1] for x in range(0,width)])
        min_top_y = min([seen[0,y] for y in range(0,height)])
        min_bottom_y = min([seen[width-1, y] for y in range(0,height)])

        print(min_top_x, min_bottom_x,min_top_y, min_bottom_y )


        even_cost_top_x, odd_cost_top_x = self.get_cost(y_cost - min_top_x, all_seens['x-8'])
        even_cost_top_y, odd_cost_top_y = self.get_cost(y_cost - min_top_y, all_seens['y-4'])
        even_cost_bottom_x, odd_cost_bottom_x = self.get_cost(y_cost - min_bottom_x, all_seens['x-3'])
        even_cost_bottom_y, odd_cost_bottom_y = self.get_cost(y_cost - min_bottom_y, all_seens['y-4'])

        print(min_top_x, y_cost - min_top_x, even_cost_top_x, odd_cost_top_x)
        self.view(grid, width, height, all_seens['x-8'])
        print( min_top_y, y_cost - min_top_y,even_cost_top_y, odd_cost_top_y)
        self.view(grid, width, height, all_seens['y-4'])

        print(min_bottom_x, y_cost - min_bottom_x, even_cost_bottom_x, odd_cost_bottom_x)
        self.view(grid, width, height, all_seens['x-3'])

        print(min_bottom_y, y_cost - min_bottom_y,even_cost_bottom_y, odd_cost_bottom_y)
        self.view(grid, width, height, all_seens['y-4'])

        self.view(grid, width, height, all_seens['y-0'])

        remaining_step = 50 - y_cost
        squares = int(remaining_step / y_cost)
        squares_remainder = remaining_step % y_cost
        squares_total = (7)**2 - 9
        total = (squares_total * found_odd) + found_odd_cost + even_cost_top_x + even_cost_top_y + odd_cost_bottom_x + even_cost_bottom_y
        total2 = (squares_total * found_even) + found_even_cost + odd_cost_top_x + odd_cost_top_y + even_cost_bottom_x + odd_cost_bottom_y
        print(found_even, found_odd)
        print(odd_cost_top_x + odd_cost_top_y + odd_cost_bottom_x + odd_cost_bottom_y)
        print(even_cost_top_x + even_cost_top_y + even_cost_bottom_x + even_cost_bottom_y)
        print(remaining_step, squares, squares_remainder, squares_total, total, total2)

        # 8  2  2  2
        # 8  2  2  2
        # 7  3  2  4
        # 6  4  2  9
        return total2



        min_top_x = width
        min_bottom_x = width
        for x in range(width):
            min_top_x = min(seen[(x,0)], min_top_x)
            min_bottom_x = min(seen[(x,height - 1)], min_bottom_x)

        min_top_y = width
        min_bottom_y = width
        for y in range(width):
            min_top_y = min(seen[(0, y)], min_top_y)
            min_bottom_y = min(seen[(width - 1, y)], min_bottom_y)

        shortest_path_horizontal = min_top_y + min_bottom_y + 1
        shortest_path_vertical = min_top_x + min_bottom_x + 1

        print(min_top_y, min_bottom_y, shortest_path_horizontal)
        print(min_top_x, min_bottom_x, shortest_path_vertical)

        diagonal1 = seen[(0,0)], seen[(width-1, height -1)]
        diagonal2 = seen[(width-1 ,0)], seen[(0, height -1)]

        print(width, height)
        print(diagonal1, diagonal2)

        return 0

        steps = 50
        up = (steps - min_top_x) % shortest_path_vertical
        down = (steps - min_bottom_x) % shortest_path_vertical
        left = (steps - min_top_y) % shortest_path_horizontal
        right = (steps - min_bottom_y) % shortest_path_horizontal
        print(up, left, down, right)

        horizontal_step = int(steps / shortest_path_horizontal)
        horizontal_step_remainder = steps % shortest_path_horizontal

        vertical_step = int(steps / shortest_path_vertical)
        vertical_step_remainder = steps % shortest_path_vertical

        found_even = len([seen[x] for x in seen if seen[x] % 2 == 0])
        found_odd = len([seen[x] for x in seen if seen[x] % 2 == 1])


        multiplier = found_odd
        odd = 1
        if steps % 2 == 0:
            multiplier = found_even
            odd =0

        total = multiplier
        total += horizontal_step * multiplier*2
        total += vertical_step * multiplier*2
        # total += int((up + odd) / 2)
        # total += int((down + odd) / 2)
        # total += int((left + odd) / 2)
        # total += int((right + odd) / 2)

        return total

    def expand_grid(self, grid, width, height, start, multiplier):
        grid2 = {}
        width2 = width * multiplier
        height2 = height * multiplier
        half_multiplier = int(multiplier / 2)
        start2 = (width * half_multiplier + start[0], height * half_multiplier + start[1])
        for mx in range(multiplier):
            for my in range(multiplier):
                for x in range(width):
                    for y in range(height):
                        grid2[(width * mx) + x, (height * my) + y] = grid[x, y]
        for x in range(width2):
            grid2[x, -1] = '#'
            grid2[x, width2] = '#'
        for y in range(height2):
            grid2[-1, y] = '#'
            grid2[height2, y] = '#'
        return grid2, start2, width2, height2

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
        return seen_bottom_pos,seen_bottom_min, seen_top_pos,  seen_top_min

    def get_even_cost(self, seen, steps):
        return len([seen[x] for x in seen if seen[x] % 2 == 0 and seen[x] <= steps])

    def get_odd_cost(self, seen, steps):
        return len([seen[x] for x in seen if seen[x] % 2 == 1 and seen[x] <= steps])


    def get_cost(self, remaining_steps, seen):
        even_cost = len([seen[x] for x in seen if seen[x] % 2 == 0 and seen[x] < remaining_steps])
        odd_cost = len([seen[x] for x in seen if seen[x] % 2 == 1 and seen[x] < remaining_steps])
        return even_cost, odd_cost

    def bfs(self, grid, start):
        seen = {start:0}
        q = [(start, 0)]
        while len(q) > 0:
            position, step = q.pop(0)
            for move in self.moves:
                next_position = (position[0] + move[0], position[1] + move[1])
                if grid[next_position[0], next_position[1]] in self.walls:
                    continue
                else:
                    if next_position not in seen:
                        seen[next_position] = step + 1
                        q.append((next_position, step + 1))
        return seen

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

        depth = int(data[height +1])

        # self.display(grid, width, height)
        return grid, width, height, start, depth

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc2023010()
    failed, results = aoc.run("partx1_[0-9]+.txt", "part2_[1-1]+.txt")
    if failed:
        sys.exit(1)
