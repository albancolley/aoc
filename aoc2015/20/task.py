"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure
from functools import reduce


class Aoc201600(AocBase):
    """
    AOC Day 10 Class
    """

    def factors(self, n):
        return list(reduce(list.__add__,
                          ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))

    def calc_1(self, data: dict) -> int:
        target = 34000000
        # target = 7
        start = 0
        presents = 0
        while presents < target:
            start += 1
            presents = sum(self.factors(start))*10
        return start

    def calc_2(self, data: [str]) -> int:
        target = 34000000
        # target = 7
        start = 0
        presents = 0
        while presents < target:
            # if start % 10000 == 0:
            #     print(start, presents)
            start += 1
            factors = self.factors(start)
            valid_factors = []
            for factor in factors:
                if factor * 50 > start:
                    valid_factors.append(factor)

            presents = sum(valid_factors) * 11
        return start
    #952920

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
