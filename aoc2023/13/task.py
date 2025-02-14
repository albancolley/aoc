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

    def calc_1(self, data: dict) -> int:
        result = 0
        for b in data:
            rows = data[b]['r']
            cols = data[b]['c']
            r = self.find_middle(rows)
            c = self.find_middle(cols)
            if r==0 and c==0:
                return 0
            result += c
            result += (100*r)

        # 21639 too low
        return result

    def find_middle(self, rows):
        for i in range(1, len(rows)):
            first = list(reversed(rows[0:i]))
            second = rows[i:]
            no_match = False
            loop_size = min(len(first), len(second))
            for j in range(0, loop_size):
                if first[j] != second[j]:
                    no_match = True
            if not no_match:
                return i

        return 0

    def find_middle2(self, rows):
        for i in range(1, len(rows)):
            first = list(reversed(rows[0:i]))
            second = rows[i:]
            loop_size = min(len(first), len(second))
            new = []
            for j in range(0, loop_size):
                new.append(first[j] - second[j])
            if new.count(0) == len(new) - 1:
                n = abs([x for x in new if x != 0][0])
                if (n & (n - 1) == 0) and n != 0:
                    return i
        return 0
    def calc_2(self, data: [str]) -> int:
        result = 0
        for b in data:
            rows = data[b]['r']
            cols = data[b]['c']
            r = self.find_middle2(rows)
            c = self.find_middle2(cols)

            result += c
            result += (100 * r)

        return result

    def load_handler_part1(self, data: [str]) -> [str]:
        blocks = {}
        block_number = 1
        blocks[block_number] = {"r": [], "c": []}
        cols = {}
        for d in data:
            if not d:
                for i in range(0, len(n)):
                    blocks[block_number]['c'].append(int(cols[i], 2))
                block_number += 1
                blocks[block_number] = {"r": [], "c": []}
                cols = {}
                continue
            n = d.replace('#', '1').replace('.', '0')
            for i in range(0, len(n)):
                if i not in cols:
                    cols[i] = ''
                cols[i] += n[i]
            blocks[block_number]['r'].append(int(n,2))
        return blocks

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc2023010()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
