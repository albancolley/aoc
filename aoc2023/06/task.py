"""
AOC Day 6
"""
import sys
from common import AocBase
from common import configure


class Aoc202306(AocBase):
    """
    AOC Day 6 Class
    """

    def calc_1(self, data: dict) -> int:
        total = 1
        for race in data:
            time = race[0]
            distance = race[1]
            wins = 0
            for i in range(0, time):
                my_distance = i*(time - i)
                if my_distance > distance:
                    wins += 1
            total = total * wins
        return total

    def calc_2(self, data: [str]) -> int:
        time, distance = data
        middle = time // 2

        jump_size = middle // 2
        pos = middle
        while True:
            my_distance = pos * (time - pos)
            if my_distance > distance:
                pos = pos - jump_size
            else:
                pos = pos + jump_size
            jump_size = jump_size // 2
            if jump_size == 0:
                break
        start = pos
        if start * (time - start) <= distance:
            start += 1

        jump_size = middle // 2
        pos = middle
        while True:
            my_distance = pos * (time - pos)
            if my_distance > distance:
                pos = pos + jump_size
            else:
                pos = pos - jump_size
            jump_size = jump_size // 2
            if jump_size == 0:
                break
        end = pos
        if end * (time - start) <= distance:
            end += 1
        return end - start

    def load_handler_part1(self, data: [str]) -> [str]:

        times = [int(x) for x in data[0].split(':')[1].strip().split(' ') if x]
        distance = [int(x) for x in data[1].split(':')[1].strip().split(' ') if x]
        races = list(zip(times, distance))
        return races

    def load_handler_part2(self, data: [str]) -> [str]:
        time = int(data[0].split(':')[1].replace(' ',''))
        distance = int(data[1].split(':')[1].replace(' ',''))
        return time, distance


if __name__ == '__main__':
    configure()
    aoc = Aoc202306()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
