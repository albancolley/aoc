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

    def calc_1(self, data: dict) -> int:
        nos = ['ab', 'cd', 'pq', 'xy']
        vowels = ['a','e','i','o','u']
        result = 0
        for d in data:
            valid = True
            for no in nos:
                if no in d:
                    valid = False
                    break
            if not valid:
                continue

            last = '?'
            valid = False
            for l in d:
                if l == last:
                    valid = True
                    break
                last = l

            vowel_count = 0
            for l in d:
                if l in vowels:
                    vowel_count += 1
                    if vowel_count == 3:
                        break


            if valid and vowel_count == 3:
                result += 1

        return result

    def calc_2(self, data: [str]) -> int:
        total = 0
        for d in data:
            valid1 = False
            if len(d) > 2:
                for i in range(len(d) - 2):
                    if d[i] == d[i+2]:
                        r1 = d[i:i+3]
                        valid1 = True
                        break

            valid2 = False
            if len(d) > 4:
                for i in range(len(d) - 2):
                    # print(d[i:i+2], d[0:max(i,0)] + d[i+2:])
                    if d[i:i+2] in d[0:max(i,0)] or d[i:i+2] in   d[i+2:]:
                        r2 = d[i:i+2]
                        r2_b= d[0:max(i,0)] + '|' + d[i+2:]
                        valid2 = True
                        break

            if valid1 and valid2:
                # print(r1, r2, r2_b, d)
                total += 1

        return total

    def load_handler_part1(self, data: [str]) -> [str]:
       return data

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201600()
    failed, results = aoc.run("part1x_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
