import dataclasses
import math
import os.path
import string
import sys
import heapq

import numpy as np

from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
from dataclasses import dataclass
import re
from collections import deque
import operator

logger = logging.getLogger("ACO2022-17")


class Aoc202225(AocBase):

    convertions = {
        "2" : 2,
        "1": 1,
        "0": 0,
        "-" : -1,
        "=" : -2
    }

    convertions_back = {
        2: "2",
        1: "1",
        0: "0",
        -1: "-",
        -2: "="
    }

    def base5(self, n):
        base = 1
        result = 0
        r = n[::-1]
        for c in r:
            result += self.convertions[c] * base
            base = base * 5
        return result

    def base5r(self, n):
        result = ""
        while n > 0:
            remainder = n % 5
            match remainder:
                case 3:
                    remainder = "="
                    n = n + 5
                case 4:
                    remainder = "-"
                    n = n + 5
            n = int(n / 5)
            result += str(remainder)
        return result[::-1]


    def calc_1(self, data) -> int:
        total = 0
        for row in data:
            total += self.base5(row)
        return self.base5r(total)

    def calc_2(self, data: []) -> int:
        count = 1

        return count

    def load_handler_part1(self, data: [(int, int)]) -> {}:

        return data

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)

    # def distance(self, pos, end_position):
    #     dis = (pos[0] - end_position[0]) * (pos[0] - end_position[0])
    #     dis += (pos[1] - end_position[1]) * (pos[1] - end_position[1])
    #     math.sqrt()


if __name__ == '__main__':
    configure()
    aoc = Aoc202225()
    failed, results = aoc.run("part1_[1-2]+.txt", "part2x_[1-2]+.txt")
    if failed:
        exit(1)
