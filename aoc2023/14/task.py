"""
AOC Day 10
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math

class Aoc2023010(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict) -> int:
        tray, rocks = data
        self.north(rocks, tray)

        result = self.calc_score(tray)

        return result

    def calc_score(self, tray):
        row_count = len(tray)
        result = 0
        for r in tray:
            r_row = sum(r) * row_count
            result += r_row
            row_count -= 1
        return result

    def north(self, rocks, tray):
        for row in range(1, len(tray)):
            for col in range(0, len(tray[0])):
                for height in range(row, 0, -1):
                    if tray[height][col] == 1 and tray[height - 1][col] == 0 and (height - 1, col) not in rocks:
                        tray[height - 1][col] = 1
                        tray[height][col] = 0

    def south(self, rocks, tray):
        for row in range(len(tray)-2, -1, -1):
            for col in range(0, len(tray[0])):
                for height in range(row, len(tray) -1):
                    if tray[height][col] == 1 and tray[height + 1][col] == 0 and (height + 1, col) not in rocks:
                        tray[height + 1][col] = 1
                        tray[height][col] = 0

    def west(self, rocks, tray):
        col_count = len(tray[0])
        row_count = len(tray)
        for col in range(1, col_count):
            for row in range(row_count):
                for col_pos in range(col_count-1, 0, -1):
                    if tray[row][col_pos] == 1 and tray[row][col_pos - 1] == 0 and (row, col_pos - 1) not in rocks:
                        tray[row][col_pos - 1] = 1
                        tray[row][col_pos] = 0

    def east(self, rocks, tray):
        col_count = len(tray[0])
        row_count = len(tray)
        for col in range(col_count -2, -1, -1):
            for row in range(row_count):
                for col_pos in range(col, col_count - 1):
                    if tray[row][col_pos] == 1 and tray[row][col_pos + 1] == 0 and (row, col_pos + 1) not in rocks:
                        tray[row][col_pos + 1] = 1
                        tray[row][col_pos] = 0

    def calc_2(self, data: [str]) -> int:
        tray, rocks = data
        history = []
        same = False
        while not same:
            self.north(rocks, tray)
            self.west(rocks, tray)
            self.south(rocks, tray)
            self.east(rocks, tray)
            snapshot = ""
            for row in tray:
                for col in row:
                    snapshot += str(col)
            history.append(snapshot)
            history_len = len(history)
            if history_len == 1:
                continue
            history_middle = math.floor(history_len / 2)
            for size in range(history_middle, 0,  -1):
                first_index_start = history_len - size
                second_index_start = history_len - size*2
                first = history[first_index_start: ]
                second = history[second_index_start: first_index_start]
                same = True
                for i in range(len(first)):
                    if first[i] != second[i]:
                        same = False
                        break
                if same:
                    pos = (1000000000 - second_index_start) % len(first)
                    new_tray_string = first[pos-1]
                    pos = 0
                    result = 0
                    for x in range(len(tray), 0, -1):
                        row_total = 0
                        for y in range(len(tray[0])):
                            if new_tray_string[pos] == "1":
                                row_total += 1
                            pos +=1
                        result += row_total * x

                    return result
        total = 0
        return total

    def load_handler_part1(self, data: [str]) -> [str]:
        result = []
        rocks = {}
        row = 0
        for d in data:
            line = [0] * len(d)
            pos = 0
            for r in d:
                if r == 'O':
                    line[pos] = 1
                elif r =='#':
                  rocks[(row, pos)] = True
                pos += 1
            result.append(line)
            row += 1
        return result, rocks

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)

    def get_value(self, x):
        if x == "O":
            return 1
        else:
            return 0


if __name__ == '__main__':
    configure()
    aoc = Aoc2023010()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
