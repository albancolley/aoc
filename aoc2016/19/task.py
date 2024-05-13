"""
AOC Day X
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math
import numpy as np

class Aoc201600(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict) -> int:

        size = int(data[0])
        power = 1
        last = 3
        while True:
            power += 1
            value = 2**power
            if value > size:
                break
            last = value
        # print(value, last, size)
        return ((size - last + 1)*2) -1

        # for size in range(1, 2000, 2):
        #     present_count = np.arange(1, size + 1, 1)
        #     total = size
        #     pos = -1
        #     while True:
        #         # print(present_count)
        #         size = len(present_count)
        #         if size == 1:
        #             print(total, present_count[0])
        #             break
        #         pos = (pos + 1) % size
        #         next_pos = (pos + 1) % size
        #         # present_count[pos] = (present_count[pos][0], present_count[pos][1] + present_count[next_pos][1])
        #         present_count = np.delete(present_count, next_pos)
        #         if next_pos < pos:
        #             pos -= 1
        # return 0
        #
        # size = int(data[0])
        # present_count = [1] * size
        # pos = -1
        # while True:
        #     pos = (pos + 1) % size
        #     if present_count[pos] == 0:
        #         continue
        #     next_pos = (pos +1) % size
        #     while present_count[next_pos] == 0:
        #         next_pos = (next_pos + 1) % size
        #     present_count[pos] += present_count[next_pos]
        #     present_count[next_pos] = 0
        #     if present_count[pos] == size:
        #         return pos+1

    def calc_2(self, data: [str]) -> int:
        size = int(data[0])
        power = 1
        last = 3
        while True:
            power += 1
            value = 3**power
            if value > size:
                break
            last = value
        return size - last


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
