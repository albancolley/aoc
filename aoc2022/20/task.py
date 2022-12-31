import dataclasses
import os.path
import string

from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
from dataclasses import dataclass
import re
from collections import deque

logger = logging.getLogger("ACO2022-17")


@dataclass()
class Entry:
    initial_pos: int
    value: int
    previous = None
    next = None


class Aoc202212(AocBase):

    def calc_1(self, input) -> int:
        mix, zero = input
        self.mixer(mix)

        count = 0
        c = zero
        while c.next != zero:
            c = c.next
            count += 1
        print(count)

        current_entry = zero
        total = 0
        for i in range(0, 1000):
            current_entry = current_entry.next
        print(current_entry)
        total += current_entry.value
        for i in range(0, 1000):
            current_entry = current_entry.next
        print(current_entry)
        total += current_entry.value
        for i in range(0, 1000):
            current_entry = current_entry.next
        print(current_entry)
        total += current_entry.value

        return total

    def mixer(self, mix):
        for current_entry_key in range(1, len(mix) + 1):
            current_entry = mix[current_entry_key]
            # print(current_entry)
            new_entry = current_entry
            value = current_entry.value
            if value != 0:
                p = current_entry.previous
                n = current_entry.next
                p.next = n
                n.previous = p

                # //value = value - int(value / (len(mix)-1)) * (len(mix)-1)
                if value < 0:
                    new_entry = p
                    if abs(value) >= (len(mix) - 1):
                        value = -((abs(value) % (len(mix)-1)))
                    for i in range(value, 0):
                        new_entry = new_entry.previous
                else:
                    if abs(value) >= (len(mix) - 1):
                        value = value % (len(mix) - 1 )
                    new_entry = p
                    # start = 1
                    # initial_pos = new_entry.initial_pos
                    # found = False
                    for i in range(0, value):
                        new_entry = new_entry.next
                    #     if initial_pos == new_entry.initial_pos:
                    #         print(f'   {value} {len(mix)} {start}')
                    #         start = 1
                    #         found = True
                    #     start += 1
                    # if found:
                    #     print(f'XX {value} {len(mix)} {start}')

                left = new_entry
                right = new_entry.next

                left.next = current_entry
                right.previous = current_entry
                current_entry.previous = left
                current_entry.next = right


    def output(self, data, value, count):
        first = data[1]
        x = []
        for i in range(0, len(data)):
            x.append(first.value)
            first = first.next
        print(f'{count:10}:{value:10}:{x}')

    def calc_2(self, data: []) -> int:

        total = 0
        mix, zero = data
        # self.output(mix, 0, 0)
        for i in range(1 , 11):
            self.mixer(mix)
            # self.output(mix, 0, i)

        current_entry = zero
        total = 0
        for i in range(0, 1000):
            current_entry = current_entry.next
        print(current_entry)
        total += current_entry.value
        for i in range(0, 1000):
            current_entry = current_entry.next
        print(current_entry)
        total += current_entry.value
        for i in range(0, 1000):
            current_entry = current_entry.next
        print(current_entry)
        total += current_entry.value



        return total

    def load_handler_part1(self, data: [(int, int)]) -> {}:

        zero = None
        result = {}
        value = int(data[0])
        last_entry = Entry(1, value)
        result[1] = last_entry
        if value == 0:
            zero = last_entry
        pos = 2
        for row in data[1:]:
            value = int(row)
            entry = Entry(pos, value)
            entry.previous = last_entry
            last_entry.next = entry
            result[pos] = entry
            last_entry = entry
            pos += 1
            if value == 0:
                zero = entry
        result[1].previous = result[pos-1]
        result[pos-1].next = result[1]
        return result, zero

    def load_handler_part1x(self, data: [(int, int)]) -> {}:

        result = []
        pos = 0
        for row in data:
            result.append((int(row), pos))
            pos += 1
        return result

    def load_handler_part2(self, data: [str]) -> [str]:
        zero = None
        result = {}
        value = int(data[0]) * 811589153
        last_entry = Entry(1, value)
        result[1] = last_entry
        if value == 0:
            zero = last_entry
        pos = 2
        for row in data[1:]:
            value = int(row) * 811589153
            entry = Entry(pos, value)
            entry.previous = last_entry
            last_entry.next = entry
            result[pos] = entry
            last_entry = entry
            pos += 1
            if value == 0:
                zero = entry
        result[1].previous = result[pos - 1]
        result[pos - 1].next = result[1]
        return result, zero



if __name__ == '__main__':
    configure()
    aoc = Aoc202212()
    failed, results = aoc.run("part1_[2-2]+.txt", "part2_[1-2]+.txt")
    if failed:
        exit(1)
