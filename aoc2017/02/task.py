"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure


class Aoc201702(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: [[int]]) -> int:
        result = 0
        for r in data:
            result += max(r) - min(r)
        return result

    def calc_2(self, data: [[int]]) -> int:
        result = 0
        for r in data:
            found = False
            for i in range(len(r)):
                if found:
                    break
                for j in range(len(r)):
                    if i != j:
                        if r[i] / r[j] == int(r[i] / r[j]):
                            result += int(r[i] / r[j])
                            found = True
                            break
        return result

    def load_handler_part1(self, data: [[int]]) -> [str]:
        new_data = []
        for r in data:
            new_data.append([int(x) for x in r.split()])
        return new_data

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201702()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
