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
        for mode, value in steps:
            match mode:
                case 'NS':
                    new_cards = cards[::-1]
                case 'C':
                    if value > 0:
                        new_cards = cards[value:] + cards[0:value]
                    else:
                        new_cards = cards[value:] + cards[0:len(cards)+value]
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
            result = cards[2019-1]
        return result

    def calc_2(self, data) -> int:

        return 0

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
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201922()
    failed, results = aoc.run("part1_[5-5]*.txt", "part2x_[1-4]+.txt")
    if failed:
        exit(1)
