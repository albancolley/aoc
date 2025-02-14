"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure
from dataclasses import dataclass
import re

@dataclass
class Bot:
    name: int
    values: []
    low: int
    high: int
    output_low: bool
    output_high: bool

class Aoc201600(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, bots: dict[Bot]) -> int:
        result = -1
        bot : Bot
        while True:
            for bot_name in bots:
                bot = bots[bot_name]
                if len(bot.values) == 2:
                    low = min(bot.values[0], bot.values[1])
                    high = max(bot.values[0], bot.values[1])
                    if low == 2 and high == 5:
                        # print(bot_name)
                        return bot_name
                    if low == 17 and high == 61:
                        # print(bot_name)
                        return bot_name
                    if not bot.output_low:
                        bots[bot.low].values.append(low)
                    if not bot.output_high:
                        bots[bot.high].values.append(high)
                    bot.values = []
        return result

    def calc_2(self, bots: [str]) -> int:
        outputs = {}
        result = -1
        bot: Bot
        while True:
            for bot_name in bots:
                bot = bots[bot_name]
                if len(bot.values) == 2:
                    low = min(bot.values[0], bot.values[1])
                    high = max(bot.values[0], bot.values[1])
                    if not bot.output_low:
                        bots[bot.low].values.append(low)
                    else:
                        outputs[bot.low] = low
                    if not bot.output_high:
                        bots[bot.high].values.append(high)
                    else:
                        outputs[bot.high] = high
                    bot.values = []
                    continue
                if 1 in outputs and 2 in outputs and 3 in outputs:
                    return outputs[0] * outputs[1] * outputs[2]


    def load_handler_part1(self, data: [str]) -> {}:
        bots = {}
        p_value = re.compile(r'value (\d+) goes to bot (\d+)')
        p_moves = re.compile(r'bot (\d+) gives low to bot (\d+) and high to bot (\d+)')
        p_moves_low_output = re.compile(r'bot (\d+) gives low to output (\d+) and high to bot (\d+)')
        p_moves_high_output = re.compile(r'bot (\d+) gives low to bot (\d+) and high to output (\d+)')
        p_moves_both_output = re.compile(r'bot (\d+) gives low to output (\d+) and high to output (\d+)')
        for line in data:
            m = re.match(p_value, line)
            if m:
                value = int(m.group(1))
                bot = int(m.group(2))
                if bot not in bots:
                    bots[bot] = Bot(bot, [value], 0, 0, False, False)
                else:
                    bots[bot].values.append(value)
            m = re.match(p_moves, line)
            if m:
                bot = int(m.group(1))
                low = int(m.group(2))
                high = int(m.group(3))
                if bot not in bots:
                    bots[bot] = Bot(bot, [], low, high, False, False)
                else:
                    bots[bot].low = low
                    bots[bot].high = high
            m = re.match(p_moves_low_output, line)
            if m:
                bot = int(m.group(1))
                low = int(m.group(2))
                high = int(m.group(3))
                if bot not in bots:
                    bots[bot] = Bot(bot, [], low, high, True, False)
                else:
                    bots[bot].low = low
                    bots[bot].high = high
                    bots[bot].output_low = True
            m = re.match(p_moves_high_output, line)
            if m:
                bot = int(m.group(1))
                low = int(m.group(2))
                high = int(m.group(3))
                if bot not in bots:
                    bots[bot] = Bot(bot, [], low, high, False, True)
                else:
                    bots[bot].low = low
                    bots[bot].high = high
                    bots[bot].output_high = True
            m = re.match(p_moves_both_output, line)
            if m:
                bot = int(m.group(1))
                low = int(m.group(2))
                high = int(m.group(3))
                if bot not in bots:
                    bots[bot] = Bot(bot, [], low, high, True, True)
                else:
                    bots[bot].low = low
                    bots[bot].high = high
                    bots[bot].output_high = True
                    bots[bot].output_low = True
        # print(bots)
        return bots

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201600()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
