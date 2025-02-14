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

    def calc_1(self, data: [str]) -> int:
        loops = int(data[0])
        start = data[1]
        for i in range(loops):
            # print(i)
            new_start = ""
            last = start[0]
            count = 0
            for c in start:
                count += 1
                if c != last:
                    new_start += str(count - 1)
                    new_start += last
                    count = 1
                last = c
            new_start += str(count)
            new_start += last
            start = new_start

        return len(start)

    def calc_2(self, data: [str]) -> int:
        loops = int(data[0])
        start = data[1]
        for i in range(loops):
            # print(i)
            new_start = ""
            last = start[0]
            count = 0
            for c in start:
                count += 1
                if c != last:
                    new_start += str(count - 1)
                    new_start += last
                    count = 1
                last = c
            new_start += str(count)
            new_start += last
            start = new_start

        return len(start)

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
