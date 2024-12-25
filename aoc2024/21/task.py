"""
AOC Day X
"""
import heapq
import sys
from idlelib.debugger_r import start_remote_debugger

from aoc2023.common.aocbase import AocBase
from aoc2023.common.setup import configure
from collections import Counter
import math

class Aoc202421(AocBase):
    """
    AOC Day 10 Class
    """

    keypad_str = [
        "#####",
        "#789#",
        "#456#",
        "#123#",
        "##0A#",
        "#####"
    ]

    directional_str = [
        "#####",
        "##^A#",
        "#<v>#",
        "#####"
    ]

    moves = {
        'v': 0 + 1j,
        '^': 0 - 1j,
        '<': -1 + 0j,
        '>': 1 + 0j
    }


    def to_grid(self, data: [str]):
        width = len(data[0])
        grid = dict()
        positions = dict()
        y = 0
        for _ in data:
            for x in range(width):
                value = data[y][x]
                pos = complex(x, y)
                grid[pos] = value
                if value != '#':
                    positions[value] = pos
            y += 1
        return grid, positions

    shortest_path_cache = {}

    def shortest_path(self, grid, start, end, cache_name):
        if cache_name not in self.shortest_path_cache:
            self.shortest_path_cache[cache_name] = {}

        if start in self.shortest_path_cache[cache_name]:
            if end in self.shortest_path_cache[cache_name][start]:
                return self.shortest_path_cache[cache_name][start][end]

        seen = {start: True}
        shortest_paths = []
        queue = [(start, [start], "")]
        while len(queue) > 0:
            pos, path, buttons = queue.pop(0)
            for move in self.moves:
                next_pos = pos + self.moves[move]
                if next_pos in path:
                    continue

                seen[next_pos] = True

                if next_pos == end:
                    shortest_paths += [buttons + move]
                    continue

                if grid[next_pos] == "#":
                    continue

                queue.append((next_pos, path + [next_pos], buttons + move))

        if len(shortest_paths) == 0:
            return []

        shortest_path_length = len(shortest_paths[0])
        for s in shortest_paths[1:]:
            if len(s) < shortest_path_length:
                shortest_path_length = len(s)

        shortest_paths = list(set([s for s in shortest_paths if len(s) == shortest_path_length]))

        if start not in self.shortest_path_cache[cache_name]:
            self.shortest_path_cache[cache_name][start] = dict()

        self.shortest_path_cache[cache_name][start][end] = shortest_paths
        return shortest_paths

    def shortest_path_dir(self, grid, start, end, cache_name):
        if cache_name not in self.shortest_path_cache:
            self.shortest_path_cache[cache_name] = {}

        if start in self.shortest_path_cache[cache_name]:
            if end in self.shortest_path_cache[cache_name][start]:
                return self.shortest_path_cache[cache_name][start][end]

        seen = {start: True}
        shortest_paths = []
        queue = [(start, [start], "")]
        while len(queue) > 0:
            pos, path, buttons = queue.pop(0)
            for move in self.moves:
                next_pos = pos + self.moves[move]
                if next_pos in path:
                    continue

                seen[next_pos] = True

                if next_pos == end:
                    shortest_paths += [buttons + move]
                    continue

                if grid[next_pos] == "#":
                    continue


                queue.append ((next_pos, path + [next_pos],  buttons + move))

        if len(shortest_paths) == 0:
            return ""

        shortest_path_length = len(shortest_paths[0])
        for s in shortest_paths[1:]:
            if len(s) < shortest_path_length:
                shortest_path_length = len(s)

        shortest_paths = list(set([s for s in shortest_paths if len(s) == shortest_path_length]))

        for shortest_path in shortest_paths:
            if ">>" in shortest_path or "<<" in shortest_path:
                shortest_paths = [shortest_path]
                break

        # hack - couldn't work out why these are the best paths
        if len(shortest_paths) > 1:
            if '<v' in shortest_paths:
                shortest_paths = ['<v']
            if '^>' in shortest_paths:
                shortest_paths = ['^>']
            if '<^' in shortest_paths:
                shortest_paths = ['<^']
            if 'v>' in shortest_paths:
                shortest_paths = ['v>']

        for shortest_path in shortest_paths:
            shortest_paths = [shortest_path]
            break

        if start not in self.shortest_path_cache[cache_name]:
            self.shortest_path_cache[cache_name][start] = dict()

        self.shortest_path_cache[cache_name][start][end] = shortest_paths[0]
        return shortest_paths[0]

    def calc_1(self, data: dict) -> int:
        result = 0
        keypad_grid, key_positions = self.to_grid(self.keypad_str)
        direction_grid, direction_positions = self.to_grid(self.directional_str)

        for code in data:
            current_key = 'A'
            possible_keypad_sequences = ['']
            for c in code:
                paths = self.shortest_path(keypad_grid, key_positions[current_key], key_positions[c], 'key')
                next_possible_keypad_sequences = []
                for possible_keypad_sequence in possible_keypad_sequences:
                    for path in paths:
                        next_possible_keypad_sequences += [possible_keypad_sequence + path + "A"]
                possible_keypad_sequences = next_possible_keypad_sequences

                current_key = c

            total = sys.maxsize

            for direction_sequence in possible_keypad_sequences:

                counts = Counter()
                parts = direction_sequence.split('A')[0:-1]
                for i in range(len(parts)):
                    counts.update({parts[i] + "A": 1})
                # print(counts)

                for i in range(2):
                    new_counts = Counter()

                    new_key = ""
                    for key in counts:
                        count = counts[key]
                        last_pos = direction_positions['A']
                        next_values = ""
                        for value in key:
                            pos = direction_positions[value]
                            next_values += self.shortest_path_dir(direction_grid, last_pos, pos, 'direction2') + "A"
                            last_pos = pos

                        parts = next_values.split('A')[0:-1]
                        # print(key, next_values, parts)
                        for j in range(len(parts)):
                            new_counts.update({parts[j] + "A": count})

                        new_key += next_values
                    counts = new_counts

                length = 0
                for key2 in counts:
                    length += len(key2) * counts[key2]

                total = min(total, length * int(code[:-1]))

            result += total

        return result

    def get_directional_sequences(self, direction_grid, direction_positions, possible_keypad_sequences):
        direction_sequences = []
        for seq in possible_keypad_sequences:
            current_key = 'A'
            possible_direction_sequences = set()
            possible_direction_sequences.add('')
            for c in seq:
                paths = self.shortest_path(direction_grid, direction_positions[current_key], direction_positions[c], 'direction')
                next_possible_direction_sequences = set()
                for possible_direction_sequence in possible_direction_sequences:
                    for path in paths:
                        new_path = possible_direction_sequence + path + "A"
                        next_possible_direction_sequences.add(new_path)
                if len(paths) == 0:
                    for possible_direction_sequence in possible_direction_sequences:
                        next_possible_direction_sequences.add(possible_direction_sequence + "A")

                possible_direction_sequences = next_possible_direction_sequences
                current_key = c

            direction_sequences += possible_direction_sequences


        shortest_path_length = len(direction_sequences[0])
        for s in direction_sequences[1:]:
            if len(s) < shortest_path_length:
                shortest_path_length = len(s)

        direction_sequences = [s for s in direction_sequences if len(s) == shortest_path_length]


        return list(set(direction_sequences))

    def calc_2(self, data: [str]) -> int:

        result = 0
        keypad_grid, key_positions = self.to_grid(self.keypad_str)
        direction_grid, direction_positions = self.to_grid(self.directional_str)

        for code in data:
            current_key = 'A'
            possible_keypad_sequences = ['']
            for c in code:
                paths = self.shortest_path(keypad_grid, key_positions[current_key], key_positions[c], 'key')
                next_possible_keypad_sequences = []
                for possible_keypad_sequence in possible_keypad_sequences:
                    for path in paths:
                        next_possible_keypad_sequences += [possible_keypad_sequence + path + "A"]
                possible_keypad_sequences = next_possible_keypad_sequences

                current_key = c

            total = sys.maxsize

            for direction_sequence in possible_keypad_sequences:

                counts = Counter()
                parts = direction_sequence.split('A')[0:-1]
                for i in range(len(parts)):
                    counts.update({parts[i] + "A": 1})
                # print(counts)

                for i in range(25):
                    new_counts = Counter()

                    new_key = ""
                    for key in counts:
                        count = counts[key]
                        last_pos = direction_positions['A']
                        next_values = ""
                        for value in key:
                            pos = direction_positions[value]
                            next_values += self.shortest_path_dir(direction_grid, last_pos, pos, 'direction2') + "A"
                            last_pos = pos

                        parts = next_values.split('A')[0:-1]
                        # print(key, next_values, parts)
                        for j in range(len(parts)):
                            new_counts.update({parts[j] + "A": count})

                        new_key += next_values
                    counts = new_counts

                length = 0
                for key2 in counts:
                    length += len(key2) * counts[key2]

                total = min(total, length * int(code[:-1]))
                # print(code, length)

            result += total

        return result


    def load_handler_part1(self, data: [str]) -> [str]:
       return data

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc202421()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
