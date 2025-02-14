"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure


class Aoc201600(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict) -> int:
        last = data[0]
        rows = int(data[1])
        safe = 0
        while True:
            if rows == 0:
                break
            rows -= 1
            next = ""
            for c in last:
                if c == '.':
                    safe += 1

            temp = ('.' + last + '.')
            for i in range(len(last)):
                test = temp[i:i+3]
                if test in ['^^.', '.^^', '^..', '..^']:
                    next += '^'
                else:
                    next += '.'
            last = next

        return safe

    def calc_2(self, data: [str]) -> int:
        return self.calc_1(data)

    def load_handler_part1(self, data: [str]) -> [str]:
       return data

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201600()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
