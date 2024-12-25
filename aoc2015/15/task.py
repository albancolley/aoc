"""
AOC Day X
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math
from itertools import combinations
import re
from functools import reduce
from operator import mul

class Aoc201600(AocBase):
    """
    AOC Day 10 Class
    """

    def to_sum_k_iter(self, n, k):
        index = [0] * (n + 1)
        index[-1] = k
        for j in combinations(range(0, k), n - 1):
            index[1:-1] = j
            yield tuple(index[i + 1] - index[i] for i in range(n))

    def calc_1(self, data: dict) -> int:

        regex = r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)"

        recipies = []
        for d in data:
            match = re.match(regex, d)
            name = match.group(1)
            capacity = int(match.group(2))
            durability = int(match.group(3))
            flavor = int(match.group(4))
            texture = int(match.group(5))
            calories = int(match.group(6))
            recipies.append((name, capacity, durability, flavor, texture, calories))


        nums = self.to_sum_k_iter(len(recipies),100)

        max_score = 0
        for num in nums:
            score = [0] * 4
            for i in range(len(recipies)):
                for j in range(4):
                    score[j] += recipies[i][j+1] * num[i]
            negative = False
            for s in score:
                if s <= 0:
                    negative = True
            if not negative:
                max_score = max( reduce(mul, score), max_score)
        return max_score

    def calc_2(self, data: [str]) -> int:
        regex = r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)"

        recipies = []
        for d in data:
            match = re.match(regex, d)
            name = match.group(1)
            capacity = int(match.group(2))
            durability = int(match.group(3))
            flavor = int(match.group(4))
            texture = int(match.group(5))
            calories = int(match.group(6))
            recipies.append((name, capacity, durability, flavor, texture, calories))


        nums = self.to_sum_k_iter(len(recipies), 100)

        max_score = 0
        for num in nums:
            score = [0] * 4
            cals = 0
            for i in range(len(recipies)):
                for j in range(4):
                    score[j] += recipies[i][j + 1] * num[i]
                cals += recipies[i][5] * num[i]
            negative = False
            for s in score:
                if s <= 0:
                    negative = True
            if not negative and cals == 500:
                max_score = max(reduce(mul, score), max_score)
        return max_score
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
