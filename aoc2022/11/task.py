import string

from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
from dataclasses import dataclass, field
from collections import OrderedDict

logger = logging.getLogger("ACO2022-11")

@dataclass()
class Monkey:
    id: int
    items: [int]
    operation: [str]
    test: int
    test_true: int
    test_false: int
    inspections: int = 0
    worry_div = 3
    divisor = 1

    def inspect(self, item: int) -> int:
        self.inspections += 1

        item = item % self.divisor

        worry = 0
        if self.operation[0] == "*":
            if self.operation[1] == "old":
                worry = item * item
            else:
                worry = item * int(self.operation[1])
        if self.operation[0] == "+":
            if self.operation[1] == "old":
                worry = item + item
            else:
                worry = item + int(self.operation[1])

        if self.worry_div != 1:
            worry = int(worry / self.worry_div)

        if worry % self.test == 0:
            return self.test_true, worry


        return self.test_false, worry


class Aoc202211(AocBase):

    def calc_1(self, data:[Monkey]) -> int:
        loops = 20
        for _ in range(0, loops):
            for monkey in data:
                for item in monkey.items:
                    next_monkey, worry = monkey.inspect(item)
                    data[next_monkey].items.append(worry)
                monkey.items = []
        totals = [monkey.inspections for monkey in data]
        totals.sort()
        return totals[-1] * totals[-2]

    def calc_2(self, data: [str]) -> int:
        loops = 10000
        for i in range(0, loops):
            for monkey in data:
                for item in monkey.items:
                    next_monkey, worry = monkey.inspect(item)
                    data[next_monkey].items.append(worry)
                monkey.items = []
            if i % 20 == 0:
                print(f'{i}:{data[0].inspections}')
        totals = [monkey.inspections for monkey in data]
        totals.sort()
        return totals[-1] * totals[-2]

    def load_handler_part1(self, data: [str]) -> {Monkey}:
        new_data: [Monkey] = []
        pos = 0
        while pos < len(data):
            id = data[pos][len("Monkey "):]
            items = [int(int_value) for int_value in data[pos+1][len("  Starting items: "):].split(",")]
            operation = data[pos+2][len("  Operation: new = old "):].split(" ")
            test = int(data[pos+3][len("  Test: divisible by "):])
            test_true = int(data[pos+4][len("    If true: throw to monkey "):])
            test_false = int(data[pos+5][len("    If false: throw to monkey "):])
            m = Monkey(id, items, operation, test, test_true, test_false)
            pos += 7
            new_data.append(m)

        return new_data

    def load_handler_part2(self, data: [str]) -> [str]:
        new_data = self.load_handler_part1(data)
        divisor = 1
        for monkey in new_data:
            monkey.worry_div = 1
            divisor *= monkey.test
        for monkey in new_data:
            monkey.divisor = divisor
        return new_data


if __name__ == '__main__':
    configure()
    aoc = Aoc202211()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        exit(1)
