"""
AOC Day X
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
from collections import defaultdict
import math

import re


class Aoc201600(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict) -> int:

        regex = r"(\w+) can fly (\d+) km\/s for (\d+) seconds, but then must rest for (\d+) seconds."

        period = int(data[0])

        times = []
        for d in data[1:]:
            match = re.match(regex, d)
            name = match.group(1)
            speed = int(match.group(2))
            time = int(match.group(3))
            rest = int(match.group(4))

            # print(name, speed, time, rest)
            repeats = int(period /(time + rest))
            total_distance = repeats * speed * time
            remaining_time = period - repeats * (time+rest)
            if remaining_time > time:
                remaining_time = time
            total_distance += int(remaining_time * speed)
            # print(total_distance)
            times.append(total_distance)

        return max(times)

    def calc_2(self, data: [str]) -> int:
        regex = r"(\w+) can fly (\d+) km\/s for (\d+) seconds, but then must rest for (\d+) seconds."

        period = int(data[0])

        times = []
        reindeers = []
        for d in data[1:]:
            match = re.match(regex, d)
            name = match.group(1)
            speed = int(match.group(2))
            time = int(match.group(3))
            rest = int(match.group(4))
            reindeers.append((name, speed, time, rest))

        scores = defaultdict(int)
        positions = defaultdict(int)
        for i in range(0, period + 1):
            max_position = 0
            for reindeer in reindeers:
                name, speed, time, rest = reindeer
                pos = i % (time + rest)
                if pos < time:
                    positions[name] += speed
                max_position = max(max_position, positions[name])

            for name in positions:
                if max_position == positions[name]:
                    scores[name] += 1

        max_score = 0
        for reindeer in scores:
            max_score = max(max_score, scores[reindeer])

        return max_score

    def load_handler_part1(self, data: [str]) -> [str]:
        return data

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201600()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
