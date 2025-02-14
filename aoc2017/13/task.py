"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure


class Aoc201713(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict[int,int]) -> int:
        length = max(data.keys())
        score = 0
        for i in range(length+1):
            if i in data:
                if i % (data[i]*2-2) == 0:
                    score += i * data[i]
        return score

    def calc_2(self, data: [str]) -> int:
        length = max(data.keys())
        delay = 0
        while True:
            score = 0
            for i in range(length + 1):
                if i in data:
                    if (i+delay) % (data[i] * 2 - 2) == 0:
                        score = 1
                        break
            if score == 0:
                break
            delay += 1
        return delay
    def load_handler_part1(self, data: [str]) -> dict[int,int]:
        d : str
        firewall = {}
        for d in data:
            v = d.split(': ')
            firewall[int(v[0])] = int(v[1])
        return firewall

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201713()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
