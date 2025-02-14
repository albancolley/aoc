"""
AOC Day 20
"""
import sys
from common import AocBase
from common import configure

from collections import defaultdict

class Aoc2023020(AocBase):
    """
    AOC Day 20 Class
    """

    def calc_1(self, instructions: dict) -> int:
        result = 0
        pulses = {False: 0, True: 0}

        for i in range(1000):
            modules_to_process = [(instructions['broadcaster'], False, '')]
            pulses[False] += 1
            while len(modules_to_process) > 0:
                next_modules_to_process = []
                for start_module, pulse, caller_module in modules_to_process:
                    # print(start_module, pulse, caller_module)
                    parent_name = start_module['name']
                    # print(f'{caller_module} {pulse} {parent_name}')

                    if parent_name == 'output':
                        # pulses[pulse] += 1
                        continue

                    type = start_module['type']
                    if type == 'S':
                        for module_name in start_module['next_modules']:
                            module = instructions[module_name]
                            next_modules_to_process.append((module, pulse, parent_name))
                            pulses[pulse] += 1
                    elif type == '%':
                        if not pulse:
                            start_module['status']['filp'] = not start_module['status']['filp']
                            for module_name in start_module['next_modules']:
                                module = instructions[module_name]
                                next_modules_to_process.append((module, start_module['status']['filp'], parent_name))
                                pulses[start_module['status']['filp']] += 1
                    elif type == '&':
                        start_module['status'][caller_module] = pulse
                        high = True
                        for parent in start_module['parents']:
                            if not start_module['status'][parent]:
                                high = False
                                break
                        for module_name in start_module['next_modules']:
                            pulses[not high] += 1
                            if module_name in instructions:
                                module = instructions[module_name]
                                next_modules_to_process.append((module, not high, parent_name))

                modules_to_process = next_modules_to_process

        print(pulses[False], pulses[True])
        return pulses[True] * pulses[False]

    def calc_2(self, instructions: [str]) -> int:
        pulses = {False: 0, True: 0}

        differences = {}

        i = 0
        while True:
            i += 1
            modules_to_process = [(instructions['broadcaster'], False, '')]
            pulses[False] += 1

            if len(differences) == len(instructions['zh']["parents"]):
                total = 1
                for difference in differences:
                    total *= differences[difference]
                return total

            while len(modules_to_process) > 0:
                next_modules_to_process = []
                for start_module, pulse, caller_module in modules_to_process:
                    # print(start_module, pulse, caller_module)
                    parent_name = start_module['name']
                    # print(f'{caller_module} {pulse} {parent_name}')

                    if parent_name == 'output':
                        # pulses[pulse] += 1
                        continue

                    if parent_name == 'rx':
                        if not pulses:
                            return i
                        continue

                    type = start_module['type']
                    if type == 'S':
                        for module_name in start_module['next_modules']:
                            module = instructions[module_name]
                            next_modules_to_process.append((module, pulse, parent_name))
                            pulses[pulse] += 1
                    elif type == '%':
                        if not pulse:
                            start_module['status']['filp'] = not start_module['status']['filp']
                            for module_name in start_module['next_modules']:
                                module = instructions[module_name]
                                next_modules_to_process.append(
                                    (module, start_module['status']['filp'], parent_name))
                                pulses[start_module['status']['filp']] += 1
                    elif type == '&':
                        start_module['status'][caller_module] = pulse
                        high = True
                        x = ""
                        for parent in start_module['parents']:
                            if start_module['status'][parent]:
                                x += '1'
                            else:
                                x += '0'

                        if parent_name == "zh" and "1" in x:
                            if x not in differences:
                                differences[x] = i
                        for parent in start_module['parents']:
                            if not start_module['status'][parent]:
                                high = False
                                break
                        for module_name in start_module['next_modules']:
                            pulses[not high] += 1
                            if module_name in instructions:
                                module = instructions[module_name]
                                next_modules_to_process.append((module, not high, parent_name))

                modules_to_process = next_modules_to_process

        print(pulses[False], pulses[True])
        return pulses[True] * pulses[False]
    def load_handler_part1(self, data: [str]) -> [str]:
        instructions = {
            "output": {"name": "output", "type": "O", "next_modules": [], "status" : set()},
            "rx": {"name": "rx", "type": "X", "next_modules": [], "status": set()}
        }
        parents = defaultdict(set)
        for line in data:
            d = line.split(' -> ')
            name = d[0]
            type = 'S'
            if name[0] in ['%', '&']:
                type=name[0]
                name = name[1:]
            next_modules = d[1].split(', ')
            for next_module in next_modules:
                parents[next_module].add(name)
            status = defaultdict(bool)
            instructions[name] = {"name": name, "type":type, "next_modules": next_modules, "status" : status}

        for i in instructions:
            instructions[i]['parents'] = parents[i]
            if instructions[i]['type'] == "&":
                for parent in parents[i]:
                    instructions[i]['status'][parent] = False


        return instructions

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc2023020()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
