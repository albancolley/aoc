"""
AOC Day 7
"""
import sys
from common import AocBase
from common import configure


class Aoc202309(AocBase):
    """
    AOC Day 9 Class
    """

    def difference(self, row):
        new_row = []
        for i in range(0, len(row)-1):
            second = row[i+1]
            first = row[i]
            diff = second - first
            new_row.append(diff)
        same = new_row.count(new_row[0]) == len(new_row)
        if same:
            result = new_row[0]
        else:
            result = new_row[-1] + self.difference(new_row)
        return result

    def calc_1(self, data: dict) -> int:
        total = 0
        for r in data:
            result = self.difference(r)
            total += r[-1] + result
        return total

    def difference_reverse(self, row):
        new_row = []
        for i in range(0, len(row)-1):
            second = row[i+1]
            first = row[i]
            diff = second - first
            new_row.append(diff)
        same = new_row.count(new_row[0]) == len(new_row)
        if same:
            result = new_row[0]
        else:
            diff = self.difference_reverse(new_row)
            result = new_row[0] - diff
        return result

    def calc_2(self, data: [str]) -> int:
        total = 0
        for r in data:
            result = self.difference_reverse(r)
            total += r[0] - result
        return total

    def load_handler_part1(self, data: [str]) -> [str]:
        result = []
        for d in data:
            result.append([int(x) for x in d.split()])
        return result

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc202309()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
