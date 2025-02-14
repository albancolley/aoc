"""
AOC Day 7
"""
import sys
from common import AocBase
from common import configure
import collections

class Aoc202307(AocBase):
    """
    AOC Day 7 Class
    """

    order = {
                'A' : '14', 'K': '13', 'Q':'12', 'J':'11', 'T':'10', '9':'09', '8': '08', '7':'07', '6':'06', '5':'05', '4':'04', '3':'03', '2':'02'
    }

    def calc_1(self, data: dict) -> int:
        result =[]
        for round in data:
            hand:str = round[0]
            bid:int = round[1]
            counts = collections.Counter(hand)
            value = 0
            pairs = 0
            for c in counts:
                if counts[c] == 2:
                    pairs += 1
                value = max(counts[c], value)
            if value == 1:
                value = 0
            if value > 3:
                value += 1
            if value == 3:
                for c in counts:
                    if counts[c] == 2:
                        value = 4
                        break
            if value == 2:
                value = pairs
            fixed_hand = hand.replace('A','F').replace('K', 'E').replace('Q','D').replace('J', 'C').replace('T', 'B')
            result.append((value,fixed_hand, bid,hand))
        result.sort()
        total = 0
        count = 1
        for i in result:
            total += count * i[2]
            count += 1
        return total


    def calc_2(self, data: [str]) -> int:
        result =[]
        for round in data:
            hand:str = round[0]
            bid:int = round[1]
            counts = collections.Counter(hand)
            value = 0
            pairs = 0
            for c in counts:
                if c == 'J':
                    continue
                if counts[c] == 2:
                    pairs += 1
                value = max(counts[c], value)
            if value == 1:
                value = 0
            if value > 3:
                value += 1
            if value == 3 and pairs == 1:
                value = 4
            if value == 2:
                value = pairs
            if 'J' in counts:
                jokers = counts['J']
                if jokers == 5:
                    value = 6
                elif value == 0: # high card
                    value += jokers
                    if jokers > 1:
                        value += 1
                    if jokers >= 3:
                        value += 1
                elif value == 1: # one pair
                    value += jokers + 1
                    if jokers > 1:
                        value += 1
                elif value == 2: # two pairs
                    value = 4
                elif value == 3: #3 of a kind
                    value += jokers + 1
                elif value == 4: # full house - shoudn't happen
                    print(value, hand)
                elif value == 5: # four fo a kind
                    value += jokers
                elif value == 6: # 5 of a kind
                    print(value, hand)

            fixed_hand = hand.replace('A','F').replace('K', 'E').replace('Q','D').replace('J', '0').replace('T', 'B')
            result.append((value,fixed_hand, bid,hand))
        result.sort()
        total = 0
        count = 1
        for i in result:
            total += count * i[2]
            count += 1
        return total

    def load_handler_part1(self, data: [str]) -> [str]:
        result = []
        for r in data:
            d = r.split(' ')
            result.append((d[0], int(d[1])))
        return result

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc202307()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
