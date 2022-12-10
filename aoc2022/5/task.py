import string

from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
import re
logger = logging.getLogger("ACO2022-4")


class Aoc202201(AocBase):

    def calc_1(self, data: {}) -> int:
        total: int = 0
        for item in data['instructions']:
            for i in range(0, item[0]):
                crate = data[item[1]].pop()
                if not item[2] in data:
                    data[item[2]] = []
                data[item[2]] += [crate]
        result = ""
        for i in range(1, 10):
            if i in data:
                if len(data[i]) > 0:
                    result += str(data[i][-1])
        return result

    def calc_2(self, data: {}) -> int:
        total: int = 0
        for item in data['instructions']:
            new_crates = []
            for i in range(0, item[0]):
                crate = data[item[1]].pop()
                new_crates.insert(0, crate)
            if not item[2] in data:
                data[item[2]] = []
            data[item[2]] += new_crates
        result = ""
        for i in range(1, 10):
            if i in data:
                if len(data[i]) > 0:
                    result += str(data[i][-1])
        return result

    def load_handler_part1(self, data: [str]) -> {}:
        new_data = {}
        row = 0
        for item in data:
            if item[1] == '1':
                break
            for i in range(1, 10):
                if len(item) > (i-1)*4+1:
                    crate = item[(i-1)*4+1]
                    if crate in string.ascii_uppercase:
                        if i not in new_data:
                            new_data[i] = []
                        new_data[i].insert(0, crate)
            row += 1
        new_data['instructions'] = []
        p = re.compile(r'move (\d+) from (\d+) to (\d+)')
        for instruction in data[row+2:]:
            m = re.match(p, instruction)
            new_data['instructions'].append([int(m.group(1)), int(m.group(2)), int(m.group(3))])
        return new_data

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc202201()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        exit(1)
