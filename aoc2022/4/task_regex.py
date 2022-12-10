from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
import re
from dataclasses import dataclass

logger = logging.getLogger("ACO2022-4")


@dataclass
class Pair:
    start1: int
    end1: int
    start2: int
    end2: int

class Aoc202201(AocBase):

    def calc_1(self, data: [Pair]) -> int:
        total: int = 0
        for item in data:
            if (item.start1 >= item.start2 and item.end1 <= item.end2) \
                    or (item.start2 >= item.start1 and item.end2 <= item.end1):
                total += 1
        return total

    def calc_2(self, data: [str]) -> int:
        total: int = 0
        for item in data:
            if not(item.end1 < item.start2 or item.end2 < item.start1):
                total += 1
        return total

    def load_handler_part1(self, data: [str]) -> [Pair]:
        new_data = []
        p = re.compile(r'(\d+)-(\d+),(\d+)-(\d+)')
        for row in data:
            m = re.match(p, row)
            if m:
                pair = Pair(int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)))
                new_data.append(pair)
        return new_data

    def load_handler_part2(self, data: [str]) -> [()]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc202201()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        exit(1)
