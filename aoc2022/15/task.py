import os.path
import string

from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
import re
from PIL import Image, ImageColor

logger = logging.getLogger("ACO2022-14")


class Aoc202212(AocBase):

    def calc_1(self, data) -> int:
        count = 0
        target_y = data[0]
        coverage = []
        beacons_in_row = {}
        for sensor in data[1]:
            mid_point = sensor
            mid_point_x = sensor[0]
            mid_point_y = sensor[1]
            beacon = data[1][sensor][0]
            distance = data[1][sensor][1]
            ranges = []
            if beacon[1] == target_y:
                if beacon not in beacons_in_row:
                    beacons_in_row[beacon] = True
            if mid_point_y == target_y:
                ranges = [mid_point_x - distance, mid_point_x + distance]
            else:
                if mid_point_y < target_y <= mid_point_y + distance:
                    vertices = [
                        (mid_point_x - distance, mid_point_y),
                        (mid_point_x, mid_point_y + distance),
                        (mid_point_x + distance, mid_point_y)]
                elif mid_point_y > target_y >= mid_point_y - distance:
                    vertices = [
                        (mid_point_x - distance, mid_point_y),
                        (mid_point_x, mid_point_y - distance),
                        (mid_point_x + distance, mid_point_y)]
                else:
                    continue
                for i in range(2):
                    v1 = vertices[i]
                    v2 = vertices[(i + 1) % 4]
                    x1 = v1[0]
                    x2 = v2[0]
                    y1 = v1[1]
                    y2 = v2[1]
                    # y = ((y2 - y1) / (x2 - x1))*(target_y - x1)
                    x = ((int(target_y) - y1) * (x2 - x1) / (y2 - y1)) + x1
                    ranges.append(int(x))
                pass
            coverage.append((ranges[0], ranges[1]))
        min_x = coverage[0][0]
        max_x = coverage[0][1]
        for i in coverage[1:]:
            min_x = min(i[0], min_x)
            max_x = max(i[1], max_x)
        result = max_x - min_x + 1 - len(beacons_in_row)
        return result



    def calc_2(self, data: [str]) -> int:
        rows_left = {}
        total_x = data[0]
        for j in range(0, total_x + 1):
            rows_left[j] = []
        iterations = 0
        sensors = data[1]
        for sensor in sensors:
            mid_point_x = sensor[0]
            mid_point_y = sensor[1]
            distance = sensors[sensor][1]
            beacon = sensors[sensor][0]
            if sensor[1] in rows_left:
                rows_left[sensor[1]].append((sensor[0], sensor[0]))
            if beacon[1] in rows_left:
                rows_left[beacon[1]].append((beacon[0], beacon[0]))

            # if beacon[1] == target_y:
            #     if beacon not in beacons_in_row:
            #         beacons_in_row[beacon] = True
            for target_y in list(rows_left):
                iterations += 1
                if mid_point_y == target_y:
                    x1 = mid_point_x - distance
                    x2 = mid_point_x + distance
                else:
                    if mid_point_y < target_y <= mid_point_y + distance:
                        vertices = [
                            (mid_point_x - distance, mid_point_y),
                            (mid_point_x, mid_point_y + distance),
                            (mid_point_x + distance, mid_point_y)]
                    elif mid_point_y > target_y >= mid_point_y - distance:
                        vertices = [
                            (mid_point_x - distance, mid_point_y),
                            (mid_point_x, mid_point_y - distance),
                            (mid_point_x + distance, mid_point_y)]
                    else:
                        continue

                    v1 = vertices[0]
                    v2 = vertices[1]
                    v3 = vertices[2]
                    x1 = v1[0]
                    x2 = v2[0]
                    x3 = v3[0]
                    y1 = v1[1]
                    y2 = v2[1]
                    y3 = v3[1]
                    # y = ((y2 - y1) / (x2 - x1))*(target_y - x1)
                    start_x = int(((target_y - y1) * (x2 - x1) / (y2 - y1)) + x1)
                    end_x = int(((target_y - y2) * (x3 - x2) / (y3 - y2)) + x2)
                rows_left[target_y].append((start_x, end_x))
                rows_left[target_y].sort()
                min_x = rows_left[target_y][0][0]
                max_x = rows_left[target_y][0][1]
                new_ranges = []
                for x in rows_left[target_y][1:]:
                    if max_x + 1 >= x[0]:
                        if max_x > x[1]:
                            continue
                        else:
                            max_x = x[1]
                    else:
                        new_ranges.append((min_x, max_x))
                        min_x = x[0]
                        max_x = x[1]
                if min_x <= 0 and max_x >= total_x:
                    del rows_left[target_y]
                    continue

                if (min_x, max_x) not in new_ranges:
                    new_ranges.append((min_x, max_x))
                rows_left[target_y] = new_ranges

        result = 0
        for key in rows_left:
            x = rows_left[key][0][1] + 1
            y = key
            result = x * 4000000 + y
        row_by_row = len(sensors) * y
        row_by_row_reverse = len(sensors) * (total_x-y)
        print(f'row {y}, pos {x}, iterations {iterations}, row_by_row_iterations {row_by_row}, reverse {row_by_row_reverse}')
        return result

    def load_handler_part1(self, data: [str]) -> {}:
        sensors = {}
        target_row = int(data[0])
        p = re.compile(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')
        for row in data[1:]:
            m = re.match(p, row)
            if m:
                x1 = int(m.group(1))
                y1 = int(m.group(2))
                x2 = int(m.group(3))
                y2 = int(m.group(4))
                md = abs(x1 - x2) + abs(y1 - y2)
                sensors[(x1, y1)] = ((x2, y2), md)
        return target_row, sensors

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc202212()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        exit(1)
