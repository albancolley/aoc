"""
AOC Day 10
"""
import sys
from collections import defaultdict
from typing import Any

from common import AocBase
from common import configure
import collections


class Aoc2023010(AocBase):
    """
    AOC Day 10 Class
    """

    moves = {'D': (0, 1), 'U': (0, -1), 'R': (1, 0), 'L': (-1, 0),
             '1': (0, 1), '3': (0, -1), '0': (1, 0), '2': (-1, 0)}

    full_moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def calc_1(self, data: dict) -> int:
        return self.calc_2(data)
        result = 0
        position = (0, 0)
        hole = {position: True}
        min_point = (0, 0)
        max_point = (0, 0)
        for d in data:
            direction = d[0]
            steps = d[1]
            for i in range(steps):
                move = self.moves[direction]
                position = (position[0] + move[0], position[1] + move[1])
                min_point = (min(min_point[0], position[0]), min(min_point[1], position[1]))
                max_point = (max(max_point[0], position[0]), max(max_point[1], position[1]))
                hole[position] = True

        q = [(1, 1)]
        seen = set()
        seen.add((1, 1))
        # for i in hole:
        #     seen.add(i)
        while len(q) > 0:
            position = q.pop()
            for move in self.full_moves:
                new_position = (position[0] + move[0], position[1] + move[1])
                if new_position not in seen:
                    if position not in hole:
                        seen.add(new_position)
                        q.insert(0, new_position)

        for i in seen:
            hole[i] = True

        self.view(hole, max_point, min_point)
        return len(hole)

    def view(self, hole, max_point, min_point):
        for y in range(min_point[1], max_point[1] + 1):
            line = ""
            for x in range(min_point[0], max_point[0] + 1):
                if (x, y) == (0, 0):
                    line += "S"
                elif (x, y) in hole:
                    line += "#"
                else:
                    line += "."
            print(line)

    def calc_2(self, data: [str]) -> int:
        result = 0
        position = (0, 0)
        x_index = set()
        x_lookup: defaultdict[Any, list] = collections.defaultdict(list)
        min_point = (0, 0)
        max_point = (0, 0)
        edge_length = 0
        for d in data:
            direction = d[0]
            steps = d[1]
            edge_length += steps
            move = self.moves[direction]
            end_position = (position[0] + move[0] * steps, position[1] + move[1] * steps)
            min_point = (min(min_point[0], position[0]), min(min_point[1], position[1]))
            max_point = (max(max_point[0], position[0]), max(max_point[1], position[1]))
            if move[1] != 0:
                x = end_position[0]
                x_index.add(x)
                r = (min(position[1], end_position[1]), max(position[1], end_position[1]))
                x_lookup[x].append(r)
            position = end_position

        x_index = sorted(x_index)
        # print(x_index)
        for x in x_lookup:
            x_lookup[x] = sorted(x_lookup[x])

        # for x in x_index[-10:]:
        #     print(x, x_lookup[x])

        total = 0

        last_ranges = []
        end = 0
        for i in range(len(x_index) - 1):
            x = x_index[i]
            new_ranges, removed_count, range_length = self.interect(last_ranges, x_lookup[x])
            area = 0
            if i < len(x_index) - 1:
                area += range_length * (x_index[i + 1] - x)
                end = x_index[i + 1]
            area += removed_count
            # print(x, end, new_ranges, last_ranges, removed_count, range_length, area)
            total += area
            last_ranges = new_ranges

        for r in new_ranges:
            t = r[1] - r[0] + 1
            total += t

        return total

    def interect(self, last_ranges_in, new_ranges_in):
        merged_ranges = []
        removed_count = 0

        last_ranges = last_ranges_in.copy()
        new_ranges = new_ranges_in.copy()

        if len(last_ranges_in) > 0 and len(new_ranges_in) > 0:
            last_range = last_ranges.pop(0)
            new_range = new_ranges.pop(0)
            while True:
                if new_range[1] <= last_range[0]:
                    # new range ends before last range
                    merged_ranges.append(new_range)
                    if len(new_ranges) == 0:
                        merged_ranges.append(last_range)
                        break
                    new_range = new_ranges.pop(0)
                elif last_range[1] <= new_range[0]:
                    # last range end before new range
                    merged_ranges.append(last_range)
                    if len(last_ranges) == 0:
                        merged_ranges.append(new_range)
                        break
                    last_range = last_ranges.pop(0)
                # Overlaps
                elif new_range[0] < last_range[0]:
                    merged_ranges.append((new_range[0], last_range[0]))
                    new_range = (last_range[0], new_range[1])

                elif last_range[0] < new_range[0]:
                    merged_ranges.append((last_range[0], new_range[0]))
                    last_range = (new_range[0], last_range[1])

                elif last_range[0] == new_range[0] and last_range[1] < new_range[1]:
                    removed_count += last_range[1] - last_range[0]
                    new_range = (last_range[1], new_range[1])
                    if len(last_range) == 0:
                        merged_ranges.append(new_range)
                        break
                    last_range = last_ranges.pop(0)

                elif last_range[0] == new_range[0] and new_range[1] < last_range[1]:
                    removed_count += new_range[1] - new_range[0] - 1
                    last_range = (new_range[1], last_range[1])
                    if len(new_ranges) == 0:
                        merged_ranges.append(last_range)
                        break
                    new_range = new_ranges.pop(0)

                elif last_range[0] == new_range[0] and new_range[1] == last_range[1]:
                    removed_count += new_range[1] - new_range[0] + 1
                    if len(last_ranges) == 0 or len(new_ranges) == 0:
                        break
                    new_range = new_ranges.pop(0)
                    last_range = last_ranges.pop(0)

        for r in new_ranges:
            merged_ranges.append(r)

        for r in last_ranges:
            merged_ranges.append(r)

        merged_ranges = self.merge_ranges(merged_ranges)

        range_length = 0
        for r in merged_ranges:
            range_length += r[1] - r[0] + 1

        return merged_ranges, removed_count, range_length

    def merge_ranges(self, ranges):
        if len(ranges) == 0:
            return []
        if len(ranges) == 1:
            return [(ranges[0][0], ranges[0][1])]
        ranges_sorted = sorted(ranges)
        start, end = ranges_sorted[0]
        merged = []
        for r in ranges_sorted[1:]:
            new_start, new_end = r
            if new_start != end:
                merged.append((start, end))
                start = new_start
                end = new_end
            else:
                end = new_end
        if new_end:
            merged.append((start, new_end))
        else:
            merged.append((start, end))
        return merged

    def load_handler_part1(self, data: [str]) -> [str]:
        result = []
        for line in data:
            s = line.split()
            result.append((s[0], int(s[1])))
        return result

    def load_handler_part2(self, data: [str]) -> [str]:
        result = []
        for line in data:
            s = line.split()
            command = s[2]
            hex = command[2:7]
            direction = command[7:-1]
            result.append((direction, int(hex, 16)))
        return result


if __name__ == '__main__':
    configure()
    aoc = Aoc2023010()
    failed, results = aoc.run("part1_[1-9]+.txt", "part2x_[1-9]+.txt")
    if failed:
        sys.exit(1)
