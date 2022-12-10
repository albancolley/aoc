from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
from dataclasses import dataclass

logger = logging.getLogger("ACO2019-2")

@dataclass
class IntCode:
    m: dict
    ip: int = 0

class Aoc201901(AocBase):

    def calc_1(self, data: [str]) -> int:
        c = IntCode({})
        for i in range(0, len(data)):
            c.m[i] = data[i]
        while c.m[c.ip] != 99:
            if c.m[c.ip] == 1:
                c.m[c.m[c.ip+3]] = c.m[c.m[c.ip+1]] + c.m[c.m[c.ip+2]]
            elif c.m[c.ip] == 2:
                c.m[c.m[c.ip+3]] = c.m[c.m[c.ip+1]] * c.m[c.m[c.ip+2]]
            c.ip += 4
        return c.m[0]


    def calc_2(self, data: [str]) -> int:
        for noun in range(0, 100):
            for verb in range(0, 100):
                c = IntCode({})
                for i in range(0, len(data)):
                    c.m[i] = data[i]
                c.m[1] = noun
                c.m[2] = verb
                while c.m[c.ip] != 99:
                    if c.m[c.ip] == 1:
                        c.m[c.m[c.ip + 3]] = c.m[c.m[c.ip + 1]] + c.m[c.m[c.ip + 2]]
                    elif c.m[c.ip] == 2:
                        c.m[c.m[c.ip + 3]] = c.m[c.m[c.ip + 1]] * c.m[c.m[c.ip + 2]]
                    c.ip += 4
                if c.m[0] == 19690720:
                    return (100 * noun) + verb
        return 0

    def load_handler_part1(self, data: [str]) -> [str]:
        return [int(numeric_string) for numeric_string in data[0].split(",")]

    def load_handler_part2(self, data: [str]) -> [str]:
        return [int(numeric_string) for numeric_string in data[0].split(",")]


if __name__ == '__main__':
    configure()
    aoc = Aoc201901()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        exit(1)
