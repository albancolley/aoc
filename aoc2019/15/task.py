import operator

from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
from dataclasses import dataclass, field
from collections import defaultdict, deque

import _pickle as pickle

logger = logging.getLogger("ACO2019-15")

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

        self.move = 0

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
        i = self.move
        self.write(1, i)
        self.instruction_pointer += 2

    def output(self, p: Params):
        self.value = p.parameter1
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

    def run(self, move):
        self.move = move
        while not self.done:
            full_instruction = self.memory[self.instruction_pointer]
            instruction, pm1, pm2 = self.split_instruction(full_instruction)
            if instruction in self.operations:
                operation = self.operations[instruction]
                parameters = self.get_params(operation, pm1, pm2)
                # print(self.instruction_pointer+1, full_instruction, operation['name'], parameters)
                operation["func"](parameters)
                if instruction == 4:
                    return self.value



class Aoc201915(AocBase):



    def calc_1(self, data: [str]) -> int:

        moves = {1:(0,1), 2:(0,-1), 3: (1,0), 4: (-1,0)}
        reverse = {1:2, 2:1, 3:4, 4:3}

        queue = deque()
        queue.append([1])
        queue.append([2])
        queue.append([3])
        queue.append([4])
        length = 0
        been = {(0,0) : 1}
        while len(queue) > 0:
            c = IntCode(data)
            position = (0, 0)
            path = queue.popleft()
            for p in path:
                c.run(p)
                position = tuple(map(operator.add, position, moves[p]))
            if position in been:
                continue
            match c.value:
                case 0:
                    been[position] = 0
                    continue
                case 1:
                    been[position] = 1
                case 2:
                    been[position] = 2
                    length = len(path)
                    break
            queue.append(path + [1])
            queue.append(path + [2])
            queue.append(path + [3])
            queue.append(path + [4])


        # with open('map.txt', 'w') as file:
        #     file.write(pickle.dumps(been))

        return length



    def calc_2(self, data: [str]) -> int:
        moves = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
        reverse = {1: 2, 2: 1, 3: 4, 4: 3}

        queue = deque()
        queue.append([1])
        queue.append([2])
        queue.append([3])
        queue.append([4])
        length = 0
        oxygen = (0,0)
        been = {(0, 0): 1}
        while len(queue) > 0:
            c = IntCode(data)
            position = (0, 0)
            path = queue.popleft()
            for p in path:
                c.run(p)
                position = tuple(map(operator.add, position, moves[p]))
            if position in been:
                continue
            match c.value:
                case 0:
                    been[position] = 0
                    continue
                case 1:
                    been[position] = 1
                case 2:
                    been[position] = 2
                    oxygen = position
                    length = len(path)
            queue.append(path + [1])
            queue.append(path + [2])
            queue.append(path + [3])
            queue.append(path + [4])

        queue = deque()
        queue.append([1])
        queue.append([2])
        queue.append([3])
        queue.append([4])
        seen = {oxygen : True}
        max_path = 0
        while len(queue) > 0:
            position = oxygen
            path = queue.popleft()
            for p in path:
                position = tuple(map(operator.add, position, moves[p]))
            if position in seen:
                continue
            seen[position] = True
            if been[position] ==  0:
                continue
            max_path = max(max_path,len(path))
            queue.append(path + [1])
            queue.append(path + [2])
            queue.append(path + [3])
            queue.append(path + [4])

        return max_path



    def load_handler_part1(self, data: [str]) -> [str]:
        return data[0].split(",")

    def load_handler_part2(self, data: [str]) -> [str]:
        return data[0].split(",")


if __name__ == '__main__':
    configure()
    aoc = Aoc201915()
    failed, results = aoc.run("part1_[0-9]*.txt", "part2_[0-9]+.txt")
    if failed:
        exit(1)
