"""
AOC Day X
"""
import re
import sys
from collections import defaultdict

from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math

class Aoc201904(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict) -> int:
        guard_sleep_totals = {}
        for d in data:
            if len(d[1]) <= 1:
                continue
            guard:int = d[0]
            if guard not in guard_sleep_totals:
                guard_sleep_totals[guard] = defaultdict(int)
            records = d[1]
            last:int = records[1][1]
            if records[1][0] != 0:
                last = 0
            pos:int = 2
            while pos < len(records):
                awake = records[pos][2]
                minutes = records[pos][1]
                if not awake:
                    for i in range(last, minutes):
                        guard_sleep_totals[guard][i] += 1
                last = minutes
                pos += 1

        guard_total = defaultdict(int)
        for gs in guard_sleep_totals:
            guard_total[gs] += sum(guard_sleep_totals[gs].values())

        guard_total_max = max(guard_total.values())
        guard = list(guard_total.keys())[list(guard_total.values()).index(guard_total_max)]

        minute_total_max = max(guard_sleep_totals[guard].values())
        minute_total_max_time = list(guard_sleep_totals[guard].keys())[list(guard_sleep_totals[guard].values()).index(minute_total_max)]


        return guard * minute_total_max_time

    def calc_2(self, data: [str]) -> int:
        guard_sleep_totals = {}
        for d in data:
            if len(d[1]) <= 1:
                continue
            guard:int = d[0]
            if guard not in guard_sleep_totals:
                guard_sleep_totals[guard] = defaultdict(int)
            records = d[1]
            last:int = records[1][1]
            if records[1][0] != 0:
                last = 0
            pos:int = 2
            while pos < len(records):
                awake = records[pos][2]
                minutes = records[pos][1]
                if not awake:
                    for i in range(last, minutes):
                        guard_sleep_totals[guard][i] += 1
                last = minutes
                pos += 1

        guard_maxes = {}
        for guard in guard_sleep_totals:
            minute_total_max = max(guard_sleep_totals[guard].values())
            guard_maxes[guard]= minute_total_max


        guard_total_max = max(guard_maxes.values())
        guard = list(guard_maxes.keys())[list(guard_maxes.values()).index(guard_total_max)]

        guard_time = list(guard_sleep_totals[guard].keys())[list(guard_sleep_totals[guard].values()).index(guard_total_max)]


        return guard * guard_time

    def load_handler_part1(self, data: [str]) -> [str]:
        data.sort()
        regex = r"\[.* (\d+):(\d+)\] (.*)"

        records = []
        night = []
        guard_id = -1
        asleep = False
        for d in data:
            match = re.match(regex, d)
            hour = int(match.group(1))
            minute = int(match.group(2))
            rest:str = match.group(3)
            if rest.startswith("Guard"):
                if guard_id != -1:
                    records.append((guard_id, night))
                    night=[]
                guard_id = int(rest.split(' ')[1][1:])
            elif rest.startswith('falls'):
                asleep = True
            elif rest.startswith('wakes'):
                asleep = False

            night.append((hour, minute, asleep))

        records.append((guard_id, night))
        return records

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201904()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
