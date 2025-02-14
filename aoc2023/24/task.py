"""
AOC Day 10
"""
import sys
from common import AocBase
from common import configure
import math
from sympy import *


class Vector:
    x: int
    dx: int
    y: int
    dy: int
    z: int
    dz: int

    def get_gradient(self, axis: str) -> int:
        if axis == 'x':
            return self.dx
        if axis == 'y':
            return self.dy
        if axis == 'z':
            return self.dz

    def get_coord(self, axis: str) -> int:
        if axis == 'x':
            return self.x
        if axis == 'y':
            return self.y
        if axis == 'z':
            return self.z


    def __str__(self):
        return f'{self.x}, {self.y}, {self.z} @ {self.dx}, {self.dy}, {self.dz}'

    def __repr__(self):
        return f'({self.x}, {self.y}, {self.z} @ {self.dx}, {self.dy}, {self.dz})'

class Aoc2023010(AocBase):
    """
    AOC Day 10 Class
    """

    def intersect(selfself, hailstone1, hailstone2, range_start, range_end):

        dy1 = hailstone1[1][1]
        dx1 = hailstone1[1][0]
        a = dy1 / dx1
        x1 = hailstone1[0][0]
        y1 = hailstone1[0][1]
        c = -x1 * a + y1

        dy2 = hailstone2[1][1]
        dx2 = hailstone2[1][0]
        b = dy2 / dx2
        x2 = hailstone2[0][0]
        y2 = hailstone2[0][1]
        d = -x2*b + y2

        if a == b:
            return False, 0 , 0

        intercept_x = (d-c) / (a-b)
        intercept_y = a * ((d-c) / (a-b)) + c

        if intercept_x < range_start or intercept_x > range_end:
            return False, 0 , 0

        if intercept_y < range_start or intercept_y > range_end:
            return False, 0 , 0

        if dx1 >= 0:
            if intercept_x < x1:
                return False, 0 , 0
        
        if dx1 < 0:
            if intercept_x > x1:
                return  False, 0 , 0

        if dx2 >= 0:
            if intercept_x < x2:
                return False, 0 , 0
        
        if dx2 < 0:
            if intercept_x > x2:
                return  False, 0 , 0

        if dy1 >= 0:
            if intercept_y < y1:
                return False, 0 , 0

        if dy1 <= 0:
            if intercept_y > y1:
                return False, 0 , 0

        if dy2 >= 0:
            if intercept_y < y2:
                return False, 0 , 0

        if dy2 <= 0:
            if intercept_y > y2:
                return False, 0 , 0

        return True, intercept_x, intercept_y

    def calc_1(self, data: dict) -> int:
        result = 0

        range_start = 200000000000000
        range_end = 400000000000000

        if len(data) == 5:
            range_start = 7
            range_end = 27
        pos = 0
        hits = []
        for hailstone in data:
            pos += 1
            for second_hailstone in data[pos:]:
                hit, intercept_x, intercept_y = self.intersect(hailstone, second_hailstone, range_start, range_end)
                hits.append(hit)

        result = hits.count(True)
        return result

    def no_intersection(self, hailstone1, hailstone2):

        dy1 = hailstone1[1][1]
        dx1 = hailstone1[1][0]
        a = dy1 / dx1
        x1 = hailstone1[0][0]
        y1 = hailstone1[0][1]
        c = -x1 * a + y1

        dy2 = hailstone2[1][1]
        dx2 = hailstone2[1][0]
        b = dy2 / dx2
        x2 = hailstone2[0][0]
        y2 = hailstone2[0][1]
        d = -x2 * b + y2

        if a == b:
            return False, (0,0)

        intercept_x = (d - c) / (a - b)
        intercept_y = a * ((d - c) / (a - b)) + c
        intercept_point = (intercept_x, intercept_y)

        if dx1 >= 0:
            if intercept_x < x1:
                return True, intercept_point

        if dx1 < 0:
            if intercept_x > x1:
                return True, intercept_point

        if dx2 >= 0:
            if intercept_x < x2:
                return True, intercept_point

        if dx2 < 0:
            if intercept_x > x2:
                return True, intercept_point

        if dy1 >= 0:
            if intercept_y < y1:
                return True, intercept_point

        if dy1 <= 0:
            if intercept_y > y1:
                return True, intercept_point

        if dy2 >= 0:
            if intercept_y < y2:
                return True, intercept_point

        if dy2 <= 0:
            if intercept_y > y2:
                return True, intercept_point


        return False, intercept_point

    def intersect2(self, c, a, d, b):
        if (a-b) == 0:
            return math.inf, math.inf
        x = (d-c) / (a-b)
        y = a*(d-c)/(a-b) + c

        return x, y

    def calc_2(self, data: [Vector]) -> int:

        x, y, z = symbols('x y z')
        dx, dy, dz = symbols('dx dy dz')
        variables = [x, y, z, dx, dy, dz]

        count = 1
        equations =[]
        for hailstone in data[:3]:
            t = symbols(f't{count}')
            variables.append(t)
            equations.append(x + dx*t - hailstone.x - hailstone.dx*t)
            equations.append(y + dy*t - hailstone.y - hailstone.dy*t)
            equations.append(z + dz*t - hailstone.z - hailstone.dz*t)
            count += 1

        result = solve(equations,variables)

        print(result)
        total = result[0][0] + result[0][1] + result[0][2]
        return total

    def get_min_max_coord(self, axis, data):
        hailstones = sorted(data, key=lambda vector: vector.get_coord(axis))
        return hailstones[0].get_coord(axis), hailstones[-1].get_coord(axis)

    def get_possible_gradient(self, axis, data):

        hailstone: Vector
        gradients: dict[int, [Vector]] = dict()
        hailstones_x = sorted(data, key=lambda v: v.get_coord(axis))
        for hailstone in hailstones_x:
            gradient = hailstone.get_gradient(axis)
            if gradient not in gradients:
                gradients[gradient] = []
            gradients[gradient].append(hailstone)

        possible_gradients = set()
        for i in range(-1000, 1000):
            possible_gradients.add(i)

        for gradient in gradients:
            vectors: list = list(reversed(gradients[gradient]))
            if len(vectors) > 1:
                intersections = []
                x = vectors[0].get_coord(axis)
                for i in range(-1000, 1000):
                    possible = True
                    for vector in vectors[1:]:
                        intersection = self.intersect2(x, i, vector.get_coord(axis), vector.get_gradient(axis))

                        if not intersection[0].is_integer():
                            possible = False
                            break
                    if possible:
                        intersections.append(i)

                #x = vectors[-1].get_coord(axis)
                # for i in range(-1000, 1000):
                #     possible = True
                #     for vector in list(reversed(vectors))[1:]:
                #         intersection = self.intersect2(x, i, vector.get_coord(axis), vector.get_gradient(axis))
                #         print(intersection)
                #         if intersection[0] == math.inf:
                #             possible = False
                #             break
                #         else:
                #             print(intersection)
                #     if possible:
                #         intersections.append(i)
                print(intersections)
                possible_gradients = possible_gradients.intersection(intersections)

        return possible_gradients

    def load_handler_part1(self, data: [str]) -> [str]:
        hailstones = []
        for line in data:
            s = line.split(' @ ')
            p = [int(x.strip()) for x in s[0].split(',')]
            v = [int(x.strip()) for x in s[1].split(',')]
            hailstones.append((p, v))
        return hailstones

    def load_handler_part2(self, data: [str]) -> [str]:
        hailstones: [Vector] = []
        for line in data:
            vector = Vector()
            s = line.split(' @ ')
            p = [int(x.strip()) for x in s[0].split(',')]
            vector.x = p[0]
            vector.y = p[1]
            vector.z = p[2]
            dp = [int(x.strip()) for x in s[1].split(',')]
            vector.dx = dp[0]
            vector.dy = dp[1]
            vector.dz = dp[2]
            hailstones.append(vector)
        return hailstones



if __name__ == '__main__':
    configure()
    aoc = Aoc2023010()
    failed, results = aoc.run("part1x_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
