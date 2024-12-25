"""
AOC Day X
"""
import sys

from astroid.raw_building import register_arguments

from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math

class Aoc202417(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict) -> str:
        reg_A, reg_B, reg_C, code = data
        output = self.run_machine(code, reg_A, reg_B, reg_C)

        return ",".join([str(x) for x in output])

    def run_machine(self, code, reg_A, reg_B, reg_C):
        regs: dict[str, int] = {
            "A": reg_A,
            "B": reg_B,
            "C": reg_C
        }
        output = []
        ip = 0
        while ip < len(code):
            opcode = code[ip]
            operand = code[ip + 1]
            match opcode:
                case 0:  # adv
                    value = self.combo(operand, regs)
                    regs["A"] = regs["A"] >>  value
                case 1:  # bxl
                    regs["B"] = regs["B"] ^ operand
                case 2:  # bst
                    value = self.combo(operand, regs)
                    regs["B"] = value & 0b111
                case 3:  # jnz
                    if regs["A"] != 0:
                        ip = operand
                        continue
                case 4:  # bxc
                    regs["B"] = regs["B"] ^ regs["C"]
                case 5:  # out
                    output.append(self.combo(operand, regs) & 0b111)
                case 6:  # Bdv
                    value = self.combo(operand, regs)
                    regs["B"] =regs["A"] >>  value
                case 7:  # cdv
                    value = self.combo(operand, regs)
                    regs["C"] = regs["A"] >>  value

            ip += 2
        return output

    def combo(self, operand, regs):
        value = operand
        if 3 < value < 7:
            value = regs[chr(ord("A") + value - 4)]
        return value

    def calc_2(self, data: [str]) -> int:
        reg_A, reg_B, reg_C, code = data

        possibles = {}

        for a in range(0b1000000000000):
            output = self.run_machine(code, a, 0, 0)
            o = output[0]
            if o not in possibles:
                possibles[o] = []
            possibles[o] += [a]




        valid = set(possibles[code[0]])
        for depth in range(1, len(code)):
            new_valid = set()
            for p in possibles[code[depth]]:
                for q in valid:
                    a = q >> (3*depth)
                    a = a & 0b11111111
                    b = p & 0b11111111
                    if b == a:
                        t = p << (3*depth)
                        t = t | q
                        new_valid.add(t)
            valid = new_valid


        return min(valid)


    def load_handler_part1(self, data: [str]) -> [str]:
        reg_A = int(data[0].split(": ")[1])
        reg_B = int(data[1].split(": ")[1])
        reg_C = int(data[2].split(": ")[1])
        code = [int(x) for x in data[4].split(": ")[1].split(",")]
        return reg_A, reg_B, reg_C, code

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc202417()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
