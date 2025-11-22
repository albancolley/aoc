"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure
from common.linked_list import DoublyLinkedCircularList


class Aoc201909(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict) -> int:
        result = 0
        dlist = DoublyLinkedCircularList()
        dlist.insert(0)

        max_value = 0

        players = 459
        last_marble = 72103

        scores = [0] * players


        while max_value <= last_marble:
            for i in range(0, players):
                dlist.next()
                max_value += 1
                if max_value % 23 == 0:
                    dlist.previous(8)
                    scores[i] += max_value + dlist.curr.data
                    dlist.remove_elem(dlist.curr)
                else:
                    dlist.insert(max_value)

                if max_value > last_marble:
                    break


                # print(dlist.to_list(dlist.find(0)))
                # print(dlist.to_list())

        return max(scores)

    def calc_2(self, data: [str]) -> int:
        result = 0
        dlist = DoublyLinkedCircularList()
        dlist.insert(0)

        max_value = 0

        players = 459
        last_marble = 72103 * 100

        scores = [0] * players

        while max_value <= last_marble:
            for i in range(0, players):
                dlist.next()
                max_value += 1
                if max_value % 23 == 0:
                    dlist.previous(8)
                    scores[i] += max_value + dlist.curr.data
                    dlist.remove_elem(dlist.curr)
                else:
                    dlist.insert(max_value)

                if max_value > last_marble:
                    break

                # print(dlist.to_list(dlist.find(0)))
                # print(dlist.to_list())

        return max(scores)

    def load_handler_part1(self, data: [str]) -> [str]:
       return data

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201909()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
