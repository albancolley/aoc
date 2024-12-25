"""
AOC Day X
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections


class Aoc201718(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: [str]) -> int:
        regs = collections.defaultdict(int)
        sound = 0
        pos = 0
        while True:
            cmd = data[pos]
            # print(cmd)
            reg_1 = cmd[1]
            value_1 = self.get_value(cmd[1], regs)
            value_2 = self.get_value(cmd[2], regs) if len(cmd) > 2 else 0
            match cmd[0]:
                case 'snd':
                    sound = regs[reg_1]
                case 'set':
                    regs[reg_1] = value_2
                case 'add':
                    regs[reg_1] += value_2
                case 'mul':
                    regs[reg_1] *= value_2
                case 'mod':
                    regs[reg_1] = value_1 % value_2
                case 'rcv':
                    if value_1 != 0:
                        return sound
                case 'jgz':
                    if value_1 > 0:
                        pos += value_2
                        continue
            pos += 1


    def get_value(self, reg:str, regs):
        if not reg.isalpha():
            return int(reg)
        else:
            return regs[reg]

    def calc_2(self, data: [str]) -> int:
        regs_array:[] = [collections.defaultdict(int), collections.defaultdict(int)]
        input_array:[] = [[],[]]
        sent_array:[] = [0,0]
        pos_array:[] = [0,0]
        finished_array:[] = [False, False]
        program = 0
        regs_array[1]['p'] = 1
        while not(finished_array[0] and finished_array[1]):
            pos = pos_array[program]
            regs = regs_array[program]
            # print(input_array)
            cmd = data[pos]
            # print(cmd)
            reg_1 = cmd[1]
            value_1 = self.get_value(cmd[1], regs)
            value_2 = self.get_value(cmd[2], regs) if len(cmd) > 2 else 0
            next_program = program
            match cmd[0]:
                case 'snd':
                    input_array[(program + 1) % 2].append(value_1)
                    # print(value_1)
                    sent_array[program] += 1
                case 'set':
                    regs[reg_1] = value_2
                case 'add':
                    regs[reg_1] += value_2
                case 'mul':
                    regs[reg_1] *= value_2
                case 'mod':
                    regs[reg_1] = value_1 % value_2
                case 'rcv':
                    if len(input_array[program]) > 0:
                        regs[reg_1] = input_array[program].pop(0)
                        finished_array[(program + 1) % 2] = False
                    else:
                        finished_array[program] = True
                        # print(input_array)
                        program = (program + 1) % 2
                        continue
                case 'jgz':
                    if value_1 > 0:
                        pos_array[program] += value_2
                        continue
            pos_array[program] += 1

        return sent_array[1]

    def load_handler_part1(self, data: [str]) -> [str]:
        return [x.split() for x in data]

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)




if __name__ == '__main__':
    configure()
    aoc = Aoc201718()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
