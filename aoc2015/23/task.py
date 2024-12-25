"""
AOC Day X
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math

class Aoc201600(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict) -> int:
        commands = []
        for command in data:
            instruction, reg, *offset = command.split(' ')
            commands.append((instruction, reg.replace(',',''), offset[0] if offset else None))

        regs = {'a':0, 'b':0}

        pos = 0
        while pos < len(commands):
            command = commands[pos]
            instruction =  command[0]
            first_op = command[1]
            second_op = command[2]
            match instruction:
                case "inc":
                    regs[first_op] += 1
                case "jie":
                    if regs[first_op] % 2 == 0:
                        pos += int(second_op)
                        continue
                case "jio":
                    if regs[first_op] == 1:
                        pos += int(second_op)
                        continue
                case "jmp":
                    pos += int(first_op)
                    continue
                case "hlf":
                    regs[first_op] = int(regs[first_op] / 2)
                case "tpl":
                    regs[first_op] *= 3
            pos += 1

        return regs['b']

    def calc_2(self, data: [str]) -> int:
        commands = []
        for command in data:
            instruction, reg, *offset = command.split(' ')
            commands.append((instruction, reg.replace(',',''), offset[0] if offset else None))

        regs = {'a':1, 'b':0}

        pos = 0
        while pos < len(commands):
            command = commands[pos]
            instruction =  command[0]
            first_op = command[1]
            second_op = command[2]
            match instruction:
                case "inc":
                    regs[first_op] += 1
                case "jie":
                    if regs[first_op] % 2 == 0:
                        pos += int(second_op)
                        continue
                case "jio":
                    if regs[first_op] == 1:
                        pos += int(second_op)
                        continue
                case "jmp":
                    pos += int(first_op)
                    continue
                case "hlf":
                    regs[first_op] = int(regs[first_op] / 2)
                case "tpl":
                    regs[first_op] *= 3
            pos += 1

        return regs['b']


    def load_handler_part1(self, data: [str]) -> [str]:
       return data

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201600()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
