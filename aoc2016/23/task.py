"""
AOC Day X
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math

class Aoc201600(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict) -> int:
        a = int(data[0])
        reg = [a,0,0,0]
        pos = 0
        data = data[1:]
        while pos < len(data):
            instruction = data[pos]
            command = instruction[0:3]
            x = instruction[4:].split(' ')[0]
            x_is_reg = x in ['a','b','c','d']
            # print(instruction)
            match command:
                case "cpy":
                    if x_is_reg:
                        value = reg[int(ord(x) - ord('a'))]
                    else:
                        value = int(x)
                    y = instruction[4:].split(' ')[1]
                    y_is_reg = y in ['a', 'b', 'c', 'd']
                    if y_is_reg:
                        reg[int(ord(y) - ord('a'))] = value
                    else:
                        reg[int(y)] = value
                    pos += 1
                case "inc":
                    if x_is_reg:
                        reg[int(ord(x) - ord('a'))] += 1
                    pos += 1
                case "dec":
                    if x_is_reg:
                        reg[int(ord(x) - ord('a'))] -= 1
                    pos += 1
                case "jnz":
                    y = instruction[4:].split(' ')[1]
                    y_is_reg = y in ['a', 'b', 'c', 'd']
                    if y_is_reg:
                        y = reg[int(ord(y) - ord('a'))]
                    else:
                        y = int(y)
                    if x_is_reg:
                        value = reg[int(ord(x) - ord('a'))]
                    else:
                        value = int(x)
                    if value != 0:
                        pos += y
                    else:
                        pos += 1
                case "tgl":
                    if x_is_reg:
                        value = reg[int(ord(x) - ord('a'))]
                    else:
                        value = int(x)
                    tg_pos = pos + value
                    if 0 <= tg_pos < len(data):
                        tgl_cmd = data[tg_pos][0:3]
                        new_command = ""
                        match tgl_cmd:
                            case "inc":
                                new_command = "dec"
                            case "dec":
                                new_command = "inc"
                            case "tgl":
                                new_command = "inc"
                            case "jnz":
                                new_command = "cpy"
                            case "cpy":
                                new_command = "jnz"
                        data[tg_pos] = new_command + data[tg_pos][3:]
                    pos += 1
        return reg[0]

    def calc_2(self, data: [str]) -> int:
        a = int(data[0])
        reg = [a, 0, 0, 0]
        pos = 0
        data = data[1:]
        while pos < len(data):
            instruction = data[pos]
            # print(instruction, reg)
            command = instruction[0:3]
            x = instruction[4:].split(' ')[0]
            x_is_reg = x in ['a', 'b', 'c', 'd']
            # print(instruction)
            match command:
                case "cpy":
                    if x_is_reg:
                        value = reg[int(ord(x) - ord('a'))]
                    else:
                        value = int(x)
                    y = instruction[4:].split(' ')[1]
                    y_is_reg = y in ['a', 'b', 'c', 'd']
                    if y_is_reg:
                        reg[int(ord(y) - ord('a'))] = value
                    else:
                        reg[int(y)] = value
                    pos += 1
                case "inc":
                    if x_is_reg:
                        reg[int(ord(x) - ord('a'))] += 1
                    pos += 1
                case "dec":
                    if x_is_reg:
                        reg[int(ord(x) - ord('a'))] -= 1
                    pos += 1
                case "jnz":
                    y = instruction[4:].split(' ')[1]
                    y_is_reg = y in ['a', 'b', 'c', 'd']
                    if y_is_reg:
                        y = reg[int(ord(y) - ord('a'))]
                    else:
                        y = int(y)
                    if x_is_reg:
                        value = reg[int(ord(x) - ord('a'))]
                    else:
                        value = int(x)
                    if value != 0:
                        pos += y
                    else:
                        pos += 1
                case "tgl":
                    if x_is_reg:
                        value = reg[int(ord(x) - ord('a'))]
                    else:
                        value = int(x)
                    tg_pos = pos + value
                    if 0 <= tg_pos < len(data):
                        tgl_cmd = data[tg_pos][0:3]
                        new_command = ""
                        match tgl_cmd:
                            case "inc":
                                new_command = "dec"
                            case "dec":
                                new_command = "inc"
                            case "tgl":
                                new_command = "inc"
                            case "jnz":
                                new_command = "cpy"
                            case "cpy":
                                new_command = "jnz"
                        data[tg_pos] = new_command + data[tg_pos][3:]
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
