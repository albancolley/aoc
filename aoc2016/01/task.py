"""
AOC Day X
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math
from dataclasses import dataclass
from turtle import *

@dataclass
class Sequence:
    turn: str
    blocks: int

directions = {
    1 + 0j: [0 - 1j, 0 + 1j],
    -1 + 0j: [0 + 1j, 0 - 1j],
    0 + 1j: [1 + 0j, -1 + 0j],
    0 - 1j: [-1 + 0j, 1 + 0j],
}

class Aoc201600(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: [Sequence]) -> int:
        pos = 0 + 0j
        direction = 0 + 1j
        sequence: Sequence
        for sequence in data:
            index:int = 0
            if sequence.turn == 'R':
                index = 1
            direction = directions[direction][index]
            pos += direction * sequence.blocks

        return int(abs(pos.real) + abs(pos.imag))

    def calc_2(self, data: [str]) -> int:

        # color('blue')
        # for sequence in data:
        #     if sequence.turn == 'R':
        #         right(90)
        #     else:
        #         left(90)
        #     for i in range(0, sequence.blocks):
        #         forward(1)
        #         print(position())
        # mainloop()
        # return 0

        x_y = 0 + 0j
        seen = [x_y]
        direction = 1 + 0j
        sequence: Sequence
        found = False
        for sequence in data:
            index:int = 1
            if sequence.turn == 'R':
                index = 0
            direction = directions[direction][index]
            for i in range(0, sequence.blocks):
                x_y += direction
                if x_y in seen:
                    found = True
                    break
                seen.append(x_y)
            if found:
                break

        return int(abs(x_y.real) + abs(x_y.imag))

    def load_handler_part1(self, data: [str]) -> [Sequence]:
        sequences: [Sequence] = []
        for step in data[0].split(', '):
            sequence = Sequence(step[0], int(step[1:]))
            sequences.append(sequence)
        return sequences

    def load_handler_part2(self, data: [str]) -> [Sequence]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201600()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
