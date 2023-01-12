import math

from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
from dataclasses import dataclass, field
import collections

logger = logging.getLogger("ACO2019-9")

class Aoc201908(AocBase):

    def calc_1(self, data: [int]) -> int:
        layers = data[0]
        size = data[1]
        pixels = size[0]*size[1]

        pos = 0
        least_zeros = math.inf
        ones = 0
        twos = 0
        row = layers[pos:pos + pixels]
        while len(row) > 0:

            counter = collections.Counter(row)
            if counter[0] < least_zeros:
                least_zeros = counter[0]
                ones = counter[1]
                twos = counter[2]
            pos += pixels
            row = layers[pos:pos + pixels]

        return ones * twos


    def calc_2(self, data: [str]) -> int:
        layers = data[0]
        size = data[1]
        pixels = size[0]*size[1]

        pos = 0
        result = [2] * pixels
        row = layers[pos:pos + pixels]
        while len(row) > 0:
            for i, v in enumerate(row):
                if v != 2 and result[i] == 2:
                    result[i] = row[i]
            pos += pixels
            row = layers[pos:pos + pixels]

        screen = ""
        pos = 0
        for i in range(0, size[1]):
            screen += ''.join([str(x) for x in result[pos:pos+size[0]]])
            print(''.join([str(x) for x in result[pos:pos+size[0]]]))
            pos += size[0]

        return screen


    def load_handler_part1(self, data: [str]) -> [str]:
        return [[int(x) for x in data[0]], (int(data[1]), int(data[2]))]

    def load_handler_part2(self, data: [str]) -> [str]:
        return [[int(x) for x in data[0]], (int(data[1]), int(data[2]))]

if __name__ == '__main__':
    configure()
    aoc = Aoc201908()
    failed, results = aoc.run("part1x_[0-9]*.txt", "part2_[1-2]+.txt")
    if failed:
        exit(1)
