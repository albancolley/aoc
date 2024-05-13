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



    def bfs(self, start_pos, start_passcode):
        steps = [(start_pos, start_passcode)]
        while len(steps) > 0:
            pos, passcode = steps.pop(0)
            if pos == (3,3):
                return passcode[len(start_passcode):]
            md5 = hashlib.md5(passcode.encode()).hexdigest()
            if pos[1] > 0 and md5[0] in self.OPEN:
                steps.append(((pos[0], pos[1] - 1), passcode + 'U'))
            if pos[1] < 3 and md5[1] in self.OPEN:
                steps.append(((pos[0], pos[1] + 1), passcode + 'D'))
            if pos[0] > 0 and md5[2] in self.OPEN:
                steps.append(((pos[0] - 1, pos[1]), passcode + 'L'))
            if pos[0] < 3 and md5[3] in self.OPEN:
                steps.append(((pos[0] + 1, pos[1]), passcode + 'R'))
        return ""
    def calc_1(self, data: dict) -> int:
        self.OPEN = ['b','c','d','e','f']
        start_value = data[0]
        pos = (0,0)
        return self.bfs(pos, start_value)

    def bfs_longest(self, start_pos, start_passcode):
        steps = [(start_pos, start_passcode)]
        longest = 0
        while len(steps) > 0:
            pos, passcode = steps.pop(0)
            if pos == (3,3):
                longest = max(len(passcode) - len(start_passcode), longest)
                continue
            md5 = hashlib.md5(passcode.encode()).hexdigest()
            if pos[1] > 0 and md5[0] in self.OPEN:
                steps.append(((pos[0], pos[1] - 1), passcode + 'U'))
            if pos[1] < 3 and md5[1] in self.OPEN:
                steps.append(((pos[0], pos[1] + 1), passcode + 'D'))
            if pos[0] > 0 and md5[2] in self.OPEN:
                steps.append(((pos[0] - 1, pos[1]), passcode + 'L'))
            if pos[0] < 3 and md5[3] in self.OPEN:
                steps.append(((pos[0] + 1, pos[1]), passcode + 'R'))
        return longest
    def calc_2(self, data: [str]) -> int:
        self.OPEN = ['b','c','d','e','f']
        start_value = data[0]
        pos = (0,0)
        return self.bfs_longest(pos, start_value)

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
