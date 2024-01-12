"""
AOC Day 20
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
from collections import defaultdict
from dataclasses import dataclass, field


@dataclass
class Module:
    name: str
    module_type: str
    next_modules: list = field(default_factory=lambda: [])
    memory: defaultdict = field(default_factory=lambda: defaultdict(lambda: False))
    parents: list = field(default_factory=lambda: [])
    flip: bool = field(default_factory=lambda: False)

class Aoc2023020(AocBase):
    """
    AOC Day 20 Class
    """

    def calc_1(self, modules: dict[str, Module]) -> int:
        # Pulses - False for low, True for high
        pulses: dict[bool, int] = {False: 0, True: 0}

        # Button pressed 1000 times
        for i in range(1000):
            # Start at broadcaster - use modules_to_process as a queue
            # list of tuples with instruction, pulse level, caller module
            # Broadcaster sends a False pulse
            pulse: bool = False
            pulses[pulse] += 1
            modules_to_process: list[(Module, bool, str)] = []
            # add broadcaster modules to modules_to_process
            for module_name in modules['broadcaster'].next_modules:
                modules_to_process.append((modules[module_name], pulse, 'broadcaster'))
                pulses[pulse] += 1

            while len(modules_to_process) > 0:
                # store modules to be process in the next loop
                next_modules_to_process = []
                start_module: Module
                caller_module: str
                for start_module, pulse, caller_module in modules_to_process:
                    match start_module.module_type:
                        case '%':
                            # Flip-flop module, only flip if low (False) input pulse
                            if not pulse:
                                start_module.flip = not start_module.flip
                                for module_name in start_module.next_modules:
                                    next_modules_to_process.append(
                                        (modules[module_name], start_module.flip, start_module.name))
                                    pulses[start_module.flip] += 1
                        case '&':
                            # Conjunction module - send low pulse if all memory high else send low pulse
                            start_module.memory[caller_module] = pulse
                            next_pulse: bool = False
                            # check if all memory is high
                            for parent in start_module.parents:
                                if not start_module.memory[parent]:
                                    next_pulse = not next_pulse
                                    break
                            for module_name in start_module.next_modules:
                                # count pluses
                                pulses[next_pulse] += 1
                                if module_name in modules:
                                    next_modules_to_process.append((modules[module_name], next_pulse, start_module.name))

                modules_to_process = next_modules_to_process

        return pulses[True] * pulses[False]

    def calc_2(self, modules: dict[str, Module]) -> int:
        pulses = {False: 0, True: 0}

        last_module = [m.name for m in modules.values() if m.next_modules[0] == 'rx'][0]
        last_module_parent_count = len(modules[last_module].parents)

        differences = {}

        loop_count: int = 0
        while len(differences) != last_module_parent_count:
            loop_count += 1
            pulse: bool = False
            pulses[pulse] += 1
            modules_to_process: list[(Module, bool, str)] = []
            # add broadcaster modules to modules_to_process
            for module_name in modules['broadcaster'].next_modules:
                modules_to_process.append((modules[module_name], pulse, 'broadcaster'))
                pulses[pulse] += 1

            while len(modules_to_process) > 0:
                next_modules_to_process = []
                start_module: Module
                for start_module, pulse, caller_module in modules_to_process:
                    match start_module.module_type:
                        case '%':
                            # Flip-flop module, only flip if low (False) input pulse
                            if not pulse:
                                start_module.flip = not start_module.flip
                                for module_name in start_module.next_modules:
                                    next_modules_to_process.append(
                                        (modules[module_name], start_module.flip, start_module.name))
                                    pulses[start_module.flip] += 1
                        case '&':
                            # Conjunction module - send low pulse if all memory high else send low pulse
                            start_module.memory[caller_module] = pulse


                            next_pulse: bool = False
                            # check if all memory is high
                            for parent in start_module.parents:
                                if not start_module.memory[parent]:
                                    next_pulse = not next_pulse
                                    break

                            # send pulse to next modules
                            for module_name in start_module.next_modules:
                                # count pluses
                                pulses[next_pulse] += 1
                                if module_name in modules:
                                    next_modules_to_process.append((modules[module_name], next_pulse, start_module.name))

                            # Noticed that all parents of the last node where Conjunction modules and where firing at
                            # primary number intervals. so if I find these and multiply them will get when they
                            # all fire at the same time and send low pulse to the last_module
                            if start_module.name == last_module:
                                x = False
                                for parent in start_module.parents:
                                    if start_module.memory[parent]:
                                        x = parent
                                        break

                                if x and x not in differences:
                                    # the variable loop_count is the number of iterations before parent fires for the first time
                                    differences[x] = loop_count

                modules_to_process = next_modules_to_process

        # multiple up primes when last modules parents fire.
        total = 1
        for difference in differences:
            # print(difference, differences[difference])
            total *= differences[difference]

        return total

    def load_handler_part1(self, data: [str]) -> [str]:
        modules: dict[str, Module] = {}
        parents = defaultdict(set)
        for line in data:
            d = line.split(' -> ')
            name = d[0]
            module_type = 'S'
            if name[0] in ['%', '&']:
                module_type = name[0]
                name = name[1:]
            next_modules = d[1].split(', ')
            for next_module in next_modules:
                parents[next_module].add(name)
            status = defaultdict(bool)
            modules[name] = Module(name, module_type, next_modules, status)

        for i in modules:
            modules[i].parents = parents[i]
            if modules[i].module_type == '&':
                for parent in parents[i]:
                    modules[i].memory[parent] = False

        return modules

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc2023020()
    failed, results = aoc.run('part1_[0-9]+.txt', 'part2_[0-9]+.txt')
    if failed:
        sys.exit(1)
