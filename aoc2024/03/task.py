"""
AOC Day X
"""
import re
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math

class Aoc202400(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: [int]) -> int:
        result = 0
        for d in data:
            result += d[0] * d[1]
        return result

    def calc_2(self, data: [str]) -> int:
        result = 0
        for d in data:
            result += d[0] * d[1]
        return result

    def load_handler_part1(self, data: [str]) -> [str]:
        regex = r"mul\(\d+,\d+\)"
        regex2 = r"mul\((\d+),(\d+)\)"

        data1 = []
        for l in data:
            all = re.findall(regex, l)
            # print(all)
            for d in all:
                match = re.match(regex2, d)
                data1.append((int(match.group(1)), int(match.group(2))))
        return data1

    def load_handler_part2(self, data: [str]) -> [str]:
        regex = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
        regex2 = r"(mul)\((\d+),(\d+)\)|(do)\(\)|(don't)\(\)"

        data1 = []

        include = True

        for l in data:
            all = re.findall(regex, l)
            # print(all)
            for d in all:
                match = re.match(regex2, d)
                if match.group(0) == "do()":
                    include = True
                elif match.group(0) == "don't()":
                    include = False
                elif include:
                    data1.append((int(match.group(2)), int(match.group(3))))
        return data1


if __name__ == '__main__':
    configure()
    aoc = Aoc202400()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
