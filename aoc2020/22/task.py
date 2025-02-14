"""
AOC Day 10
"""
import sys
from common import AocBase
from common import configure


class Aoc2023010(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: (list[int],list[int])) -> int:
        player_1: list[int]
        player_2: list[int]
        player_1, player_2 = data
        while not( len(player_2) == 0 or len(player_1) == 0):
            p1_card = player_1.pop(0)
            p2_card = player_2.pop(0)
            if p1_card > p2_card:
                player_1 += [p1_card, p2_card]
            else:
                player_2 += [p2_card, p1_card]

        winner = player_2
        if len(player_1) > 0:
            winner = player_1

        mult = 1
        result = 0
        for i in range(len(winner) - 1, -1, -1 ):
            result += mult * winner[i]
            mult += 1
        return result

    def calc_2(self, data: [str]) -> int:
        total = 0
        return total

    def load_handler_part1(self, data: [str]) -> [str]:
        position = 1
        player_1 = []
        while len(data[position]) > 0:
            player_1.append(int(data[position]))
            position += 1

        position += 2
        player_2 = []
        while position < len(data):
            player_2.append(int(data[position]))
            position += 1

        return player_1, player_2

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc2023010()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
