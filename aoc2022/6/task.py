import string

from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
import re
logger = logging.getLogger("ACO2022-4")


class Aoc202206(AocBase):

    def calc_1(self, data: [str]) -> int:
        total: int = 0
        row = data[0]
        for i in range(4, len(row)):
            check = row[i-4:i]
            dups = {}
            has_dups = False
            for c in check:
                if c in dups:
                    has_dups = True
                    break
                dups[c] = True
            if not has_dups:
                break
        return i

    def calc_2(self, data: [str]) -> int:
        total: int = 0
        row = data[0]
        for i in range(14, len(row)):
            check = row[i-14:i]
            dups = {}
            has_dups = False
            for c in check:
                if c in dups:
                    has_dups = True
                    break
                dups[c] = True
            if not has_dups:
                break
        return i

    def load_handler_part1(self, data: [str]) -> [str]:
        return data

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc202206()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        exit(1)
