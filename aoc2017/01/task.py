"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure


class Aoc201701(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: [str]) -> int:
        result = 0
        captcha = data[0] + data[0][0]
        for i in range(len(captcha)-1):
            if captcha[i] == captcha[i+1]:
                result += int(captcha[i])
        return result

    def calc_2(self, data: [str]) -> int:
        result = 0
        captcha = data[0]
        half_len = int(len(captcha) / 2)
        for i in range(len(captcha)):
            if captcha[i] == captcha[(i+half_len) % len(captcha)]:
                result += int(captcha[i])
        return result

    def load_handler_part1(self, data: [str]) -> [str]:
       return data

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201701()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
