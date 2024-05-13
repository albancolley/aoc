"""
AOC Day X
"""
import re
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math

class Aoc201601(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict) -> int:
        result = 0
        line: str
        p = re.compile(r' *(\d+) *(\d+) *(\d+)')
        for line in data:
            m = re.match(p, line)
            num1 = int(m.group(1))
            num2 = int(m.group(2))
            num3 = int(m.group(3))
            if num1 + num2 <= num3:
                continue
            if num2 + num3 <= num1:
                continue
            if num1 + num3 <= num2:
                continue

            result += 1

        return result

    def check(self, num1, num2,  num3):
        if num1 + num2 <= num3:
            return False
        if num2 + num3 <= num1:
            return False
        if num1 + num3 <= num2:
            return False
        return True
    def calc_2(self, data: [str]) -> int:
        result = 0
        line: str
        p = re.compile(r' *(\d+) *(\d+) *(\d+)')
        for i in range(0, len(data), 3):
            m = re.match(p, data[i])
            num11 = int(m.group(1))
            num21 = int(m.group(2))
            num31 = int(m.group(3))
            m = re.match(p, data[i+1])
            num12 = int(m.group(1))
            num22 = int(m.group(2))
            num32 = int(m.group(3))
            m = re.match(p, data[i+2])
            num13 = int(m.group(1))
            num23 = int(m.group(2))
            num33 = int(m.group(3))
            if self.check(num11,num12, num13):
                result += 1
            if self.check(num21,num22, num23):
                result += 1
            if self.check(num31,num32, num33):
                result += 1

        return result

    def load_handler_part1(self, data: [str]) -> [str]:
       return data

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201601()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
