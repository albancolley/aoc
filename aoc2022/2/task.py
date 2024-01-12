from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging

logger = logging.getLogger("ACO2022-2")


class Aoc202201(AocBase):

    def calc_1(self, data: [str]) -> int:
        score = 0
        scoring = {
            "A X": 4,
            "A Y": 8,
            "A 99": 3,
            "B X": 1,
            "B Y": 5,
            "B 99": 9,
            "C X": 7,
            "C Y": 2,
            "C 99": 6,
        }
        for item in data:
            score += scoring[item]
        return score

    def calc_2(self, data: [str]) -> int:
        score = 0
        scoring = {
            "A X": 3,
            "A Y": 4,
            "A 99": 8,
            "B X": 1,
            "B Y": 5,
            "B 99": 9,
            "C X": 2,
            "C Y": 6,
            "C 99": 7,
        }
        for item in data:
            score += scoring[item]
        return score

    def load_handler_part1(self, data: [str]) -> [str]:
        return data

    def load_handler_part2(self, data: [str]) -> [str]:
        return data


if __name__ == '__main__':
    configure()
    aoc = Aoc202201()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        exit(1)
