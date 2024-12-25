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
        result = 0
        d: str
        for d in data:
            original_length = len(d)
            new_list = list(d[1:-1])
            new_string = ""
            while len(new_list) > 0:
                c = new_list.pop(0)
                if c == '\\':
                    c2 = new_list.pop(0)
                    if c2 == '"' or c2 == '\\':
                        new_string += c2
                    elif c2 == 'x':
                        c3 = new_list.pop(0)
                        c4 = new_list.pop(0)
                        new_string += chr(int(c3+c4, 16))
                    else:
                        new_list.insert(0, c2)
                else:
                    new_string += c
            result += original_length - len(new_string)
        return result

    def calc_2(self, data: [str]) -> int:
        result = 0
        d: str
        for d in data:
            original_length = len(d)
            new_list = list(d)
            new_string = '"'
            while len(new_list) > 0:
                c = new_list.pop(0)
                if c == '"':
                    new_string += '\\"'
                elif c == '\\':
                    new_string += '\\\\'
                else:
                    new_string += c
            new_string += '"'
            result += len(new_string) - original_length
        return result

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
