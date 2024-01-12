"""
AOC Day 10
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math
import re

from collections import deque
class Aoc2023010(AocBase):
    """
    AOC Day 10 Class
    """

    def is_possible(self, result, groups):
        if len(result) == 0:
            return True
        r = re.sub(r'\.+', '.', result)
        if r[0] == ".":
            r = r[1:]
        if len(r) > 0 and r[-1] == ".":
            r = r[0:-1]
        s = r.split(".")

        if len(s) > len(groups):
            return False

        for group_num in range(0, len(s)):
            if len(s[group_num]) < groups[group_num]:
                return True

            if len(s[group_num]) > groups[group_num]:
                return False

        return True

    def is_valid(self, result, groups):
        r = re.sub(r'\.+', '.', result)
        if r[0] == ".":
            r = r[1:]
        if len(r) > 0 and r[-1] == ".":
            r = r[0:-1]
        s = r.split(".")
        if len(s) != len(groups):
            return False
        group_num = 0
        for group in groups:
            if len(s[group_num]) != group:
                return False
            group_num += 1

        return True



    def calc_1(self, data: dict) -> int:
        result = 0
        for r in data:
            line, groups = r
            count = self.find_combinations2(line, groups)
            print(line,groups, count)
            result += count
        return result


    def find_combinations2x(self, line_in, groups_in):
        q = deque()
        q.append((line_in , groups_in, '', 'N'))
        count = 0
        while len(q) > 0:
            line, groups, result, mode = q.pop()
            group_sum = sum(groups) + len(groups) - 1
            print(line, groups, result, mode, len(line), group_sum)
            if len(line) < group_sum:
                continue

            if len(line) == 0:
                if len(groups) == 0:
                    # print(result, groups)
                    count += 1
                continue

            # if len(groups) and line.count('#') == 0:
            #     count += 1
            #     continue

            if mode == 'G':
                if line[0] in ['#', '?']:
                    if len(groups) == 0:
                        continue
                    current_group = groups[0]
                    current_group -= 1
                    new_groups = []
                    new_mode = mode
                    if current_group > 0:
                        new_groups = [current_group]
                    else:
                        new_mode = "S"
                    new_groups += groups[1:]
                    q.append((line[1:], new_groups, result + "#",  new_mode))
            elif mode == 'S':
                if line[0] in ['.', '?']:
                    if len(line) == 1:
                        q.append(('', groups, result + ".", mode))
                    else:
                        if line[1] == '.':
                            q.append((line[1:], groups, result + ".", 'S'))
                        elif line[1] == '#':
                            q.append((line[1:], groups, result + ".", 'G'))
                        elif line[1] == "?":
                            q.append((line[1:], groups, result + ".", 'S'))
                            q.append((line[1:], groups, result + ".", 'G'))
            else:
                if line[0] == '.':
                    q.append((line[1:], groups, result + ".", 'N'))
                elif line[0] == '#':
                    q.append((line, groups, result, 'G'))
                elif line[0] == '?':
                    q.append((line, groups, result, 'G'))
                    q.append((line[1:], groups, result + ".", 'N'))

        return count

    def find_combinations2(self, line_in, groups_in):
        q = deque()
        q.append((line_in , groups_in, '', 'N', []))
        winners = {}
        count = 0
        while len(q) > 0:
            line, groups, result, mode, group_starts = q.pop()
            position = len(line_in) - len(line)
            group_sum = sum(groups) + len(groups) - 1
            # if len(line) < group_sum:
            #     continue

            if len(line) == 0:
                if len(groups) == 0:
                    # print(line, groups, result, mode, len(line), group_sum, group_starts)
                    for i in range(len(group_starts)):
                        group_position = group_starts[i]
                        if i not in winners:
                            winners[i] = {}
                        if group_position not in winners[i]:
                            winners[i][group_position] = 0
                        winners[i][group_position] += 1

                    count += 1
                continue

            # if len(groups) and line.count('#') == 0:
            #     count += 1
            #     continue

            if mode == 'G':
                if line[0] in ['#', '?']:
                    if len(groups) == 0:
                        continue
                    current_group = groups[0]
                    current_group -= 1
                    new_groups = []
                    new_mode = mode
                    if current_group > 0:
                        new_groups = [current_group]
                    else:
                        new_mode = "S"
                    new_groups += groups[1:]
                    q.append((line[1:], new_groups, result + "#",  new_mode, group_starts))
            elif mode == 'S':
                if line[0] in ['.', '?']:
                    if len(line) == 1:
                        q.append(('', groups, result + ".", mode, group_starts))
                    else:
                        if line[1] == '.':
                            q.append((line[1:], groups, result + ".", 'S', group_starts))
                        elif line[1] == '#':
                            if len(group_starts) in winners and position + 1 in winners[len(group_starts)]:
                                winners[len(group_starts)][position + 1] += 1
                            else:
                                q.append((line[1:], groups, result + ".", 'G', group_starts + [position+1]))
                        elif line[1] == "?":
                            q.append((line[1:], groups, result + ".", 'S', group_starts))
                            if len(group_starts) in winners and position + 1 in winners[len(group_starts)]:
                                winners[len(group_starts)][position + 1] += 1
                            else:
                                q.append((line[1:], groups, result + ".", 'G', group_starts + [position+1]))
            else:
                if line[0] == '.':
                    q.append((line[1:], groups, result + ".", 'N', group_starts))
                elif line[0] == '#':
                    if len(group_starts) in winners and position in winners[len(group_starts)]:
                        winners[len(group_starts)][position] += 1
                    else:
                        q.append((line, groups, result, 'G',  group_starts + [position]))
                elif line[0] == '?':
                    if len(group_starts) in winners and position in winners[len(group_starts)]:
                        winners[len(group_starts)][position] += 1
                    else:
                        q.append((line, groups, result, 'G',  group_starts + [position]))
                    q.append((line[1:], groups, result + ".", 'N', group_starts))

        print(count, winners)
        return count


    def calc_2(self, data: [str]) -> int:
        result = 0
        for r in data:
            line, groups = r
            print(line, groups)
            count = self.find_combinations2(line, groups)
            print(line,groups, count)
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
    failed, results = aoc.run("part1_[3-3]+.txt", "part2x_[4-4]+.txt")
    if failed:
        sys.exit(1)
