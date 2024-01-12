import time

from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
from dataclasses import dataclass, field
from collections import defaultdict
import numpy as np
from collections import deque
from threading import Thread

logger = logging.getLogger("ACO2019-19")

@dataclass
class Params:
    parameter1: int
    parameter2: int

class IntCode:

    def __init__(self, data: [int], network: {}, name: int):
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

        self.network = network
        self.name = name
        self.startup = True
        self.values = []
        self.saved = None

        for j in range(0, len(data)):
            self.memory[j] = int(data[j])

    def read(self, parameter: int):
        mode = self.get_mode(parameter)
        parameter_address = self.instruction_pointer + parameter
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
        i = -1
        if self.startup:
            i = self.name
            self.startup = False
        elif self.saved:
            i = self.saved
            self.saved = None
        elif len(self.network[self.name]) > 0:
            x, y = self.network[self.name].popleft()
            i = x
            self.saved = y
        # self.input_data_pos += 1
        self.write(1, i)
        self.instruction_pointer += 2

    def output(self, p: Params):
        self.value = p.parameter1
        self.values.append(self.value)
        if len(self.values) == 3:
            address = self.values[0]
            self.network[address].append((self.values[1], self.values[2]))
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
                # print(self.instruction_pointer+1, full_instruction, operation['name'], parameters)
                operation["func"](parameters)


class Aoc201923(AocBase):

    def calc_1(self, data: [str]) -> int:
        return "use taskp1"
        # network = {}
        # for x in range(0, 50):
        #     network[x] = deque()
        # threads = {}
        # for x in range(0, 50):
        #     c = IntCode(data, network, x)
        #     t = Thread(target=c.run, args=[])
        #     threads[x] = t
        #     t.start()
        #
        # for x in range(0, 50):
        #     threads[x].join()
        #
        # return network[255][2]


    def calc_2(self, data: [str]) -> int:
        result = None
        nic = {}
        network = {}
        computers ={}
        for x in range(0, 50):
            network[x] = deque()
        network[255] = deque()
        threads = {}
        for x in range(0, 50):
            c = IntCode(data, network, x)
            t = Thread(target=c.run, args=[])
            threads[x] = t
            computers[x] = c
            t.start()

        while True:
            done = True
            time.sleep(1)
            for x in range(0, 50):
                if len(network[x]) != 0:
                    done = False
                    break
            if done:
                print(network[255])
                v = network[255].pop()
                x = v[0]
                y = v[1]
                print(x, y)
                if y in nic:
                    result = y
                    break
                nic[y] = True
                network[255].clear()
                network[255].append((x, y))
                network[0].append((x, y))

        for x in range(0, 50):
            computers[x].done = True

        return result

    def load_handler_part1(self, data: [str]) -> [str]:
        return data[0].split(",")

    def load_handler_part2(self, data: [str]) -> [str]:
        return data[0].split(",")


if __name__ == '__main__':
    configure()
    aoc = Aoc201923()
    failed, results = aoc.run("part1x_[1-4]*.txt", "part2_[1-1]+.txt")
    if failed:
        exit(1)
