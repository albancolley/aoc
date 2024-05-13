"""
AOC Day X
"""
from dataclasses import dataclass
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math
import re

@dataclass
class Node:
    x: int
    y: int
    size: int
    used: int
    avail: int
    use: int

@dataclass
class Cluster:
    height: int
    width: int
    nodes: dict[str,Node]

class Aoc201600(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, cluster: Cluster) -> int:
        result = 0
        for ax in range(cluster.width):
            for ay in range(cluster.height):
                a: Node = cluster.nodes[f'{ax}-{ay}']
                if a.used == 0:
                    continue
                for bx in range(cluster.width):
                    for by in range(cluster.height):
                        if ax == bx and ay == by:
                            continue
                        b: Node = cluster.nodes[f'{bx}-{by}']
                        if a.used <= b.avail:
                            result += 1
        return result


    def load_handler_part1(self, data: [str]) -> Cluster:
        height = 0
        width = 0
        nodes: dict[str, Node] = {}
        for row in data[2:]:
            p = re.compile(r'/dev/grid/node-x(\d+)-y(\d+) *(\d+)T *(\d+)T *(\d+)T *(\d+)%')
            for i in range(0, len(data), 3):
                m = re.match(p, row)
                x: int = int(m.group(1))
                y: int = int(m.group(2))
                size: int = int(m.group(3))
                used: int = int(m.group(4))
                avail: int = int(m.group(5))
                use: int = int(m.group(6))
                node: Node = Node(x, y, size, used, avail, use)
                nodes[f'{x}-{y}'] = node
                width = max(width, x)
                height = max(height, y)
        cluster = Cluster(height+1, width+1, nodes)
        return cluster

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)

    def can_move(self, pos : str, cluster: Cluster):
        start_cluster: Node = cluster.nodes[pos]
        for x in range(cluster.width):
            for y in range(cluster.width):
                index =  f'{x}-{y}'
                if index != pos:
                    if start_cluster.used < cluster.nodes[index].avail:
                        return True

        return False

    def manhattan_distance(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    def calc_2(self, cluster: Cluster) -> int:
        wall_pos_start_x = 100
        wall_pos_start_y = 100
        zero_pos_start_x = 100
        zero_pos_start_y = 100
        for y in range(cluster.width):
            line = ""
            for x in range(cluster.width):
                index= f'{x}-{y}'
                if index == "0-0":
                    line += "E"
                elif index == f"{cluster.width-1}-0":
                    line += "P"
                elif cluster.nodes[index].used == 0:
                    line += "0"
                    zero_pos_start_x = x
                    zero_pos_start_y = y
                elif self.can_move(index, cluster):
                    line += "."
                else:
                    line += "#"
                    wall_pos_start_x = min(x, wall_pos_start_x)
                    wall_pos_start_y = min(y, wall_pos_start_y)

            print(line)

        print(wall_pos_start_x, wall_pos_start_y)
        print(zero_pos_start_x, zero_pos_start_y)

        distance_to_start = self.manhattan_distance(wall_pos_start_x-1, wall_pos_start_y, zero_pos_start_x, zero_pos_start_y)
        print(distance_to_start)
        distance_to_start += self.manhattan_distance(cluster.width - 2, 0, wall_pos_start_x-1, wall_pos_start_y)
        print(self.manhattan_distance(cluster.width - 2, 0,0,0))
        distance_to_start += self.manhattan_distance(cluster.width - 2, 0,0,0) * 5 +1

        # target = (0, 0)
        # start = (0, cluster.width-1)
        # moves = self.possible_moves(start, cluster)
        # print(moves)
        return distance_to_start

    def possible_moves(self, pos, cluster):
        moves = []
        for move in [(0,1), (0,-1), (1,0), (-1,0)]:
            next_pos = (pos[0] + move[0], pos[1] + move[1])
            if 0 <= next_pos[0] < cluster.width and 0 <= next_pos[1] < cluster.height:
                if cluster.nodes[f'{next_pos[0]}-{next_pos[1]}'].avail >= cluster.nodes[f'{pos[0]}-{pos[1]}'].used:
                    moves.append(next_pos)
        return moves


if __name__ == '__main__':
    configure()
    aoc = Aoc201600()
    failed, results = aoc.run("part1x_[0-1]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
