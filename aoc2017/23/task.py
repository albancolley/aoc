"""
AOC Day X
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math


class Aoc201718(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: [str]) -> int:
        regs = collections.defaultdict(int)
        pos = 0
        mul = 0
        while True:
            if pos < 0 or pos >= len(data):
                break

            cmd = data[pos]
            reg_1 = cmd[1]
            value_1 = self.get_value(cmd[1], regs)
            value_2 = self.get_value(cmd[2], regs) if len(cmd) > 2 else 0
            match cmd[0]:
                case 'set':
                    regs[reg_1] = value_2
                case 'sub':
                    regs[reg_1] -= value_2
                case 'mul':
                    mul += 1
                    regs[reg_1] *= value_2
                case 'jnz':
                    if value_1 != 0:
                        pos += value_2
                        continue
            pos += 1

        return mul

    def get_value(self, reg:str, regs):
        if not reg.isalpha():
            return int(reg)
        else:
            return regs[reg]

    def prime(self, a):
        return not (a < 2 or any(a % x == 0 for x in range(2, int(a ** 0.5) + 1)))

    def calc_2(self, data: [str]) -> int:

        # count non primes between b and c in steps of 17.
        b = 65
        c = 65
        h = 0
        a = 1
        if a == 1:
            b *= 100
            b += 100000
            c = b
            c += 17000
        while True:
            if not self.prime(b):
                h += 1
            b = b + 17
            if b > c:
                return h

    def load_handler_part1(self, data: [str]) -> [str]:
        return [x.split() for x in data]

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)




if __name__ == '__main__':
    configure()
    aoc = Aoc201718()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
