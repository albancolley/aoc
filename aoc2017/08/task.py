"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure
import collections


class Aoc201708(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, commands: []) -> int:
        regs = collections.defaultdict(int)

        for command in commands:
            valid = False
            match command[4]:
                case '>':
                    valid = regs[command[3]] > command[5]
                case '>=':
                    valid = regs[command[3]] >= command[5]
                case '<':
                    valid = regs[command[3]] < command[5]
                case '<=':
                    valid = regs[command[3]] <= command[5]
                case '==':
                    valid = regs[command[3]] == command[5]
                case '!=':
                    valid = regs[command[3]] != command[5]

            if valid:
                match command[1]:
                    case 'inc':
                        regs[command[0]] += command[2]
                    case 'dec':
                        regs[command[0]] -= command[2]

        return max(regs.values())

    def calc_2(self, commands: [[]]) -> int:
        regs = collections.defaultdict(int)
        max_reg = 0

        for command in commands:
            valid = False
            match command[4]:
                case '>':
                    valid = regs[command[3]] > command[5]
                case '>=':
                    valid = regs[command[3]] >= command[5]
                case '<':
                    valid = regs[command[3]] < command[5]
                case '<=':
                    valid = regs[command[3]] <= command[5]
                case '==':
                    valid = regs[command[3]] == command[5]
                case '!=':
                    valid = regs[command[3]] != command[5]

            if valid:
                match command[1]:
                    case 'inc':
                        regs[command[0]] += command[2]
                    case 'dec':
                        regs[command[0]] -= command[2]

            max_reg = max(max_reg, max(regs.values()))

        return max_reg

    def load_handler_part1(self, data: [str]) -> [str]:
        commands = []
        for l in data:
            temp = l.split()
            commands.append([temp[0], temp[1], int(temp[2]), temp[4], temp[5], int(temp[6])])
        return commands

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201708()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
