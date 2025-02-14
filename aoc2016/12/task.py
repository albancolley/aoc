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

    def calc_1(self, data: dict) -> int:
        reg = [0,0,0,0]
        pos = 0
        while pos < len(data):
            instruction = data[pos]
            command = instruction[0:3]
            x = instruction[4:].split(' ')[0]
            x_is_reg = x in ['a','b','c','d']
            match command:
                case "cpy":
                    if x_is_reg:
                        value = reg[int(ord(x) - ord('a'))]
                    else:
                        value = int(x)
                    y = instruction[4:].split(' ')[1]
                    reg[int(ord(y) - ord('a'))] = value
                    pos += 1
                case "inc":
                    reg[int(ord(x) - ord('a'))] += 1
                    pos += 1
                case "dec":
                    reg[int(ord(x) - ord('a'))] -= 1
                    pos += 1
                case "jnz":
                    y = int(instruction[4:].split(' ')[1])
                    if x_is_reg:
                        value = reg[int(ord(x) - ord('a'))]
                    else:
                        value = int(x)
                    if value != 0:
                        pos += y
                    else:
                        pos += 1
        return reg[0]

    def calc_2(self, data: [str]) -> int:
        reg = [0,0,1,0]
        pos = 0
        while pos < len(data):
            instruction = data[pos]
            command = instruction[0:3]
            x = instruction[4:].split(' ')[0]
            x_is_reg = x in ['a','b','c','d']
            match command:
                case "cpy":
                    if x_is_reg:
                        value = reg[int(ord(x) - ord('a'))]
                    else:
                        value = int(x)
                    y = instruction[4:].split(' ')[1]
                    reg[int(ord(y) - ord('a'))] = value
                    pos += 1
                case "inc":
                    reg[int(ord(x) - ord('a'))] += 1
                    pos += 1
                case "dec":
                    reg[int(ord(x) - ord('a'))] -= 1
                    pos += 1
                case "jnz":
                    y = int(instruction[4:].split(' ')[1])
                    if x_is_reg:
                        value = reg[int(ord(x) - ord('a'))]
                    else:
                        value = int(x)
                    if value != 0:
                        pos += y
                    else:
                        pos += 1
        return reg[0]

    def load_handler_part1(self, data: [str]) -> [str]:
       return data

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201600()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
