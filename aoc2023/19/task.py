"""
AOC Day 10
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math
import copy

class Aoc2023010(AocBase):
    """
    AOC Day 10 Class
    """

    def process_command(self, command, part):
        if command[0] == '>':
            if part[command[1]] > command[2]:
                return command[3]
        elif command[0] == '<':
            if part[command[1]] < command[2]:
                return command[3]
        else:
            return command

        return 'N'
    def process_workflow(self, workflow, part):
        for command in workflow:
            result = self.process_command(command, part)
            if result != 'N':
                return  result

    def calc_1(self, data: dict) -> int:
        workflows, parts = data
        accepted =[]
        for part in parts:
            current_workflow = workflows['in']
            while True:
                output = self.process_workflow(current_workflow, part)
                if output == 'A':
                    accepted += [part]
                    break
                elif output == 'R':
                    break
                else:
                    current_workflow = workflows[output]

        total = 0
        for part in accepted:
            for v in part:
                total += part[v]

        return total


    def process_command_cominations(self, command, part):
        return_party = copy.deepcopy(part)
        return_party2 = copy.deepcopy(part)
        if command[0] == '>':
            part_start, part_end = part[command[1]]
            value = command[2]
            if part_start > value:
                return_party[command[1]] = (part_start, part_end)
                return_party2[command[1]] = (0, 0)
                return command[3], return_party, return_party2
            elif part_end > value:
                return_party[command[1]] = (value + 1, part_end)
                return_party2[command[1]] = (part_start, value)
                return command[3], return_party, return_party2
            else:
                return_party2[command[1]] = (0, 0)
                return "R", return_party, return_party2
        elif command[0] == '<':
            part_start, part_end = part[command[1]]
            value = command[2]
            if part_end < value:
                return_party2[command[1]] = (0, 0)
                return_party[command[1]] = (part_start, part_end)
                return command[3], return_party, return_party2
            elif part_start < value <= part_end:
                return_party[command[1]] = (part_start, value- 1)
                return_party2[command[1]] = (value, part_end)
                return command[3], return_party, return_party2
            else:
                return_party2[command[1]] = (0, 0)
                return "R", return_party, return_party2
        else:
            return command, return_party, return_party2

        return 'N'

    def process_workflow_combinations(self, workflow, part):
        new_commands = []
        for command in workflow:
            result, new_part, new_part2 = self.process_command_cominations(command, part)
            if result != "R":
                new_commands.append((result, new_part))
            part = new_part2
        return new_commands


    def calc_2(self, data: [str]) -> int:

        workflows, parts = data
        queue = [('in', {'x':(1,4000),'m':(1,4000),'a':(1,4000),'s':(1,4000)})]
        accepted = []
        while len(queue) > 0:
            workflow, values = queue.pop()
            if workflow == 'pv':
                pass
            if workflow == 'A':
                accepted += [values]
            elif workflow != 'R':
                current_workflow = workflows[workflow]
                new_entries = self.process_workflow_combinations(current_workflow, values)
                queue += new_entries


        total = 0
        for part in accepted:
            sub_total = 1
            for v in part:
                sub_total *= part[v][1] - part[v][0] + 1
            total += sub_total
        return total

    def load_handler_part1(self, data: [str]) -> [str]:
        workflows = {}
        parts = []
        pos = 0
        while True:
            if len(data[pos]) == 0:
                break
            s1 = data[pos].split('{')
            name = s1[0]
            s2 = s1[1][:-1]
            workflows[name] =[]
            for rule in s2.split(','):
                if '<' in rule:
                    r1 = rule.split('<')
                    r2 = r1[1].split(':')
                    workflows[name].append(('<',r1[0], int(r2[0]), r2[1]))
                elif '>' in rule:
                    r1 = rule.split('>')
                    r2 = r1[1].split(':')
                    workflows[name].append(('>',r1[0], int(r2[0]), r2[1]))
                else:
                    workflows[name].append(rule)
            pos += 1

        for line in data[pos+1:]:
            values = line[1:-1].split(',')
            ratings ={}
            for value in values:
                v = value.split('=')
                ratings[v[0]] = int(v[1])
            parts.append(ratings)
        return workflows, parts

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc2023010()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
