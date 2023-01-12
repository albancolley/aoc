from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
from dataclasses import dataclass, field
from collections import defaultdict
import numpy as np
from collections import deque

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
        self.output_data: [int] = []
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

        for j in range(0, len(data)):
            self.memory[j] = int(data[j])

    def read(self, parameter: int):
        string_instruction = str(self.memory[self.instruction_pointer])
        mode = 0
        if len(string_instruction) >= 2 + parameter:
            mode = int(string_instruction[-(parameter + 1)])
        parameter_address =  self.instruction_pointer + parameter
        if mode == 0:
            return self.memory[self.memory[parameter_address]]
        elif mode == 1:
            return self.memory[parameter_address]
        elif mode == 2:
            return self.memory[self.relative_base + self.memory[parameter_address]]

    def write(self, parameter: int, value:int):
        string_instruction = str(self.memory[self.instruction_pointer])
        mode = 0
        if len(string_instruction) >= 2 + parameter:
            mode = int(string_instruction[-(parameter + 2)])
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
        string_instruction = str(self.memory[self.instruction_pointer])
        apm1 = 0
        if len(string_instruction) > 2:
            apm1 = int(string_instruction[-3])
        if apm1 == 2:
            self.memory[self.relative_base + self.memory[self.instruction_pointer+1]] = self.input_data[self.input_data_pos]
        else:
            self.memory[p.parameter1] = self.input_data[self.input_data_pos]
        self.input_data_pos += 1
        self.instruction_pointer += 2

    def output(self, p: Params):
        self.value = p.parameter1
        self.output_data.append(self.value)
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
            p1 = self.get_value(self.instruction_pointer + 1, pm1)
        p2 = 0
        if operation["params"] == 2:
            p2 = self.get_value(self.instruction_pointer + 2, pm2)
        p = Params(p1, p2)
        return p

    def run(self):
        while not self.done:
            full_instruction = self.memory[self.instruction_pointer]
            instruction, pm1, pm2 = self.split_instruction(full_instruction)
            if instruction in self.operations:
                operation = self.operations[instruction]
                parameters = self.get_params(operation, pm1, pm2)
                # print(self.instruction_pointer+1, full_instruction, operation['name'], parameters)
                operation["func"](parameters)


class Aoc201905(AocBase):

    def calc_1(self, data: [str]) -> int:
        c = IntCode(data)
        c.input_data.append(1)
        c.run()

        all =[]
        grid_array = []
        row = []
        width = 0
        for p in c.output_data:
            if p==10:
                break
            width += 1

        for p in c.output_data:
            if p==10:
                grid_array.append(row)
                print(''.join(row))
                row = []
            else:
                row.append(chr(p))
                all.append(p)

        grid = np.array(all).reshape((-1, width))

        junctions = []
        for x in range(1, grid.shape[0]-2):
            for y in range(1, grid.shape[1]-2):
                if grid[x, y] == 35:
                    if grid[x+1, y] == 35 and grid[x-1, y] == 35 and grid[x, y+1] == 35  and grid[x, y-1] == 35:
                        junctions.append(x*y)
        return sum(junctions)



    def calc_2(self, data: [str]) -> int:
        c = IntCode(data)
        c.input_data.append(1)
        c.run()

        all = []
        grid_array = []
        row = []
        width = 0
        for p in c.output_data:
            if p == 10:
                break
            width += 1

        for p in c.output_data:
            if p == 10:
                grid_array.append(row)
                print(''.join(row))
                row = []
            else:
                row.append(chr(p))
                all.append(p)

        grid = np.array(all).reshape((-1, width))
        np_position = np.where(grid == 94)
        position = (np_position[0][0], np_position[1][0])
        done = False
        path = ['L']
        facing = (0, -1)
        turns = {(0, -1): [('L', (1, 0)), ('R', (-1, 0))],
                 (0, 1): [('L', (-1, 0)), ('R', (1, 0))],
                 (-1, 0): [('L', (0, 1)), ('R', (0,  -1))],
                 (1, 0): [('L', (0, -1)), ('R', (0,  1))]}

        while not done:
            new_position = (position[0] + facing[0], position[1] + facing[1])
            steps = 0
            while grid[new_position] == 35:
                position = new_position
                steps += 1
                new_position = (position[0] + facing[0], position[1] + facing[1])
                if new_position[0] < 0 or new_position[0] >= grid.shape[0]-1 \
                        or new_position[1] < 0 or new_position[1] >= grid.shape[1]-1:
                    break
            if steps > 0:
                path.append(steps)
            done = True
            for direction, new_facing in turns[facing]:
                new_position = (position[0] + new_facing[0], position[1] + new_facing[1])
                if new_position[0] < 0 or new_position[0] > grid.shape[0] \
                        or new_position[1] < 0 or new_position[0] > grid.shape[1]:
                    continue
                if grid[new_position] == 35:
                    done = False
                    facing = new_facing
                    path.append(direction)

        return path

    def load_handler_part1(self, data: [str]) -> [str]:
        return data[0].split(",")

    def load_handler_part2(self, data: [str]) -> [str]:
        return data[0].split(",")


if __name__ == '__main__':
    configure()
    aoc = Aoc201905()
    failed, results = aoc.run("part1x_[1-4]*.txt", "part2_[1-1]+.txt")
    if failed:
        exit(1)
