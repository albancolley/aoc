from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging

logger = logging.getLogger("ACO2022-1")


class Aoc201901(AocBase):

    def calc_1(self, data: [str]) -> int:
        total = 0
        for item in data:
            total += int(item / 3) - 2
        return total

    def calc_2(self, data: [str]) -> int:
        total = 0
        for item in data:
            fuel = int(item / 3) - 2
            while fuel > 0:
                total += fuel
                fuel = int(fuel / 3) - 2
        return total

        return total

    def load_handler_part1(self, data: [str]) -> [str]:
        new_data = []
        for item in data:
            new_data.append(int(item))
        return new_data

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201901()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        exit(1)
