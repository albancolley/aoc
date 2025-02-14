"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure
import re


class Aoc201600(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, aunts: dict) -> int:
        gift_ant = {"children": 3,
                    "cats": 7,
                    "samoyeds": 2,
                    "pomeranians": 3,
                    "akitas": 0,
                    "vizslas": 0,
                    "goldfish": 5,
                    "trees": 3,
                    "cars": 2,
                    "perfumes": 1}

        result = 0
        for aunt in aunts:
            aunt_things = aunts[aunt]
            found = 0
            for gift in gift_ant:
                if gift in aunt_things and aunt_things[gift] == gift_ant[gift]:
                    found += 1
            if found == len(aunt_things):
                return aunt

        return 0

    def calc_2(self, aunts: dict) -> int:
        gift_ant = {"children": 3,
                    "cats": 7,
                    "samoyeds": 2,
                    "pomeranians": 3,
                    "akitas": 0,
                    "vizslas": 0,
                    "goldfish": 5,
                    "trees": 3,
                    "cars": 2,
                    "perfumes": 1}

        for aunt in aunts:
            aunt_things = aunts[aunt]
            found = 0
            for gift in gift_ant:
                if gift in aunt_things:
                    if gift in ['cats', 'trees']:
                        if aunt_things[gift] > gift_ant[gift]:
                            found += 1
                    elif gift in ['pomeranians', 'goldfish']:
                        if aunt_things[gift] < gift_ant[gift]:
                            found += 1
                    elif aunt_things[gift] == gift_ant[gift]:
                        found += 1

            if found == len(aunt_things):
                return aunt

        return 0

    def load_handler_part1(self, data: [str]) -> [str]:
        aunts = {}
        for d in data:
            num: int = int(re.findall(r'Sue (\d+):', d)[0])
            things = re.findall(r'(\w+): (\d+)', d)
            aunts[num] = {}
            for thing in things:
                aunts[num][thing[0]] = int(thing[1])
        # print(aunts)
        return aunts

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201600()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
