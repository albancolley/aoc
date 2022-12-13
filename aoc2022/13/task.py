import string

from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
import numpy as np
from dataclasses import dataclass, field
from collections import OrderedDict
from collections import deque
from functools import cmp_to_key

logger = logging.getLogger("ACO2022-13")

import math

@dataclass()
class Pairs:
    pair1: []
    pair2: []

class Aoc202212(AocBase):

    def compare(self, a,  b):
        if isinstance(a, list) and isinstance(b, list):
            for pos in range(0, min(len(a), len(b))):
                c = self.compare(a[pos], b[pos])
                if c != 0:
                    return c
            if len(a) < len(b):
                return -1
            if len(a) > len(b):
                return 1
            return 0

        elif isinstance(a, list):
            return self.compare(a, [b])
        elif isinstance(b, list):
            return self.compare([a], b)
        else:
            return (a > b) - (a < b)

    def calc_1(self, data: [Pairs]) -> int:
        index = 1
        matching_packets = 0
        for pair in data:
            result = self.compare(pair.pair1, pair.pair2)
            if result == -1:
                matching_packets += index
            index += 1
        return matching_packets

    def calc_2(self, data: [str]) -> int:
        data2 = sorted(data, key=cmp_to_key(self.compare))
        pos1 = data2.index([[2]]) + 1
        pos2 = data2.index([[6]]) + 1
        return pos1 * pos2

    def load_handler_part1(self, data: [str]) -> [Pairs]:
        pos = 0
        pairs: [Pairs] = []
        while pos < len(data):
            pair = Pairs(eval(data[pos]), eval(data[pos+1]))
            pos += 3
            pairs.append(pair)
        return pairs

    def load_handler_part2(self, data: [str]) -> [str]:
        pos = 0
        pairs: [] = []
        while pos < len(data):
            pairs.append(eval(data[pos]))
            pairs.append(eval(data[pos+1]))
            pos += 3
        pairs.append([[2]])
        pairs.append([[6]])
        return pairs


if __name__ == '__main__':
    configure()
    aoc = Aoc202212()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        exit(1)
