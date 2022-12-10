import string

from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
from dataclasses import dataclass
import sys
import re
logger = logging.getLogger("ACO2022-9")

class Aoc202210(AocBase):

    def calc_1(self, data ) -> int:
        total = 0
        reg_x = 1
        cycle = 0
        for item in data:
            match item.split(' '):
                case ['noop']:
                    cycle += 1
                    cycle_mod = abs(cycle - 20) % 40
                    if cycle_mod == 0:
                        total += cycle * reg_x
                        print(f'{cycle} {cycle_mod} {total} {cycle * reg_x} {reg_x} ')
                case['addx', value]:
                    cycle += 2
                    cycle_mod = abs(cycle - 20) % 40
                    match cycle_mod:
                        case 0:
                            total += cycle * reg_x
                            print(f'{cycle} {cycle_mod} {total} {cycle * reg_x} {reg_x} ')
                        case 1:
                            total += (cycle - 1) * reg_x
                            print(f'{cycle} {cycle_mod} {total} {(cycle-1) * reg_x} {reg_x} ')
                    reg_x += int(value)

        return total


    def build_sprite(self, regx):
        sprite = [regx-1, regx, regx +1]
        if sprite[0] < 0:
            sprite[0] += 240
        if sprite[2] > 239:
            sprite[2] -= 240
        return sprite

    def calc_2(self, data: [str]) -> int:
        screen = ['.' for i in range(0, 240)]
        reg_x = 1
        cycle = 1
        pixel = 0
        for item in data:
            match item.split(' '):
                case ['noop']:
                    sprite = self.build_sprite(reg_x)
                    if pixel % 40 in sprite:
                        screen[pixel] = "#"
                    cycle += 1
                    pixel = (pixel + 1) % 240
                case ['addx', value]:
                    for step in range(0, 2):
                        sprite = self.build_sprite(reg_x)
                        if pixel % 40 in sprite:
                            screen[pixel] = "#"
                        cycle += 1
                        pixel = (pixel+1) % 240
                    reg_x += int(value)
        for i in range(0, 7):
            print(''.join(screen[i*40:i*40+40]))
        return ''.join(screen)

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
