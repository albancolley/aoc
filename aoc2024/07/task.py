"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure


class Aoc202407(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict) -> int:
        result = []
        for s in data:
            total = s[0]
            values = s[1]
            possibles = [values[0]]
            for v in values[1:]:
                new_possibles = []
                for p in possibles:
                    new_possibles.append(p*v)
                    new_possibles.append(p + v)
                possibles = new_possibles
            if total in possibles:
                result += [total]

        return sum(result)

    def calc_2(self, data: [str]) -> int:
        result = []
        for s in data:
            total = s[0]
            values = s[1]
            possibles = [values[0]]
            for v in values[1:]:
                new_possibles = []
                for p in possibles:
                    added = p + v
                    multiply = p * v
                    concatenate = int(str(p) + str(v))
                    if added <= total:
                        new_possibles.append(added)
                    if multiply <= total:
                        new_possibles.append(multiply)
                    if concatenate <= total:
                        new_possibles.append(concatenate)
                possibles = new_possibles
                if len(possibles) == 0:
                    break
            if total in possibles:
                result += [total]
                continue
        return sum(result)

    def load_handler_part1(self, data: [str]) -> [str]:
        sums = []
        for d in data:
            a = d.split(': ')
            sums.append((int(a[0]), [int(v) for v in a[1].split(' ')]))
        return sums

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc202407()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
