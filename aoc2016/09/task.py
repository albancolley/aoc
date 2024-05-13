"""
AOC Day X
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math

class Aoc201600(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict) -> int:
        length = 0
        d = data[0]
        pos = 0
        while True:
            # print(pos, d[pos])
            if d[pos] == '(':
                start_pos = pos
                while d[pos] != ')':
                    pos += 1
                marker = d[start_pos+1: pos].split("x")
                characters = int(marker[0])
                repeats = int(marker[1])
                pos += characters + 1
                length += characters * repeats
            else:
                length += 1
                pos += 1
            if pos > len(d)-1:
                break

        return length


    def bfs(self, data):


        if '(' not in data:
            return len(data)
        l = 0
        pos = 0
        while data[pos] != '(':
            l += 1
            pos += 1

        start_pos = pos
        while data[pos] != ')':
            pos += 1
        marker = data[start_pos + 1: pos].split("x")
        characters = int(marker[0])
        repeats = int(marker[1])

        l += self.bfs(data[pos+1: pos+1+ characters]) * repeats
        l += self.bfs(data[pos+1 + characters:])

        return l

    def calc_2(self, data: [str]) -> int:
        return self.bfs(data[0])

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
