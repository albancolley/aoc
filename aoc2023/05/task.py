from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import logging
import re
from collections import deque

logger = logging.getLogger("ACO2023-1")

class Aoc202301(AocBase):


    def calc_1(self, data: dict) -> int:
        total = 0
        next_target = 'seed'
        locations = []
        for seed in data['input']:
            location = -1
            value = seed
            next_target = 'seed'
            while next_target != 'location':
                if next_target in data:
                    info = data[next_target]
                    next_target = info['target']
                    for x in info['ranges']:
                        if x[0] <= value <= x[1]:
                            value = value + x[2] - x[0]
                            break
            locations.append(value)
        return min(locations)

    def calc_2(self, data: [str]) -> int:
        next_target = 'seed'
        locations = []
        seeds = data['input']
        seed_pairs = [(seeds[i], seeds[i] + seeds[i+1] - 1) for i in range(0, len(seeds), 2)]
        winning_cards = [0] * len(data)
        total = 0
        for pair in seed_pairs:
            next_target = 'seed'
            current_pairs = [pair]
            while next_target != 'location':
                info = data[next_target]
                next_target = info['target']
                next_pairs = []
                for x in info['ranges']:
                    range_start, range_end, new_start = x
                    diff = new_start - range_start
                    current_pairs2 = []
                    for c_pair in current_pairs:
                        start, end = c_pair
                        if range_start <= start and range_end >= end:
                            next_pairs.append((start+diff, end + diff))
                        elif range_start > end:
                            current_pairs2.append((start, end))
                        elif range_end < start:
                            current_pairs2.append((start, end))
                        elif range_start > start and range_end >= end:
                            current_pairs2.append((start, range_start - 1))
                            next_pairs.append((range_start+diff, end+diff))
                        elif range_start <= start and range_end < end:
                            current_pairs2.append((range_end+1, end))
                            next_pairs.append((start+diff, range_end+diff))
                        else:
                            current_pairs2.append((start, range_start-1))
                            current_pairs2.append((range_end+1, end))
                            next_pairs.append((range_start+diff, range_end + diff))
                    current_pairs = current_pairs2
                current_pairs = next_pairs + current_pairs2
            locations.append(min([x[0] for x in current_pairs]))
        return min(locations)

    def load_handler_part1(self, data: [str]) -> [str]:

        maps = {}
        seeds = data[0].split(':')[1].strip().split(' ')
        seeds = [int(s) for s in seeds]
        row : str
        source : str
        target :str
        for row in data[1:]:
            if row:
                if row.endswith(':'):
                    names = row.split("-")
                    source = names[0]
                    target = names[2].split(' ')[0]
                else:
                    r = row.split(" ")
                    destination_range_start = int(r[0])
                    source_range_start =  int(r[1])
                    range_length =  int(r[2]) -1
                    if source not in maps:
                        maps[source] = {
                            'source': source,
                            'target': target,
                            'ranges': [] }
                    maps[source]['ranges'].append((source_range_start, source_range_start + range_length, destination_range_start))
        maps['input'] = seeds
        return maps

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc202301()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        exit(1)
