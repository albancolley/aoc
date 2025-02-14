"""
AOC Day X
"""
import re
import sys

from common import AocBase
from common import configure


class Aoc201720(AocBase):
    """
    AOC Day 10 Class
    """

    def manhattan_distance(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])


    def calc_1(self, data: [dict]) -> int:
        result = 0
        closest = (0, 0)
        for i in range(0,500):
            new_data = []
            position = 0
            for d in data:
                a = d["a"]
                v = (d["v"][0] + d["a"][0], d["v"][1] + d["a"][1], d["v"][2] + d["a"][2])
                p = (d["p"][0] + v[0], d["p"][1] + v[1], d["p"][2] + v[2])
                new_data.append({"p":p, "v":v, "a":a})
                distance = self.manhattan_distance((0,0,0), p )
                if position == 0:
                    closest = (position, distance)
                else:
                    if distance < closest[1] :
                        closest = (position, distance)
                position += 1
            data = new_data
        return closest[0]

    def calc_2(self, data: [str]) -> int:
        result = 0
        for i in range(0, 500):
            new_data = {}
            position = 0
            for d in data:
                a = d["a"]
                v = (d["v"][0] + d["a"][0], d["v"][1] + d["a"][1], d["v"][2] + d["a"][2])
                p = (d["p"][0] + v[0], d["p"][1] + v[1], d["p"][2] + v[2])
                p_key = f'{p[0]}-{p[1]}-{p[2]}'
                if p_key not in new_data:
                    new_data[p_key] = []
                new_data[p_key].append({"p": p, "v": v, "a": a})
                distance = self.manhattan_distance((0, 0, 0), p)
                if position == 0:
                    closest = (position, distance)
                else:
                    if distance < closest[1]:
                        closest = (position, distance)
                position += 1

            data=[]
            for p_key in new_data:
                if len(new_data[p_key]) == 1:
                    data += new_data[p_key]
        return len(data)

    def load_handler_part1(self, data: [str]) -> [str]:
        pattern = ".*<(.+),(.+),(.+)>.*v=<(.+),(.+),(.+)>.*a=<(.+),(.+),(.+)>"
        result = []
        for line in data:
            m = re.match(pattern, line)
            p = (int(m.group(1)), int(m.group(2)) , int(m.group(3)))
            v = (int(m.group(4)), int(m.group(5)) , int(m.group(6)))
            a = (int(m.group(7)), int(m.group(8)) , int(m.group(9)))
            result.append({"p":p, "v":v, "a":a})
        return result

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201720()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
