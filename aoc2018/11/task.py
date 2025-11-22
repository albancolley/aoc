"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure


class Aoc201900(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_square(self, x, y, serial):
        rack_id = x+ 10
        power_level = y * rack_id
        power_level += serial
        power_level *= rack_id
        power_level = (int(power_level / 100) ) % 10
        power_level -= 5
        return power_level

    def calc_1(self, data: dict) -> str:
        serial = 9110
        grid = {}
        for x in range(1, 301):
            for y in range(1,301):
                grid[(x,y)] = self.calc_square(x, y, serial)
        max_fuel = - 100000000000000000000000
        max_x = 0
        max_y = 0
        for x in range(1, 299):
            for y in range(1,299):
                total = 0
                for x1 in range(3):
                    for  y1 in range(3):
                        total += grid[(x+x1, y+y1)]
                if total > max_fuel:
                    max_y = y
                    max_x = x
                    max_fuel = total
        result = 0
        return f'{max_x},{max_y}'

    def calc_2(self, data: [str]) -> str:
        serial = 9110
        grid = {}
        for x in range(1, 301):
            for y in range(1, 301):
                grid[(x, y)] = self.calc_square(x, y, serial)

        # for y in range(269, 269 + 16):
        #     line = ""
        #     for x in range(90, 90 + 16):
        #         line += " " + str(grid[(x, y)])
        #     print(line)


        max_fuel = - 100000000000000000000000
        max_x = 0
        max_y = 0
        max_size = 0
        for x in range(1, 301):
            for y in range(1,301):
                max_grid_size = abs(min(300 - x, 300- y))
                total = 0
                for size in range(0, max_grid_size+1):
                    total += grid[(x+size, y +size)]
                    # print((x+size, y +size), grid[(x+size, y +size)])
                    for s in range(0, size):
                        # print((x + s, y+size), grid[(x + s, y + size)])
                        # print((x + size, y + s), grid[(x + size, y + s)])
                        total += grid[(x + s, y + size)]
                        total += grid[(x + size, y + s)]
                    if total > max_fuel:
                        max_y = y
                        max_x = x
                        max_size = size + 1
                        max_fuel = total
                        print(max_x, max_y, max_size, max_fuel)
            print(x,y)
        return f'{max_x},{max_y},{max_size}'

    def load_handler_part1(self, data: [str]) -> [str]:
       return data

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201900()
    failed, results = aoc.run("part1x_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
