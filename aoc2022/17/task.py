import os.path
import string

from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
import re
from collections import deque


logger = logging.getLogger("ACO2022-17")


class Aoc202212(AocBase):

    def hit(self, rock, chamber, position):
        for i in range(0, len(rock)):
            if chamber[position+i] & rock[i] != 0:
                return True
        return False

    def output(self, chamber):
        print()
        output = []
        for row in chamber:
            output.insert(0, '{:09b}'.format(row))
        for row in output:
7            print(row)
        print()


    def calc_1(self, data) -> int:
        return self.calc(data,2022)

    def calc(self, data, rock_count):
        rocks, jets = data

        chamber = {}
        full_row = int('111111111', 2)
        empty_row = int('100000001', 2)
        chamber[0] = full_row
        count = 0
        rock_index = 0
        jet_index = 0
        max_rock_height = 0
        history = []
        history_jets = []
        ending_chamber_pos = 0
        calculated_chamber_height = 0
        heights = []
        while count < rock_count:
            rock = rocks[rock_index]
            chamber_pos = max_rock_height
            if rock_index == 0:
                current = (count, chamber_pos, jet_index)
                history.append(current)
                history_jets.append(jet_index)
                history_jets_copy = history_jets[:]
                pos = 0
                while len(history_jets_copy) > 1:
                    mid_point = int(len(history_jets_copy)/2)
                    first_half = history_jets_copy[0:mid_point]
                    second_half = history_jets_copy[mid_point:]
                    if first_half == second_half:
                        first = history[pos]
                        second = history[pos + len(first_half)]
                        a = first[0]
                        b = second[0] - first[0]
                        c = second[1] - first[1]
                        d = first[1]
                        number_of_loops = int((rock_count - a)/b)
                        remainder = (rock_count - a) % b
                        return number_of_loops*c + d + heights[a + remainder -1] - d
                    history_jets_copy = history_jets_copy[1:]
                    pos += 1
            for i in range(chamber_pos, chamber_pos + 3 + len(rock) + 1):
                if i > len(chamber) - 1:
                    chamber[i] = empty_row
            chamber_pos += 4
            while True:
                new_rock = []
                match jets[jet_index]:
                    case "<":
                        for row in rock:
                            new_rock.append(row << 1)
                    case ">":
                        for row in rock:
                            new_rock.append(row >> 1)

                jet_index = (jet_index + 1) % len(jets)

                if not self.hit(new_rock, chamber, chamber_pos):
                    rock = new_rock

                if self.hit(rock, chamber, chamber_pos - 1):
                    for i in range(0, len(rock)):
                        chamber[chamber_pos + i] = chamber[chamber_pos + i] | rock[i]
                    max_rock_height = max(chamber_pos + i, max_rock_height)
                    chamber_pos += len(rock)
                    heights.append(max_rock_height)
                    break

                chamber_pos -= 1

            # self.output(chamber)

            rock_index = (rock_index + 1) % len(rocks)
            count += 1
        total = 0
        for i in range(len(chamber) - 1, -1, -1):
            if chamber[i] != 257:
                total = i
                break
        result = total - ending_chamber_pos + calculated_chamber_height
        return result

    def calc_2(self, data: [str]) -> int:
        return self.calc(data, 1000000000000)


    def load_handler_part1(self, data: [str]) -> {}:
        rocks =[]
        rock =[]
        for row in data:
            if row == "":
                rocks.append(rock)
                rock = []
            elif "<" in row or ">" in row:
                return rocks, row
            else:
                bin_rock = "0" * 3
                bin_rock += row.replace('.', '0').replace('#', '1')
                bin_rock += "0" * (9 - len(bin_rock))
                rock.insert(0, int(bin_rock, 2))
        return [], ""

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc202212()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        exit(1)
