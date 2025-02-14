"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure
from itertools import combinations


class Aoc201600(AocBase):
    """
    AOC Day 10 Class
    """


    weapons = {
        'Dagger': (8, 4, 0),
        'Shortsword': (10, 5, 0),
        'Warhammer': (25, 6, 0),
        'Longsword': (40, 7, 0),
        'Greataxe': (74, 8, 0)
    }

    armor = {
        'None': (0, 0, 0),
        'Leather': (13, 0, 1),
        'Chainmail': (31, 0, 2),
        'Splintmail': (53, 0, 3),
        'Bandedmail': (75, 0, 4),
        'Platemail': (102, 0, 5)
    }

    rings = {
        'Damage +1': (25, 1, 0),
        'Damage +2': (50, 2, 0),
        'Damage +3': (100, 3, 0),
        'Defense +1': (20, 0, 1),
        'Defense +2': (40, 0, 2),
        'Defense +3': (80, 0, 3)
    }

    def fight(self, boss, me) -> bool:
        boss_hit_points, boss_damage, boss_armor = boss
        me_hit_points, me_damage, me_armor = me

        while True:
            boss_hit_points -= max(1, me_damage - boss_armor)
            # print(f'The player deals {me_damage}-{boss_armor} = {max(1, me_damage - boss_armor)} damage; the boss goes down to {boss_hit_points} hit points.')
            if boss_hit_points <= 0:
                return True

            me_hit_points -= max(1, boss_damage - me_armor)
            # print(f'The boss deals {boss_damage}-{me_armor} = {max(1, boss_damage - me_armor)} damage; the player goes down to {me_hit_points} hit points.')
            if me_hit_points <= 0:
                return False


    def calc_1(self, data: [str]) -> int:
        boss_hit_points = int(data[0].split(": ")[1])
        boss_damage = int(data[1].split(": ")[1])
        boss_armor = int(data[2].split(": ")[1])

        ring_combos = list()
        ring_combos.append((0,0,0))
        for ring_combo in self.rings.values():
            ring_combos.append(ring_combo)

        double_combs = combinations(self.rings.values(), 2)
        for ring_combo in double_combs:
            ring_combos.append((ring_combo[0][0] + ring_combo[1][0], ring_combo[0][1] + ring_combo[1][1], ring_combo[0][2] + ring_combo[1][2]))

        min_cost = 1000000
        for weapon in self.weapons.values():
            for armor in self.armor.values():
                for ring_combo in ring_combos:
                    me_hit_points = 100
                    cost = weapon[0] + armor[0] + ring_combo[0]
                    damage = weapon[1] + armor[1] + ring_combo[1]
                    armor_cost = weapon[2] + armor[2] + ring_combo[2]

                    if cost < min_cost:
                        if self.fight((boss_hit_points, boss_damage, boss_armor), (me_hit_points, damage, armor_cost)):
                            min_cost = cost

        return min_cost


    def calc_2(self, data: [str]) -> int:
        boss_hit_points = int(data[0].split(": ")[1])
        boss_damage = int(data[1].split(": ")[1])
        boss_armor = int(data[2].split(": ")[1])

        ring_combos = list()
        ring_combos.append((0, 0, 0))
        for ring_combo in self.rings.values():
            ring_combos.append(ring_combo)

        double_combs = combinations(self.rings.values(), 2)
        for ring_combo in double_combs:
            ring_combos.append((ring_combo[0][0] + ring_combo[1][0], ring_combo[0][1] + ring_combo[1][1],
                                ring_combo[0][2] + ring_combo[1][2]))

        max_cost = 0
        for weapon in self.weapons.values():
            for armor in self.armor.values():
                for ring_combo in ring_combos:
                    me_hit_points = 100
                    cost = weapon[0] + armor[0] + ring_combo[0]
                    damage = weapon[1] + armor[1] + ring_combo[1]
                    armor_cost = weapon[2] + armor[2] + ring_combo[2]

                    if max_cost < cost:
                        if not self.fight((boss_hit_points, boss_damage, boss_armor), (me_hit_points, damage, armor_cost)):
                            max_cost = cost

        return max_cost

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
