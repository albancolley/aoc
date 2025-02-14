"""
AOC Day 10
"""
import sys
from common import AocBase
from common import configure
import re

from collections import defaultdict

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
            count = self.find_combinations2x(line, groups)
            print(line, count)
            result += count
        return result

    def find_combinations2(self, line, groups):
        q = [(0, 0, 'N', [])]
        line_length = len(line)
        groups_length = len(groups)
        while len(q) > 0:
            position, group_number, mode, postion_starts = q.pop()

            if mode == 'N':
                while line[position] == '.':
                    position += 1
                value = line[position]
                if value in  ['#', '?']:
                    q.append((position, group_number, 'G', postion_starts))
                if value =='?':
                    q.insert(0, (position+1, group_number, mode, postion_starts))
            if mode == 'G':
                is_group = True
                start_position = position
                group_length = groups[group_number]
                if position + group_length > line_length:
                    continue

                for i in range(group_length):
                    position += 1

                    if line[position] == '.':
                        is_group = False
                        break

                if is_group:
                    print(start_position)
                    # if group_number + 1 == groups_length:
                    #     print(postion_starts)
                    # else:
                    q.insert(0, (position, group_number + 1, "S", postion_starts + [start_position]))
            if mode == 'S':
                is_end = False
                while line[position] == '.':
                    position += 1
                    if position == line_length:
                        is_end = True
                        break

                if not is_end:
                    if line[position] == '#' or line == '?':
                        q.append((position, group_number, 'G', postion_starts))

                    if line == '?':
                        q.insert(0, (position + 1, group_number, mode, postion_starts))

        return 0

    def find_combinations2x(self, line_in, groups_in):
        q = [(line_in , groups_in, '', 'N', [])]
        winners = {}
        counts = defaultdict(int)
        last_groups = []
        last_groups_starts = []
        count = 0
        while len(q) > 0:
            line, groups, result, mode, group_starts = q.pop()
            position = len(line_in) - len(line)
            group_sum = sum(groups) + len(groups) - 1
            # if len(line) < group_sum:
            #     continue
            # print(result)
            if len(line) == 0:
                if len(groups) == 0:
                    if len(last_groups) > 0:
                        for i in range(len(group_starts)-1, -1, -1):
                            if group_starts[i] != last_groups[i]:
                                break
                            else:
                                index = f"{i}-{group_starts[i]}"
                                if index not in winners:
                                    winners[index] = 0
                                winners[index] += 1

                    last_groups = group_starts

                    #
                    # last_start_group = group_starts[-1]
                    # index = f"1-{last_start_group}"
                    # counts[index] += 1
                    #
                    # if last_groups != group_starts:
                    #     if last_groups:
                    #         last_index = f"1-{last_groups[-1]}"
                    #         winners[last_index] = counts[last_index]
                    #     last_groups = group_starts


                    # print(result, group_starts, winners)


                    count += 1
                continue

            # if len(groups) and line.count('#') == 0:
            #     count += 1
            #     continue

            if mode == 'G':
                if line[0] in ['#', '?']:
                    current_group = groups[0]
                    current_group -= 1
                    new_groups = []
                    if current_group > 0:
                        new_groups = [current_group]
                    new_groups += groups[1:]

                    if current_group > 0:
                        q.append((line[1:], new_groups, result + "#", "G", group_starts))
                    else:
                        q.insert(0, (line[1:], new_groups, result + "#", "S", group_starts))
            elif mode == 'GS':
                if len(groups) == 0:
                    continue
                i = len(group_starts)-1

                index = f"{i}-{group_starts[i]}"
                # print(index, group_starts)
                if index in winners:
                    pass

                else:
                    q.append((line, groups, result, 'G', group_starts))
            elif mode == 'S':
                if line[0] in ['.', '?']:
                    if len(line) == 1:
                        q.append(('', groups, result + ".", mode, group_starts))
                    else:
                        if line[1] == '.':
                            q.insert(0, (line[1:], groups, result + ".", 'S', group_starts))
                        elif line[1] == '#':
                            q.append((line[1:], groups, result + ".", 'GS', group_starts + [position+1]))
                        elif line[1] == "?":
                            q.insert(0, (line[1:], groups, result + ".", 'S', group_starts))
                            q.append((line[1:], groups, result + ".", 'GS', group_starts + [position+1]))
            else:
                if line[0] == '.':
                    q.insert(0, (line[1:], groups, result + ".", 'N', group_starts))
                elif line[0] == '#':
                    q.append((line, groups, result, 'GS',  group_starts + [position]))
                elif line[0] == '?':
                    q.append((line, groups, result, 'GS',  group_starts + [position]))
                    q.insert(0, (line[1:], groups, result + ".", 'N', group_starts))

        # print(count, winners)
        return count


    def calc_2(self, data: [str]) -> int:
        result = 0
        for r in data:
            line, groups = r
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
