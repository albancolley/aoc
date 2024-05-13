"""
AOC Day X
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math
import hashlib

class Aoc201600(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict) -> str:
        d: str
        code = ""
        count = 0
        for d in data:
            index = 1
            while True:
                value = d + str(index)
                ms5 = hashlib.md5(value.encode())
                if ms5.hexdigest()[0:5] == "00000":
                    # print(index, value)
                    code += ms5.hexdigest()[5]
                    count += 1
                    if count == 8:
                        break
                index += 1
        return code

    def calc_2(self, data: [str]) -> str:
        d: str
        code = ['X'] * 8
        count = 0
        for d in data:
            index = 1
            while True:
                value = d + str(index)
                ms5 = hashlib.md5(value.encode())
                if ms5.hexdigest()[0:5] == "00000":
                    # print(index, value)
                    pos = ms5.hexdigest()[5]
                    c = ms5.hexdigest()[6]
                    if pos in ['0','1','2','3','4','5','6','7']:
                        if code[int(pos)] == 'X':
                            code[int(pos)] = c[0]
                            print(code)
                            count += 1
                            if count == 8:
                                break
                index += 1
        return "".join(code)

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
