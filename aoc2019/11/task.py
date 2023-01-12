import operator

from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
from dataclasses import dataclass, field
from collections import defaultdict

logger = logging.getLogger("ACO2019-2")

@dataclass
class Params:
    parameter1: int
    parameter2: int

class IntCode:

    def __init__(self, data: [int]):
        self.memory: {} = defaultdict(int)
        self.instruction_pointer: int = 0
        self.value: str = "None"
        self.done: bool = False
        self.input_data: [int] = []
        self.input_data_pos: int = 0
        self.relative_base: int = 0
        self.operations = {
            1: {"name": "add", "params": 2, "func": self.add},
            2: {"name": "multiply", "params": 2, "func": self.mul},
            3: {"name": "input", "params": 1, "func": self.input},
            4: {"name": "output", "params": 1, "func": self.output},
            5: {"name": "jump-if-true", "params": 2, "func": self.jump_if_true},
            6: {"name": "jump-if-false", "params": 2, "func": self.jump_if_false},
            7: {"name": "less than", "params": 2, "func": self.less_than},
            8: {"name": "equals", "params": 2, "func": self.equals},
            9: {"name": "adjusts the relative base", "params": 1, "func": self.adjust_relative_base},
            99: {"name": "exit", "params": 0, "func": self.exit},
        }

        self.position = (0, 0)
        self.facing = (0, 1)
        self.panels = defaultdict(int)
        self.values: [] = []

        self.turn = {
            0: {(0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0), (1, 0): (0, 1)},
            1: {(0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1)},
        }

        for j in range(0, len(data)):
            self.memory[j] = int(data[j])

    def read(self, parameter: int):
        mode = self.get_mode(parameter)
        parameter_address =  self.instruction_pointer + parameter
        if mode == 0:
            return self.memory[self.memory[parameter_address]]
        elif mode == 1:
            return self.memory[parameter_address]
        elif mode == 2:
            return self.memory[self.relative_base + self.memory[parameter_address]]

    def get_mode(self, parameter):
        string_instruction = str(self.memory[self.instruction_pointer])
        inst = int(string_instruction)
        op = inst % 100
        mode3, mode2, mode1 = f"{inst // 100:03d}"
        if parameter == 1:
            mode = int(mode1)
        if parameter == 2:
            mode = int(mode2)
        if parameter == 3:
            mode = int(mode3)
        return mode

    def write(self, parameter: int, value:int):
        mode = self.get_mode(parameter)
        parameter_address = self.instruction_pointer + parameter
        if mode == 0:
            self.memory[self.memory[parameter_address]] = value
        elif mode == 2:
            self.memory[self.relative_base + self.memory[parameter_address]] = value

    def adjust_relative_base(self, p: Params):
        old = self.relative_base
        self.relative_base = old + p.parameter1
        # print(self.relative_base)
        self.instruction_pointer += 2

    def add(self, p: Params):
        self.write(3, p.parameter1 + p.parameter2)
        self.instruction_pointer += 4

    def mul(self, p: Params):
        self.write(3, p.parameter1 * p.parameter2)
        self.instruction_pointer += 4

    def input(self, p: Params):
        i = self.panels[self.position]
        self.write(1, i)
        self.instruction_pointer += 2

    def output(self, p: Params):
        self.values.append(p.parameter1)
        if len(self.values) == 1:
            self.panels[self.position] = self.values[0]
        elif len(self.values) == 2:
            self.facing = self.turn[self.values[1]][self.facing]
            self.position = tuple(map(operator.add, self.position, self.facing))
            self.values = []
        self.instruction_pointer += 2

    def jump_if_true(self, p: Params):
        if p.parameter1 != 0:
            self.instruction_pointer = p.parameter2
        else:
            self.instruction_pointer += 3

    def jump_if_false(self, p: Params):
        if p.parameter1 == 0:
            self.instruction_pointer = p.parameter2
        else:
            self.instruction_pointer += 3

    def less_than(self, p: Params):
        if p.parameter1 < p.parameter2:
            self.write(3, 1)
        else:
            self.write(3, 0)
        self.instruction_pointer += 4

    def equals(self, p: Params):
        if p.parameter1 == p.parameter2:
            self.write(3, 1)
        else:
            self.write(3, 0)
        self.instruction_pointer += 4

    def exit(self, p: Params):
        self.done = True

    def get_value(self, ip: int, pm: int):
        if pm == 0:
            return self.memory[self.memory[ip]]
        elif pm == 1:
            return self.memory[ip]
        elif pm == 2:
            return self.memory[self.relative_base + self.memory[ip]]

    @staticmethod
    def split_instruction(full_instruction):
        string_instruction = str(full_instruction)
        instruction = int(string_instruction[-2:])
        apm1 = 0
        if len(string_instruction) > 2:
            apm1 = int(string_instruction[-3])
        apm2 = 0
        if len(string_instruction) > 3:
            apm2 = int(string_instruction[-4])
        return instruction, apm1, apm2

    def get_params(self, operation, pm1, pm2):
        p1 = 0
        if operation["params"] >= 1:
            p1 = self.read(1)
        p2 = 0
        if operation["params"] == 2:
            p2 = self.read(2)
        p = Params(p1, p2)
        return p

    def run(self):
        while not self.done:
            full_instruction = self.memory[self.instruction_pointer]
            instruction, pm1, pm2 = self.split_instruction(full_instruction)
            if instruction in self.operations:
                operation = self.operations[instruction]
                parameters = self.get_params(operation, pm1, pm2)
                print(self.instruction_pointer+1, full_instruction, operation['name'], parameters)
                operation["func"](parameters)


class Aoc201905(AocBase):

    def calc_1(self, data: [str]) -> int:
        c = IntCode(data)
        c.run()
        return len(c.panels)



    def calc_2(self, data: [str]) -> int:
        c = IntCode(data)
        c.panels[(0,0)] = 1
        c.run()
        self.draw(c.panels)
        return len(c.panels)

    def draw(self, panels):
        minx = min(panels, key=operator.itemgetter(0))[0]
        maxx = max(panels, key=operator.itemgetter(0))[0]
        miny = min(panels, key=operator.itemgetter(1))[1]
        maxy = max(panels, key=operator.itemgetter(1))[1]
        for y in range(maxy + 1, miny - 2, -1):
            out = ""
            for x in range(minx - 1, maxx + 2):
                out += str(panels[(x, y)]).replace('0',' ')
            print(out)
#CBLPJZCU
    def load_handler_part1(self, data: [str]) -> [str]:
        return data[0].split(",")

    def load_handler_part2(self, data: [str]) -> [str]:
        return data[0].split(",")


if __name__ == '__main__':
    configure()
    aoc = Aoc201905()
    failed, results = aoc.run("part1x_[1-4]*.txt", "part2_[0-9]+.txt")
    if failed:
        exit(1)
