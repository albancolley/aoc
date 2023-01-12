import dataclasses

from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
from dataclasses import dataclass, field
from collections import defaultdict
import math
from collections import deque
import copy

logger = logging.getLogger("ACO2019-16")



class Aoc201916(AocBase):

    def calc_1(self, data) -> int:
        cycle = [0, 1, 0, -1]

        values = data
        for r in range(0, 100):
            result = []
            index = 0
            for i in range(0, len(values)):
                next_value = 0
                step = 0
                for j, value in enumerate(values):
                    if step == i:
                        index = (index + 1) % 4
                        step = 0
                    else:
                        step += 1
                    next_value += value * cycle[index]

                result.append(int(str(next_value)[-1]))
                index = 0
            values = result
        return ''.join([str(x) for x in result])[0:8]


    def calc_2(self, data) -> int:
        return 0

    def load_handler_part1(self, data: [str]) -> [str]:
        return [int(c) for c in data[0]]



    def load_handler_part1s(self, data: [str]) -> [str]:
        factories: {} = {}
        ores: {} = {}
        for line in data:
            a = line.split(' => ')
            b = a[0].split(', ')
            ingredients = []
            f = a[1].split(' ')
            f_number = int(f[0])
            f_name = f[1]
            for c in b:
                d = c.split(' ')
                ingredients_name = d[1]
                ingredients_number = int(d[0])
                ingredients.append((ingredients_number, ingredients_name))
                if ingredients_name == 'ORE':
                    ores[f_name] = (ingredients_number, f_number)
            factories[f_name] = ((f_number, f_name), ingredients)

        return factories, ores

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201916()
    failed, results = aoc.run("part1_[0-9]*.txt", "part2x_[0-9]+.txt")
    if failed:
        exit(1)
