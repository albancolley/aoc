"""
AOC Day 10
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math

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
                    value = self.hash_label(c, value)
                result += value
        return result

    def calc_2(self, data: [str]) -> int:
        result = 0
        boxes = []
        box_number = 0

        label_hashes={}
        for d in data:
            x = d.split(',')
            for command in x:
                if "-" in command:
                    command = command.split('-')[0]
                else:
                    command = command.split('=')[0]
                value = self.hash_label(command)
                label_hashes[command] = value
                result += value

        for i in range(256):
            boxes.append([])
        x = data[0].split(',')
        for l in x:
            if '-' in l:
                t = l.split('-')
                label = t[0]
                box_number = label_hashes[label]
                box = boxes[box_number]
                for v in boxes[box_number]:
                    s, l, f = v
                    if l == label:
                        box.remove(v)
            elif "=" in l:
                t = l.split('=')
                label = t[0]
                focus = t[1]
                box_number = label_hashes[label]
                found = False
                box = boxes[box_number]
                for v in box:
                    s, l, f  = v
                    if l == label:
                        box.remove(v)
                        box.append((s, l, int(focus)))
                        found = True
                        break
                if not found:
                    max_slot = 0
                    for v in boxes[box_number]:
                        s, l, f = v
                        max_slot = max(max_slot, s)
                    box.append((max_slot + 1, label, int(focus)))

        result = 0
        for i in range(len(boxes)):
            values = boxes[i]
            v2 = sorted(values)
            slot = 1
            total = 0
            for v in v2:
                s, l, f = v
                x = (i+1) * slot * f
                total += x
                slot += 1
            print(v2, total)
            result += total
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
    failed, results = aoc.run("part1x_[0-9]+.txt", "part2_[2-2]+.txt")
    if failed:
        sys.exit(1)
