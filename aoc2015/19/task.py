"""
AOC Day X
"""
import sys
from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
import collections
import math
import re
from queue import PriorityQueue

class Aoc201600(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: ({}, str)) -> int:
        replacements, molecule = data
        new_molecules = set()
        for replacement in replacements:
            for change in replacements[replacement]:
                for match in re.finditer(replacement, molecule):
                    new_molecules.add(molecule[0:match.start()] + change + molecule[match.end():])

        # print(replacements)
        # print(molecule)
        # print(new_molecules)
        return len(new_molecules)

    def calc_2(self, data: [str]) -> int:
        #Stole this from https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4cu5b/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
        #Seemed to be OK to just run reach subitition type once, just have to try different orders.
        from random import shuffle

        replacements_dict, target_molecule = data

        replacements = []
        for r in replacements_dict:
            for c in replacements_dict[r]:
                replacements.append((r, c))

        reps = replacements
        mol = target_molecule

        target = mol
        part2 = 0

        while target != 'e':
            tmp = target
            for a, b in reps:
                if b not in target:
                    continue

                target = target.replace(b, a, 1)
                part2 += 1

            if tmp == target:
                target = mol
                part2 = 0
                shuffle(reps)

        return(part2)

    def calc_2x(self, data: [str]) -> int:
        replacements_dict, target_molecule = data

        replacements = []
        for r in replacements_dict:
            for c in replacements_dict[r]:
                replacements.append((r, c))

        replacements = sorted(replacements, key=lambda x: -len(x[1]))

        def f(X):
            for j, i in replacements:
                for k in range(len(X)):
                    if X[k:k + len(i)] == i:
                        y = X[:k] + j + X[k + len(i):]
                        yield y

        molecules = [target_molecule]
        seen = {target_molecule}
        step = 1
        while len(molecules) > 0:
            new_molecules = []
            for molecule in molecules:
                for new_molecule in f(molecule):
                    new_molecules.append(new_molecule)
                    if new_molecule in seen:
                        continue
                    if new_molecule == "e":
                        return step
                    seen.add(new_molecule)
                    print(new_molecule)
                    # break
            molecules = new_molecules
            step += 1

        return 0

    def calc_2_x(self, data: [str]) -> int:
        replacements, target_molecule = data

        molecules = PriorityQueue()
        seen = {}
        molecules.put((len(target_molecule), 0, target_molecule))
        min_steps = 10000000
        while not molecules.empty():
            # print(molecules.qsize())
            priority, step, molecule = molecules.get()
            if molecule in seen and step > seen[new_molecule]:
                continue

            step = step + 1
            if step > min_steps:
                continue

            if priority <= 10:
                print(priority, step, molecule)

            has_match = False
            for replacement in replacements:
                for change in replacements[replacement]:
                    for match in re.finditer(change, molecule):
                        new_molecule = molecule[0: match.start()]
                        new_molecule += replacement
                        new_molecule += molecule[match.end():]
                        if new_molecule == "e":
                            min_steps = min(step, min_steps)
                            print("found", step)
                            continue
                        if new_molecule in seen and step >= seen[new_molecule]:
                             continue
                        seen[new_molecule] = step
                        molecules.put((len(new_molecule), step, new_molecule))
                        has_match = True

            if not has_match:
                seen[molecules] = 0

                        # print(new_molecule)
            # print(len(new_molecules))
            # for molecules in new_molecules:
            #     if "e" == molecules:
            #         return steps
            # molecules = new_molecules
            # for molecule in new_molecules:
            #     if len(molecule) < len(target_molecule):
            #         molecules.add(molecule)
        return min_steps

    def load_handler_part1(self, data: [str]) -> [str]:
        replacements = {}
        for l in data[:-2]:
            r = l.split(" => ")
            if r[0] not in replacements:
                replacements[r[0]] = []
            replacements[r[0]].append(r[1])
        molecule = data[-1]
        return replacements, molecule

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc201600()
    failed, results = aoc.run("part1x_[0-9]+.txt", "part2_[3-3]+.txt")
    if failed:
        sys.exit(1)
