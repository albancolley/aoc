"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure


class Aoc201900(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: tuple[str, list[str]]) -> int:
        initial_state, spreads = data
        current_line = initial_state
        pos = current_line.index('#')
        current_line = current_line[pos:]
        for i in range(0, 20):
            pos -= 2

            current_line = "...." + current_line  + "...."
            new_line = ""
            for j in range(0, len(current_line) - 4):
                if current_line[j:j + 5] in spreads:
                    new_line += "#"
                else:
                    new_line += "."

            index = new_line.index('#')
            pos += index

            current_line = new_line[index:].strip(".")
            # print(pos)

        total = 0
        for c in current_line:
            if c == "#":
                total += pos
            pos += 1
        return total

    def calc_2(self, data: [str]) -> int:
        initial_state, spreads = data
        current_line = initial_state
        current_line = "...." + current_line + "...."
        # print(initial_state, spreads)
        pos = -4
        history = {}
        i = 0
        while True:
            pos -= 2

            current_line = "...." + current_line + "...."
            new_line = ""
            for j in range(0, len(current_line) - 4):
                if current_line[j:j + 5] in spreads:
                    new_line += "#"
                else:
                    new_line += "."

            index = new_line.index('#')
            pos += index

            i += 1

            current_line = new_line[index:].strip(".")
            if new_line.strip(".") in history:
                # print(i, pos, new_line.strip("."))
                pos = 50000000000 - (i - pos)
                break
            history[new_line.strip(".")] = pos
            # print(pos)

        total = 0
        for c in current_line:
            if c == "#":
                total += pos
            pos += 1
        return total

    def load_handler_part1(self, data: [str]) -> [str]:
        initial_state = data[0][15:]
        spreads = []
        line : str
        for line in data[2:]:
            if line[-1] == '#':
                spreads += [line[0:5]]

        return initial_state, spreads

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201900()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
