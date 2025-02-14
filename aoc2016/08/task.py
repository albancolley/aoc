"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure


class Aoc201600(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict) -> []:
        result = []
        for i in range(6):
            result += [['.'] * 50]

        command : str
        for command in data:
            output = ""
            for r in result:
                output += "".join(r) + "\n"
            print(output)

            print(command)
            if command.startswith("rect "):
                xy = command[5:].split('x')
                for x in range(int(xy[0])):
                    for y in range(int(xy[1])):
                        result[y][x] = '#'
            if command.startswith("rotate column x="):
                rot_cmd = command[len("rotate column x="):].split(' by ')
                x = int(rot_cmd[0])
                pixels = int(rot_cmd[1])
                for i in range(pixels):
                    last = result[-1][x]
                    for j in range(len(result)-2, -1, -1):
                        result[j+1][x] = result[j][x]
                    result[0][x] = last
            if command.startswith("rotate row y="):
                rot_cmd = command[len("rotate row y="):].split(' by ')
                y = int(rot_cmd[0])
                pixels = int(rot_cmd[1])
                result[y] = result[y][-pixels:] + result[y][0:len(result[y]) - pixels]

        output = ""
        for r in result:
            output += "".join(r) + "\n"
        print(output)

        total = 0
        for y in range(len(result)):
            for x in range(len(result[0])):
                if result[y][x] == '#':
                    total += 1

        return total

    def calc_2(self, data: [str]) -> int:
        total = 0
        return total

    def load_handler_part1(self, data: [str]) -> [str]:
       return data

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201600()
    failed, results = aoc.run("part1_[2-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
