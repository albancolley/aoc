from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import logging

logger = logging.getLogger("ACO2023-1")

digits = { '1': 1,
               '2':2,
               '3':3,
               '4':4,
               '5':5,
               '6':6,
               '7': 7,
               '8': 8,
               '9' : 9
               }

word_digits = {'one': 1, '1': 1,
               'two': 2, '2':2,
               'three': 3, '3':3,
               'four': 4, '4':4,
               'five': 5, '5':5,
               'six': 6, '6':6,
               'seven': 7, '7': 7,
               'eight': 8, '8': 8,
               'nine': 9, '9' : 9
               }


class Aoc202301(AocBase):

    def calc_1(self, data: [str]) -> int:
        total = 0
        for item in data:
            value = 0
            for i in range(len(item)):
                if item[i] in digits:
                    value += 10 * digits[item[i]]
                    break
            for i in range(len(item) - 1, -1, -1):
                if item[i] in digits:
                    value += digits[item[i]]
                    break
            total += value

        return total

    def calc_2(self, data: [str]) -> int:
        total = 0
        for item in data:
            value = 0
            found = False
            for i in range(len(item)):
                for k in word_digits:
                    if item[i:].startswith(k):
                        value += 10 * word_digits[k]
                        found = True
                        break
                if found:
                    break

            found = False
            for i in range(len(item) - 1, -1, -1):
                for k in word_digits:
                    if item[i:].startswith(k):
                        value += 1 * word_digits[k]
                        found = True
                        break
                if found:
                    break

            total += value

        return total

    def load_handler_part1(self, data: [str]) -> [str]:
        return data

    def load_handler_part2(self, data: [str]) -> [str]:
        return data


if __name__ == '__main__':
    configure()
    aoc = Aoc202301()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        exit(1)
