"""
AOC Day X
"""
import sys

from common import AocBase
from common import configure
import heapq

class Aoc202419(AocBase):
    """
    AOC Day 19 Class
    """

    def calc_1(self, data: dict) -> int:
        result = 0
        towels, designs = data

        # print(towels, designs)
        for design in designs:
            # print(design)
            queue = []
            seen = {design}
            heapq.heappush(queue, (len(design), design))
            found = False
            while len(queue) > 0 and not found:
                # print(queue)
                _, partial_design = heapq.heappop(queue)
                for towel in towels:
                    if partial_design.startswith(towel):
                        if partial_design == towel:
                            found = True
                            result += 1
                            break
                        new_design = partial_design[len(towel):]
                        if new_design not in seen:
                            heapq.heappush(queue, (len(new_design), new_design))
                            seen.add(new_design)

        return result

    def calc_2(self, data: [str]) -> int:
        result = 0
        towels, designs = data

        # print(towels)
        for design in designs:
            # print(design)
            queue = []
            seen = {design: [], 'END':[]}
            heapq.heappush(queue, (len(design), design))

            found = False
            while len(queue) > 0:
                # print(queue)
                _, partial_design = heapq.heappop(queue)
                for towel in towels:
                    if partial_design.startswith(towel):
                        if partial_design == towel:
                            seen['END'] += [towel]
                            found = True
                            continue

                        new_design = partial_design[len(towel):]
                        if new_design not in seen:
                            heapq.heappush(queue, (len(new_design), new_design, ))
                            seen[new_design] = []
                        seen[new_design] += [partial_design]

            if found:
                counts = dict()
                for patterns in seen.values():
                    for pattern in patterns:
                        counts[pattern] = 0
                for towel in seen['END']:
                    counts[towel] = 1

                for i in range(1, len(design)):
                    for c in counts:
                        if len(c) == i:
                            for v in seen[c]:
                                counts[v] += counts[c]
                result += counts[design]
        return result

    def load_handler_part1(self, data: [str]) -> [str]:
        towels = data[0].split(", ")
        line = 2
        designs = []
        while line < len(data):
            designs += [data[line]]
            line+= 1
        return towels, designs

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc202419()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
