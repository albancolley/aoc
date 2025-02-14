"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure


class Aoc201703(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: int) -> int:
        if data == 1:
            return 0
        start = 3
        while True:
            if data <= start**2:
                height = int(start / 2)
                left = data - (start-2)**2
                pos = left % (start -1)
                mid = int(start / 2)
                width2 = abs(pos - mid)
                return height + width2
            start += 2

    def calc_2(self, data: [str]) -> int:
        spiral = {"0-0": 1}
        side_length= 3
        x = 0
        y = 0
        while True:
            y += 1
            for i in range(side_length-1):
                self.calc_value(spiral, x, y)

                if spiral[f"{x}-{y}"] > data:
                    return spiral[f"{x}-{y}"]
                x += 1

            x -= 1
            for i in range(side_length-1):
                y -= 1
                self.calc_value(spiral, x, y)

                if spiral[f"{x}-{y}"] > data:
                    return spiral[f"{x}-{y}"]

            for i in range(side_length-1):
                x -= 1
                self.calc_value(spiral, x, y)

                if spiral[f"{x}-{y}"] > data:
                    return spiral[f"{x}-{y}"]

            for i in range(side_length-1):
                y += 1
                self.calc_value(spiral, x, y)

                if spiral[f"{x}-{y}"] > data:
                    return spiral[f"{x}-{y}"]

            side_length += 2

    def calc_value(self, sprial, x, y):
        sprial[f"{x}-{y}"] = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                if f"{x + dx}-{y + dy}" in sprial:
                    sprial[f"{x}-{y}"] += sprial[f"{x + dx}-{y + dy}"]

    def load_handler_part1(self, data: [str]) -> int:
       return int(data[0])

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201703()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
