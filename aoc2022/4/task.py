from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging

logger = logging.getLogger("ACO2022-4")


class Aoc202201(AocBase):

    def calc_1(self, data: [str]) -> int:
        total: int = 0
        for item in data:
            item_split = item.split(',')
            left = item_split[0]
            right = item_split[1]
            left_split = left.split('-')
            start1 = int(left_split[0])
            end1 = int(left_split[1])
            right_split = right.split('-')
            start2 = int(right_split[0])
            end2 = int(right_split[1])
            if (start1 >= start2 and end1 <= end2) or (start2 >= start1 and end2 <= end1):
                total += 1
        return total

    def calc_2(self, data: [str]) -> int:
        total: int = 0
        for item in data:
            item_split = item.split(',')
            left = item_split[0]
            right = item_split[1]
            left_split = left.split('-')
            start1 = int(left_split[0])
            end1 = int(left_split[1])
            right_split = right.split('-')
            start2 = int(right_split[0])
            end2 = int(right_split[1])
            if not(end1 < start2 or end2 < start1) :
                total += 1
        return total

    def load_handler_part1(self, data: [str]) -> [str]:
        return data

    def load_handler_part2(self, data: [str]) -> [str]:
        return data


if __name__ == '__main__':
    configure()
    aoc = Aoc202201()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        exit(1)
