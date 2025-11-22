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

        self.regs = [0,0, 0, 0, 0, 0, 0]

        counter =0

        instructions, ip_reg = data
        ip = 0
        while 0 <= ip < len(instructions):
            self.regs[ip_reg] = ip
            instruction = instructions[ip]
            output = f'ip={ip} {str(self.regs)} {instruction[0]} {instruction[1]} {instruction[2]} {instruction[3]} '
            self.commands[instruction[0]](self, instruction[1], instruction[2], instruction[3])
            ip = self.regs[ip_reg]
            output += f'{str(self.regs)}'
            ip += 1
            counter+=1
            print(output)
            if ip == 29:
                break

        return self.regs[3]


    def calc_2(self, data: [str]) -> int:
        a=b=c=d=e=f=0
        #a b c d e f
        #0 1 2 3 4 5

        e = 0
        c = d | 65536  # 7
        d = 10736359  # 8
        while True:
            b = c & 255     #9
            d += b          #10
            d &= 16777215   #11
            d *= 65899      #12
            d &= 16777215   #13
            if 256 > c:     #14 - #18
                print(d)
                return d

            e = e // 256






        return 0

        self.regs = [0, 0, 0, 0, 0, 0, 0]

        seen = []

        instructions, ip_reg = data
        ip = 0

        while 0 <= ip < len(instructions):
            self.regs[ip_reg] = ip
            instruction = instructions[ip]
            output = f'ip={ip} {str(self.regs)} {instruction[0]} {instruction[1]} {instruction[2]} {instruction[3]} '
            self.commands[instruction[0]](self, instruction[1], instruction[2], instruction[3])
            ip = self.regs[ip_reg]
            output += f'{str(self.regs)}'
            ip += 1
            if ip == 29:
                # break 9107763.0
                if self.regs[3] in seen:
                    lowest = seen[-1]
                    break

                seen += [self.regs[3]]

                print(output)
                # instruction_count = counter

        return lowest

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
    failed, results = aoc.run("part1_[0-9]+.txt", "part2x_[0-9]+.txt")
    if failed:
        sys.exit(1)
