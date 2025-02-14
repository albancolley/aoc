"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure


class Aoc201711(AocBase):
    """
    AOC Day 10 Class
    """



    moves= {
        "n": (1, 0 , -1),
        "ne": (0, 1 , -1),
        "se": (-1, 1 , 0),
        "s": (-1, 0 , 1),
        "sw": (0, -1 , 1),
        "nw": (1, -1 ,0)
    }

    def calc_1(self, data: [str]) -> int:
        # see https://www.redblobgames.com/grids/hexagons/
        pos = (0,0,0)
        for step in data:
            move = self.moves[step]
            pos = (pos[0] + move[0], pos[1] + move[1], pos[2] + move[2])

        result = int((abs(pos[0]) + abs(pos[1]) + abs(pos[2])) / 2)

        return result

    def calc_2(self, data: [str]) -> int:
        result = 0
        pos = (0, 0, 0)
        for step in data:
            move = self.moves[step]
            pos = (pos[0] + move[0], pos[1] + move[1], pos[2] + move[2])

            result = max(result, int((abs(pos[0]) + abs(pos[1]) + abs(pos[2])) / 2))

        return result
    def load_handler_part1(self, data: [str]) -> [str]:
        return data[0].split(",")

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201711()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
