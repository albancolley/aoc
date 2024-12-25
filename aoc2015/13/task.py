"""
AOC Day X
"""
import sys
from itertools import permutations

from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math

class Aoc201600(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict) -> int:
        people = set()
        happiness = {}
        for d in data:
            person_1, _, state , amount, _, _, _, _, _, _, person_2 = d.split()
            person_2 = person_2[0:-1]
            value = int(amount)
            if state == 'lose':
                value = -value
            people.add(person_1)
            people.add(person_2)
            happiness[(person_1, person_2)] = value

        combs = permutations(list(people), len(people))

        totals = []
        for comb in combs:
            last = comb[0]
            total=0
            total = happiness[(comb[0], comb[-1])]
            total += happiness[(comb[-1], comb[0])]
            for c in comb[1:]:
                total += happiness[(last, c)]
                total += happiness[(c, last)]
                last = c
            totals += [total]

        return max(totals)

    def calc_2(self, data: [str]) -> int:
        people = set()
        happiness = {}
        for d in data:
            person_1, _, state , amount, _, _, _, _, _, _, person_2 = d.split()
            person_2 = person_2[0:-1]
            value = int(amount)
            if state == 'lose':
                value = -value
            people.add(person_1)
            people.add(person_2)
            happiness[(person_1, person_2)] = value

        for p in people:
            happiness[(p, "Alban")] = 0
            happiness[("Alban",p)] = 0

        people.add("Alban")

        combs = permutations(list(people), len(people))

        totals = []
        for comb in combs:
            last = comb[0]
            total=0
            total = happiness[(comb[0], comb[-1])]
            total += happiness[(comb[-1], comb[0])]
            for c in comb[1:]:
                total += happiness[(last, c)]
                total += happiness[(c, last)]
                last = c
            totals += [total]

        return max(totals)
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
