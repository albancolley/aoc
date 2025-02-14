"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure


class Aoc201611(AocBase):
    """
    AOC Day 10 Class
    """



    def get_next(self, password: [str]) -> [str]:
        pos = len(password) - 1
        new_password = password
        while True:
            if new_password[pos] == 'z':
                new_password[pos] = 'a'
                pos -= 1
            else:
                new_password[pos] = chr(ord( new_password[pos]) + 1 )
                break

        return new_password

    def is_valid(self, next):
        for l in ['i','o', 'l']:
            if l in next:
                return False

        last = next[0]
        repeats = set()
        for c in next[1:]:
            if c == last:
                repeats.add(c)
            last = c

        if len(repeats) < 2:
            return False

        triple = False
        for i in range(len(next) - 3):
            if ord(next[i]) == ord(next[i+1]) -1 == ord(next[i+2]) - 2:
                triple = True


        return triple

    def calc_1(self, data: [str]) -> str:
        password = list(data[0])
        while True:
            password = self.get_next(password)
            if self.is_valid(password):
                return "".join(password)

    def calc_2(self, data: [str]) -> str:
        password = self.calc_1(data)
        return  self.calc_1([password])

    def load_handler_part1(self, data: [str]) -> [str]:
       return data

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201611()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
