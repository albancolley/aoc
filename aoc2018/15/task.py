"""
AOC Day X
"""
import sys
from dataclasses import dataclass

from common import AocBase
from common import configure

@dataclass
class Unit:
    type: str
    attack_power: int
    hit_points: int

@dataclass
class Grid:
    grid: dict[complex, Unit]
    width: int
    height: int


MOVES: list[complex] = [
    0 - 1j,

    -1 + 0j,
    1 + 0j,
    0 + 1j,
]

class Aoc201900(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, grid: Grid) -> int:
        # self.view_grid(grid)
        pos: complex
        finished = False
        count= 0
        while not finished:
            count += 1
            for pos in self.get_start_positions(grid):
                if grid.grid[pos].type == ".":
                    continue
                golbins = [x.type for x in grid.grid.values() if x.type == 'G']
                elfs = [x.type for x in grid.grid.values() if x.type == 'E']

                finished = len(golbins) == 0 or len(elfs) == 0
                if finished:
                    count -= 1
                    break


                if self.attack(pos, grid):
                    continue
                new_pos = self.move(pos, grid)
                self.attack(new_pos, grid)

            # print(count)
            # self.view_grid(grid)
            # golbins = [x.type for x in grid.grid.values() if x.type == 'G']
            # elfs = [x.type for x in grid.grid.values() if x.type == 'E']
            #
            # finished = len(golbins) == 0 or len(elfs) == 0

        # print(count, sum([x.hit_points for x in grid.grid.values() if x.type in ['G','E']]))
        total =  count * sum([x.hit_points for x in grid.grid.values() if x.type in ['G','E']])

        return total

    def attack(self, pos: complex, grid: Grid):
        target_type = 'E'
        if grid.grid[pos].type == 'E':
            target_type = 'G'

        target: complex = None
        min_hit_points = 201
        for move in MOVES:
            target_pos = pos + move
            # print(pos, move, target_pos)
            # print( grid.grid[target_pos])
            if grid.grid[target_pos].type != target_type:
                continue
            if grid.grid[target_pos].type == target_type and grid.grid[target_pos].hit_points < min_hit_points:
                target = target_pos
                min_hit_points = grid.grid[target_pos].hit_points

        if target:
            # print(target, pos)
            # print(grid.grid[target], grid.grid[pos])
            grid.grid[target].hit_points -= grid.grid[pos].attack_power
            if grid.grid[target].hit_points <= 0:
                grid.grid[target].type = '.'
            return True

        return False

    def move(self, unit_pos, grid) -> complex | None:
        new_pos = unit_pos

        target_type = 'E'
        if grid.grid[unit_pos].type == 'E':
            target_type = 'G'

        queue = []
        seen = [unit_pos]
        queue += [(unit_pos,None)]
        targets = []
        while len(queue) > 0:
            new_queue = []
            while len(queue) > 0:
                pos, path = queue.pop(0)
                for move in MOVES:
                    next_pos = move + pos
                    if next_pos in seen:
                        continue
                    seen += [next_pos]
                    if grid.grid[next_pos].type not in ['.', target_type]:
                        continue
                    if grid.grid[next_pos].type == target_type:
                        # targets += [path]
                        new_pos = path
                        temp = grid.grid[new_pos]
                        grid.grid[new_pos] = grid.grid[unit_pos]
                        grid.grid[unit_pos] = temp
                        return new_pos

                    new_path = path
                    if not new_path:
                        new_path = next_pos
                    new_queue += [(next_pos, new_path)]

            # if len(targets) > 0:
            #     break

            queue = new_queue

        return unit_pos
        # print(unit_pos, targets)
        if len(targets) == 0:
            return unit_pos

        targets.sort(key = lambda c: (c.imag, c.real))
        if len(targets) > 1:
            print(targets)

        new_pos = targets[0]
        temp = grid.grid[new_pos]
        grid.grid[new_pos] = grid.grid[unit_pos]
        grid.grid[unit_pos] = temp
        return new_pos



    def calc_2(self, org_grid: Grid) -> int:

        elves_count = len([x for x in org_grid.grid.values() if x.type == 'E'])

        elves_attach_power = 3

        while True:
            elves_attach_power += 1




            sub_grid: dict[complex, Unit] = dict()

            for g in org_grid.grid:
                orig_unit = org_grid.grid[g]
                sub_grid[g] = Unit(orig_unit.type, orig_unit.attack_power, orig_unit.hit_points)
                if sub_grid[g].type == "E":
                    sub_grid[g].attack_power = elves_attach_power

            grid: Grid = Grid(sub_grid, org_grid.width, org_grid.height)

            # self.view_grid(grid)
            pos: complex
            finished = False
            count = 0
            while not finished:
                count += 1
                for pos in self.get_start_positions(grid):
                    if grid.grid[pos].type == ".":
                        continue
                    golbins = [x.type for x in grid.grid.values() if x.type == 'G']
                    elfs = [x.type for x in grid.grid.values() if x.type == 'E']

                    if len(elfs) < elves_count:
                        finished = True
                        break

                    finished = len(golbins) == 0 or len(elfs) == 0
                    if finished:
                        count -= 1
                        break

                    if self.attack(pos, grid):
                        continue
                    new_pos = self.move(pos, grid)
                    self.attack(new_pos, grid)

            elfs = [x.type for x in grid.grid.values() if x.type == 'E']

            if len(elfs) == elves_count:
                total = count * sum([x.hit_points for x in grid.grid.values() if x.type in ['G', 'E']])
                return total

                # print(count)
                # self.view_grid(grid)
                # golbins = [x.type for x in grid.grid.values() if x.type == 'G']
                # elfs = [x.type for x in grid.grid.values() if x.type == 'E']

                # finished = len(golbins) == 0 or len(elfs) == 0

        print(count, sum([x.hit_points for x in grid.grid.values() if x.type in ['G','E']]))
        total = count * sum([x.hit_points for x in grid.grid.values() if x.type in ['G', 'E']])

        return total

    def view_grid(self, grid: Grid):
        for y in range(grid.height):
            line: str = ""
            detail = []
            for x in range(grid.width):
                unit: Unit  = grid.grid[complex(x, y)]
                line += unit.type
                if unit.type in ['G','E']:
                    detail += [f'{unit.type}({unit.hit_points})']
            print(line + "    " + ", ".join(detail))

    def get_start_positions(self, grid:Grid):
        start_positions = []
        for y in range(grid.height):
            line: str = ""
            for x in range(grid.width):
                value =  grid.grid[complex(x, y)].type
                if value in ['G','E']:
                    start_positions += [complex(x, y)]
        return start_positions

    def load_handler_part1(self, data: [str]) -> (dict[complex, str], int, int):
        grid: dict[complex, Unit] = dict()
        line: str
        height = len(data)
        width = len(data[0])
        y = 0
        for line in data:
            x = 0
            for c in line:
                grid[complex(x,y)] = Unit(c, 3, 200)
                x += 1
            y += 1

        return Grid(grid, width, height)

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)

# 242016 246176

if __name__ == '__main__':
    configure()
    aoc = Aoc201900()
    failed, results = aoc.run("part1x_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
