"""
AOC Day X
"""
import dataclasses
import sys
from queue import PriorityQueue

from common import AocBase
from common import configure
from dataclasses import dataclass
from itertools import count



@dataclass
class Spell():
    name: str
    mana_cost: int
    mana_increase: int
    health: int
    armor: int
    damage: int
    duration: int

@dataclass
class Battle:
    my_mana: int
    my_hit_points: int
    active_spells: [Spell]
    boss_hit_points: int
    boss_damage: int
    my_turn: bool
    mana_cost: int = 0
class Aoc201600(AocBase):
    """
    AOC Day 10 Class
    """

    #name, mana, health, armor, damage, duration
    spells = [
        Spell('magic_missile', 53, 0, 0, 0, 4, 0),
        Spell('drain', 73, 0, 2, 0, 2, 1),
        Spell('shield', 113, 0, 0, 7, 0, 6),
        Spell('poison', 173, 0, 0, 0, 3, 6),
        Spell('recharge', 229, 101, 0, 0, 0, 5)
    ]

    unique = count()

    def clone_battle(self, battle: Battle)-> Battle:
        active_spells = []
        active_spell : Spell
        for active_spell in battle.active_spells:
            active_spells.append(
                Spell(
                    active_spell.name,
                    active_spell.mana_cost,
                    active_spell.mana_increase,
                    active_spell.health,
                    active_spell.armor,
                    active_spell.damage,
                    active_spell.duration
                )
            )
        return Battle(
            battle.my_mana,
            battle.my_hit_points,
            active_spells,
            battle.boss_hit_points,
            battle.boss_damage,
            battle.my_turn,
            battle.mana_cost,
        )

    def calc_1(self, data: dict) -> int:
        min_mana_cost = 10000000
        my_mana = 500
        my_hit_points = 50
        boss_hit_points = int(data[0].split(": ")[1])
        boss_damage = int(data[1].split(": ")[1])
        q = PriorityQueue()
        battle = Battle(my_mana, my_hit_points, [], boss_hit_points, boss_damage, True)
        q.put((boss_hit_points, my_mana, next(self.unique), battle))
        while not q.empty():
            _, _, _, battle = q.get()
            if battle.mana_cost > min_mana_cost:
                continue
            spells_in_use = {s.name for s in battle.active_spells if s.duration > 1}
            for spell in self.spells:
                if spell.name not in spells_in_use and spell.mana_cost < battle.my_mana:
                    new_battle: battle = self.clone_battle(battle)
                    # print(new_battle)
                    self.round(new_battle, spell)

                    if new_battle.boss_hit_points <= 0:
                        # if min_mana_cost > new_battle.mana_cost:
                        #     print(new_battle.mana_cost, min_mana_cost)
                        min_mana_cost = min(min_mana_cost, new_battle.mana_cost)
                        continue

                    if new_battle.my_hit_points <= 0:
                        continue


                    q.put((
                        new_battle.boss_hit_points,
                        new_battle.my_mana,
                        next(self.unique),
                        new_battle
                    ))

        return min_mana_cost

    def cast(self, battle: Battle, spell: Spell):
        battle.mana_cost += spell.mana_cost
        battle.my_mana -= spell.mana_cost
        battle.active_spells += [dataclasses.replace(spell)]

    def round(self, battle: Battle, spell):

        if spell.name == 'magic_missile':
            self.cast(battle, spell)

        health, armor, damage, mana = 0, 0, 0, 0
        active_spell: Spell
        new_active_spells = []
        for active_spell in battle.active_spells:
            health += active_spell.health
            armor += active_spell.armor
            damage += active_spell.damage
            mana += active_spell.mana_increase
            active_spell.duration -= 1
            if active_spell.duration > 0:
                new_active_spells += [active_spell]

        battle.my_mana += mana
        battle.my_hit_points += health
        battle.active_spells = new_active_spells
        battle.boss_hit_points -= damage

        if spell.name != 'magic_missile':
            self.cast(battle, spell)

        # print("my turn  ", battle)

        health, armor, damage, mana = 0, 0, 0, 0
        active_spell: Spell
        new_active_spells = []
        for active_spell in battle.active_spells:
            health += active_spell.health
            armor += active_spell.armor
            damage += active_spell.damage
            mana += active_spell.mana_increase
            active_spell.duration -= 1
            if active_spell.duration > 0:
                new_active_spells += [active_spell]

        battle.my_mana += mana
        battle.my_hit_points += health
        battle.active_spells = new_active_spells
        battle.boss_hit_points -= damage

        if armor > 0:
            battle.my_hit_points -= max(1, battle.boss_damage - armor)
        else:
            battle.my_hit_points -= battle.boss_damage

        # print("boss turn", battle)

        return battle

    def calc_2(self, data: [str]) -> int:
        min_mana_cost = 10000000
        my_mana = 500
        my_hit_points = 50
        boss_hit_points = int(data[0].split(": ")[1])
        boss_damage = int(data[1].split(": ")[1])
        q = PriorityQueue()
        q.put((boss_hit_points, my_mana, next(self.unique), Battle(my_mana, my_hit_points, [], boss_hit_points, boss_damage, True)))
        while not q.empty():
            _, _, _, battle = q.get()
            if battle.mana_cost > min_mana_cost:
                continue

            spells_in_use = {s.name for s in battle.active_spells if s.duration > 1}
            for spell in self.spells:
                if spell.name not in spells_in_use and spell.mana_cost < battle.my_mana:
                    new_battle: battle = self.clone_battle(battle)

                    # print(new_battle)

                    self.round2(new_battle, spell)

                    if new_battle.boss_hit_points <= 0:
                        # if min_mana_cost > new_battle.mana_cost:
                        #     print(new_battle.mana_cost, min_mana_cost)
                        min_mana_cost = min(min_mana_cost, new_battle.mana_cost)
                        continue

                    if new_battle.my_hit_points <= 0:
                        continue

                    q.put((
                        new_battle.boss_hit_points,
                        new_battle.my_mana,
                        next(self.unique),
                        new_battle
                    ))

        return min_mana_cost

    def round2(self, battle: Battle, spell):

        battle.my_hit_points = battle.my_hit_points - 1
        if battle.my_hit_points <= 0:
            return battle

        if spell.name == 'magic_missile':
            self.cast(battle, spell)

        health, armor, damage, mana = 0, 0, 0, 0
        active_spell: Spell
        new_active_spells = []
        for active_spell in battle.active_spells:
            health += active_spell.health
            armor += active_spell.armor
            damage += active_spell.damage
            mana += active_spell.mana_increase
            active_spell.duration -= 1
            if active_spell.duration > 0:
                new_active_spells += [active_spell]

        battle.my_mana += mana
        battle.my_hit_points += health
        battle.active_spells = new_active_spells
        battle.boss_hit_points -= damage

        if spell.name != 'magic_missile':
            self.cast(battle, spell)

        # print("my turn  ", battle)

        health, armor, damage, mana = 0, 0, 0, 0
        active_spell: Spell
        new_active_spells = []
        for active_spell in battle.active_spells:
            health += active_spell.health
            armor += active_spell.armor
            damage += active_spell.damage
            mana += active_spell.mana_increase
            active_spell.duration -= 1
            if active_spell.duration > 0:
                new_active_spells += [active_spell]

        battle.my_mana += mana
        battle.my_hit_points += health
        battle.active_spells = new_active_spells
        battle.boss_hit_points -= damage

        if armor > 0:
            battle.my_hit_points -= max(1, battle.boss_damage - armor)
        else:
            battle.my_hit_points -= battle.boss_damage

        # print("boss turn", battle)

        return battle

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
