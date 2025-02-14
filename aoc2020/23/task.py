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

    def calc_1(self, data: str) -> int:
        values = [int(d) for d in data[0]]
        start = values[0]
        repeats = int(data[1])
        length = len(values)
        for repeat in range(repeats):
            pos = values.index(start)
            temp = []
            for i in range(1,4):
                new_pos = (pos + i) % length
                temp.append(values[new_pos])

            new_values = []
            for value in values:
                if value not in temp:
                    new_values.append(value)

            destination = ((start - 1) % length)
            if destination ==0:
                destination = length
            while destination in temp:
                destination = ((destination - 1) % length)
                if destination ==0:
                    destination = length

            destination_pos = new_values.index(destination)

            next_values = new_values[0:destination_pos+1] + temp + new_values[destination_pos+1:]
            next_pos = (next_values.index(start) + 1) % length
            start = next_values[next_pos]
            # print(temp, destination, destination_pos, new_values, values, next_values)
            values= next_values

        start_pos = (values.index(1) + 1) % length
        result = values[start_pos]
        start_pos += 1
        for i in range(length-2):
            result *=10
            result += values[(start_pos + i) % length]
        return result

    def calc_2(self, data: [str]) -> int:
        total = 0
        return total

    def load_handler_part1(self, data: [str]) -> [str]:
       return data

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc2023010()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
