"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure


class Aoc201706(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: [int]) -> int:
        count = 0
        seen = {str(data): 1}

        while True:
            count += 1
            max_block = max(data)
            pos = 0
            for i in range(len(data)):
                if data[i] == max_block:
                    pos = i
                    break

            data[pos] = 0
            for i in range(max_block):
                data[(pos + i + 1) % len(data)] += 1

            if str(data) in seen:
                return count

            seen[str(data)] = 1


    def calc_2(self, data: [str]) -> int:
        seen = {str(data): 1}

        while True:
            max_block = max(data)
            pos = 0
            for i in range(len(data)):
                if data[i] == max_block:
                    pos = i
                    break

            data[pos] = 0
            for i in range(max_block):
                data[(pos + i + 1) % len(data)] += 1

            if str(data) in seen:
                break

            seen[str(data)] = 1

        target = str(data)
        count = 0
        while True:
            count += 1
            max_block = max(data)
            pos = 0
            for i in range(len(data)):
                if data[i] == max_block:
                    pos = i
                    break

            data[pos] = 0
            for i in range(max_block):
                data[(pos + i + 1) % len(data)] += 1

            if str(data) == target:
                return count

            seen[str(data)] = 1

    def load_handler_part1(self, data: [str]) -> [str]:
        return [int(d) for d in data[0].split()]

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201706()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
