"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure
import math

class Aoc202405(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict) -> int:
        result = 0
        orders, prints = data
        for p in prints:
            ok = self.is_valid(orders, p)
            if ok:
                mid = math.floor(len(p) / 2)
                result += p[mid]

        return result

    def calc_2(self, data: [str]) -> int:
        result = 0
        corrected = []
        orders, prints = data
        for p in prints:
            if not self.is_valid(orders, p):
                fixed = self.is_valid_fix(orders, p)
                corrected.append(fixed)

        for p in corrected:
            mid = math.floor(len(p) / 2)
            result += p[mid]

        return result


    def is_valid_fix(self, orders, p):
        start = p
        while True:
            ok = True
            for i in range(len(start)):
                page = start[i]
                if page in orders:
                    previous: [] = start[0:i]
                    for j in orders[page]:
                        if j in previous:
                            ok = False
                            pos = previous.index(j)
                            start=previous[0:pos] + previous[pos+1:] + [page] + [j] + start[i+1:]
                            break
            if ok:
                return start

    def is_valid(self, orders, p):
        ok = True
        for i in range(len(p)):
            page = p[i]
            if page in orders:
                previous = p[0:i]
                for j in orders[page]:
                    if j in previous:
                        ok = False
                        break
            if not ok:
                break
        return ok

    def load_handler_part1(self, data: [str]) -> [str]:
        ordering = {}
        pos = 0
        while True:
            d = data[pos]
            if d == "":
                break
            orders = d.split("|")
            l = int(orders[0])
            r = int(orders[1])
            if l not in ordering:
                ordering[l] = []
            ordering[l].append(r)
            pos+=1

        prints = []
        pos+=1
        while pos < len(data):
            prints.append([int(x) for x in data[pos].split(",")])
            pos+=1

        return ordering, prints

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc202405()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
