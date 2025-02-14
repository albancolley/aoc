"""
AOC Day 7
"""
import sys
from common import AocBase
from common import configure
import math

class Aoc202307(AocBase):
    """
    AOC Day 7 Class
    """


    def calc_1(self, data: dict) -> int:
        steps = 0
        pos = 'AAA'
        instruction = data['instruction']
        while pos != 'ZZZ':
            for i in instruction:
                steps += 1
                options = data[pos]
                if i == 'L':
                    pos = options[0]
                else:
                    pos = options[1]
                if pos == 'ZZZ':
                    break
        return steps


    def calc_2(self, data: [str]) -> int:
        positions = data['starting']
        instruction = data['instruction']
        end_counts = []
        for pos in positions:
            start_pos = pos
            steps = 0
            while True:
                for i in instruction:
                    steps += 1
                    options = data[pos]
                    if i == 'L':
                        pos = options[0]
                    else:
                        pos = options[1]
                    if pos.endswith('99'):
                        break
                if pos.endswith('99'):
                    end_counts.append(steps)
                    break
        lcm = math.lcm(*end_counts)
        return lcm

    def load_handler_part1(self, data: [str]) -> [str]:
        result = {}
        result['instruction'] = data[0]
        for r in data[2:]:
            d = r.split('=')
            m = d[1].replace(' ', '')[1:-1].split(',')
            result[d[0].strip()] = m
        return result

    def load_handler_part2(self, data: [str]) -> [str]:
        result = {}
        starting = []
        result['instruction'] = data[0]
        result['starting'] = starting
        for r in data[2:]:
            d = r.split('=')
            m :str = d[1].replace(' ', '')[1:-1].split(',')
            pos = d[0].strip()
            if pos.endswith('A'):
                starting.append(pos)
            result[pos] = m
        return result


if __name__ == '__main__':
    configure()
    aoc = Aoc202307()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
