"""
AOC Day 10
"""
import sys

from common import AocBase
from common import configure


class Aoc2023010(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, tiles: dict) -> int:
        values = list(tiles.values())
        intersections = set()
        for i in range(len(values)):
            for j in range(i+1, len(values)):
                intersections = intersections.union(values[i].intersection(values[j]))

        result = 1
        for tile in tiles:
            if len(tiles[tile].difference(intersections)) == 4  :
                result *= tile
        return result

    def view(self, grid):
        print()
        for line in grid:
            print(''.join(line))
        print()

    def calc_2(self, data: dict) -> int:
        # print(len(data)**.5,data)
        grid ={}
        links={}
        keys = list(data.keys())
        for tile in data:
            # print(tile)
            # self.view(data[tile][0])
            # rotated = self.rotate_clockwise(data[tile][0])
            # self.view(rotated)
            # flipped = self.flip(rotated)
            # self.view(flipped)
            # rotated = list(zip(*rotated[::-1]))
            # self.view(rotated)
            # rotated = list(zip(*rotated[::-1]))
            # self.view(rotated)
            # rotated = list(zip(*rotated[::-1]))
            # self.view(rotated)
            # flipped = [reversed(x) for x in rotated]
            # self.view(flipped)
            # # self.view(data[tile][0].copy().reverse())
            # if tile == 1427:
            #     pass
            links[tile] = []
            for tile_2 in data:
                if tile == tile_2:
                    continue
                if len(data[tile][1].intersection(data[tile_2][1])) > 0:
                    links[tile] += [tile_2]
        print(links)
        grid = {}
        pos = (0,0)
        tiles: list = list(links.keys())
        grid[tiles[0]] = ((0, 0), data[tiles[0]][0])
        for tile_name in tiles:
            pos, tile = grid[tile_name]
            top = tile[0]
            bot
            for link_tile in links[tile_name]:
                if link_tile in grid:
                    continue
                new_tile = data[link_tile][0]
                for i in range(2):
                    for j in range(4):

        zip


        return 0

    def rotate_clockwise(self, tile):
        return list(zip(*tile[::-1]))

    def flip(self, tile):
        return [reversed(x) for x in tile]

    def load_handler_part1(self, data: [str]) -> [str]:
        tiles = {}
        pos = 0
        while pos < len(data):
            tile_name = int(data[pos].split(' ')[1][0:-1])
            pos += 1
            top = data[pos]
            left = data[pos][0]
            right = data[pos][-1]
            pos += 1
            while pos < len(data) and data[pos] != '':
                left += data[pos][0]
                right += data[pos][-1]
                pos += 1
            bottom = data[pos-1]
            tiles[tile_name] = set((top, top[::-1], left, left[::-1], right, right[::-1], bottom, bottom[::-1]))
            pos += 1
        return tiles

    def load_handler_part2(self, data: [str]) -> [str]:
        tiles = {}
        pos = 0
        while pos < len(data):
            tile_name = int(data[pos].split(' ')[1][0:-1])
            tile = []
            pos += 1
            top = data[pos]
            left = data[pos][0]
            right = data[pos][-1]
            tile.append(list(data[pos]))
            pos += 1
            while pos < len(data) and data[pos] != '':
                left += data[pos][0]
                right += data[pos][-1]
                tile.append(list(data[pos]))
                pos += 1
            bottom = data[pos - 1]
            tiles[tile_name] = (tile, set((top, top[::-1], left, left[::-1], right, right[::-1], bottom, bottom[::-1])))
            pos += 1
        return tiles


if __name__ == '__main__':
    configure()
    aoc = Aoc2023010()
    failed, results = aoc.run("part1x_[0-9]+.txt", "part2_[0-1]+.txt")
    if failed:
        sys.exit(1)
