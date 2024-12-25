"""
AOC Day X
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math

class Aoc201719(AocBase):
    """
    AOC Day 10 Class
    """

    moves = {
        'D': 0 + 1j,
        'U': 0 - 1j,
        'L': -1 + 0j,
        'R': 1 + 0j
    }

    def calc_1(self, grid: list[str]) -> str:
        pos = grid[0].index('|') + 0j
        direction = 'D'
        visited = ""
        while True:
            pos += self.moves[direction]
            value:str = grid[int(pos.imag)][int(pos.real)]
            if value == ' ':
                return visited
            if value.isalpha():
                visited += value
                continue
            elif value == '+':
                if direction in ['D', 'U']:
                    new_pos = pos + self.moves['L']
                    value: str = grid[int(new_pos.imag)][int(new_pos.real)]
                    if value.isalpha() or value == '-':
                        direction = 'L'
                        continue
                    new_pos = pos + self.moves['R']
                    value: str = grid[int(new_pos.imag)][int(new_pos.real)]
                    if value.isalpha() or value == '-':
                        direction = 'R'
                        continue
                elif direction in ['L', 'R']:
                    new_pos = pos + self.moves['U']
                    value: str = grid[int(new_pos.imag)][int(new_pos.real)]
                    if value.isalpha() or value == '|':
                        direction = 'U'
                        continue
                    new_pos = pos + self.moves['D']
                    value: str = grid[int(new_pos.imag)][int(new_pos.real)]
                    if value.isalpha() or value == '|':
                        direction = 'D'
                        continue


        return visited

    def calc_2(self, grid: [str]) -> int:
        pos = grid[0].index('|') + 0j
        direction = 'D'
        visited = 0
        while True:
            visited += 1
            pos += self.moves[direction]
            value:str = grid[int(pos.imag)][int(pos.real)]
            if value == ' ':
                return visited
            # if value.isalpha():
            #     visited += value
            #     continue
            elif value == '+':
                if direction in ['D', 'U']:
                    new_pos = pos + self.moves['L']
                    value: str = grid[int(new_pos.imag)][int(new_pos.real)]
                    if value.isalpha() or value == '-':
                        direction = 'L'
                        continue
                    new_pos = pos + self.moves['R']
                    value: str = grid[int(new_pos.imag)][int(new_pos.real)]
                    if value.isalpha() or value == '-':
                        direction = 'R'
                        continue
                elif direction in ['L', 'R']:
                    new_pos = pos + self.moves['U']
                    value: str = grid[int(new_pos.imag)][int(new_pos.real)]
                    if value.isalpha() or value == '|':
                        direction = 'U'
                        continue
                    new_pos = pos + self.moves['D']
                    value: str = grid[int(new_pos.imag)][int(new_pos.real)]
                    if value.isalpha() or value == '|':
                        direction = 'D'
                        continue


        return visited

    def load_handler_part1(self, data: [str]) -> [str]:
        width = 0
        height = 0
        for row in data:
            width = max(width, len(row))
            if len(row.strip()) > 0:
                height += 1
        grid = []
        for row in data:
            spaces = ' ' * (width + 1 - len(row))
            grid.append(row + spaces)
        grid.append('' * (width + 1))
        return grid

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201719()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
