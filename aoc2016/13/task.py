"""
AOC Day X
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math
from queue import PriorityQueue

class Aoc201600(AocBase):
    """
    AOC Day 10 Class
    """

    def distance_squared(self, pos1, pos2):
        p0 = (int(pos1.real), int(pos1.imag))
        p1 = (int(pos2.real), int(pos2.imag))
        return (p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2

    def is_wall(self, pos, offset):
        x = int(pos.real)
        y = int(pos.imag)
        if x < 0 or y < 0:
            return True
        value: int = x*x + 3*x + 2*x*y + y + y*y
        value += offset
        return not value.bit_count() % 2 == 0

    def calc_1(self, data: str) -> int:
        input = data[0].split(' ')
        offset = int(input[0])
        x = int(input[1])
        y = int(input[2])
        directions = [
            1 + 0j,
            -1 + 0j,
            0 + 1j,
            0 + -1j
        ]
        target = complex(x,y)
        q = PriorityQueue()
        q.put((0, self.distance_squared(target, 1 + 1j), (1,1)))
        cache = {1 + 1j: True}
        while not q.empty():
            steps, distance, position_tuple = q.get()
            x, y = position_tuple
            position = complex(x, y)
            if position == target:
                print(steps, distance, position)
                return  steps

            for d in directions:
                new_position = position + d
                if self.is_wall(new_position, offset) or new_position in cache:
                    continue
                cache[new_position] = True
                q.put((steps + 1, self.distance_squared(target, new_position), (int(new_position.real), int(new_position.imag))))


        return 0


    def calc_2(self, data: [str]) -> int:
        input = data[0].split(' ')
        offset = int(input[0])
        x = int(input[1])
        y = int(input[2])
        directions = [
            1 + 0j,
            -1 + 0j,
            0 + 1j,
            0 + -1j
        ]
        target = complex(x, y)
        q = PriorityQueue()
        q.put((0, self.distance_squared(target, 1 + 1j), (1, 1)))
        cache :dict = {1 + 1j: 0}
        while not q.empty():
            steps, distance, position_tuple = q.get()
            x, y = position_tuple
            position = complex(x, y)
            if steps == 51:
                count = 0
                for c in cache:
                    if cache[c] < 51:
                        count += 1
                return count

            for d in directions:
                new_position = position + d
                if self.is_wall(new_position, offset) or new_position in cache:
                    continue
                cache[new_position] = steps + 1
                q.put((steps + 1, self.distance_squared(target, new_position),
                       (int(new_position.real), int(new_position.imag))))

        return 0

    def load_handler_part1(self, data: [str]) -> [str]:
       return data

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201600()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
