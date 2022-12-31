import dataclasses
import math
import os.path
import string
import sys
import heapq

import numpy as np

from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
from dataclasses import dataclass
import re
from collections import deque
import operator

logger = logging.getLogger("ACO2022-17")

moves = {
    "^": (0, 1),
    "v": (0, -1),
    "<": (-1, 0),
    ">": (1, 0),
    "" : (0,0)
}


# class definition
class Entry:

    # constructor
    def __init__(self, d, p, path):
        self.distance = d
        self.position = p
        self.path = path

    # # override the comparison operator
    def __lt__(self, nxt):
        if self.distance == nxt.distance:
            return len(self.path) < len(nxt.path)

        return self.distance < nxt.distance

    # def __lt__(self, nxt):
    #       return self.distance > nxt.distance
    #
    # def __lt__(self, nxt):
    #         return self.distance + len(self.path) < nxt.distance + len(nxt.path)


class MyHeap(object):
    def __init__(self, initial=None, key=lambda x : x):
        self.key = key
        self.index = 0
        if initial:
            self._data = [(key(item), i, item) for i, item in enumerate(initial)]
            self.index = len(self._data)
        else:
            self._data = []
        heapq.heapify(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, item):
        heapq.heappush(self._data, (item.distance + len(item.path), self.index, item))
        self.index += 1

    def pop(self):
        return heapq.heappop(self._data)[2]

class Aoc202212(AocBase):


    def output(self, site, width, height, r, position):
        print(f'Round: {r}')
        for y in range(height, -1, -1):
            line = ""
            for x in range(0, width + 1):
                if position == (x, y):
                    line += "E"
                    continue
                loc = site[(x, y)]
                if isinstance(loc, list):
                    l = len(loc)
                    if l > 1:
                        line += str(l)
                    elif l == 1:
                        line += loc[0]
                    else:
                        line += "."
                else:
                    line += loc
            print(line)
        print()

    def calc_1(self, data) -> int:
        site, start_position, end_position, width, height = data


        position = start_position
        self.output(site, width, height, 0, position)
        #paths = []
        seen = {}
        #heapq.heapify(paths)
        e = Entry(math.dist([end_position[0], end_position[1]], [position[1], position[1]]),
            position, [position])
        myheap = MyHeap(key=lambda a: a.distance)
        myheap.push(e)
        #heapq.heappush(paths, e)
        min_path_length = math.inf
        sites = {0: site}
        self.output(site, width, height, 0, position)

        seen[(position[0], position[1], 1)] = True
        while not myheap.is_empty():
            e = myheap.pop()
            if len(e.path) == min_path_length:
                continue

            #e = paths.popleft()
            # position, path = paths.popleft()
            position = e.position
            path = e.path
            if len(path) not in sites:
                for i in range(1, len(path) + 1):
                    if i not in sites:
                        sites[i] = self.move(sites[i - 1], width, height)
            next_site = sites[len(path)]
            next_positions = self.get_positions(next_site, position, width, height, end_position, start_position)
            for next_position in next_positions:
                new_path = path[:]
                new_path.append(next_position)
                new_pos = (next_position[0], next_position[1], len(new_path))
                if new_pos in seen:
                    continue

                seen[new_pos] = True

                if next_position == end_position:
                    if len(new_path) < min_path_length:
                        min_path_length = len(new_path)
                        min_path = new_path
                        print(min_path_length, min_path)
                    continue
                if len(new_path) > min_path_length:
                    continue


                e = Entry(math.dist([end_position[0], end_position[1]], [next_position[0], next_position[1]]),
                           next_position, new_path)
                myheap.push(e)

        # count = 0
        # for pos in min_path:
        #     self.output(sites[count], width, height, count, pos)
        #     count += 1

        print(min_path_length, min_path)
        return min_path_length -1

    def move(self, site, width, height):
        new_site = {}
        for y in range(height, -1, -1):
            for x in range(0, width):
                new_site[(x, y)] = []
        for point in site:
            value = site[point]
            if isinstance(value, list):
                if len(value) != 0:
                    for direction in value:
                        new_point = tuple(map(operator.add, point, moves[direction]))
                        x, y = new_point
                        if direction == "<" and x == 0:
                             new_point = (width - 1, y)
                        if direction == ">" and x == width:
                            new_point = (1, y)
                        if direction == "^" and y == height:
                            new_point = (x, 1)
                        if direction == "v" and y == 0:
                            new_point = (x, height - 1)
                        new_site[new_point].append(direction)
            else:
                new_site[point] = "#"

        return new_site

    def get_positions(self, site, position, width, height, end_position, start_position):
        new_positons = []
        for move in moves:
            m = moves[move]
            new_point = tuple(map(operator.add, position, m))
            x, y = new_point
            # if new_point == end_position:
            #     new_positons.append(new_point)
            #     continue
            if x < 0:
                continue
            if y < 0:
                continue
            if x > width:
                continue
            if y > height:
                continue
            if len(site[x, y]) == 0:
                new_positons.append(new_point)

        # sorted_positions = sorted(new_positons, key=lambda pos: math.dist([pos[0], position[0]], [pos[1], position[1]]))
        sorted_positions = new_positons

        return sorted_positions

    def get_points(self, grove):
        points = set()
        for pos in grove:
            points.add(pos)
        return points

    def calc_2(self, data: []) -> int:
        site, o_start_position, o_end_position, width, height = data

        trips = [(o_start_position, o_end_position), (o_end_position, o_start_position),  (o_start_position, o_end_position)]
        final_length = 0
        sites = {0: site}
        min_path = [o_start_position]
        for trip in trips:
            min_path_length = math.inf
            start_position = trip[0]
            position = trip[0]
            end_position = trip[1]
            seen = {}
            e = Entry(math.dist([end_position[0], end_position[1]], [position[1], position[1]]),
                      position, min_path)
            my_heap = MyHeap(key=lambda a: a.distance)
            my_heap.push(e)
            new_pos = (start_position[0], start_position[1], len(min_path))
            seen[new_pos] = True
            while not my_heap.is_empty():
                e = my_heap.pop()
                if len(e.path) == min_path_length:
                    continue

                # e = paths.popleft()
                # position, path = paths.popleft()
                position = e.position
                path = e.path
                if len(path) not in sites:
                    for i in range(1, len(path) + 1):
                        if i not in sites:
                            sites[i] = self.move(sites[i - 1], width, height)
                next_site = sites[len(path)]
                next_positions = self.get_positions(next_site, position, width, height, end_position, start_position)
                for next_position in next_positions:
                    new_path = path[:]
                    new_path.append(next_position)
                    new_pos = (next_position[0], next_position[1], len(new_path))
                    if new_pos in seen:
                        continue

                    seen[new_pos] = True

                    if next_position == end_position:
                        if len(new_path) < min_path_length:
                            min_path_length = len(new_path)
                            min_path = new_path
                            print(min_path_length, min_path)
                        continue
                    if len(new_path) > min_path_length:
                        continue

                    e = Entry(math.dist([end_position[0], end_position[1]], [next_position[0], next_position[1]]),
                              next_position, new_path)
                    my_heap.push(e)

            print(min_path_length)
            final_length += min_path_length

        return min_path_length - 1

    def load_handler_part1(self, data: [(int, int)]) -> {}:

        result = {}
        y = len(data) - 1
        x = 0
        for row in data:
            for c in row:
                if y == len(data) - 1 and  c == '.':
                    start_x = x
                    result[(x, y)] = []
                elif y == 0 and c == '.':
                    endt_x = x
                    result[(x, y)] = []
                elif c in ['<', '>', '^', 'v']:
                    result[(x, y)] = [c]
                elif c == ".":
                    result[(x, y)] = []
                else:
                    result[(x, y)] = c
                x += 1
            x = 0
            y -= 1
        return result, (start_x, len(data) - 1), (endt_x, 0), len(data[1]) -1, len(data) - 1

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)

    # def distance(self, pos, end_position):
    #     dis = (pos[0] - end_position[0]) * (pos[0] - end_position[0])
    #     dis += (pos[1] - end_position[1]) * (pos[1] - end_position[1])
    #     math.sqrt()


if __name__ == '__main__':
    configure()
    aoc = Aoc202212()
    failed, results = aoc.run("part1x_[1-1]+.txt", "part2_[1-2]+.txt")
    if failed:
        exit(1)
