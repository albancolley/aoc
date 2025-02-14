"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure


class Aoc201716(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: tuple) -> str:
        programs: list[str]
        programs, steps = data
        number_programs = len(programs)
        programs = self.dance(number_programs, programs, steps)
        return ''.join(programs)

    def dance(self, number_programs, programs, steps):
        for step in steps:
            match step[0]:
                case 's':
                    moves = int(step[1:]) % number_programs
                    for i in range(moves):
                        programs = programs[number_programs - 1:] + programs[0:number_programs - 1]
                case 'x':
                    p1 = int(step[1:].split('/')[0])
                    p2 = int(step[1:].split('/')[1])
                    programs[p1], programs[p2] = programs[p2], programs[p1]
                case 'p':
                    p1 = int(programs.index(step[1:].split('/')[0]))
                    p2 = int(programs.index(step[1:].split('/')[1]))
                    a = programs[p1]
                    b = programs[p2]
                    programs[p1], programs[p2] = b, a
        return programs

    def calc_2(self, data: tuple) -> str:
        programs: list[str]
        programs, steps = data
        number_programs = len(programs)
        key = ''.join(programs)
        seen: dict = {key: 0, 0: key}
        for count in range(1, 1000000000):
            programs = self.dance(number_programs, programs, steps)
            key = ''.join(programs)
            if key in seen:
                return seen[1000000000 % count]
            seen[key] = count
            seen[count] = key
        return ''.join(programs)

    def load_handler_part1(self, data: [str]) -> [str]:
        size = int(data[0])
        programs = [chr(ord('a') + x) for x in range(size)]
        steps = data[1].split(',')
        return programs, steps

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201716()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
