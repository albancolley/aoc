"""
AOC Day X
"""
import copy
import re
import sys

from networkx.algorithms.centrality import group_out_degree_centrality

from common import AocBase
from common import configure

from dataclasses import dataclass

@dataclass
class Unit:
    size: int
    hit_points: int
    attack_damage: int
    attack_type: str
    initiative: int
    weakness: list[str]
    immunities: list[str]
    unit_type: str
    group: int


class Aoc201900(AocBase):
    """
    AOC Day 10 Class
    """

    def print_units(self, units: list[Unit]):
        for unit in units:
            print(unit, unit.size*unit.attack_damage)

    def calc_1(self, units: list[Unit]) -> int:
        # self.print_units(units)
        self.fight(units)

        # self.print_units(units)

        result = 0
        for unit in units:
            result += unit.size
        return result

    def fight(self, units):
        while True:
            units.sort(key=lambda unit: (unit.size * unit.attack_damage, unit.initiative), reverse=True)
            attacks = []
            seen = []
            for unit in units:
                possibles = []
                for unit_target in units:
                    if unit.unit_type == unit_target.unit_type or unit_target in seen:
                        continue
                    multiplier = 1
                    if unit.attack_type in unit_target.weakness:
                        multiplier = 2
                    if unit.attack_type in unit_target.immunities:
                        multiplier = 0
                    damage = multiplier * unit.size * unit.attack_damage
                    possibles += [(damage, unit, unit_target)]
                if len(possibles) > 0:
                    possibles.sort(key=lambda possible: (possible[0], possible[2].size * possible[2].attack_damage,
                                                         possible[2].initiative), reverse=True)
                    # print(possibles)
                    damage, unit, unit_target = possibles[0]

                    if damage > 0:
                        seen += [unit_target]
                        attacks += [(possibles[0][0], unit, unit_target)]

            attacks.sort(key=lambda unit: unit[1].initiative, reverse=True)
            total_kills = 0
            for attack in attacks:
                damage, unit, unit_target = attack
                if unit.size == 0:
                    continue
                multiplier = 1
                if unit.attack_type in unit_target.weakness:
                    multiplier = 2
                if unit.attack_type in unit_target.immunities:
                    multiplier = 0
                damage = multiplier * unit.size * unit.attack_damage

                kills = min(int(damage / unit_target.hit_points), unit_target.size)
                total_kills += kills
                # print(f'{unit.unit_type} group {unit.group} attacks defending group {unit_target.group} , killing {kills} units')
                unit_target.size -= kills
                if unit_target.size == 0:
                    units.remove(unit_target)

            if total_kills == 0:
                return False

            unit_types: set = set()
            for unit in units:
                if unit.size > 0:
                    unit_types.add(unit.unit_type)

            if len(unit_types) == 1:
                break

        return True

            # print()
            # self.print_units(units)
            # print()

    def calc_2(self, orig_units: list[Unit]) -> int:
        increment = 50
        boost = 0
        while True:
            boost += increment
            units = copy.deepcopy(orig_units)
            for unit in units:
                if unit.unit_type == "Immune System":
                    unit.attack_damage += boost
            if not self.fight(units):
                continue
            if units[0].unit_type == "Immune System":
                if increment == 1:
                    break
                boost = boost - increment
                increment = 1



        #1657
        # self.print_units(units)
        result = 0
        for unit in units:
            result += unit.size
        return result

    def load_handler_part1(self, data: [str]) -> list[Unit]:
        regex = r"(\d+) units each with (\d+) hit points(.*)with an attack that does (\d+) (\w+) damage at initiative (\d+)"\

        mode = ""
        units: list[Unit] = []
        group = 1
        for line in data:
            if len(line.strip()) == 0:
                continue
            if line == "Immune System:":
                mode = "Immune System"
                group = 1
                continue
            if line == "Infection:":
                mode = "Infection"
                group = 1
                continue
            match = re.match(regex, line)
            size = int(match.group(1))
            hit_points = int(match.group(2))
            weaknesses_immunities = match.group(3).strip()
            attack_damage = int(match.group(4))
            attack_type = match.group(5)
            initiative = int(match.group(6))
            weakness =[]
            immunities=[]
            if weaknesses_immunities:
                weaknesses_immunities = weaknesses_immunities.replace('(', '').replace(')','')
                for weaknesses_immunity in weaknesses_immunities.split("; "):
                    if weaknesses_immunity.startswith("weak to "):
                        weakness = weaknesses_immunity[8:].split(', ')
                    else:
                        immunities = weaknesses_immunity[10:].split(', ')


            unit = Unit(
                size=size, hit_points= hit_points,
                attack_damage= attack_damage, attack_type= attack_type,
                initiative= initiative, weakness=weakness, immunities=immunities, unit_type=mode, group=group)
            units.append(unit)
            group += 1

        return units

    def load_handler_part2(self, data: [str]) -> list[Unit]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201900()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[1-9]+.txt")
    if failed:
        sys.exit(1)
