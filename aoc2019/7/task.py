from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
from dataclasses import dataclass, field

logger = logging.getLogger("ACO2019-2")


@dataclass
class IntCode:
    memory: dict
    instruction_pointer: int = 0
    value: str = "None"
    done: bool = False
    input_data: list[str] = field(default_factory=list)
    input_data_pos: int = 0

@dataclass
class Params:
    parameter1: int
    parameter2: int


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
        c.memory[int(c.memory[c.instruction_pointer + 1])] = c.input_data[c.input_data_pos]
        c.input_data_pos += 1
        c.instruction_pointer += 2

    @staticmethod
    def output(c: IntCode, p: Params):
        c.value = str(p.parameter1)
        # print(c.value)
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
        phases = self.get_phases()
        result = []
        for phase in phases:
            if phase == "43210":
                pass
            last_output = 0
            for i in range(0, 5):
                c = IntCode({})
                for j in range(0, len(data)):
                    c.memory[j] = data[j]
                c.input_data.append(phase[i])
                c.input_data.append(last_output)
                while not c.done:
                    full_instruction = c.memory[c.instruction_pointer]
                    instruction, pm1, pm2 = self.split_instruction(full_instruction)
                    if instruction in self.operations:
                        operation = self.operations[instruction]
                        parameters = self.get_params(c, data, operation, pm1, pm2)
                        operation["func"](c, parameters)
                last_output = int(c.value)
            result.append(last_output)
        result.sort()
        return result[-1]

    def get_phases(self, start=0, end=4):
        phases = []
        for i1 in range(start, end+1):
            for i2 in range(start, end+1):
                if i2 == i1:
                    continue
                for i3 in range(start, end+1):
                    if i3 == i1 or i3 == i2:
                        continue
                    for i4 in range(start, end+1):
                        if i4 == i1 or i4 == i2 or i4 == i3:
                            continue
                        for i5 in range(start, end+1):
                            if i5 == i1 or i5 == i2 or i5 == i3 or i5 == i4:
                                continue
                            phases.append(f'{i1}{i2}{i3}{i4}{i5}')
        return phases

    def get_params(self, c, data, operation, pm1, pm2):
        p1 = 0
        if operation["params"] >= 1:
            p1 = self.get_value(c.memory, c.instruction_pointer + 1, pm1)
        p2 = 0
        if operation["params"] == 2:
            p2 = self.get_value(c.memory, c.instruction_pointer + 2, pm2)
        p = Params(p1, p2)
        return p

    def calc_2(self, data: [str]) -> int:
        phases = self.get_phases(5, 9)
        result = []
        for phase in phases:
            last_output = 0
            amps = self.build_amps(data, phase)
            done = False
            while not done:
                done = True
                for index, amp in enumerate(amps):
                    while not amp.done:
                        full_instruction = amp.memory[amp.instruction_pointer]
                        instruction, pm1, pm2 = self.split_instruction(full_instruction)
                        if instruction in self.operations:
                            operation = self.operations[instruction]
                            parameters = self.get_params(amp, data, operation, pm1, pm2)
                            operation["func"](amp, parameters)
                            if operation["name"] == "output":
                                amps[(index+1) % 5].input_data.append(str(int(amp.value)))
                                done = False
                                break
                last_output = int(amp.value)
            result.append(last_output)
        result.sort()
        return result[-1]

    def build_amps(self, data, phase):
        amps: [IntCode] = []
        for i in range(0, 5):
            c = IntCode({})
            for j in range(0, len(data)):
                c.memory[j] = data[j]
            c.input_data.append(phase[i])
            amps.append(c)
        amps[0].input_data.append('0')
        return amps

    def load_handler_part1(self, data: [str]) -> [str]:
        return data[0].split(",")

    def load_handler_part2(self, data: [str]) -> [str]:
        return data[0].split(",")


if __name__ == '__main__':
    configure()
    aoc = Aoc201905()
    failed, results = aoc.run("part1x_[0-9]*.txt", "part2_[0-9]+.txt")
    if failed:
        exit(1)
