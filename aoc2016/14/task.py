"""
AOC Day X
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math
import hashlib

class Aoc201600(AocBase):
    """
    AOC Day 10 Class
    """

    def tripple(self, hash):
        last = hash[0]
        count = 1
        for c in hash[1:]:
            if c == last:
                count += 1
                if count == 3:
                    return c
            else:
                last = c
                count = 1
        return None


    def calc_1(self, data: dict) -> str:
        d: str
        code = ""
        count = 0
        md5_dictionary = {}
        d = data[0]
        index = 0
        key = 0
        while True:
            if index not in md5_dictionary:
                value = d + str(index)
                md5_dictionary[index] = hashlib.md5(value.encode()).hexdigest()
            md5 = md5_dictionary[index]
            tripple_value = self.tripple(md5)
            if tripple_value:
                for i in range(index+1, index+1001):
                    if i not in md5_dictionary:
                        value = d + str(i)
                        md5_dictionary[i] = hashlib.md5(value.encode()).hexdigest()
                    if tripple_value*5 in md5_dictionary[i]:
                        # print(md5, tripple_value, index)
                        key += 1
                        if key == 64:
                            return index
            index += 1
        return code

    def stretched_hash(self, key):
        hash = key
        for i in range(2016+1):
            hash = hashlib.md5(hash.encode()).hexdigest()
        return hash

    def calc_2(self, data: [str]) -> str:
        d: str
        md5_dictionary = {}
        d = data[0]
        index = 0
        key = 0
        while True:
            if index not in md5_dictionary:
                value = d + str(index)
                md5_dictionary[index] = self.stretched_hash(value)
            md5 = md5_dictionary[index]
            tripple_value = self.tripple(md5)
            if tripple_value:
                for i in range(index + 1, index + 1001):
                    if i not in md5_dictionary:
                        value = d + str(i)
                        md5_dictionary[i] = self.stretched_hash(value)
                    if tripple_value * 5 in md5_dictionary[i]:
                        # print(md5, tripple_value, index)
                        key += 1
                        if key == 64:
                            return index
            index += 1

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
