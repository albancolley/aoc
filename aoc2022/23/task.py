import dataclasses
import os.path
import string

import numpy as np

from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
from dataclasses import dataclass
import re
from collections import deque
import operator

logger = logging.getLogger("ACO2022-17")

@dataclass()
class Elf:
    id : int
    current_pos : (int, int)
    next_pos : (int, int) = (0 , 0)

next_direction = {
    "N": "S",
    "S": "W",
    "W": "E",
    "E": "N"
}

all_around = [
    (-1, 1), (0, 1),  (1, 1),
    (-1, 0),          (1,  0),
    (-1, -1), (0, -1), (1, -1)
]

moves = {
    "N": (0, 1),
    "S": (0, -1),
    "W": (-1, 0),
    "E": (1,  0)
}


checks = {
    "N": [ (-1, 1), (0, 1),  (1, 1)],
    "S": [(-1, -1), (0, -1),(1, -1)],
    "W": [(-1, 1), (-1, 0), (-1, -1)],
    "E": [(1, 1), (1, 0), (1, -1)],
}

class Aoc202212(AocBase):

    def can_move(self, grove, elf, current_direction):
        has_elves = False
        for point in all_around:
            current_pos = elf.current_pos
            new_point = tuple(map(operator.add, current_pos, point))
            if new_point in grove:
                has_elves = True
                break

        if not has_elves:
            return

        cd = current_direction
        for i in range(0, 4):
            no_elf = True
            for point in checks[cd]:
                new_point = tuple(map(operator.add, elf.current_pos, point))
                if new_point in grove:
                    no_elf = False
                    break

            if no_elf:
                break
            cd = next_direction[cd]

        if no_elf:
            new_point = tuple(map(operator.add, elf.current_pos, moves[cd]))
            elf.next_pos = new_point

        return no_elf

    def get_max_min(self, grove):
        min_x = 'X'
        max_x = 'X'
        min_y = 'X'
        max_y = 'X'
        for elf in grove:
            x = elf[0]
            y = elf[1]
            min_x = x
            max_x = x
            min_y = y
            max_y = y
            break

        for elf in grove:
            x = elf[0]
            y = elf[1]
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
        return min_y, max_y, min_x, max_x

    def output(self, grove, r):
        print(f'Round: {r}')
        min_y, max_y, min_x, max_x = self.get_max_min(grove)
        for y in range(max_y + 1, min_y - 2, -1):
            line = ""
            for x in range(min_x - 1, max_x + 2):
                if (x, y) in grove:
                    line += "#"
                else:
                    line += "."
            print(line)
        print()

    def calc_1(self, data) -> int:

        current_direction = 'N'
        # self.output(data, 0)
        for i in range(0, 10):
            self.move(current_direction, data)
            current_direction = next_direction[current_direction]
            # self.output(data, i+1)

        min_y, max_y, min_x, max_x = self.get_max_min(data)
        area = (max_y - min_y + 1) * (max_x - min_x + 1)
        result = area - len(data)
        return result

    def move(self, current_direction, data):
        movements = {}
        for elf_location in data:
            elf = data[elf_location]
            if self.can_move(data, elf, current_direction):
                if elf.next_pos not in movements:
                    movements[elf.next_pos] = (True, elf)
                else:
                    movements[elf.next_pos] = (False, None)
        for pos in movements:
            movement = movements[pos]
            if movement[0]:
                elf = movement[1]
                cur_pos = elf.current_pos
                del data[cur_pos]
                elf.current_pos = pos
                data[pos] = elf

    def get_points(self, grove):
        points = set()
        for pos in grove:
            points.add(pos)
        return  points

    def calc_2(self, data: []) -> int:
        current_direction = 'N'
        count = 1
        last_points = self.get_points(data)
        while True:
            self.move(current_direction, data)
            new_points =  self.get_points(data)
            diff = new_points - last_points
            if len(diff) == 0:
                break
            current_direction = next_direction[current_direction]
            last_points = new_points
            count +=1

        return count

    def load_handler_part1(self, data: [(int, int)]) -> {}:

        result = {}
        elf_id = 1
        columns = len(data[0])
        y = 0
        for row in data:
            x = -columns
            for c in row:
                if c =='#':
                    elf = Elf(elf_id, (x, y))
                    result[(x, y)] = elf
                    elf_id = elf_id + 1
                x += 1
            y -= 1
        return result

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)



if __name__ == '__main__':
    configure()
    aoc = Aoc202212()
    failed, results = aoc.run("part1_[1-2]+.txt", "part2_[1-2]+.txt")
    if failed:
        exit(1)
