"""
AOC Day X
"""
import sys
from functools import total_ordering

from networkx.algorithms.centrality import subgraph_centrality_exp
from sympy.physics.units import length

from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math

class Aoc202400(AocBase):
    """
    AOC Day 10 Class
    """
    moves = {
        'D': 0 + 1j,
        'U': 0 - 1j,
        'L': -1 + 0j,
        'R': 1 + 0j
    }

    def calc_1(self, data: dict) -> int:
        result = 0
        seen: [complex, bool]= {}
        grid, width, height = data

        for y in range(height):
            for x in range(width):
                pos = complex(x,y)
                if pos in seen:
                    continue
                current_plant = grid[pos]
                plot:[complex]  = [pos]
                area = 0
                perimeter = 0
                while len(plot) > 0:
                    plot_pos = plot.pop(0)
                    if plot_pos in seen:
                        continue
                    seen[plot_pos] = True
                    area += 1
                    perimeter += 4
                    for direction in self.moves:
                        move:complex = self.moves[direction]
                        new_plot_pos = plot_pos + move
                        plant = grid[new_plot_pos]
                        if plant == current_plant:
                            perimeter -= 1
                            plot.append(new_plot_pos)

                price = perimeter * area
                # print(f'A region of {current_plant} plants with price {area} * {perimeter} = {price}')
                result += price

        return result

    def calc_2(self, data: [str]) -> int:
        result = 0
        seen: [complex, bool] = {}
        grid, width, height = data

        for y in range(height):
            for x in range(width):
                pos = complex(x, y)
                if pos in seen:
                    continue
                current_plant = grid[pos]
                plot: [complex] = [pos]
                area = 0
                perimeter = 0
                edges: set[tuple[str, complex]] = set()

                while len(plot) > 0:
                    plot_pos = plot.pop(0)
                    if plot_pos in seen:
                        continue
                    seen[plot_pos] = True
                    area += 1
                    perimeter += 4
                    for direction in self.moves:
                        move: complex = self.moves[direction]
                        new_plot_pos = plot_pos + move
                        plant = grid[new_plot_pos]
                        if plant == current_plant:
                            perimeter -= 1
                            plot.append(new_plot_pos)
                        else:
                            edges.add((direction, new_plot_pos))

                price = area * self.count_sides(edges)
                # print(f'A region of {current_plant} plants with price {area} * {sides} = {price}')
                result += price

        return result

    def count_sides(self, edges):
        sides = 0
        while len(edges) > 0:
            sides += 1
            edge: tuple[str, complex] = edges.pop()
            direction, pos = edge
            if direction in ['U', 'D']:
                x = pos.real +1
                while (direction, complex(x, pos.imag)) in edges:
                    edges.remove((direction, complex(x, pos.imag)))
                    x += 1
                x = pos.real - 1
                while (direction, complex(x, pos.imag)) in edges:
                    edges.remove((direction, complex(x, pos.imag)))
                    x -= 1
            elif direction in ['L', 'R']:
                y = pos.imag + 1
                while (direction, complex(pos.real, y)) in edges:
                    edges.remove((direction, complex(pos.real, y)))
                    y += 1
                y = pos.imag - 1
                while (direction, complex(pos.real, y)) in edges:
                    edges.remove((direction, complex(pos.real, y)))
                    y -= 1
        return sides

    def load_handler_part1(self, data: [str]) -> [str]:
        width = len(data[0])
        height = len(data)
        grid = {}
        for x in range(-1, width + 1):
            grid[complex(x, -1)] = ' '
            grid[complex(x, height)] = ' '

        row: str
        for y in range(len(data)):
            grid[complex(-1, y)] = ' '
            grid[complex(width, y)] = ' '
            for x in range(width):
                grid[complex(x, y)] = data[y][x]

        return grid, width, height

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc202400()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
