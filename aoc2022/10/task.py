import string

from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging

logger = logging.getLogger("ACO2022-10")


class CPU:

    def __init__(self, instructions: [str], reg_x=1, screen_width=40, screen_height=6, signal_check_start=20, signal_check_cycle=40):
        self.instructions = instructions
        self.reg_x: int = reg_x
        self.clock: int = 0
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen_pixels = screen_width * screen_height
        self.screen = ['.' for i in range(0, self.screen_pixels)]
        self.sprite: list[int] = [0, 1, 2]
        self.pixel = 0
        self.total = 0
        self.signal_strength = 0
        self.signal_check_start = signal_check_start
        self.signal_check_cycle = signal_check_cycle
        self.operations = {
            "noop": {"name": "noop", "params": 0, "func": self.nop, "cycles": 1},
            "addx": {"name": "addx", "params": 1, "func": self.add_x, "cycles": 2},
        }

    def run(self):
        for item in self.instructions:
            instruction = item.split(' ')
            instruction.append("")
            if instruction[0] in self.operations:
                opp = self.operations[instruction[0]]
                opp["func"](instruction[1])

    def nop(self, _):
        self.draw_pixel()
        self.clock += self.operations["noop"]["cycles"]
        self.check_signal()

    def add_x(self, param):
        for _ in range(0, self.operations["addx"]["cycles"]):
            self.clock += 1
            self.draw_pixel()
            self.check_signal()
        self.reg_x += int(param)

    def check_signal(self):
        signal_check = (self.clock + self.signal_check_start) % self.signal_check_cycle
        if signal_check == 0:
            self.total += self.clock * self.reg_x

    def update_sprite(self) -> [int]:
        sprite = [self.reg_x-1, self.reg_x, self.reg_x+1]
        if sprite[0] < 0:
            sprite[0] += self.screen_pixels
        if sprite[2] >= self.screen_pixels:
            sprite[2] -= self.screen_pixels
        self.sprite = sprite

    def draw_pixel(self):
        self.update_sprite()
        if self.pixel % 40 in self.sprite:
            self.screen[self.pixel] = "#"
        self.pixel = (self.pixel + 1) % self.screen_pixels


class Aoc202210(AocBase):

    def calc_1(self, data) -> int:
        cpu = CPU(data)
        cpu.run()
        return cpu.total

    def calc_2(self, data: [str]) -> int:
        cpu = CPU(data)
        cpu.run()
        for i in range(0, 7):
            print(''.join(cpu.screen[i*40:i*40+40]))
        return ''.join(cpu.screen)

    def load_handler_part1(self, data: [str]) -> [str]:
        return data

    def load_handler_part2(self, data: [str]) -> [str]:
        return data


if __name__ == '__main__':
    configure()
    aoc = Aoc202210()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        exit(1)
