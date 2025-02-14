"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure


class Aoc201600(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, input: [str]) -> str:
        result = 0
        length: int = int(input[0])
        data: str = input[1]
        while len(data) < length:
            b: str = data[::-1].replace('0', '2').replace('1', '0').replace('2','1')
            data = data + '0' + b

        data = data[0:length]
        checksum = data
        while len(checksum) % 2 == 0:
            new_checksum = ""
            for i in range(0,len(checksum), 2):
                if checksum[i] == checksum[i+1]:
                    new_checksum += '1'
                else:
                    new_checksum += '0'
            checksum = new_checksum

        return checksum

    def calc_2(self, data: [str]) -> str:
        return self.calc_1(data)

    def load_handler_part1(self, data: [str]) -> [str]:
       return data

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201600()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
