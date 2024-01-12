import os.path
import string

from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging

from PIL import Image, ImageColor

logger = logging.getLogger("ACO2022-14")

class Aoc202212(AocBase):


    def calc_1(self, data ) -> int:
        count = 0
        cave, max_y, min_x, max_x = data
        sand_pos_x = 500
        sand_pos_y = 0
        pos = None
        self.draw(count, cave, (1 + (max_x - min_x), max_y + 1), min_x, pos)
        while True:
            pos = (sand_pos_x, sand_pos_y)
            below = (sand_pos_x, sand_pos_y+1)
            left = (sand_pos_x-1, sand_pos_y+1)
            right = (sand_pos_x+1, sand_pos_y+1)
            if below in cave:
                if left in cave and right in cave:
                    cave[pos] = "o"
                    self.draw(count, cave, (1 + (max_x - min_x), max_y + 1), min_x, pos)
                    count += 1
                    sand_pos_x = 500
                    sand_pos_y = 0
                    continue
                if left not in cave:
                    sand_pos_x -= 1
                    sand_pos_y += 1
                elif right not in cave:
                    sand_pos_x += 1
                    sand_pos_y += 1
            else:
                sand_pos_y += 1
            if max_y < sand_pos_y:
                break
        self.draw(count, cave, (1 + (max_x - min_x), max_y + 1), min_x, None)
        return count

    def calc_2(self, data: [str]) -> int:
        count = 0
        cave, max_y, min_x, max_x = data
        sand_pos_x = 500
        sand_pos_y = 0
        pos = None
        extra = 200
        size = (extra*2 + (max_x - min_x), max_y + 4)
        self.draw(count, cave, size, min_x, pos, extra)
        while True:
            pos = (sand_pos_x, sand_pos_y)
            below = (sand_pos_x, sand_pos_y + 1)
            left = (sand_pos_x - 1, sand_pos_y + 1)
            right = (sand_pos_x + 1, sand_pos_y + 1)
            if below in cave:
                if left in cave and right in cave:

                    cave[pos] = "o"
                    if count % 100 == 0:
                        self.draw(count, cave, size, min_x, pos, extra)
                    count += 1
                    sand_pos_x = 500
                    sand_pos_y = 0
                    if (500, 0) == pos:
                        break
                    continue
                if left not in cave:
                    sand_pos_x -= 1
                    sand_pos_y += 1
                elif right not in cave:
                    sand_pos_x += 1
                    sand_pos_y += 1
            else:
                sand_pos_y += 1
            # min_x = min(min_x, sand_pos_x)
            # max_x = max(max_x, sand_pos_x)
            if max_y + 2 == sand_pos_y:
                new_pos_above = (sand_pos_x, sand_pos_y-1)
                cave[new_pos_above] = "o"
                cave[(sand_pos_x, sand_pos_y)] = "#"
                if count % 100 == 0:
                    self.draw(count, cave, size, min_x, pos, extra)
                count += 1
                sand_pos_x = 500
                sand_pos_y = 0
        self.draw(count, cave, size, min_x, None, extra)
        return count

    def load_handler_part1(self, data: [str]) -> {}:
        cave = {}
        max_y = 0
        min_x = 2000000
        max_x = 0
        for path in data:
            points = path.split(' -> ')
            last_coord = points[0].split(',')
            for point in points[1:]:
                coord = point.split(',')
                x1 = min(int(last_coord[0]), int(coord[0]))
                x2 = max(int(last_coord[0]), int(coord[0]))
                y1 = min(int(last_coord[1]), int(coord[1]))
                y2 = max(int(last_coord[1]), int(coord[1]))
                max_y = max(max_y, y2)
                min_x = min(min_x, x1)
                max_x = max(max_x, x2)
                for x in range(x1, x2+1):
                    for y in range(y1, y2+1):
                        cave[(x, y)] = '#'
                last_coord = coord
        return cave, max_y, min_x, max_x

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)

    def draw(self, count, cave, size, min_x, last_sand, extra=0):
        pass
        # image = Image.new("RGB", size, color= ImageColor.getrgb('white'))
        # source = (500 - min_x + extra, 0)
        # image.putpixel(source, ImageColor.getrgb('blue'))
        # for key in cave:
        #     value = cave[key]
        #     if value == "#":
        #         colour = ImageColor.getrgb('black')
        #     elif value == "o":
        #         colour = ImageColor.getrgb('yellow')
        #     key = (key[0] - min_x, key[1])
        #     x, y = key
        #     x = x + extra
        #     if 0 <= x < size[0] and 0 <= y < size[1]:
        #         image.putpixel((x, y), colour)
        # if last_sand:
        #     if 0 <= x < size[0] and 0 <= y < size[1]:
        #         image.putpixel((x,y), ImageColor.getrgb('red'))
        # path = os.path.join('C:\\WIP\\aoc', f'{count:06}.png')
        # # (width, height) = (image.width * 2, image.height * 2)
        # # i2 = image.resize((width, height), Image.Resampling.BOX )
        # image.save(path)


if __name__ == '__main__':
    configure()
    aoc = Aoc202212()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        exit(1)
