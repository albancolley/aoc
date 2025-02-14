"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure


class Aoc201715(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: tuple) -> int:
        gen_a , gen_b = data
        count = 1
        matches = 0
        while True:
            gen_a = (16807 * gen_a) % 2147483647
            gen_b = (48271 * gen_b) % 2147483647
            if gen_a & 0xffff == gen_b & 0xffff:
                matches += 1
            if count == 40000000:
                break
            count += 1
        return matches

    def calc_2(self, data: tuple) -> int:
        gen_a , gen_b = data
        count = 1
        matches = 0
        while True:
            gen_a = (16807 * gen_a) % 2147483647
            while gen_a % 4 != 0:
                gen_a = (16807 * gen_a) % 2147483647
            gen_b = (48271 * gen_b) % 2147483647
            while gen_b % 8 != 0:
                gen_b = (48271 * gen_b) % 2147483647
            if gen_a & 0xffff == gen_b & 0xffff:
                matches += 1
            if count == 5000000:
                break
            count += 1
        return matches

    def load_handler_part1(self, data: [str]) -> [str]:
        return int(data[0].split()[-1]),  int(data[1].split()[-1])

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201715()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
