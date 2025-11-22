"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure


class Aoc201900(AocBase):
    """
    AOC Day 10 Class
    """

    regs = [0,0,0,0]

    def tests(self):
        self.regs = [0, 5, 6, 0]
        self.addr(1,2,0)
        if self.regs != [11, 5, 6, 0]:
            return False

        self.regs = [0, 5, 6, 0]
        self.addi(1,2,0)
        if self.regs != [7, 5, 6, 0]:
            return False

        self.regs = [0, 5, 6, 0]
        self.mulr(1,2,0)
        if self.regs != [30, 5, 6, 0]:
            return False

        self.regs = [0, 5, 6, 0]
        self.muli(1,2,0)
        if self.regs != [10, 5, 6, 0]:
            return False

        self.regs = [0, 5, 6, 0]
        self.banr(1,2,0)
        if self.regs != [4, 5, 6, 0]:
            return False

        self.regs = [0, 5, 6, 0]
        self.bani(1,2,0)
        if self.regs != [0, 5, 6, 0]:
            return False

        self.regs = [0, 5, 6, 0]
        self.borr(1,2,0)
        if self.regs != [7, 5, 6, 0]:
            return False

        self.regs = [0, 10, 6, 0]
        self.bori(1,7,0)
        if self.regs != [15, 10, 6, 0]:
            return False

        self.regs = [0, 10, 6, 0]
        self.setr(1, 7, 0)
        if self.regs != [10, 10, 6, 0]:
            return False

        self.regs = [0, 10, 6, 0]
        self.seti(1, 7, 0)
        if self.regs != [1, 10, 6, 0]:
            return False

        self.regs = [0, 10, 6, 0]
        self.gtir(1, 2, 0)
        if self.regs != [0, 10, 6, 0]:
            return False

        self.regs = [0, 6, -1, 0]
        self.gtir(1, 2, 0)
        if self.regs != [1, 6, -1, 0]:
            return False

        self.regs = [0, 10, 6, 0]
        self.gtri(1, 2, 0)
        if self.regs != [1, 10, 6, 0]:
            return False

        self.regs = [0, 6, 10, 0]
        self.gtri(1, 10, 0)
        if self.regs != [0, 6, 10, 0]:
            return False

        self.regs = [0, 10, 6, 0]
        self.gtrr(1, 2, 0)
        if self.regs != [1, 10, 6, 0]:
            return False

        self.regs = [0, 6, 10, 0]
        self.gtrr(1, 2, 0)
        if self.regs != [0, 6, 10, 0]:
            return False

        self.regs = [0, 10, 1, 0]
        self.eqir(1, 2, 0)
        if self.regs != [1, 10, 1, 0]:
            return False

        self.regs = [0, 6, -1, 0]
        self.eqir(1, 2, 0)
        if self.regs != [0, 6, -1, 0]:
            return False

        self.regs = [0, 2, 1, 0]
        self.eqri(1, 2, 0)
        if self.regs != [1, 2, 1, 0]:
            return False

        self.regs = [0, 6, -1, 0]
        self.eqri(1, 2, 0)
        if self.regs != [0, 6, -1, 0]:
            return False

        self.regs = [0, 2, 2, 0]
        self.eqrr(1, 2, 0)
        if self.regs != [1, 2, 2, 0]:
            return False

        self.regs = [5, 5, 2, 0]
        self.eqrr(0, 1, 0)
        if self.regs != [1, 5, 2, 0]:
            return False

        self.regs = [0, 6, -1, 0]
        self.eqrr(1, 2, 0)
        if self.regs != [0, 6, -1, 0]:
            return False

        return True

    def addr(self, a:int, b:int, c:int):
        self.regs[c] = self.regs[a] + self.regs[b]

    def addi(self, a:int, b:int, c:int):
        self.regs[c] = self.regs[a] + b

    def mulr(self, a:int, b:int, c:int):
        self.regs[c] = self.regs[a] * self.regs[b]

    def muli(self, a:int, b:int, c:int):
        self.regs[c] = self.regs[a] * b

    def banr(self, a:int, b:int, c:int):
        self.regs[c] = self.regs[a] & self.regs[b]

    def bani(self, a:int, b:int, c:int):
        self.regs[c] = self.regs[a] & b

    def borr(self, a:int, b:int, c:int):
        self.regs[c] = self.regs[a] | self.regs[b]

    def bori(self, a:int, b:int, c:int):
        self.regs[c] = self.regs[a] | b

    def setr(self, a:int, b:int, c:int):
        self.regs[c] = self.regs[a]

    def seti(self, a:int, b:int, c:int):
        self.regs[c] = a

    def gtir(self, a:int, b:int, c:int):
        if a >  self.regs[b]:
            self.regs[c] = 1
        else:
            self.regs[c] = 0

    def gtri(self, a:int, b:int, c:int):
        if self.regs[a] > b:
            self.regs[c] = 1
        else:
            self.regs[c] = 0

    def gtrr(self, a:int, b:int, c:int):
        if self.regs[a] > self.regs[b]:
            self.regs[c] = 1
        else:
            self.regs[c] = 0

    def eqir(self, a:int, b:int, c:int):
        if a == self.regs[b]:
            self.regs[c] = 1
        else:
            self.regs[c] = 0

    def eqri(self, a:int, b:int, c:int):
        if self.regs[a] == b:
            self.regs[c] = 1
        else:
            self.regs[c] = 0

    def eqrr(self, a:int, b:int, c:int):
        if self.regs[a] == self.regs[b]:
            self.regs[c] = 1
        else:
            self.regs[c] = 0

    commands = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

    def calc_1(self, data: dict) -> int:
        result = 0
        samples, instructions = data
        for sample in samples:
            count = 0
            # print(sample)
            for command in self.commands:
                self.regs[0] = sample[0][0]
                self.regs[1] = sample[0][1]
                self.regs[2] = sample[0][2]
                self.regs[3] = sample[0][3]
                command(self, sample[1][1], sample[1][2], sample[1][3])
                if self.regs == sample[2]:
                    count += 1
            if count >= 3:
                result += 1

        return result

    def calc_2(self, data: [str]) -> int:
        result = 0
        possibles = {}
        sample_number = 0
        samples, instructions = data
        for sample in samples:
            count = 0
            for command in self.commands:
                self.regs[0] = sample[0][0]
                self.regs[1] = sample[0][1]
                self.regs[2] = sample[0][2]
                self.regs[3] = sample[0][3]
                command(self, sample[1][1], sample[1][2], sample[1][3])
                if self.regs == sample[2]:
                    if sample_number not in possibles:
                        possibles[sample_number] = set()
                    possibles[sample_number].add(command)
            sample_number += 1
        # print(possibles)

        ops_codes = {}
        ops_codes_set = set()
        while len(ops_codes) != len(self.commands):
            new_possibles = {}
            for key, value in possibles.items():
                if len(value) == 1:
                    ops_codes[samples[key][1][0]] = value.pop()
                    ops_codes_set.add(ops_codes[samples[key][1][0]])
                else:
                    new_possibles[key] = value

            new_possibles_2 = {}
            for key, value in new_possibles.items():
                new_possibles_2[key] = new_possibles[key].difference(ops_codes_set)

            possibles = new_possibles_2

        ## not 540
        # print(ops_codes)
        self.regs[0] = 0
        self.regs[1] = 0
        self.regs[2] = 0
        self.regs[3] = 0
        for instruction in instructions:
            ops_codes[instruction[0]](self, instruction[1], instruction[2], instruction[3])


        return self.regs[0]

    def load_handler_part1(self, data: [str]) -> [str]:
        pos = 0
        samples = []
        while pos < len(data) and len(data[pos]) > 0:
            if not data[pos].startswith('Before'):
                break
            before = eval(data[pos].split(": ")[1])
            instruction = eval('('  + ','.join(data[pos+1].split(' ')) + ')')
            after = eval(data[pos+2].split(": ")[1])
            samples.append((before, instruction, after))
            pos +=4

        while pos < len(data) and len(data[pos]) == 0:
            pos += 1
            pass

        instructions = []
        while pos < len(data) and len(data[pos]) > 0:
            instructions.append(eval('('  + ','.join(data[pos].split(' ')) + ')'))
            pos += 1



        return samples, instructions

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201900()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
