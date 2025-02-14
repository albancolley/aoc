"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure
import collections


class Aoc201712(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict[str, set]) -> int:

        start = 0

        seen = self.find_group(data, start)

        return len(seen)

    def find_group(self, data, start):
        queue: list = [start]
        seen: list = []
        while len(queue) > 0:
            q = queue.pop(0)
            seen.append(q)
            for i in data[q]:
                if i not in seen and i not in queue:
                    queue.append(i)
        return seen

    def calc_2(self, data: dict[str, set]) -> int:
        groups = 0
        programs_ids: list = list(data.keys())
        while len(programs_ids) > 0:
            groups += 1
            group = self.find_group(data, programs_ids[0])
            for programs_id in group:
                programs_ids.remove(programs_id)

        return groups

    def load_handler_part1(self, data: [str]) -> [str]:
        out = collections.defaultdict(set)
        d : str
        for d in data:
            s = d.split(' <-> ')
            key = int(s[0])
            values = set([int(x) for x in s[1].split(', ')])
            if key in out:
                out[key].update(values)
            else:
                out[key] = values
            for i in values:
                out[i].add(key)
        return out

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201712()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
