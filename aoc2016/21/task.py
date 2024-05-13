"""
AOC Day X
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math

class Aoc201600(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict) -> str:
        result = 0
        password = [c for c in data[0]]
        command: str
        for command in data[1:]:
            words = command.split(' ')
            if command.startswith('swap position'):
                pos1 = int(words[2])
                pos2 = int(words[5])
                temp = password[pos2]
                password[pos2] = password[pos1]
                password[pos1] = temp
            elif command.startswith('swap letter'):
                letter1 = words[2]
                letter2 = words[5]
                pos1 = password.index(letter1)
                pos2 = password.index(letter2)
                temp = password[pos2]
                password[pos2] = password[pos1]
                password[pos1] = temp
            elif command.startswith('reverse positions'):
                pos1 = min(int(words[2]),int(words[4]))
                pos2 = max(int(words[2]),int(words[4]))
                new_pasword = password.copy()
                for i in range(pos2+1 - pos1):
                    new_pasword[i+pos1] = password[pos2-i]
                password = new_pasword
            elif command.startswith('rotate left') or command.startswith('rotate right'):
                steps = int(words[2])
                new_password = password.copy()
                if words[1] == 'left':
                    for i in range(len(password)):
                        new_password[i - steps] = password[i]
                else:
                    for i in range(len(password)):
                        new_password[(i + steps) % len(password)] = password[i]
                password = new_password
            elif command.startswith('move position'):
                pos1 = int(words[2])
                pos2 = int(words[5])
                temp = password.pop(pos1)
                password = password[0:pos2] + [temp] + password[pos2:]
            elif command.startswith('rotate based on position of letter'):
                password = self.rotate_based(password, words[-1])
        return ''.join(password)

    def rotate_based(self, password, pos):
        steps = int(password.index(pos))
        if steps >= 4:
            steps += 1
        steps += 1
        new_password = password.copy()
        for i in range(len(password)):
            new_password[(i + steps) % len(password)] = password[i]
        password = new_password
        return password

    def calc_2(self, data: [str]) -> str:
        password = [c for c in data[0]]
        import itertools
        possible_passwords = list(itertools.permutations(password))
        for p in possible_passwords:
            p = list(p)
            new_password = self.calc_1([p] + data[1:])
            if new_password == data[0]:
                return ''.join(p)

        return "XXX"
    def load_handler_part1(self, data: [str]) -> [str]:
       return data

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201600()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-1]+.txt")
    if failed:
        sys.exit(1)
