import string

from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
from dataclasses import dataclass
import sys
import re
logger = logging.getLogger("ACO2022-9")

@dataclass
class Point:
    x: int
    y: int

    def add(self, p):
        self.x += p.x
        self.y += p.y

    def equal(self, p):
        return self.x == p.x and self.y == p.y

    def near(self, p) -> bool:
        for dx in range(self.x-1, self.x+2):
            for dy in range(self.y-1, self.y+2):
                point = Point(dx, dy)
                if p.equal(point):
                    return True
        return False

class Aoc202209(AocBase):

    direction = {
        'R': Point(1, 0),
        'L': Point(-1, 0),
        'U': Point(0, 1),
        'D': Point(0, -1),
    }



    def calc_1(self, data ) -> int:
        covered = {}
        h = Point(0,0)
        t = Point(0,0)
        covered["0-0"] = True
        for step in data:
            d = self.direction[step[0]]
            for i in range(0, int(step[1])):
                h.add(d)
                self.move(h, t)
                covered[f'{t.x}-{t.y}'] = True
        return len(covered)

    def move(self, h, t):
        if not t.near(h):
            if h.x == t.x:
                if h.y > t.y:
                    t.y += 1
                else:
                    t.y -= 1
            elif h.y == t.y:
                if h.x > t.x:
                    t.x += 1
                else:
                    t.x -= 1
            else:
                if h.y > t.y and h.x > t.x:
                    t.y += 1
                    t.x += 1
                elif h.y > t.y and h.x < t.x:
                    t.y += 1
                    t.x -= 1
                elif h.y < t.y and h.x < t.x:
                    t.y -= 1
                    t.x -= 1
                else:
                    t.y -= 1
                    t.x += 1

    def calc_2(self, data: [str]) -> int:
        covered = {}
        snake = []
        for i in range(0, 10):
            snake.append(Point(0,0))
        covered["0-0"] = True
        for step in data:
            d = self.direction[step[0]]
            for i in range(0, int(step[1])):
                h = snake[0]
                h.add(d)
                for p in range(0, len(snake) - 1):
                    self.move(snake[p], snake[p+1])
                covered[f'{snake[len(snake) - 1].x}-{snake[len(snake) - 1].y}'] = True
        return len(covered)

    def load_handler_part1(self, data: [str]) -> [int]:
        new_data = []
        for row in data:
            new_data.append([row[0], row[1:]])
        return new_data

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)



if __name__ == '__main__':
    configure()
    aoc = Aoc202209()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        exit(1)
