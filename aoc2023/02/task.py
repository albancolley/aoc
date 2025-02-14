from common import AocBase
from common import configure
import logging
import re


logger = logging.getLogger("ACO2023-1")

class Aoc202302(AocBase):

    def calc_1(self, data: dict) -> int:
        limits = {
            'red' : 12,
            'green': 13,
            'blue': 14,
        }
        total = 0
        for item in data:
            to_big = False
            for s in data[item]:
                for l in s:
                    if s[l] > limits[l]:
                        to_big = True
                        break
            if not to_big:
                total += item
        return total

    def calc_2(self, data: [str]) -> int:
        total = 0
        for item in data:
            maxes = {
                'red': 0,
                'green': 0,
                'blue': 0,
            }
            for s in data[item]:
                for l in s:
                    maxes[l] = max(maxes[l], s[l])
            power = maxes['red'] * maxes['green'] * maxes['blue']
            total += power
        return total

        return total

    def load_handler_part1(self, data: [str]) -> [str]:

        p = re.compile(r'Game (\d+): (.*)')
        p2 = re.compile(r'(\d+) (\w+)')
        games = {}
        for row in data:
            m = re.match(p, row)
            set_count = 0
            sets_data = m.group(2).split(";")
            sets = []
            for s in sets_data:
                colours = {}
                for (number, colour) in re.findall(p2, s):
                    if colour in colours:
                        colours[colour] += int(number)
                    else:
                        colours[colour] = int(number)
                sets.append(colours)
            games[int(m.group(1))] = sets
            colours = {}
        return games

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc202302()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        exit(1)
