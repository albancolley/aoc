"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure
import collections


class Aoc201724(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: []) -> int:
        result = 0
        paths = [[[0, max(d[0], d[1])], [d]] for d in data if d[0] ==0 or d[1] ==0]
        max_cost = 0
        for path in paths:
            max_cost = max(max_cost, sum(path[0]))
        while len(paths) > 0:
            # print(paths)
            path = paths.pop(0)
            pins_size = path[0][-1]
            next_components = [c for c in data if c not in path[1] and (c[0] == pins_size or c[1] == pins_size)]
            for next_component in next_components:
                next_pin_size = next_component[0]
                if next_pin_size == pins_size:
                    next_pin_size = next_component[1]
                new_path_1 = path[0].copy()
                new_path_1 += [pins_size, next_pin_size]
                new_path_2 = path[1].copy()
                new_path_2.append(next_component)
                paths.insert(0, [new_path_1, new_path_2])


            max_cost = max(max_cost, sum(path[0]))


        return max_cost

    def calc_2(self, data: [str]) -> int:
        paths = [[[0, max(d[0], d[1])], [d]] for d in data if d[0] ==0 or d[1] ==0]
        max_cost = collections.defaultdict(int)

        for path in paths:
            max_cost[1] = max(max_cost[1], sum(path[0]))
        while len(paths) > 0:
            # print(paths)
            path = paths.pop(0)
            pins_size = path[0][-1]
            next_components = [c for c in data if c not in path[1] and (c[0] == pins_size or c[1] == pins_size)]
            for next_component in next_components:
                next_pin_size = next_component[0]
                if next_pin_size == pins_size:
                    next_pin_size = next_component[1]
                new_path_1 = path[0].copy()
                new_path_1 += [pins_size, next_pin_size]
                new_path_2 = path[1].copy()
                new_path_2.append(next_component)
                paths.insert(0, [new_path_1, new_path_2])

            max_cost[len(path[1])] = max(max_cost[len(path[1])], sum(path[0]))

        return max_cost[max(max_cost.keys())]


    def load_handler_part1(self, data: [str]) -> [str]:
        result = []
        for d in data:
            x = d.split("/")
            result.append((int(x[0]), int(x[1])))
        return result

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201724()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
