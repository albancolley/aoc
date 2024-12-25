"""
AOC Day X
"""
import sys
from collections import defaultdict

from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math

class Aoc202422(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict) -> int:
        result = 0
        for d in data:
            secret = d
            for i in range(2000):
                new = secret * 64
                new = self.mix_and_prune(secret, new)
                new_2 = int(new / 32)
                new = self.mix_and_prune(new, new_2)
                new_3 = new * 2048
                new = self.mix_and_prune(new, new_3)
                # print(new)
                secret = new
            result += secret
        return result

    def calc_2(self, data: [str]) -> int:
        result = 0
        totals = defaultdict(int)
        for d in data:
            last_values= []
            secret = d
            last = secret  % 10
            seen = {}
            for i in range(2000):
                new = secret * 64
                new = self.mix_and_prune(secret, new)
                new_2 = int(new / 32)
                new = self.mix_and_prune(new, new_2)
                new_3 = new * 2048
                new = self.mix_and_prune(new, new_3)
                # print(new)
                secret = new
                next = secret  % 10
                diff = next - last
                last = next
                last_values.append(diff)
                if len(last_values) > 4: # and last_values[-4] != 0 and last_values[-3] != 0 and last_values[-2] != 0 and last_values[-1] != 0:
                    key = ",".join([str(x) for x in last_values[-4:]])
                    if key not in seen:
                        totals[key] += next
                        seen[key] = True

        max_money = max(totals.values())
        return  max_money

    def load_handler_part1(self, data: [str]) -> [str]:
       return [int(d) for d in data]

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)

    def mix_and_prune(self, old, new):
        return (old ^ new) % 16777216


if __name__ == '__main__':
    configure()
    aoc = Aoc202422()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
