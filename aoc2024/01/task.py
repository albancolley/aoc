"""
AOC Day X
"""
import re
import sys
from collections import Counter

from common import AocBase
from common import configure


class Aoc202400(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data:([int], [int]) ) -> int:
        result = 0
        for a, b in zip(data[0], data[1]):
            result += int(abs(a - b))
        return result

    def calc_2(self, data:([int], [int]) ) -> int:

        counts_a= Counter(data[0])
        counts_b= Counter(data[1])
        total = 0
        for a in counts_a:
            if a in counts_b:
                total += counts_b[a] * a * counts_a[a]
        return total

    def load_handler_part1(self, data: [str]) -> ([int], [int]):
        regex = r"(\d+) *(\d+)"

        data1 = []
        data2 = []
        for d in data:
            match = re.match(regex, d)
            data1.append(int(match.group(1)))
            data2.append(int(match.group(2)))

        data1.sort()
        data2.sort()
        return data1, data2

    def load_handler_part2(self, data: [str]) -> [str]:
        regex = r"(\d+) *(\d+)"

        data1 = []
        data2 = []
        for d in data:
            match = re.match(regex, d)
            data1.append(int(match.group(1)))
            data2.append(int(match.group(2)))

        return data1, data2


if __name__ == '__main__':
    configure()
    aoc = Aoc202400()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
