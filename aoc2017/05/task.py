"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure


class Aoc201705(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict) -> int:
        pos = 0
        count = 0
        while True:
            old_pos = pos
            pos += data[pos]
            data[old_pos] += 1
            count += 1
            if pos < 0 or pos >= len(data):
                return count

    def calc_2(self, data: [str]) -> int:
        pos = 0
        count = 0
        while True:
            old_pos = pos
            jump = data[pos]
            pos += jump
            if jump >= 3:
                data[old_pos] -= 1
            else:
                data[old_pos] += 1
            count += 1
            if pos < 0 or pos >= len(data):
                return count

    def load_handler_part1(self, data: [str]) -> [str]:
       return [int(x) for x in data]

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201705()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
