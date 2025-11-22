"""
AOC Day X
"""
import dataclasses
import sys
from collections import defaultdict, Counter

from common import AocBase
from common import configure

@dataclasses.dataclass
class Grid:
    grid: dict[complex, str]
    width: int
    height: int

class Aoc201818(AocBase):
    """
    AOC Day 10 Class
    """
    MOVES: list[complex] = [
        -1 - 1j,
        -1 + 0j,
        -1 + 1j,
        0 - 1j,
        0 + 1j,
        1 - 1j,
        1 + 0j,
        1 + 1j,
    ]

    def calc_1(self, grid: Grid) -> int:
        # self.view_grid(grid)

        history: dict[str, int] = dict()

        for minute in range(10):
            grid = self.grow(grid)

        cnt = Counter(grid.grid.values())
        result = cnt['#'] * cnt["|"]
        return result

    def grow(self, grid):
        new_grid = Grid(grid.grid.copy(), grid.width, grid.height)
        for g in grid.grid:
            value = grid.grid[g]
            if value == "+":
                continue

            counts: dict[str, int] = defaultdict(int)
            for move in self.MOVES:
                counts[grid.grid[g + move]] += 1

            match value:
                case ".":
                    if counts["|"] >= 3:
                        new_grid.grid[g] = "|"
                case "|":
                    if counts["#"] >= 3:
                        new_grid.grid[g] = "#"
                case "#":
                    if counts["#"] >= 1 and counts['|'] >= 1:
                        new_grid.grid[g] = "#"
                    else:
                        new_grid.grid[g] = "."
        grid = new_grid
        return grid

    def calc_2(self, grid: [str]) -> int:
        history: dict[str, int] = dict()
        history_grid: dict[int, Grid] = dict()
        minute = 1
        while True:
            grid = self.grow(grid)
            history_grid[minute] = grid
            flat = self.flat_grid(grid)
            if flat in history:
                repeat_start = history[flat]
                repeat_end = minute
                repeat_length = repeat_end - repeat_start
                final_minute = (1000000000 - repeat_start) % repeat_length
                print(repeat_start, repeat_end, repeat_length, final_minute)
                cnt = Counter(history_grid[repeat_start + final_minute].grid.values())
                result = cnt['#'] * cnt["|"]
                # 148608 too low  542531 to high  522116 to high not 204714
                return result
            history[flat] = minute
            minute += 1
            # self.view_grid(grid)



    def flat_grid(self, grid: Grid) -> str:
        line: str = ""
        for y in range(grid.height):
            for x in range(grid.width):
                value: str  = grid.grid[complex(x, y)]
                line += value

        return line


    def view_grid(self, grid: Grid):
        for y in range(grid.height):
            line: str = ""
            for x in range(grid.width):
                line += grid.grid[complex(x, y)]
            print(line + "    " + ", ".join(detail))

    def load_handler_part1(self, data: [str]) -> [Grid]:
        grid: dict[complex, str] = dict()
        line: str
        height = len(data) + 2
        width = len(data[0]) + 2
        y = 1
        for line in data:
            x = 1
            for c in line:
                grid[complex(x, y)] = c
                x += 1
            y += 1

        for x in range(0, width+1):
            grid[complex(x, 0)] = "+"
            grid[complex(x, height-1)] = "+"

        for y in range(0, height+1):
            grid[complex(0, y)] = "+"
            grid[complex(width-1, y)] = "+"

        return Grid(grid, width, height)

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201818()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
