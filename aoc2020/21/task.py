"""
AOC Day 10
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math

class Aoc2023010(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, ingredients_list: [(set, set)]) -> int:
        result = 0
        possible_allegens = {}
        for ingredients in ingredients_list:
            for allergen in ingredients[1]:
                if allergen not in possible_allegens:
                    possible_allegens[allergen] = ingredients[0]
                else:
                    possible_allegens[allergen] = possible_allegens[allergen].intersection(ingredients[0])

                if len(possible_allegens[allergen]) == 1:
                    for possible_allegen in possible_allegens:
                        if possible_allegen != allergen:
                            possible_allegens[possible_allegen] = possible_allegens[possible_allegen].difference(possible_allegens[allergen])

        possible_allegens_values = set()
        for i in possible_allegens.values():
            for j in i:
                possible_allegens_values.add(j)

        all_ingredients = []
        for ingredients in ingredients_list:
            for ingredient in ingredients[0]:
                if ingredient not in  possible_allegens_values:
                    all_ingredients.append(ingredient)

        return len(all_ingredients)

    def calc_2(self, ingredients_list: [(set, set)]) -> int:
        possible_allegens = {}
        for ingredients in ingredients_list:
            for allergen in ingredients[1]:
                if allergen not in possible_allegens:
                    possible_allegens[allergen] = ingredients[0]
                else:
                    possible_allegens[allergen] = possible_allegens[allergen].intersection(ingredients[0])

                if len(possible_allegens[allergen]) == 1:
                    for possible_allegen in possible_allegens:
                        if possible_allegen != allergen:
                            possible_allegens[possible_allegen] = possible_allegens[possible_allegen].difference(possible_allegens[allergen])

        print(possible_allegens)

        known = set()
        while len(known) != len(possible_allegens):
            know = set()
            for allegens in possible_allegens:
                if len(possible_allegens[allegens]) == 1:
                    for i in possible_allegens[allegens]:
                        known.add(i)

            for allegens in possible_allegens:
                if len(possible_allegens[allegens]) > 1:
                    possible_allegens[allegens] = possible_allegens[allegens].difference(known)

        possible_allegens_values = []
        for possible_allegen in possible_allegens:
            possible_allegens_values.append((possible_allegen, list(possible_allegens[possible_allegen])[0] ))

        possible_allegens_values = sorted(possible_allegens_values)
        print(possible_allegens_values)

        result = ",".join([x[1] for x in possible_allegens_values])
        print(result)
        return result

    def load_handler_part1(self, data: [str]) -> [str]:
        l : str
        ingredients_list:  [(set, set)] = []
        for l in data:
            temp = l.replace(")","").split(' (contains ')
            ingredients = set(temp[0].split(" "))
            allergens = set(temp[1].split(", "))
            ingredients_list.append((ingredients.copy(), allergens))
        return ingredients_list

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc2023010()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
