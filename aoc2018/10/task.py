"""
AOC Day X
"""
import math
import re
import sys
from common import AocBase
from common import configure


class Aoc201900(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, lights: []) -> int:
        pos1 = lights[0][0]
        pos2 = lights[1][0]
        vel1 = lights[0][1]
        vel2 = lights[1][1]

        count = 0
        while True:
            dist = math.hypot(pos2.real - pos1.real,pos2.imag - pos1.imag)
            if dist < 100:
                break
            count += 1
            pos1 += vel1
            pos2 += vel2

        new_lights = []
        for light in lights:
            new_lights.append((light[0] + count*light[1], light[1]))
        lights = new_lights

        while True:
            new_lights = []
            positions = []
            for light in lights:
                new_lights.append((light[0] + light[1], light[1]))
                positions.append(light[0] + light[1])
            lights = new_lights
            found = False
            for position in positions:
                found = True
                for i in range(0, 5):
                    if position + complex(0, i) not in positions:
                        found = False
                        break
                if found:
                    break
                for i in range(0, 5):
                    if position + complex(i, 0) not in positions:
                        found = False
                        break
                if found:
                    break

            if found:
                self.print_lights(positions)
                break

        return ""

    def calc_2(self, lights: []) -> int:
        pos1 = lights[0][0]
        pos2 = lights[1][0]
        vel1 = lights[0][1]
        vel2 = lights[1][1]

        count = 0
        while True:
            dist = math.hypot(pos2.real - pos1.real,pos2.imag - pos1.imag)
            if dist < 100:
                break
            count += 1
            pos1 += vel1
            pos2 += vel2

        new_lights = []
        for light in lights:
            new_lights.append((light[0] + count*light[1], light[1]))
        lights = new_lights

        while True:
            count +=1

            new_lights = []
            positions = []
            for light in lights:
                new_lights.append((light[0] + light[1], light[1]))
                positions.append(light[0] + light[1])
            lights = new_lights
            found = False
            for position in positions:
                found = True
                for i in range(0, 5):
                    if position + complex(0, i) not in positions:
                        found = False
                        break
                if found:
                    break
                for i in range(0, 5):
                    if position + complex(i, 0) not in positions:
                        found = False
                        break
                if found:
                    break

            if found:
                self.print_lights(positions)
                break

        return count

    def load_handler_part1(self, data: [str]) -> [str]:
        lights =[]
        regex = r"position=< *(-*\d+), *(-*\d+)> velocity=< *(-*\d+),  *(-*\d+)>"

        for d in data:
            match = re.match(regex, d)
            pos = complex(int(match.group(1)), int(match.group(2)))
            vel = complex(int(match.group(3)), int(match.group(4)))
            lights.append((pos, vel))
        return lights

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)

    def print_lights(self, positions : [complex]):
        min_x = positions[0].real
        max_x = positions[0].real
        min_y = positions[0].imag
        max_y = positions[0].imag

        for position in positions:
            min_x = min(min_x, position.real)
            max_x = max(max_x, position.real)
            min_y = min(min_y, position.imag)
            max_y = max(max_y, position.imag)

        min_x = int(min_x)
        min_y = int(min_y)
        max_x = int(max_x)
        max_y = int(max_y)

        for y in range(min_y-1, max_y+2):
            line = ""
            for x in range(min_x-1, max_x+2):
                if complex(x,y) in positions:
                    line += "*"
                else:
                    line += "."
            print(line)


        pass


if __name__ == '__main__':
    configure()
    aoc = Aoc201900()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
