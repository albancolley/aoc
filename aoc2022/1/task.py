from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging

logger = logging.getLogger("ACO2022-1")


class Aoc202201(AocBase):

    def calc_1(self, data: [str]) -> int:
        totals = []
        total = 0
        for item in data:
            if item.isnumeric():
                total += int(item)
            else:
                totals.append(total)
                total = 0
        totals.append(total)
        totals.sort()
        return totals[-1]

    def calc_2(self, data: [str]) -> int:
        totals = []
        total = 0
        for item in data:
            if item.isnumeric():
                total += int(item)
            else:
                totals.append(total)
                total = 0
        totals.append(total)
        totals.sort()
        return totals[-1] + totals[-2] + totals[-3]

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
