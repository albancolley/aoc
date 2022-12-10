from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
from dataclasses import dataclass

logger = logging.getLogger("ACO2019-4")


class Aoc201904(AocBase):

    def calc_1(self, data: [str]) -> int:
        count = 0
        for i in range(data[0], data[1] + 1):
            v = str(i)
            last = v[0]
            ok = True
            dup = False
            for letter in v[1:]:
                if letter < last:
                    ok = False
                    break
                if letter == last:
                    dup = True
                last = letter
            if ok and dup:
                count +=1

        return count

    def calc_2(self, data: [str]) -> int:
        count = 0
        for i in range(data[0], data[1] + 1):
            v = str(i)
            last = v[0]
            ok = True
            dup = False
            counts = {}
            for i in range(0, 10):
                counts[str(i)] = 0
            counts[v[0]] = 1
            for letter in v[1:]:
                counts[letter] += 1
                if letter < last:
                    ok = False
                    break
                elif letter == last:
                    dup = True
                last = letter
            if ok and dup:
                ok = False
                for i in range(0, 10):
                    if counts[str(i)] == 2:
                        ok = True
                if ok:
                    count += 1

        return count

    def load_handler_part1(self, data: [str]) -> [str]:
        return [int(value) for value in data[0].split('-')]

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201904()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        exit(1)
