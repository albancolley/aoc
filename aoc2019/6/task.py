from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
from dataclasses import dataclass

logger = logging.getLogger("ACO2019-6")





class Aoc201906(AocBase):

    def __init__(self):
        pass

    def calc_1(self, data: {}) -> int:
        count = 0
        for item in data:
            count += self.count_orbits(data, item)
        return count

    def calc_2(self, data: [str]) -> int:
        you_path = []
        planet = "YOU"
        while planet != "COM":
            planet = data[planet]
            you_path.append(planet)
        san_path = []
        planet = "SAN"
        while planet != "COM":
            planet = data[planet]
            san_path.append(planet)
        length = - 1
        for planet in you_path:
            length += 1
            if planet in san_path:
                break
        length += san_path.index(planet)
        return length

    def load_handler_part1(self, data: [str]) -> [[str]]:
        result = {}
        for item in data:
            parts = item.split(')')
            result[parts[1]] = parts[0]
        return result

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)

    def count_orbits(self, data, start: str):
        planet = start
        count = 0
        while planet != "COM":
            count += 1
            planet = data[planet]
        return count


if __name__ == '__main__':
    configure()
    aoc = Aoc201906()
    failed, results = aoc.run("part1_[0-9].txt", "part2_[0-9]+.txt")
    if failed:
        exit(1)
