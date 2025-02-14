"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure
import re
from dataclasses import dataclass

@dataclass
class Disk:
    disk: int
    positions: int
    time: int
    position: int

    def open(self) -> bool:
        return (self.position + self.disk) % self.positions == 0

    def __str__(self):
        return f'Disk(disk={self.disk}, positions={self.positions}, time={self.time}, position={self.position}, open={self.open()})'

    def __repr__(self):
        return f'Disk(disk={self.disk}, positions={self.positions}, time={self.time}, position={self.position}, open={self.open()})'

class Aoc201600(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: [Disk]) -> int:
        result = 0
        while True:
            all_open : bool = True
            for disk in data:
                all_open = all_open and disk.open()
                disk.position = (disk.position + 1) % disk.positions
            if all_open:
                break
            result += 1
        return result

    def calc_2(self, data: [Disk]) -> int:
        result = 0
        disk = Disk(7, 11, 0, 0)
        data.append(disk)
        while True:
            all_open : bool = True
            for disk in data:
                all_open = all_open and disk.open()
                disk.position = (disk.position + 1) % disk.positions
            if all_open:
                break
            result += 1
        return result
    def load_handler_part1(self, data: [str]) -> [Disk]:
        disks: [Disk] = []
        for row in data:
            p = re.compile(r'Disc #(\d+) has (\d+) positions; at time=(\d+), it is at position (\d+).')
            for i in range(0, len(data), 3):
                m = re.match(p, row)
                disk: int = int(m.group(1))
                positions: int = int(m.group(2))
                time: int = int(m.group(3))
                position: int = int(m.group(4))
                disk : Disk = Disk(disk, positions, time, position)
                disks.append(disk)
        return disks
    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201600()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
