"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure


class Aoc201710(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: ()) -> int:
        input_list, lengths = data
        input_list_length = len(input_list)
        step = 0
        current_pos = 0
        for length in lengths:
            new_string: [int] = input_list.copy()
            for i in range(length):
                new_pos = (current_pos + i) % input_list_length
                reverse_pos = (current_pos + length - i - 1) % input_list_length
                new_string[new_pos] = input_list[reverse_pos]
            input_list = new_string
            current_pos = (current_pos + length + step) % input_list_length
            step += 1

        return input_list[0] * input_list[1]

    def calc_2(self, data: [int]) -> str:
        input_list, lengths = data
        input_list_length = len(input_list)
        step = 0
        current_pos = 0

        for i in range(64):
            for length in lengths:
                new_string: [int] = input_list.copy()
                for i in range(length):
                    new_pos = (current_pos + i) % input_list_length
                    reverse_pos = (current_pos + length - i - 1) % input_list_length
                    new_string[new_pos] = input_list[reverse_pos]
                input_list = new_string
                current_pos = (current_pos + length + step) % input_list_length
                step += 1

        xors = [0] * 16
        for i in range(16):
            xors[i] = input_list[i*16]
            for j in range(i*16+1, i*16+16):
                xors[i] ^= input_list[j]

        result = ''.join([f'{x:0>2x}' for x in xors])

        return result
    # 9de8846431eef262be78f590e39a48
    # 9de8846431eef262be78f590e39a48

    def load_handler_part1(self, data: [str]) -> [str]:
        input_list = [i for i in range(int(data[0]))]
        lengths = [int(i) for i in data[1].split(',')]
        return input_list, lengths

    def load_handler_part2(self, data: [str]) -> [str]:
        input_list = [i for i in range(256)]
        lengths = []
        if len(data) != 0:
            for i in data[0].strip():
                lengths += [ord(i)]
        lengths += [17, 31, 73, 47, 23]
        return input_list, lengths


if __name__ == '__main__':
    configure()
    aoc = Aoc201710()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
