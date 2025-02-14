"""
AOC Day X
"""
import sys
from itertools import combinations

from common import AocBase
from common import configure
import math

class Aoc201600(AocBase):
    """
    AOC Day 10 Class
    """

    def set_partitions(self, iterable, k=None):
        L = list(iterable)
        n = len(L)
        if k is not None:
            if k < 1:
                raise ValueError(
                    "Can't partition in a negative or zero number of groups"
                )
            elif k > n:
                return

        def set_partitions_helper(L, k):
            n = len(L)
            if k == 1:
                yield [L]
            elif n == k:
                yield [[s] for s in L]
            else:
                e, *M = L
                for p in set_partitions_helper(M, k - 1):
                    yield [[e], *p]
                for p in set_partitions_helper(M, k):
                    for i in range(len(p)):
                        yield p[:i] + [[e] + p[i]] + p[i + 1:]

        if k is None:
            for k in range(1, n + 1):
                yield from set_partitions_helper(L, k)
        else:
            yield from set_partitions_helper(L, k)

    def calc_1(self, numbers: [int]) -> int:
        shortest = len(numbers)
        total = sum(numbers)
        target = int(total / 3)
        # print(numbers)
        # print(target)
        # print(shortest)
        min_qe =  float('inf')
        number_set = set(numbers)
        options = combinations(number_set, 6)
        count = 0
        count_matches = 0
        for o in options:
            count += 1
            if sum(o) == target:
                count_matches += 1
                # print(math.prod(o), o)
                options2 = combinations(number_set.difference(o), 6)
                for o2 in options2:
                    if sum(o2) == target:
                        # print(o, o2, math.prod(o), math.prod(o2))
                        min_qe = min(min_qe,math.prod(o))
                        min_qe = min(min_qe, math.prod(o2))

                options2 = combinations(number_set.difference(o), 8)
                for o2 in options2:
                    if sum(o2) == target:
                        min_qe = min(min_qe,math.prod(o))

        return min_qe

    def calc_2(self, numbers: [int]) -> int:
        shortest = len(numbers)
        total = sum(numbers)
        target = int(total / 4)
        min_qe =  float('inf')
        number_set = set(numbers)
        options = combinations(number_set, 5)
        count = 0
        count_matches = 0
        for o in options:
            count += 1
            if sum(o) == target:
                count_matches += 1
                options2 = combinations(number_set.difference(o), 5)
                for o2 in options2:
                    if sum(o2) == target:
                        min_qe = min(min_qe,math.prod(o))
                        min_qe = min(min_qe, math.prod(o2))

                options2 = combinations(number_set.difference(o), 7)
                for o2 in options2:
                    if sum(o2) == target:
                        min_qe = min(min_qe,math.prod(o))
        return min_qe

    def load_handler_part1(self, data: [str]) -> [int]:
        numbers = []
        for l in data:
            numbers.append(int(l))
        return numbers

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201600()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
