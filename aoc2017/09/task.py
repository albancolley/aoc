"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure


class Aoc201709(AocBase):
    """
    AOC Day 10 Class
    """

    garbage = 0

    def dfs(self, group: str, level: int = 1):
        score = 0

        # print(group)
        pos = 0
        while pos < len(group):
            match group[pos]:
                case '!':
                    pos += 1
                case '<':
                    pos += 1
                    while group[pos] != '>':
                        if group[pos] == '!':
                            pos += 1
                        else:
                            self.garbage += 1
                        pos += 1

                case '{':
                    score += level
                    score2, pos2 = self.dfs(group[pos+1:], level+1)
                    pos += pos2
                    score += score2
                case '}':
                    return score, pos+1
            pos += 1

        return score, 0

    def calc_1(self, data: str) -> int:

        score, _ = self.dfs(data[0])
        return score

    def calc_2(self, data: [str]) -> int:
        self.garbage = 0
        score, _ = self.dfs(data[0])
        return self.garbage

    def load_handler_part1(self, data: [str]) -> [str]:
       return data

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201709()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
