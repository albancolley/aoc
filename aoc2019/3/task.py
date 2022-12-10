from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
from dataclasses import dataclass

logger = logging.getLogger("ACO2019-2")

class Aoc201903(AocBase):

    directions = {
        "D": (0, -1),
        "U": (0, 1),
        "L": (-1, 0),
        "R": (1, 0),
    }

    def calc_1(self, data: [str]) -> int:
        map = {}
        last_item = data[0][0]
        map["0,0"] = 'o'
        distances = []
        x = 0
        y = 0
        for item in data[0]:
            dx, dy = self.directions[item[0]]
            for i in range(0, int(item[1:])):
                x += dx
                y += dy
                map[f'{x},{y}'] = '1'
        x = 0
        y = 0
        for item in data[1]:
            dx, dy = self.directions[item[0]]
            for i in range(0, int(item[1:])):
                x += dx
                y += dy
                if f'{x},{y}' in map:
                    distances.append(abs(x) + abs(y))
        distances.sort()
        return distances[0]


    def calc_2(self, data: [str]) -> int:
        map = {}
        last_item = data[0][0]
        map["0,0"] = 'o'
        distances = []
        x = 0
        y = 0
        distance = 0
        for item in data[0]:
            dx, dy = self.directions[item[0]]
            for i in range(0, int(item[1:])):
                distance += 1
                x += dx
                y += dy
                map[f'{x},{y}'] = distance
        x = 0
        y = 0
        distance = 0
        for item in data[1]:
            dx, dy = self.directions[item[0]]
            for i in range(0, int(item[1:])):
                distance += 1
                x += dx
                y += dy
                if f'{x},{y}' in map:
                    distances.append(map[f'{x},{y}'] + distance)
        distances.sort()
        return distances[0]

    def load_handler_part1(self, data: [str]) -> [str]:
        return [[item for item in data[0].split(",")], [item for item in data[1].split(",")]]

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201903()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        exit(1)
