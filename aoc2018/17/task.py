"""
AOC Day X
"""
import sys

from networkx.algorithms.threshold import right_d_threshold_sequence

from common import AocBase
from common import configure


class Aoc201900(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict) -> int:
        reservoir, low_bounds, upper_bounds = data
        start_positions = [complex(500,0)]

        min_x, min_y = low_bounds
        max_x, max_y = upper_bounds

        # self.show_reservoir(reservoir, low_bounds, upper_bounds)

        water = {}

        while len(start_positions) > 0:
            pos = start_positions.pop(0)
            if pos == complex(615, 1376):
                pass
            start_pos = self.down(low_bounds, reservoir, pos, upper_bounds, water)

            if not start_pos:
                continue

            # if int(start_pos.imag) == max_y:
            #     continue

            while True:
                holes = []
                hole, left = self.horizontal(-1, reservoir, start_pos, water, low_bounds, upper_bounds)
                holes += hole
                hole, right  = self.horizontal(1, reservoir, start_pos, water, low_bounds, upper_bounds)
                holes += hole
                if len(holes) > 0:
                    start_positions += holes
                    break
                else:
                    water[left] = "~"
                    while left != right:
                        left += 1
                        water[left] = "~"

                    start_pos -= 1j

        result = 0
        for w in water:
            if w.imag >= min_y:
                result += 1
        # self.show_reservoir(reservoir, water, low_bounds, upper_bounds)
        # not 1042
        return result

    def not_in_bounds(self, next_pos, low_bounds, upper_bounds):
        x = int(next_pos.real)
        y = int(next_pos.imag)
        min_x, min_y = low_bounds
        max_x, max_y = upper_bounds

        # if x < min_x or x > max_x:
        #     return True

        if y < 0 or y > max_y:
            return True

        return False

    def down(self, low_bounds, reservoir, start_pos, upper_bounds, water):
        while True:
            next_pos = start_pos + 1j
            if next_pos in water:
                if water[next_pos] == "~":
                    return next_pos
                else:
                    return None
            if next_pos in reservoir:
                return start_pos
            if self.not_in_bounds(next_pos, low_bounds, upper_bounds):
                return None
            if next_pos.imag == 1377.0:
                pass
            water[next_pos] = "|"
            # self.show_reservoir(reservoir, low_bounds, upper_bounds)
            start_pos = next_pos

    def horizontal(self, direction, reservoir, start_pos, water, low_bounds, upper_bounds):
        pos = start_pos + direction
        if start_pos not in reservoir:
            pos = start_pos
        while True:
            if pos in reservoir:
                return [], pos - direction
            water[pos] = "|"
            pos_below = pos + 1j
            if pos_below in water and water[pos_below] == "~":
                pos = pos + direction
                continue
            if pos_below not in reservoir:
                water[pos] = "|"
                # self.show_reservoir(reservoir, low_bounds, upper_bounds)
                if pos.imag == 1377.0:
                    pass
                return [pos], pos
            # self.show_reservoir(reservoir, low_bounds, upper_bounds)
            pos = pos + direction

    def show_reservoir(self, reservoir, water, low_bounds, upper_bounds ):
        min_x, min_y = low_bounds
        max_x, max_y = upper_bounds
        for y in range(min_y-1, max_y+2):
            line = ""
            for x in range(min_x-1, max_x+2):
                pos = complex(x,y)
                if pos in water:
                    line += water[pos]
                elif pos in reservoir:
                    line += reservoir[pos]
                else:
                    line += " "
            print(line)


    def calc_2(self, data: [str]) -> int:
        reservoir, low_bounds, upper_bounds = data
        start_positions = [complex(500, 0)]

        min_x, min_y = low_bounds
        max_x, max_y = upper_bounds

        # self.show_reservoir(reservoir, low_bounds, upper_bounds)

        water = {}

        while len(start_positions) > 0:
            pos = start_positions.pop(0)
            if pos == complex(615, 1376):
                pass
            start_pos = self.down(low_bounds, reservoir, pos, upper_bounds, water)

            if not start_pos:
                continue

            # if int(start_pos.imag) == max_y:
            #     continue

            while True:
                holes = []
                hole, left = self.horizontal(-1, reservoir, start_pos, water, low_bounds, upper_bounds)
                holes += hole
                hole, right = self.horizontal(1, reservoir, start_pos, water, low_bounds, upper_bounds)
                holes += hole
                if len(holes) > 0:
                    start_positions += holes
                    break
                else:
                    water[left] = "~"
                    while left != right:
                        left += 1
                        water[left] = "~"

                    start_pos -= 1j

        result = 0
        for w in water:
            if w.imag >= min_y and water[w] == "~":
                result += 1
        # self.show_reservoir(reservoir, water, low_bounds, upper_bounds)
        # not 1042
        return result

    def load_handler_part1(self, data: list[str]) -> tuple[dict[complex, str], tuple[int, int], tuple[int, int]]:
        reservoir: dict[complex, str] = dict()
        min_y = 1000000
        max_y = 0
        min_x = 1000000
        max_x = 0
        line: str
        for line in data:
            parts: list[str] = line.split(", ")
            left: list[str] = parts[0].split("=")
            right: list[str] = parts[1].split("=")
            if left[0] =='y':
                y:int = int(left[1])
                min_y = min(y, min_y)
                max_y = max(y, max_y)
                xs = right[1].split('..')
                x_start = int(xs[0])
                x_end = int(xs[1])
                if x_start > x_end:
                    x_temp = x_start
                    x_start = x_end
                    x_end = x_temp
                for x in range(x_start, x_end+1):
                    min_x = min(x, min_x)
                    max_x = max(x, max_x)
                    reservoir[complex(x,y)] = "#"
            if left[0] == 'x':
                x = int(left[1])
                min_x = min(x, min_x)
                max_x = max(x, max_x)
                ys = right[1].split('..')
                y_start = int(ys[0])
                y_end = int(ys[1])
                if y_start > y_end:
                    y_temp = y_start
                    y_start = y_end
                    y_end = y_temp
                y: int
                for y in range(y_start, y_end + 1):
                    min_y = min(y, min_y)
                    max_y = max(y, max_y)
                    reservoir[complex(x, y)] = "#"

        # for x in range(min_x-1, max_x+2):
        #     reservoir[complex(x, min_y-1)] = "#"
        #     reservoir[complex(x, max_y+1)] = "#"

        # for y in range(min_y-1, max_y+2):
        #     reservoir[complex(min_x-1, y)] = "#"
        #     reservoir[complex(max_x+1), y] = "#"


        return reservoir, (min_x, min_y), (max_x, max_y)

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)



if __name__ == '__main__':
    configure()
    aoc = Aoc201900()
    failed, results = aoc.run("part1_[1-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
