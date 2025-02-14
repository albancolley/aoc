"""
AOC Day 07
"""
import re
import sys

from common import AocBase
from common import configure


class Aoc201807(AocBase):
    """
    AOC Day 07 Class
    """

    def calc_1(self, data: dict) -> int:
        steps, reverse_steps, start, end= data
        print(steps, reverse_steps, start, end)
        queue = [start]
        result = []
        while len(queue) > 0:
            possibles = []
            for step in queue:
                ok = True
                for s in reverse_steps[step]:
                    if s not in result:
                        ok = False
                        break
                if ok:
                    possibles += [step]
            possibles.sort()
            if len(possibles) == 0:
                continue
            next_value = possibles[0]
            result += [next_value]
            queue.remove(next_value)
            for s in steps[next_value]:
                if s not in queue:
                    queue += [s]
        return "".join(result)

    def calc_2(self, data: [str]) -> int:
        total = 0
        return total

    def load_handler_part1(self, data: [str]) -> [str]:
        steps: dict = dict()
        reverse_steps: dict = dict()
        for d in data:
            p = r'Step (\w+) must be finished before step (\w+) can begin.'
            m = re.match(p, d)
            before = m.group(1)
            after =  m.group(2)
            if before not in reverse_steps:
                reverse_steps[before] = []
            if after not in reverse_steps:
                reverse_steps[after] = []
            if before not in steps:
                steps[before] = []
            if after not in steps:
                steps[after] = []
            steps[before] += [after]
            reverse_steps[after] += [before]

        start = ""
        end = ""

        for s in steps:
            if len(steps[s]) == 0:
                end = s
                break

        for s in reverse_steps:
            if len(reverse_steps[s]) == 0:
                start = s
                break

        return steps, reverse_steps, start, end

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201807()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
