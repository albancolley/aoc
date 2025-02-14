"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure


class Aoc201600(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: str) -> int:
        result = 0
        ip_ranges = []
        for d in data:
            ip_range = d.split('-')
            ip_ranges.append((int(ip_range[0]),int(ip_range[1]) ))

        ip_ranges = sorted(ip_ranges)
        if ip_ranges[0][0] != 0:
            return 0
        last = ip_ranges[0][1]
        for ips_range in ip_ranges[1:]:
            if last + 1 < ips_range[0]:
                return last+1
            last = ips_range[1]

        return 0

    def calc_2(self, data: [str]) -> int:
        ip_ranges = []
        for d in data:
            ip_range = d.split('-')
            ip_ranges.append((int(ip_range[0]),int(ip_range[1]) ))

        allow_ip_count = 0

        ip_ranges = sorted(ip_ranges)
        if ip_ranges[0][0] != 0:
            allow_ip_count += ip_ranges[0][0]
        last = ip_ranges[0][1]

        pos = 1
        while True:
            while last >= ip_ranges[pos][1]:
                pos += 1
                if pos == len(ip_ranges):
                    # print(last)
                    allow_ip_count += 4294967295 - last
                    return allow_ip_count
            if last + 1 < ip_ranges[pos][0]:
                # print(ip_ranges[pos], last, ip_ranges[pos][0] - last - 1)
                allow_ip_count += ip_ranges[pos][0] - last - 1
            last = ip_ranges[pos][1]


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
