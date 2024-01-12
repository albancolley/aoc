from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import logging
import re


logger = logging.getLogger("ACO2023-1")

class Aoc202301(AocBase):


    def calc_1(self, data: dict) -> int:
        total = 0
        for card in data:
            c = data[card]
            count = -1
            for w in c['winners']:
                if w in c['numbers']:
                    count += 1
            if count > -1:
                total +=  2**count
        return total

    def calc_2(self, data: [str]) -> int:
        winning_cards = [0] * len(data)
        total = 0
        for card in data:
            winning_cards[card-1] += 1
            c = data[card]
            count = 0
            for w in c['winners']:
                if w in c['numbers']:
                    count += 1
            if count > 0:
                for i in range(card, card + count):
                    winning_cards[i] += winning_cards[card-1]
        total = sum(winning_cards)
        return total

    def load_handler_part1(self, data: [str]) -> [str]:

        result = {}
        for row in data:
            d = row.split(":")
            card  = int(d[0][4:])
            d2 = d[1].strip().split("|")
            winners = d2[0].strip().split(" ")
            numbers = d2[1].strip().split(" ")
            winners = [int(w) for w in winners if w]
            numbers = [int(w) for w in numbers if w]
            result[card] = {
                'winners': winners,
                'numbers': numbers
            }
        return result

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc202301()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        exit(1)
