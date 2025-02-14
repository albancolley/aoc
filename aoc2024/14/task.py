"""
AOC Day X
"""
import sys

from common import AocBase
from common import configure


class Aoc202414(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data) -> int:
        robots: dict
        robots, width, height = data
        for second in range(100):
            for robot in robots:
                pos: complex
                vel: complex
                pos, vel = robots[robot]
                pos += vel
                if pos.real < 0:
                    pos += width
                if pos.real >= width:
                    pos -= width
                if pos.imag < 0:
                    pos += complex(0, height)
                if pos.imag >= height:
                    pos -= complex(0, height)
                robots[robot] = (pos, vel)

        width_mid = int(width / 2)
        height_mid = int(height / 2)

        Q1 = 0
        Q2 = 0
        Q3 = 0
        Q4 = 0
        locations = [x[0] for x in robots.values()]
        for x in range(0,width_mid):
            for y in range(0, height_mid):
                if complex(x,y) in locations:
                    Q1 += locations.count(complex(x,y))
        for x in range(0, width_mid):
            for y in range(height_mid+1, height):
                if complex(x,y) in locations:
                    Q2 += locations.count(complex(x,y))
        for x in range(width_mid+1,  width):
            for y in range(0, height_mid):
                if complex(x,y) in locations:
                    Q3 += locations.count(complex(x,y))
        for x in range(width_mid + 1, width):
            for y in range(height_mid+1, height):
                if complex(x,y) in locations:
                    Q4 += locations.count(complex(x,y))

        total = 1
        if Q1 > 0:
            total *= Q1
        if Q2 > 0:
            total *= Q2
        if Q3 > 0:
            total *= Q3
        if Q4 > 0:
            total *= Q4

        return total

    def calc_2(self, data: [str]) -> int:
        robots: dict
        robots, width, height = data
        second = 1
        while True:
            for robot in robots:
                pos: complex
                vel: complex
                pos, vel = robots[robot]
                pos += vel
                if pos.real < 0:
                    pos += width
                if pos.real >= width:
                    pos -= width
                if pos.imag < 0:
                    pos += complex(0, height)
                if pos.imag >= height:
                    pos -= complex(0, height)
                robots[robot] = (pos, vel)
            if self.is_tree(robots, width, height):
                # self.print_robots(second, robots, width, height)
                return second
            second += 1

    def load_handler_part1(self, data: [str]) -> [str]:
        robots = {}
        width = int(data[0].split(",")[0])
        height = int(data[0].split(",")[1])
        robot_id = 0
        for d in data[1:]:
            temp = d.split(" ")
            temp2 = temp[0][2:].split(",")
            pos = complex(int(temp2[0]),int(temp2[1]))
            temp2 = temp[1][2:].split(",")
            vel = complex(int(temp2[0]), int(temp2[1]))
            robots[robot_id] = (pos, vel)
            robot_id += 1
        return robots, width ,height

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)

    tree = [
        (-1 + 1j),
        (1 + 1j),
        (-2 + 2j),
        (2 + 2j),
        (-3 + 3j),
        (3 + 3j)

    ]

    def is_tree(self, robots:dict, width: int, height: int):
        locations = [x[0] for x in robots.values()]
        for location in locations:
            is_tree = True
            for t in self.tree:
                if location + t not in locations:
                    is_tree = False
                    break
            if is_tree:
                return True

        return False

    def print_robots(self, second: int, robots:dict, width:int, height:int):

        if not self.is_tree(robots, width, height):
            return

        locations = [x[0] for x in robots.values()]
        print(f'Second: {second+1}')
        for x in range(width):
            line = ""
            for y in range(height):
                if complex(x,y) in locations:
                    line += "*"
                else:
                    line += " "
            print(line)



if __name__ == '__main__':
    configure()
    aoc = Aoc202414()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
