"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure


class Aoc201908(AocBase):
    """
    AOC Day 10 Class
    """

    def recurse(self,  data, start) -> (int, int):
        children_count = data[start]
        meta_count = data[start +1]

        start += 2
        totals = 0
        for child in range(children_count):
            start, total = self.recurse(data, start)
            totals += total

        meta = data[start: start + meta_count]
        totals += sum(meta)

        return start + meta_count, totals


    def calc_1(self, data: list) -> int:
        start, total = self.recurse(data, 0)
        return total

    def recurse_2(self,  data, start) -> (int, int):
        children_count = data[start]
        meta_count = data[start +1]

        start += 2
        totals = []
        for child in range(children_count):
            start, total = self.recurse_2(data, start)
            totals += [total]

        meta_data = data[start: start + meta_count]
        total = 0
        if children_count == 0:
            total = sum(meta_data)
        else:
            for m in meta_data:
                if m <= len(totals):
                    total += totals[m-1]

        return start + meta_count, total


    def calc_2(self, data: list) -> int:
        start, total = self.recurse_2(data, 0)
        return total


    def load_handler_part1(self, data: [str]) -> [str]:
        return [int(x) for x in data[0].split(' ')]

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201908()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
