"""
AOC Day 10
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure

class Aoc2023010(AocBase):
    """
    AOC Day 10 Class
    """

    cache = {}
    group_positions_cache = {}

    def get_group_start_positions(self, depth, position, line, groups):
        line_length = len(line)

        if depth == 3 and position == 11:
            pass

        if position >= line_length:
            return []

        remaining_groups = groups[depth:]
        current_group_length = remaining_groups[0]
        min_length = sum(remaining_groups) + len(remaining_groups) - 1
        end_position = line_length - min_length

        group_start_positions = []
        for i in range(end_position, position -1, -1):
            is_group = True

            if '#' in line[position: i]:
                continue

            if i > 0 and line[i-1] == '#':
                continue

            for j in range(current_group_length):
                if line[i+j] == '.':
                    is_group = False
                    break

            if is_group:
                if i + j == line_length - 1:
                    group_start_positions.append(i)
                elif line[i + j + 1] != '#':
                    group_start_positions.append(i)

        return group_start_positions

    def find_combinations(self, depth, position, line, groups):


        if depth == len(groups):
            if '#' in line[position:]:
                return 0
            else:
                return 1

        score = 0

        group_positions_index = (depth, position)

        if group_positions_index in self.group_positions_cache:
            return self.group_positions_cache[group_positions_index]

        group_positions = self.get_group_start_positions(depth, position, line, groups)

        for group_position in group_positions:
            index = f'{depth}-{group_position}'
            if index in self.cache:
                r = self.cache[index]
            else:
                r = self.find_combinations(depth + 1, group_position + groups[depth] + 1, line, groups)
            score += r

        self.group_positions_cache[group_positions_index] = score

        return score

    def calc_1(self, data: dict) -> int:
        result = 0
        for r in data:
            self.cache = {}
            self.group_positions_cache = {}
            line, groups = r
            count = self.find_combinations(0, 0, line, groups)
            result += count

        return result

    def calc_2(self, data: [str]) -> int:
        result = 0
        self.cache = {}
        for r in data:
            self.cache = {}
            self.group_positions_cache = {}
            line, groups = r
            # print(line, groups)
            count = self.find_combinations(0, 0, line, groups)
            # print(line, groups, count)
            result += count

        return result

    def load_handler_part1(self, data: [str]) -> [str]:
        result = []
        for d in data:
            s = d.split(" ")
            g = [int(x) for x in s[1].split(',')]
            result.append((s[0], g))
        return result

    def load_handler_part2(self, data: [str]) -> [str]:
        result = self.load_handler_part1(data)
        new_result = []
        for r in result:
            s = (r[0] + '?') * 5
            s = s[0:-1]
            g = r[1] * 5
            new_result.append((s, g))
        return new_result


if __name__ == '__main__':
    configure()
    aoc = Aoc2023010()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
