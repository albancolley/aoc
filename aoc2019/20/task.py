"""
AOC Day 10
"""
import sys
from common import AocBase
from common import configure

from dataclasses import dataclass

@dataclass
class Unit:
    type: str
    direction: complex
    new_pos: complex
    inner: bool
    label: str = ""

@dataclass
class Maze:
    grid: dict[complex, Unit]
    start: complex
    start_dir: complex
    end: complex
    teleports: dict[str, list]

class Aoc201920(AocBase):
    """
    AOC Day 10 Class
    """
    MOVES: list[complex] = [
        -1 + 0j,
        0 - 1j,
        0 + 1j,
        1 + 0j,
    ]

    WALLS:list[str] = ["#"]

    def bfs(self, maze: Maze) -> int:
        seen: dict[complex, int] = {maze.start: 0}
        q = [(maze.start , maze.start_dir , 0)]
        while len(q) > 0:
            position, direction,  step = q.pop(0)
            move: complex
            for move in self.MOVES:
                next_position = position + move
                direction = move
                if next_position not in maze.grid:
                    continue
                unit: Unit = maze.grid[next_position]
                if unit.type in self.WALLS:
                    continue
                if unit.type == "T":
                    next_position = unit.new_pos
                    direction = unit.direction
                if next_position == maze.end:
                    return step + 1
                if next_position not in seen:
                    seen[next_position] = step + 1
                    q.append((next_position, direction, step + 1))
        return -1

    def calc_1(self, maze: Maze) -> int:
        result = 0
        return self.bfs(maze)
        
        # for key in maze.grid.keys():
        #     unit = maze.grid[key]
        #     print(key, unit)
        return result


   

    def paths(self, maze: Maze, start:complex, start_dir: complex) -> list:
        seen: dict[complex, int] = {start: 0}
        paths = {}
        q = [(start , start_dir , [],  0)]
        while len(q) > 0:
            position, direction, path, step = q.pop(0)
            move: complex
            for move in self.MOVES:
                next_position = position + move
                direction = move
                if next_position not in maze.grid:
                    continue
                unit: Unit = maze.grid[next_position]
                if unit.type in self.WALLS:
                    continue
                if (unit.type == "T" and position != start) or next_position == maze.end:
                    label = unit.label
                    if not label:
                        label = "ZZ"
                    if label in paths:
                        path_label, path_step, path_unit = paths[label]
                        if step < path_step:
                            paths[label] = (label, step, unit)        
                    else:
                        paths[label] = (label, step, unit)
                    continue
                if next_position not in path:
                    q.append((next_position, direction, path + [next_position], step + 1))
        return paths

    def bfs2(self, maze:  dict[str, tuple[str, int, Unit]]) -> int:
        # seen: dict[(str, int), int] = {("AA", 0): 0}
        q = [("AAFalse", 0, 0)]
        while len(q) > 0:
            label, depth, step = q.pop(0)
            for move in maze[label]:
                new_label, new_step, unit = maze[label][move]
                new_steps = step + new_step + 1
                
                if new_label == "ZZ":
                    if depth == 0:
                        return new_steps
                    continue
                elif depth == 0 and not unit.inner:
                    continue
                
                if unit.inner:
                    new_depth = depth + 1
                else:
                    new_depth = depth - 1
                
                q.append((new_label + str(unit.inner), new_depth, new_steps))
                
        return -1

    def calc_2(self, maze: Maze) -> int:
        
        new_maze: dict[str, tuple[str, int, Unit]] = {}
         
        new_maze["AAFalse"] = self.paths(maze, maze.start, maze.start_dir)
        for label in maze.teleports:
            pos, teleport_pos, direction, inner = maze.teleports[label][0]
            new_maze[label + str(inner)] = self.paths(maze, pos, direction)
            pos, teleport_pos, direction, inner = maze.teleports[label][1]
            new_maze[label + str(inner)] = self.paths(maze, pos, direction)
        
        return self.bfs2(new_maze)

    def load_handler_part1(self, data: [str]) -> Maze:
        grid = {}
        start = complex(0,0)
        end = complex(0,0)

        width = len(data[0])
        height = len(data)
        
        pos = complex(0,0)
        input_grid = {}
        for line in data:
            for block in line:
                input_grid[pos] = block
                pos += 1

            pos += 1j
            pos -= pos.real

        teleports: dict = {}
        pos:complex= complex(0,0)
        while pos in input_grid:
            block = input_grid[pos]
            if block in [".", "#"]:
                grid[pos] = Unit(block, None, None, False)
            if block == ".":
                    move : complex
                    for move in self.MOVES:
                        if input_grid[pos + move] not in [" ", ".", "#"]:
                            label : str
                            direction: complex = -move
                            if move.real == -1:
                                label = input_grid[(pos + move*2)] + input_grid[(pos + move)]
                            elif move.real == 1:
                                label = input_grid[(pos + move)] + input_grid[(pos + move*2)]
                            elif move.imag == -1:
                                label = input_grid[(pos + move*2)] + input_grid[(pos + move)]
                            else:
                                label = input_grid[(pos + move)] + input_grid[(pos + move*2)]

                            if label == 'AA':
                                start = (pos, dir)
                            elif label == 'ZZ':
                                end = (pos, dir)
                            else:
                                teleport_pos = pos + move
                                inner: bool = (teleport_pos.real < 2 or teleport_pos.imag < 2
                                                   or teleport_pos.real > width - 3 or teleport_pos.imag > height - 3)

                                if label in teleports:
                                    opp_pos, opp_teleport_pos, opp_direction, opp_inner = teleports[label][0]
                                    grid[opp_teleport_pos] = Unit("T", direction, pos, inner, label)
                                    grid[teleport_pos] = Unit("T", opp_direction, opp_pos, opp_inner, label)
                                    teleports[label].append((pos, teleport_pos, direction, inner))
                                else:
                                    teleports[label] = [(pos, teleport_pos, direction, inner)]
                            
            pos += 1
            if pos not in input_grid:
                pos += 1j
                pos -= pos.real

        maze = Maze(grid, start[0], start[1], end[0], teleports)

        return maze

    def add_teleport(self, teleports, label, direction, pos):
        if label:
            if label not in teleports:
                teleports[label] = []
            teleports[label].append((pos, direction))



    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201920()
    failed, results = aoc.run("part1x_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
