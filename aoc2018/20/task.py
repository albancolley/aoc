"""
AOC Day X
"""
from dataclasses import dataclass
import sys
from common import AocBase
from common import configure

@dataclass
class Room:
    location: complex
    north: 'Room' = None
    south: 'Room' = None
    east: 'Room' = None
    west: 'Room' = None


class Aoc201820(AocBase):
    """
    AOC Day 10 Class
    """

    def split(self, regex):
        depth = 0
        parts = []
        i = 0
        last_pos = 0
        while i < len(regex):
            c = regex[i]
            match c:
                case '(':
                    depth += 1
                    if depth == 1:
                        last_pos += 1
                case ')':
                    depth -= 1
                    if depth == 0:
                        parts += [regex[last_pos:i]]
                        parts += [regex[i+1:]]
                        break
                case '|':
                    if depth == 1:
                        parts += [regex[last_pos:i]]
                        last_pos = i+1
            i += 1
        return parts

    def build(self, start_regex, start_pos):

        q = [(start_regex, start_pos)]

        while len(q) > 0:
            regex, pos = q.pop(0)

            if len(regex) == 0:
                continue
            new_pos = None
            c = regex[0]
            match c:
                case '$':
                    q.append((regex[1:], pos))
                case '^':
                    q.append((regex[1:], pos))
                case '(':
                    for part in self.split(regex):
                        q.append((part, pos))
                case 'N':
                    new_pos = pos.north
                    if not pos.north:
                        new_pos = Room(south=pos, location=pos.location + 1j)
                        pos.north = new_pos
                    q.append((regex[1:], new_pos))
                case 'S':
                    new_pos = pos.south
                    if not pos.south:
                        new_pos = Room(north=pos, location=pos.location - 1j)
                        pos.south = new_pos
                    q.append((regex[1:], new_pos))
                case 'E':
                    new_pos = pos.east
                    if not pos.east:
                        new_pos = Room(west=pos, location=pos.location + 1)
                        pos.east = new_pos
                    q.append((regex[1:], new_pos))
                case 'W':
                    new_pos = pos.west
                    if not pos.west:
                        new_pos = Room(east=pos, location=pos.location - 1)
                        pos.west = new_pos
                    q.append((regex[1:], new_pos))

    def calc_1(self, data: str) -> int:
        if len(data) == 0:
            return -1
        start = Room(complex(0,0))

        self.build(data[0], start)

        max_depth, depths = self.max_depth(start)
        return max_depth

    def max_depth(self, start: Room):
        queue = [(start, 0, [])]
        depths = {}
        max_depth = 0

        while len(queue) > 0:
            pos, depth, path = queue.pop(0)
            max_depth = max(max_depth, depth)
            self.max_depth_add(pos.north, path, depth, depths, queue)
            self.max_depth_add(pos.south, path, depth, depths, queue)
            self.max_depth_add(pos.east, path, depth, depths, queue)
            self.max_depth_add(pos.west, path, depth, depths, queue)

        return max_depth, depths

    def max_depth_add(self, new_pos, path, depth, depths, queue):
        if not new_pos:
            return
        if new_pos.location in path:
            return
        new_depth = depth + 1
        if new_pos.location in depths:
            if depths[new_pos.location] < new_depth:
                return
        depths[new_pos.location] = new_depth
        queue.append((new_pos, new_depth, path + [new_pos]))

    def calc_2(self, data: [str]) -> int:
        if len(data) == 0:
            return -1
        start = Room(complex(0, 0))

        self.build(data[0], start)

        max_depth, depths = self.max_depth(start)
        return len([x for x in depths.values() if x >= 1000])

    def load_handler_part1(self, data: [str]) -> [str]:
       return data

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201820()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
