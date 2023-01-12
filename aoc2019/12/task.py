import dataclasses

from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
from dataclasses import dataclass, field
from collections import defaultdict
import math

logger = logging.getLogger("ACO2019-12")

@dataclass
class Moon:
    id: int
    x: int
    y: int
    z: int
    vx: int = 0
    vy: int = 0
    vz: int = 0



class Aoc201912(AocBase):


    def get_velocity(self, z, z1):
        if z > z1:
            return -1, 1
        elif z < z1:
            return 1, -1

        return 0, 0



    def calc_1(self, data) -> int:
        moons, loops = data
        for _ in range(1, loops + 1):
            # for m in moons:
            #     print(m)
            # print()
            for m, moon in enumerate(moons):
                for moon2 in moons[m+1:]:
                    vx1, vx2 = self.get_velocity(moon.x, moon2.x)
                    moon.vx += vx1
                    moon2.vx += vx2
                    vy1, vy2 = self.get_velocity(moon.y, moon2.y)
                    moon.vy += vy1
                    moon2.vy += vy2
                    vz1, vz2 = self.get_velocity(moon.z, moon2.z)
                    moon.vz += vz1
                    moon2.vz += vz2
            for m in moons:
                m.x += m.vx
                m.y += m.vy
                m.z += m.vz

        total = 0
        for m in moons:
            total += (abs(m.x) + abs(m.y) + abs(m.z)) * (abs(m.vx) + abs(m.vy) + abs(m.vz))

        return total


    def calc_2(self, data) -> int:
        moons, _ = data
        xc = yc = zc = 0
        original_moons = []
        for moon in moons:
            original_moons.append(dataclasses.replace(moon))
        loops = 1
        while not (xc > 0 and yc > 0 and zc > 0):
            # for m in moons:
            #     print(m)
            # print()
            for m, moon in enumerate(moons):
                for moon2 in moons[m + 1:]:
                    vx1, vx2 = self.get_velocity(moon.x, moon2.x)
                    moon.vx += vx1
                    moon2.vx += vx2
                    vy1, vy2 = self.get_velocity(moon.y, moon2.y)
                    moon.vy += vy1
                    moon2.vy += vy2
                    vz1, vz2 = self.get_velocity(moon.z, moon2.z)
                    moon.vz += vz1
                    moon2.vz += vz2
            for m in moons:
                m.x += m.vx
                m.y += m.vy
                m.z += m.vz
            ms = list(zip(moons, original_moons))
            if all([x[0].x == x[1].x and x[0].vx == x[1].vx for x in ms]) and xc == 0:
                xc = loops
            if all([x[0].y == x[1].y and x[0].vy == x[1].vy for x in ms]) and yc == 0:
                yc = loops
            if all([x[0].z == x[1].z and x[0].vz == x[1].vz for x in ms]) and zc == 0:
                zc = loops
            loops += 1
        return math.lcm(xc,yc,zc)


    def load_handler_part1(self, data: [str]) -> [str]:
        moons: [Moon] = []
        count = 0
        loops = 0
        for l in data:
            if l[0] != '<':
                loops = int(l)
                break
            coords = l.replace('>','').split(',')
            x = int(coords[0].split('=')[-1])
            y = int(coords[1].split('=')[-1])
            z = int(coords[2].split('=')[-1])
            moons.append(Moon(count, x, y, z))
            count += 1
        return moons, loops

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201912()
    failed, results = aoc.run("part1_[1-3]*.txt", "part2_[0-9]+.txt")
    if failed:
        exit(1)
