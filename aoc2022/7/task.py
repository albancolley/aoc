import string

from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
import sys
import re
logger = logging.getLogger("ACO2022-7")


class Aoc202206(AocBase):

    def calc_1(self, data: [str]) -> int:
        tree = {}
        level = tree
        mode = "cd"
        for item in data:
            if item[0] == "$":
                if item[2:4] == "ls":
                    mode = "ls"
                if item[2:4] == "cd":
                    mode = "cd"
                    if item[5] == "/":
                        level = tree
                    elif item[5:7] == "..":
                        level = level["P"]
                    else:
                        parent = level
                        level = level[item[5:]]
                        level["P"] = parent
            else:
                if item[0:3] == "dir":
                    level[item[4:]] = {}
                else:
                    file_details = item.split(" ")
                    if file_details[1] not in level:
                        level[file_details[1]] = int(file_details[0])
                        if "T" not in level:
                            level["T"] = 0
                        if "S" not in level:
                            level["S"] = 0
                        level["T"] += int(file_details[0])
                        level["S"] += int(file_details[0])
                        traverse = level
                        while "P" in traverse:
                            traverse = traverse["P"]
                            if "S" not in traverse:
                                traverse["S"] = 0
                            traverse["S"] += int(file_details[0])

        total: int = 0
        total = self._sum(tree)
        return total

    def calc_2(self, data: [str]) -> int:
        tree = {}
        level = tree
        mode = "cd"
        for item in data:
            if item[0] == "$":
                if item[2:4] == "ls":
                    mode = "ls"
                if item[2:4] == "cd":
                    mode = "cd"
                    if item[5] == "/":
                        level = tree
                        tree["D"] = "/"
                    elif item[5:7] == "..":
                        level = level["P"]
                    else:
                        parent = level
                        level = level[item[5:]]
                        level["P"] = parent
            else:
                if item[0:3] == "dir":
                    level[item[4:]] = {}
                    level[item[4:]]["D"] = item[4:]
                else:
                    file_details = item.split(" ")
                    if file_details[1] not in level:
                        level[file_details[1]] = int(file_details[0])
                        if "T" not in level:
                            level["T"] = 0
                        if "S" not in level:
                            level["S"] = 0
                        level["T"] += int(file_details[0])
                        level["S"] += int(file_details[0])
                        traverse = level
                        while "P" in traverse:
                            traverse = traverse["P"]
                            if "S" not in traverse:
                                traverse["S"] = 0
                            traverse["S"] += int(file_details[0])

        disk_size = tree["S"]
        free = 70000000 - disk_size
        need = 30000000 - free
        total: int = sys.maxsize
        flat = self._flat(tree, need)
        for i in flat:
            if flat[i] < total:
                total = flat[i]
        return total

    def load_handler_part1(self, data: [str]) -> [str]:
        return data

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)

    def _sum(self, t: dict) -> int:
        s = 0
        for item in t:
            if item != "P" and  isinstance(t[item], dict):
                s += self._sum(t[item])
            if item == "S" and t["S"] <= 100000:
                s += t[item]
        return s

    def _flat(self, t: dict, min: int) -> int:
        flat = {}
        for item in t:
            if item != "P" and  isinstance(t[item], dict):
                flat = flat | self._flat(t[item], min)
            if item == "S" and t["S"] >= min:
                flat[t["D"]] = t[item]
        return flat


if __name__ == '__main__':
    configure()
    aoc = Aoc202206()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        exit(1)
