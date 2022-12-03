from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging

logger = logging.getLogger("ACO2022-3")


class Aoc202201(AocBase):

    def calc_1(self, data: [str]) -> int:
        total: int = 0
        for item in data:
            left = item[0:int(len(item) / 2)]
            right = item[int(len(item) / 2):]
            dup: str = set.intersection(set(left), set(right)).pop()
            if dup.islower():
                total += ord(dup) - ord('a') + 1
            else:
                total += ord(dup) - ord('A') + 27
        return total

    def calc_2(self, data: [str]) -> int:
        total: int = 0
        for index in range(0, len(data), 3):
            first_set = set(data[index])
            second_set = set(data[index + 1])
            third_set = set(data[index + 2])

            dup: str = set.intersection(first_set, second_set, third_set).pop()
            if dup.islower():
                total += ord(dup) - ord('a') + 1
            else:
                total += ord(dup) - ord('A') + 27
        return total

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
