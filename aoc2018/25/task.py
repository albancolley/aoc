"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
    z: int
    t: int

class Aoc201825(AocBase):
    """
    AOC Day 10 Class
    """

    def manhatten_distance(self, p: Point, p1: Point) -> int:
        return abs(p.x - p1.x) + abs(p.y - p1.y) + abs(p.z - p1.z) + abs(p.t - p1.t)

    def point_to_tuple(self, p: Point) -> tuple[int,int, int, int]:
        return p.x, p.y, p.z, p.t

    def calc_1(self, points: list[Point]) -> int:

        constellation=[points[0]]
        # seen = [points[0]]
        constellation_count = 1
        points.remove(points[0])
        while len(points) > 0:
            found = True
            while found:
                last_point = None
                found = False
                for point in points:
                    # if point in seen:
                    #     continue
                    for constellation_point in constellation:
                        if self.manhatten_distance(point, constellation_point) <= 3:
                            # seen.append(point)
                            constellation.append(point)
                            found = True
                            last_point = point
                            break

                    if found:
                        break
                if found:
                    points.remove(last_point)
            if not found and len(points) > 0:
                constellation_count += 1
                constellation = [points[0]]
                points.remove(points[0])
        return constellation_count


    def calc_2(self, data: [str]) -> int:
        total = 0
        return total

    def load_handler_part1(self, data: list[str]) -> list[Point]:
        points: list[Point] = []
        for row in data:
            s = row.split(",")
            points.append(Point(int(s[0]), int(s[1]), int(s[2]), int(s[3])))
        return points

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201825()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2x_[0-9]+.txt")
    if failed:
        sys.exit(1)
