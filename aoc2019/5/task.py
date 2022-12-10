from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
from dataclasses import dataclass

logger = logging.getLogger("ACO2019-2")


@dataclass
class IntCode:
    memory: dict
    instruction_pointer: int = 0
    value: str = "None"
    done: bool = False

@dataclass
class Params:
    parameter1: int
    parameter2: int
    input_data: str


class Aoc201905(AocBase):

    def __init__(self):
        self.operations = {
            1: {"name": "add", "params": 2, "func": self.add},
            2: {"name": "multiply", "params": 2, "func": self.mul},
            3: {"name": "input", "params": 1, "func": self.input},
            4: {"name": "output", "params": 1, "func": self.output},
            5: {"name": "jump-if-true", "params": 2, "func": self.jump_if_true},
            6: {"name": "jump-if-false", "params": 2, "func": self.jump_if_false},
            7: {"name": "less than", "params": 2, "func": self.less_than},
            8: {"name": "equals", "params": 2, "func": self.equals},
            99: {"name": "exit", "params": 0, "func": self.exit},
        }

    @staticmethod
    def add( c: IntCode, p: Params):
        c.memory[int(c.memory[c.instruction_pointer + 3])] = str(p.parameter1 + p.parameter2)
        c.instruction_pointer += 4

    @staticmethod
    def mul( c: IntCode, p: Params):
        c.memory[int(c.memory[c.instruction_pointer + 3])] = str(p.parameter1 * p.parameter2)
        c.instruction_pointer += 4

    @staticmethod
    def input( c: IntCode, p: Params):
        c.memory[int(c.memory[c.instruction_pointer + 1])] = p.input_data
        c.instruction_pointer += 2

    @staticmethod
    def output(c: IntCode, p: Params):
        c.value = str(p.parameter1)
        print(c.value)
        c.instruction_pointer += 2

    @staticmethod
    def jump_if_true(c: IntCode, p: Params):
        if p.parameter1 != 0:
            c.instruction_pointer = p.parameter2
        else:
            c.instruction_pointer += 3

    @staticmethod
    def jump_if_false(c: IntCode, p: Params):
        if p.parameter1 == 0:
            c.instruction_pointer = p.parameter2
        else:
            c.instruction_pointer += 3

    @staticmethod
    def less_than(c: IntCode, p: Params):
        if p.parameter1 < p.parameter2:
            c.memory[int(c.memory[c.instruction_pointer + 3])] = '1'
        else:
            c.memory[int(c.memory[c.instruction_pointer + 3])] = '0'
        c.instruction_pointer += 4

    @staticmethod
    def equals(c: IntCode, p: Params):
        if p.parameter1 == p.parameter2:
            c.memory[int(c.memory[c.instruction_pointer + 3])] = '1'
        else:
            c.memory[int(c.memory[c.instruction_pointer + 3])] = '0'
        c.instruction_pointer += 4

    @staticmethod
    def exit(c: IntCode, p: Params):
        c.done = True

    @staticmethod
    def get_value(m: dict, ip: int, pm: int):
        if pm == 0:
            return int(m[int(m[ip])])
        else:
            return int(m[ip])

    @staticmethod
    def split_instruction(full_instruction):
        instruction = int(full_instruction[-2:])
        apm1 = 0
        if len(full_instruction) > 2 and full_instruction[-3] == '1':
            apm1 = 1
        apm2 = 0
        if len(full_instruction) > 3 and full_instruction[-4] == '1':
            apm2 = 1
        return instruction, apm1, apm2

    def calc_1(self, data: [str]) -> int:
        last_value = "None"
        c = IntCode({})
        for i in range(0, len(data[0])):
            c.memory[i] = data[0][i]
        while not c.done:
            full_instruction = c.memory[c.instruction_pointer]
            instruction, pm1, pm2 = self.split_instruction(full_instruction)
            if instruction in self.operations:
                operation = self.operations[instruction]
                parameters = self.get_params(c, data, operation, pm1, pm2)
                operation["func"](c, parameters)
        return c.value

    def get_params(self, c, data, operation, pm1, pm2):
        p1 = 0
        if operation["params"] >= 1:
            p1 = self.get_value(c.memory, c.instruction_pointer + 1, pm1)
        p2 = 0
        if operation["params"] == 2:
            p2 = self.get_value(c.memory, c.instruction_pointer + 2, pm2)
        p = Params(p1, p2, data[1])
        return p

    def calc_2(self, data: [str]) -> int:
        return self.calc_1(data)

    def load_handler_part1(self, data: [str]) -> [str]:
        return [data[0].split(","), data[1]]

    def load_handler_part2(self, data: [str]) -> [str]:
        return [data[0].split(","), data[1]]


if __name__ == '__main__':
    configure()
    aoc = Aoc201905()
    failed, results = aoc.run("part1_[0-9].txt", "part2_[0-9]+.txt")
    if failed:
        exit(1)
