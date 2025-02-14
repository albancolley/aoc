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

    def calc_1(self, data: list) -> int:
        d: str
        identifiers = {}
        wires: list = data
        while len(wires) > 0:
            # print(len(wires))
            wire = wires.pop(0)
            command = wire.split(' -> ')
            t = command[1]
            b = None
            if len(command[0].split(' ')) == 1:
                a = command[0]
                op = "LOAD"
            else:
                left_command = command[0].split(' ')
                if left_command[0] == 'NOT':
                    op = left_command[0]
                    a = left_command[1]
                else:
                    a = left_command[0]
                    op = left_command[1]
                    b = left_command[2]

            if a.isalpha() and a not in identifiers:
                wires.append(wire)
                continue
            if b and b.isalpha() and b not in identifiers:
                wires.append(wire)
                continue

            if a.isalpha():
                a = identifiers[a]
            a =int(a)

            if b and b.isalpha():
                b = int(identifiers[b])
            if b:
                b = int(b)
            # print(wire)
            match op:
                case 'LOAD':
                    identifiers[t] = a
                case 'NOT':
                    identifiers[t] = ~a
                case 'AND':
                    identifiers[t] = a & b
                case 'OR':
                    identifiers[t] = a | b
                case 'LSHIFT':
                    identifiers[t] = a << b
                case 'RSHIFT':
                    identifiers[t] = a >> b
            identifiers[t] = identifiers[t] & 0xFFFF

        if 'a' in identifiers:
            return identifiers['a']
        else:
            total = 0
            for i in identifiers:
                total += identifiers[i]
            return total


    def calc_2(self, data: [str]) -> int:
        original_a = self.calc_1(data.copy())
        d: str
        identifiers = {}
        wires: list = data
        while len(wires) > 0:
            # print(len(wires))
            wire = wires.pop(0)
            command = wire.split(' -> ')
            t = command[1]
            b = None
            if len(command[0].split(' ')) == 1:
                a = command[0]
                if t == 'b':
                    a = str(original_a)
                op = "LOAD"
            else:
                left_command = command[0].split(' ')
                if left_command[0] == 'NOT':
                    op = left_command[0]
                    a = left_command[1]
                else:
                    a = left_command[0]
                    op = left_command[1]
                    b = left_command[2]

            if a.isalpha() and a not in identifiers:
                wires.append(wire)
                continue
            if b and b.isalpha() and b not in identifiers:
                wires.append(wire)
                continue

            if a.isalpha():
                a = identifiers[a]
            a = int(a)

            if b and b.isalpha():
                b = int(identifiers[b])
            if b:
                b = int(b)
            match op:
                case 'LOAD':
                    identifiers[t] = a
                case 'NOT':
                    identifiers[t] = ~a
                case 'AND':
                    identifiers[t] = a & b
                case 'OR':
                    identifiers[t] = a | b
                case 'LSHIFT':
                    identifiers[t] = a << b
                case 'RSHIFT':
                    identifiers[t] = a >> b
            identifiers[t] = identifiers[t] & 0xFFFF

        if 'a' in identifiers:
            return identifiers['a']
        else:
            total = 0
            for i in identifiers:
                total += identifiers[i]
            return total

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
