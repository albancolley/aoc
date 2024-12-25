"""
AOC Day X
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math


class Aoc201714(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: ()) -> int:
        input_list, lengths = data

        count = 0
        for i in range(128):
            row = lengths + [ord('-')] + [ord(s) for s in str(i)]
            row += [17, 31, 73, 47, 23]
            result = self.knotasbinary(input_list, row)
            count += list(result).count("1")
        return count

    def knotasbinary(self, input_list, lengths):
        input_list_length = len(input_list)
        step = 0
        current_pos = 0
        for i in range(64):
            for length in lengths:
                new_string: [int] = input_list.copy()
                for i in range(length):
                    new_pos = (current_pos + i) % input_list_length
                    reverse_pos = (current_pos + length - i - 1) % input_list_length
                    new_string[new_pos] = input_list[reverse_pos]
                input_list = new_string
                current_pos = (current_pos + length + step) % input_list_length
                step += 1
        xors = [0] * 16
        for i in range(16):
            xors[i] = input_list[i * 16]
            for j in range(i * 16 + 1, i * 16 + 16):
                xors[i] ^= input_list[j]
        result = ''.join([f'{x:0>08b}' for x in xors])
        return result

    def calc_2(self, data: [str]) -> int:
        input_list, lengths = data
        count = 0
        grid = []
        for i in range(128):
            row = lengths + [ord('-')] + [ord(s) for s in str(i)]
            row += [17, 31, 73, 47, 23]
            result = self.knotasbinary(input_list, row)
            grid.append(list(result))

        grid2 = []
        for x in range(128):
            grid2.append([0] * 128)


        group = 1
        for y in range(0, 128):
            for x in range(0, 128):
                new_group_left = grid2[y][x - 1]
                if grid[y][x] == '1':
                    if y > 0:
                        new_group_up = grid2[y - 1][x]
                        if new_group_up != 0 and new_group_up != group:
                            for y2 in range(0, 128):
                                grid2[y2] = [x if x != new_group_up else group for x in grid2[y2]]
                    if x > 0:
                        if new_group_left != 0 and new_group_left != group:
                            for y2 in range(0, 128):
                                grid2[y2] = [x if x != new_group_left else group for x in grid2[y2]]
                    grid2[y][x] = group
                group += 1

        counts: set = set()
        for y in range(0, 128):
            for x in range(0, 128):
                counts.add(grid2[y][x])

        return len(counts) -1

    def load_handler_part1(self, data: [str]) -> [str]:
        input_list = [i for i in range(256)]
        lengths = []
        if len(data) != 0:
            for i in data[0].strip():
                lengths += [ord(i)]
        return input_list, lengths

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201714()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
