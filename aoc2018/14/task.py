"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure


class Aoc201900(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, recipies_target: int) -> str:
        recipies = [3,7]
        pos_1 = 0
        pos_2 = 1
        print(recipies)
        while True:
            next_value = recipies[pos_1] + recipies[pos_2]
            if next_value > 9:
                recipies += [next_value // 10, next_value % 10]
            else:
                recipies += [next_value]
            pos_1 =  (pos_1 + recipies[pos_1] + 1) % len(recipies)
            pos_2 =  (pos_2 + recipies[pos_2] + 1) % len(recipies)
            if len(recipies) >= recipies_target + 10:
                return  ''.join([str(r) for r in recipies[recipies_target:recipies_target+10]])

    def calc_2(self, recipies_target: str) -> int:
        recipies = [3, 7]
        pos_1 = 0
        pos_2 = 1
        # print(recipies)
        recipe_count = 0
        while True:
            recipe_count += 1
            next_value = recipies[pos_1] + recipies[pos_2]
            if next_value > 9:
                recipies += [next_value // 10, next_value % 10]
            else:
                recipies += [next_value]
            pos_1 = (pos_1 + recipies[pos_1] + 1) % len(recipies)
            pos_2 = (pos_2 + recipies[pos_2] + 1) % len(recipies)
            end = len(recipies) - len(recipies_target)
            end_1 = recipies[-len(recipies_target):]
            end_2 = recipies[-len(recipies_target) - 1: -1]
            # print(recipies, end_1, end_2)

            if end_1 == recipies_target:
                return len(recipies) - len(recipies_target)
            if  end_2 == recipies_target:
                return len(recipies) - len(recipies_target) - 1

    def load_handler_part1(self, data: [str]) -> int:
       return int(data[0])

    def load_handler_part2(self, data: [str]) -> str:
        return list([int(x) for x in data[0]])


if __name__ == '__main__':
    configure()
    aoc = Aoc201900()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
