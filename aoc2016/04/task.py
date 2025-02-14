"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure
import collections
from operator import itemgetter

class Aoc201600(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict) -> int:
        result = 0
        line: str
        for line in data:
            parts = line.rsplit('-',1)
            encrypted_name = parts[0].replace('-', '')
            sector_id = int(parts[1].split('[')[0])
            checksum = parts[1].split('[')[1].replace(']','')
            common = collections.Counter(encrypted_name).most_common()
            common = sorted(common, key=itemgetter(0))
            common = sorted(common, key=itemgetter(1), reverse=True)
            common_five = [x[0] for x in common][0:5]
            encrypted_name_checksum = ''.join(common_five)
            if encrypted_name_checksum == checksum:
                result += sector_id
        return result

    def calc_2(self, data: [str]) -> int:
        result = 0
        line: str
        for line in data:
            parts = line.rsplit('-',1)
            encrypted_name = parts[0].replace('-', '')
            sector_id = int(parts[1].split('[')[0])
            name = "".join([chr(((ord(c) - ord('a') + sector_id ) % 26) + ord('a')) for c in encrypted_name])
            if name in ["northpoleobjectstorage", "veryencryptedname"]:
                result += sector_id
        return result


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
