"""
AOC Day X
"""
import sys
from typing import Callable

from common import AocBase
from common import configure
from functools import reduce
from sympy import factorint

class Aoc201900(AocBase):
    """
    AOC Day 10 Class
    """

    regs = [0, 0, 0, 0, 0, 0]

    def addr(self, a: int, b: int, c: int):
        self.regs[c] = self.regs[a] + self.regs[b]

    def addi(self, a: int, b: int, c: int):
        self.regs[c] = self.regs[a] + b

    def mulr(self, a: int, b: int, c: int):
        self.regs[c] = self.regs[a] * self.regs[b]

    def muli(self, a: int, b: int, c: int):
        self.regs[c] = self.regs[a] * b

    def banr(self, a: int, b: int, c: int):
        self.regs[c] = self.regs[a] & self.regs[b]

    def bani(self, a: int, b: int, c: int):
        self.regs[c] = self.regs[a] & b

    def borr(self, a: int, b: int, c: int):
        self.regs[c] = self.regs[a] | self.regs[b]

    def bori(self, a: int, b: int, c: int):
        self.regs[c] = self.regs[a] | b

    def setr(self, a: int, b: int, c: int):
        self.regs[c] = self.regs[a]

    def seti(self, a: int, b: int, c: int):
        self.regs[c] = a

    def gtir(self, a: int, b: int, c: int):
        if a > self.regs[b]:
            self.regs[c] = 1
        else:
            self.regs[c] = 0

    def gtri(self, a: int, b: int, c: int):
        if self.regs[a] > b:
            self.regs[c] = 1
        else:
            self.regs[c] = 0

    def gtrr(self, a: int, b: int, c: int):
        if self.regs[a] > self.regs[b]:
            self.regs[c] = 1
        else:
            self.regs[c] = 0

    def eqir(self, a: int, b: int, c: int):
        if a == self.regs[b]:
            self.regs[c] = 1
        else:
            self.regs[c] = 0

    def eqri(self, a: int, b: int, c: int):
        if self.regs[a] == b:
            self.regs[c] = 1
        else:
            self.regs[c] = 0

    def eqrr(self, a: int, b: int, c: int):
        if self.regs[a] == self.regs[b]:
            self.regs[c] = 1
        else:
            self.regs[c] = 0

    commands : dict[str, Callable[..., ...]] = {"addr": addr, "addi": addi, "mulr": mulr, "muli": muli, "banr": banr, "bani": bani, "borr": borr,
                "bori": bori, "setr": setr, "seti": seti, "gtir": gtir, "gtri": gtri, "gtrr": gtrr, "eqir": eqir,
                "eqri": eqri, "eqrr": eqrr}

    def calc_1(self, data: dict) -> int:

        self.regs = [0, 0, 0, 0, 0, 0]

        reg_0 = -1

        instructions, ip_reg = data
        ip = 0
        while 0 <= ip < len(instructions):
            self.regs[ip_reg] = ip
            instruction = instructions[ip]
            output = f'ip={ip} {str(self.regs)} {instruction[0]} {instruction[1]} {instruction[2]} {instruction[3]} '
            if reg_0 != self.regs[0]:
                print(reg_0, self.regs[0] - reg_0)
                reg_0 = self.regs[0]
                print(output)
            self.commands[instruction[0]](self, instruction[1], instruction[2], instruction[3])
            ip = self.regs[ip_reg]
            output += f'{str(self.regs)}'
            # print(output)
            ip += 1

        result = self.regs[0]
        return result

    def factors(self, n):
        return set(reduce(
            list.__add__,
            ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))

    def calc_2(self, data: [str]) -> int:
        self.regs = [1, 0, 0, 0, 0, 0]

        reg_0 = -1

        result = 0

        instructions, ip_reg = data
        ip = 0
        while 0 <= ip < len(instructions):
            self.regs[ip_reg] = ip
            instruction = instructions[ip]
            output = f'ip={ip} {str(self.regs)} {instruction[0]} {instruction[1]} {instruction[2]} {instruction[3]} '
            if reg_0 != self.regs[0]:
                print(output)
                reg_0 = self.regs[0]
                if self.regs[3] > 1:
                    f = self.factors(self.regs[3])
                    print(f)
                    result = sum(list(f))
                    break
                print(reg_0, self.regs[0] - reg_0)

            self.commands[instruction[0]](self, instruction[1], instruction[2], instruction[3])
            ip = self.regs[ip_reg]
            output += f'{str(self.regs)}'
            # print(output)
            ip += 1

        return result

    def load_handler_part1(self, data: [str]) -> [str]:
        pos = 1
        instructions = []
        while pos < len(data) and len(data[pos]) > 0:
            instruction = data[pos].split(' ')
            instructions.append((instruction[0], int(instruction[1]), int(instruction[2]), int(instruction[3])))
            pos += 1

        ip_reg = int(data[0].split(' ')[-1])

        return instructions, ip_reg

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201900()
    failed, results = aoc.run("part1x_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
