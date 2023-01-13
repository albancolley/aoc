import dataclasses

from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
from dataclasses import dataclass, field
from collections import defaultdict
import math
from collections import deque
import copy

logger = logging.getLogger("ACO2019-16")



class Aoc201916(AocBase):

    def calc_1(self, data) -> int:
        cycle = [0, 1, 0, -1]

        values = data
        for r in range(0, 100):
            result = []
            index = 0
            for i in range(0, len(values)):
                next_value = 0
                step = 0
                for j, value in enumerate(values):
                    if step == i:
                        index = (index + 1) % 4
                        step = 0
                    else:
                        step += 1
                    next_value += value * cycle[index]

                result.append(int(str(next_value)[-1]))
                index = 0
            values = result
        return ''.join([str(x) for x in result])[0:8]

    def calc_2(self, data) -> int:
        values = data
        target = int(''.join(map(str, values[0:7])))
        message_sum = sum(values)
        message_len = len(values)
        messages_to_sum = 10000 - int(target / message_len) - 1
        position_in_messages = (target % message_len)
        message = values[position_in_messages:] + values * messages_to_sum
        for i in range(0, 100):
            new_message = []
            total = sum(message)
            for j in range(0, len(message)):
                new_message.append(total % 10)
                total -= message[j]
            message = new_message
        return ''.join([str(x) for x in message[0:8]])

    def load_handler_part1(self, data: [str]) -> [str]:
        return [int(c) for c in data[0]]




    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201916()
    failed, results = aoc.run("part1x_[0-9]*.txt", "part2_[1-4]+.txt")
    if failed:
        exit(1)
