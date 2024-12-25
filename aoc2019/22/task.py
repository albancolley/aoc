import dataclasses

from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
from dataclasses import dataclass, field
from collections import defaultdict
import math
from collections import deque
import copy
import numpy as np

logger = logging.getLogger("ACO2019-22")



class Aoc201922(AocBase):

    def calc_1(self, data) -> int:
        size, steps = data
        cards = [x for x in range(0, size)]
        new_cards = []
        for mode, value in steps:
            match mode:
                case 'NS':
                    new_cards = cards[::-1]
                case 'C':
                    if value > 0:
                        new_cards = cards[value:] + cards[0:value]
                        print(mode, value)
                    if value < 0:
                        new_cards = cards[value:] + cards[0:len(cards)+value]
                        print(mode,value)
                case 'I':
                    start = 0
                    new_cards = [0] * size
                    for i in range(0, size):
                        new_cards[start] = cards[i]
                        start = (start + value) % size
            cards = new_cards
        if len(cards) == 10:
            result = ' '.join([str(x) for x in cards])
        else:
            pos = 0
            print(len(cards))

            for card in cards:
                if cards[card] == 2019:
                    result = card
                pos += 1
        return result

    def calc_2(self, data) -> int:
        size, repeats, steps = data
        cards = [x for x in range(0, size)]
        new_cards = []
        for mode, value in steps:
            match mode:
                case 'NS':
                    new_cards = cards[::-1]
                case 'C':
                    if value > 0:
                        new_cards = cards[value:] + cards[0:value]
                        print(mode, value)
                    if value < 0:
                        new_cards = cards[value:] + cards[0:len(cards)+value]
                        print(mode,value)
                case 'I':
                    start = 0
                    new_cards = [0] * size
                    for i in range(0, size):
                        new_cards[start] = cards[i]
                        start = (start + value) % size
            cards = new_cards
        if len(cards) == 10:
            result = ' '.join([str(x) for x in cards])
        else:
            pos = 0
            print(len(cards))

            for card in cards:
                if cards[card] == 2019:
                    result = card
                pos += 1
        return result

    def load_handler_part1(self, data: [str]) -> [str]:
        values = []
        size = int(data[0])
        steps = []
        for line in data[1:]:
            if line == "deal into new stack":
                steps.append(('NS', 0))
            elif line.startswith("cut"):
                cards = int(line.split(' ')[-1])
                steps.append(('C', cards))
            else:
                cards = int(line.split(' ')[-1])
                steps.append(('I', cards))
        return size, steps


    def load_handler_part2(self, data: [str]) -> [str]:
        values = []
        size = int(data[0])
        repeats = int(data[1])
        steps = []
        for line in data[2:]:
            if line == "deal into new stack":
                steps.append(('NS', 0))
            elif line.startswith("cut"):
                cards = int(line.split(' ')[-1])
                steps.append(('C', cards))
            else:
                cards = int(line.split(' ')[-1])
                steps.append(('I', cards))
        return size, repeats, steps


if __name__ == '__main__':
    configure()
    aoc = Aoc201922()
    failed, results = aoc.run("part1x_[5-5]*.txt", "part2_[1-9]+.txt")
    if failed:
        exit(1)
