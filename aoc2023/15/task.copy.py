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

    def calc_1(self, data: dict) -> int:
        result = 0
        for d in data:
            x = d.split(',')
            for l in x:
                value = 0
                for c in l:
                    value = ((value +ord(c)) * 17) % 256
                result += value
        return result

    def calc_2(self, data: [str]) -> int:
        result = 0
        boxes = []
        for i in range(256):
            boxes.append({})
        for d in data:
            x = d.split(',')
            for l in x:
                if '-' in l:
                    t = l.split('-')
                    label = t[0]
                    box_number = self.hash_label(label)
                    if label in boxes[box_number]:
                        boxes[box_number].pop(label)
                elif "=" in l:
                    t = l.split('=')
                    label = t[0]
                    focus = t[1]
                    box_number = self.hash_label(label)
                    boxes[box_number][label] = int(focus)

        print(boxes)
        for i in range(len(boxes)):
            values = boxes[i]
            slot = 1
            for v in values:
                x = (i+1) * slot * values[v]
                result += x
                slot += 1
        return result

    # 245141 too high

    def hash_label(self, x):
        value = 0
        for c in x:
            value = ((value + ord(c)) * 17) % 256
        return value

    def load_handler_part1(self, data: [str]) -> [str]:
       return data

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc2023010()
    failed, results = aoc.run("part1x_[0-9]+.txt", "part2_[1-2]+.txt")
    if failed:
        sys.exit(1)
