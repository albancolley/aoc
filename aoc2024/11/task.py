"""
AOC Day X
"""
import sys
from collections import defaultdict

from common import AocBase
from common import configure


class Aoc202411(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1_working(self, data: dict) -> int:
        result = 0
        queue:[] = data
        for i in range(25):
            new_queue = []
            while len(queue) > 0:
                d = queue.pop(0)
                str_d = str(d)
                if d ==0:
                    new_queue += [1]
                elif len(str_d) % 2 == 0:
                    half = int(len(str_d) / 2)
                    new_queue += [int(str_d[0:half]), int(str_d[half:])]
                else:
                    new_queue += [d*2024]
            queue = new_queue
            # print(' '.join([str(x) for x in new_queue]))
        return len(queue)

    def calc_1(self, data: dict) -> int:
        result = 0
        queue:[int,int] = defaultdict(int)
        for d in data:
            queue[d] += 1

        for i in range(25):
            new_queue = defaultdict(int)
            for d in queue:
                count = queue[d]
                str_d = str(d)
                if d ==0:
                    new_queue[1] += count
                elif len(str_d) % 2 == 0:
                    half = int(len(str_d) / 2)
                    new_queue[int(str_d[0:half])] += count
                    new_queue[int(str_d[half:])] += count
                else:
                    new_queue[(d*2024)] += count

            queue = new_queue
            # print(queue)
            # print(i, len(queue))
        return sum(queue.values())

    def calc_2(self, data: [str]) -> int:
        queue: [int, int] = defaultdict(int)
        for d in data:
            queue[d] += 1

        for i in range(75):
            new_queue = defaultdict(int)
            for d in queue:
                count = queue[d]
                str_d = str(d)
                if d == 0:
                    new_queue[1] += count
                elif len(str_d) % 2 == 0:
                    half = int(len(str_d) / 2)
                    new_queue[int(str_d[0:half])] += count
                    new_queue[int(str_d[half:])] += count
                else:
                    new_queue[(d * 2024)] += count

            queue = new_queue
            # print(queue)
            # print(i, len(queue))
        return sum(queue.values())

        return len(queue)

    def load_handler_part1(self, data: [str]) -> [str]:
       return [int(d) for d in data[0].split(' ')]

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)

"""
253 0 2024 14168
253 0 2024 14168

512072 1 0 20 24 28676032
512072 1 20 24 28676032

512 72 2024 1 0 2 0 2 4 2867 6032
512 72 2024 2 0 2 4 2867 6032

1036288 7 2 20 24 2024 1 0 4048 1 0 4048 8096 28 67 60 32
1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32



2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2
2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2
"""

if __name__ == '__main__':
    configure()
    aoc = Aoc202411()
    failed, results = aoc.run("part1_[1-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
