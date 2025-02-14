"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure
import itertools
import copy


class Aoc201600(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict[int,[str]] ) -> int:
        seen = []
        lowest = 1000000
        queue = [(1, copy.deepcopy(data), 0)]
        last_count = 1
        while len(queue) > 0:
            level, arrangement, count = queue.pop(0)

            if count == last_count:
                print(len(queue), level, arrangement, count)
                last_count += 1

            match = self.match_str(arrangement, level)
            if match in seen:
                continue

            invalid = self.is_invalid(arrangement)

            if invalid:
                # print('I', len(queue), level, arrangement, count)
                continue

            # print(len(queue), level, arrangement, count)
            if len(arrangement[1]) == 0 and len(arrangement[2]) == 0 and len(arrangement[3]) == 0 and level ==4:
                lowest = min(lowest, count)
                print (lowest)
                break

            seen += [match]

            seen_pair = False
            for L in range(1, 3):
                for subset in itertools.combinations(arrangement[level], L):
                    new_arrangement: dict[int,[str]] = copy.deepcopy(arrangement)
                    if seen_pair:
                        continue
                    if len(subset) == 2 and subset[0][0] != subset[1][0] and subset[0][1] != subset[1][1]:
                        continue
                    if len(subset) == 2 and subset[0][1] == subset[1][1]:
                        seen_pair = True
                    for s in subset:
                        new_arrangement[level].remove(s)
                    if level > 1:
                        are_empty = True
                        for i in range(1, level):
                            if len(new_arrangement[i]) > 0:
                                are_empty = False
                                break
                        if not are_empty:
                            new_arrangement2 = copy.deepcopy(new_arrangement)
                            new_arrangement2[level -1] += subset
                            if not self.is_invalid(new_arrangement2) and not self.match_str(new_arrangement2, level-1) in seen:
                                queue.append((level - 1, new_arrangement2 ,count+1))
                    if level < 4:
                        new_arrangement2 = copy.deepcopy(new_arrangement)
                        new_arrangement2[level + 1] += subset
                        if not self.is_invalid(new_arrangement2) and not self.match_str(new_arrangement2, level+1) in seen:
                            queue.append((level + 1, new_arrangement2, count+1))

        return lowest

    def match_str(self, arrangement, level):
        match = f'{level}:{sorted(arrangement[1])}:{sorted(arrangement[2])}:{sorted(arrangement[3])}:{sorted(arrangement[4])}'
        return match

    def is_invalid(self, arrangement):
        invalid = False
        for check_level in range(1, 5):
            floor_m = set([c[1] for c in arrangement[check_level] if c[0] == 'microchip'])
            floor_g = set([c[1] for c in arrangement[check_level] if c[0] == 'generator'])

            diff = floor_m - floor_g

            if len(floor_g) > 0 and len(diff) > 0:
                invalid = True
                break
        return invalid

    def calc_2(self, data: [str]) -> int:
        total = 0
        return total

    def load_handler_part1(self, data: [str]) -> {}:
        floor_lookup = {
            'first': 1,
            'second': 2,
            'third': 3,
            'fourth': 4,
        }
        floors = {
            1: [],
            2: [],
            3: [],
            4: [],
        }
        row: str
        for row in data:
            sections = row.split(' a ')
            floor = floor_lookup[sections[0].split(' ')[1]]
            for section in sections[1:]:
                if '-' in section:
                    floors[floor].append(('microchip', section.split('-')[0]))
                else:
                    floors[floor].append(('generator', section.split(' ')[0]))
        return floors

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201600()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2x_[0-9]+.txt")
    if failed:
        sys.exit(1)
