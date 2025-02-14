"""
AOC Day X
"""
import sys
from collections import defaultdict

from common import AocBase
from common import configure


class Aoc202400(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict) -> int:
        result = 0
        locks, keys = data

        print(locks, keys)
        for lock in locks:
            for key in keys:
                failed = False
                for i in range(5):
                    if lock[i] + key[i] > 5:
                        failed = True
                if not failed:
                    result += 1


        return result

    def calc_2(self, data: [str]) -> int:
        total = 0
        return total

    def load_handler_part1(self, data: [str]) -> [str]:
        keys = []
        locks = []
        pos = 0
        while pos < len(data):
            lock = data[pos] == "#####"
            counts= defaultdict(int)
            if lock:
                pos += 1
            for i in range(6):
                row = data[pos]
                for j in range(len(row)):
                    if row[j] == '#':
                        counts[j] += 1
                pos += 1
            line = []
            for i in range(len(data[0])):
                line+=[counts[i]]
            pos += 1
            if lock:
                locks.append(line)
            else:
                keys.append(line)
                pos += 1

        return locks, keys

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc202400()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
