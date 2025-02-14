"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure


class Aoc201601(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict) -> str:
        result = ""
        keypad = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        moves = {
            'U': 0 - 1j,
            'D': 0 + 1j,
            'L': -1,
            'R': 1
        }
        pos = 1 + 1j
        for line in data:
            for move in line:
                new_pos = pos + moves[move]
                if 0 <= new_pos.real <= 2 and 0 <= new_pos.imag <= 2:
                    pos = new_pos
            result += str(keypad[int(pos.imag)][int(pos.real)])
        return result

    def calc_2(self, data: [str]) -> str:
        result = ""
        keypad = [
            ['0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '1', '0', '0', '0'],
            ['0', '0', '2', '3', '4', '0', '0'],
            ['0', '5', '6', '7', '8', '9', '0'],
            ['0', '0', 'A', 'B', 'C', '0', '0'],
            ['0', '0', '0', 'D', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0']
        ]
        moves = {
            'U': 0 - 1j,
            'D': 0 + 1j,
            'L': -1,
            'R': 1
        }
        pos = 1 + 3j
        for line in data:
            for move in line:
                new_pos = pos + moves[move]
                value = str(keypad[int(new_pos.imag)][int(new_pos.real)])
                if value != '0':
                    pos = new_pos
            result += str(keypad[int(pos.imag)][int(pos.real)])
        return result

    def load_handler_part1(self, data: [str]) -> [str]:
       return data

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201601()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
