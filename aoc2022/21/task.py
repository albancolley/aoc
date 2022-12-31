import dataclasses
import os.path
import string

from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
from dataclasses import dataclass
import re
from collections import deque

logger = logging.getLogger("ACO2022-17")


@dataclass()
class Monkey:
    name: str
    has_answer: bool
    answer: int
    formula: ()


class Aoc202212(AocBase):

    def calc_1(self, data) -> int:
        while not data['root'].has_answer:
            for key in data:
                m = data[key]
                if m.has_answer:
                    continue
                if data[m.formula[0]].has_answer and data[m.formula[2]].has_answer:
                    answer = 0
                    match m.formula[1]:
                        case '+':
                            answer = data[m.formula[0]].answer + data[m.formula[2]].answer
                        case '-':
                            answer = data[m.formula[0]].answer - data[m.formula[2]].answer
                        case '*':
                            answer = data[m.formula[0]].answer * data[m.formula[2]].answer
                        case '/':
                            answer = int(data[m.formula[0]].answer / data[m.formula[2]].answer)
                    m.has_answer = True
                    m.answer = answer

        return data['root'].answer

    def calc_2(self, data: []) -> int:
        change = True
        while change:
            change = False
            for key in data:
                m = data[key]
                if m.has_answer:
                    continue
                if key == 'humn':
                    continue
                if data[m.formula[0]].has_answer and data[m.formula[2]].has_answer:
                    answer = 0
                    match m.formula[1]:
                        case '+':
                            answer = data[m.formula[0]].answer + data[m.formula[2]].answer
                        case '-':
                            answer = data[m.formula[0]].answer - data[m.formula[2]].answer
                        case '*':
                            answer = data[m.formula[0]].answer * data[m.formula[2]].answer
                        case '/':
                            answer = int(data[m.formula[0]].answer / data[m.formula[2]].answer)
                    m.has_answer = True
                    m.answer = answer
                    change = True

        if data[data['root'].formula[0]].has_answer:
            data['root'].has_answer = True
            data['root'].answer = data[data['root'].formula[0]].answer
            data[data['root'].formula[2]].answer = data['root'].answer
            name = data['root'].formula[2]
        elif data[data['root'].formula[2]].has_answer:
            data['root'].has_answer = True
            data['root'].answer = data[data['root'].formula[2]].answer
            data[data['root'].formula[0]].answer = data['root'].answer
            name = data['root'].formula[0]

        while name != 'humn':
            monkey = data[name]
            left = data[monkey.formula[0]]
            right = data[monkey.formula[2]]
            target = right
            if not left.has_answer:
                target = left

            name = target.name
            answer = monkey.answer
            match monkey.formula[1]:
                case '+':
                    if left.has_answer:
                        answer = answer - left.answer
                    else:
                        answer = answer - right.answer
                case '-':
                    if left.has_answer:
                        answer = left.answer - answer
                    else:
                        answer = answer + right.answer
                case '*':
                    if left.has_answer:
                        answer = int(answer / left.answer)
                    else:
                        answer = int(answer / right.answer)
                case '/':
                    if left.has_answer:
                        answer = int(left.answer / answer)
                    else:
                        answer = int(answer * right.answer)

            target.has_answer = True
            target.answer = answer



        return data['humn'].answer


    def load_handler_part1(self, data: [(int, int)]) -> {}:

        result = {}
        for row in data:
            r = row.split(':')
            name = r[0]
            part2 = r[1].strip()
            formula = None
            answer = 0
            has_answer = False
            if part2.isnumeric():
                has_answer = True
                answer = int(part2)
            else:
                formula = part2.split(' ')
            m = Monkey(name, has_answer, answer, formula)
            result[name] = m
        return result

    def load_handler_part2(self, data: [str]) -> [str]:
        m = self.load_handler_part1(data)
        m["root"].formula[1] = '='
        m["humn"].has_answer = False
        return m

if __name__ == '__main__':
    configure()
    aoc = Aoc202212()
    failed, results = aoc.run("part1_[1-9]+.txt", "part2_[1-9]+.txt")
    if failed:
        exit(1)
