import dataclasses
import os.path
import string

from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
from dataclasses import dataclass
import re
from collections import deque

logger = logging.getLogger("ACO2022-17")


@dataclass
class Blueprint:
    id: int
    ore_robot_cost: int
    clay_robot_cost: int
    obsidian_robot_cost: (int, int)
    geode_robot_cost: (int, int)
    ore: int = 0
    clay: int = 0
    obsidian: int = 0
    geode: int = 0
    ore_robots: int = 1
    clay_robots: int = 0
    obsidian_robots: int = 0
    geode_robots: int = 0

    def get_max_ore_robots(self):
        return max(self.ore_robot_cost, self.clay_robot_cost, self.obsidian_robot_cost[0],
                             self.geode_robot_cost[0])

    def get_max_clay_robots(self):
        return self.obsidian_robot_cost[1]

    def get_max_obsidian_robots(self):
        return self.geode_robot_cost[1]


    def __hash__(self):
        key = (self.ore, self.clay, self.obsidian, self.geode,
               self.ore_robots, self.clay_robots, self.obsidian_robots, self.geode_robots)
        return hash(key)

    def get_key(self):
        key = (self.ore_robots, self.clay_robots, self.obsidian_robots, self.geode_robots)
        return key

    def get_score(self):
        score = (self.ore, self.clay, self.obsidian, self.geode)
        return score


class Aoc202212(AocBase):

    def process_blueprint(self, blueprint: Blueprint, turn: int, total_turns: int) -> [Blueprint]:
        new_blueprints = set()

        blueprint_template = dataclasses.replace(blueprint)
        blueprint_template.ore += blueprint.ore_robots
        blueprint_template.clay += blueprint.clay_robots
        blueprint_template.obsidian += blueprint.obsidian_robots
        blueprint_template.geode += blueprint.geode_robots

        remaining_turns = total_turns - turn

        if blueprint.ore >= blueprint.geode_robot_cost[0] and blueprint.obsidian >= blueprint.geode_robot_cost[1]:
            geode_blueprint = dataclasses.replace(blueprint_template)
            geode_blueprint.ore -= blueprint.geode_robot_cost[0]
            geode_blueprint.obsidian -= blueprint.geode_robot_cost[1]
            geode_blueprint.geode_robots += 1
            new_blueprints.add(geode_blueprint)

        if blueprint.obsidian_robots < blueprint.get_max_obsidian_robots():
            if blueprint.ore >= blueprint.obsidian_robot_cost[0] and blueprint.clay >= blueprint.obsidian_robot_cost[1]:

                obsidian_blueprint = dataclasses.replace(blueprint_template)
                obsidian_blueprint.ore -= blueprint.obsidian_robot_cost[0]
                obsidian_blueprint.clay -= blueprint.obsidian_robot_cost[1]
                obsidian_blueprint.obsidian_robots += 1
                new_blueprints.add(obsidian_blueprint)

        if blueprint.ore_robots < blueprint.get_max_ore_robots():
            if blueprint.ore_robot_cost <= blueprint.ore:
                max_ore_usage = remaining_turns * (blueprint.get_max_ore_robots() - blueprint.ore_robots)
                if blueprint.ore < max_ore_usage:
                    ore_blueprint = dataclasses.replace(blueprint_template)
                    ore_blueprint.ore -= blueprint.ore_robot_cost
                    ore_blueprint.ore_robots += 1
                    new_blueprints.add(ore_blueprint)

        if blueprint.clay_robots < blueprint.get_max_clay_robots():
            if blueprint.clay_robot_cost <= blueprint.ore:
                max_clay_usage = remaining_turns * (blueprint.get_max_clay_robots() - blueprint.clay_robots)
                if blueprint.ore < max_clay_usage:
                    clay_blueprint = dataclasses.replace(blueprint_template)
                    clay_blueprint.ore -= blueprint.clay_robot_cost
                    clay_blueprint.clay_robots += 1
                    new_blueprints.add(clay_blueprint)

        no_change = dataclasses.replace(blueprint_template)
        new_blueprints.add(no_change)

        return new_blueprints

    def calc_1(self, data: [Blueprint]) -> int:

        total = 0
        for blueprint in data:
            blueprint.ore_robots = 1

            next_blueprints = set()
            next_blueprints.add(blueprint)
            turns = 24
            print(blueprint.id, 0, len(next_blueprints))
            for i in range(1, turns+1):
                new_blueprints = set()
                for next_blueprint in next_blueprints:
                    blueprints = self.process_blueprint(next_blueprint, i, turns)
                    new_blueprints = new_blueprints.union(blueprints)

                maxes = {}
                for new_blueprint in new_blueprints:
                    key = (new_blueprint.ore_robots, new_blueprint.clay_robots, new_blueprint.obsidian_robots,
                           new_blueprint.geode_robots)
                    if key not in maxes:
                        maxes[key] = set()
                    maxes[key].add(new_blueprint)

                next_blueprints = set()
                for key in maxes:
                    for bp in maxes[key]:
                        smaller = False
                        for bp2 in maxes[key]:
                            if bp == bp2:
                                continue
                            if all(x <= y for x, y in zip(bp.get_score(), bp2.get_score())):
                                smaller = True
                                break
                        if not smaller:
                            next_blueprints.add(bp)
                print(blueprint.id, i, len(next_blueprints))

            geodes = 0
            for p in next_blueprints:
                geodes = max(p.geode, geodes)

            total += geodes * blueprint.id
            print(blueprint.id, geodes, geodes * blueprint.id)

        return total

    def calc_2(self, data: [Blueprint]) -> int:

        total = 1
        count = min(3, len(data))
        for blueprint in data[0:count]:
            blueprint.ore_robots = 1

            next_blueprints = set()
            next_blueprints.add(blueprint)
            turns = 32
            print(blueprint.id, 0, len(next_blueprints))
            for i in range(1, turns+1):
                new_blueprints = set()
                for next_blueprint in next_blueprints:
                    blueprints = self.process_blueprint(next_blueprint, i, turns)
                    new_blueprints = new_blueprints.union(blueprints)

                maxes = {}
                for new_blueprint in new_blueprints:
                    key = (new_blueprint.ore_robots, new_blueprint.clay_robots, new_blueprint.obsidian_robots,
                           new_blueprint.geode_robots)
                    if key not in maxes:
                        maxes[key] = set()
                    maxes[key].add(new_blueprint)

                next_blueprints = set()
                for key in maxes:
                    for bp in maxes[key]:
                        smaller = False
                        for bp2 in maxes[key]:
                            if bp == bp2:
                                continue
                            if all(x <= y for x, y in zip(bp.get_score(), bp2.get_score())):
                                smaller = True
                                break
                        if not smaller:
                            next_blueprints.add(bp)
                print(blueprint.id, i, len(next_blueprints))

            geodes = 0
            for p in next_blueprints:
                geodes = max(p.geode, geodes)

            total *= geodes
            print(blueprint.id, geodes)

        return total

    def load_handler_part1(self, data: [Blueprint]) -> {}:
        blueprints: [Blueprint] = []
        p = re.compile(
            r'Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.')
        for row in data:
            m = re.match(p, row)
            if m:
                blueprints.append(Blueprint(
                    int(m.group(1)),
                    int(m.group(2)),
                    int(m.group(3)),
                    (int(m.group(4)), int(m.group(5))),
                    (int(m.group(6)), int(m.group(7)))
                ))
        return blueprints

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc202212()
    failed, results = aoc.run("part1x_[1-1]+.txt", "part2_[1-1]+.txt")
    if failed:
        exit(1)
