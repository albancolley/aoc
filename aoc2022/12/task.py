import string

from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
import numpy as np
from dataclasses import dataclass, field
from collections import OrderedDict
from collections import deque

logger = logging.getLogger("ACO2022-12")

import math



@dataclass
class HillMap:

    input: np.ndarray
    distance: np.ndarray
    start: (int,int)
    end: (int,int)
    seen = {}

class Aoc202212(AocBase):

    def build_graph(self, data, items, graph):
        x_max, y_max = data.input.shape
        while len(items) > 0:
            start_pos = items.pop()
            if start_pos in data.seen:
                continue
            x, y = start_pos
            height = data.input[x, y]
            node = x * y_max + y
            if x > 0:
                pos = (x - 1, y)
                if height + 1 >= data.input[pos]:
                    node1 = pos[0] * y_max + pos[1]
                    if node1 not in graph:
                        graph[node1] = set()
                    graph[node].add(node1)
                    if pos not in data.seen:
                        items.append(pos)
            if x < x_max - 1:
                pos = (x + 1, y)
                if height + 1 >= data.input[pos]:
                    node1 = pos[0] * y_max + pos[1]
                    if node1 not in graph:
                        graph[node1] = set()
                    graph[node].add(node1)
                    if pos not in data.seen:
                        items.append(pos)
            if y > 0:
                pos = (x, y - 1)
                if height + 1 >= data.input[pos]:
                    node1 = pos[0] * y_max + pos[1]
                    if node1 not in graph:
                        graph[node1] = set()
                    graph[node].add(node1)
                    if pos not in data.seen:
                        items.append(pos)
            if y < y_max - 1:
                pos = (x, y + 1)
                if height + 1 >= data.input[pos]:
                    node1 = pos[0] * y_max + pos[1]
                    if node1 not in graph:
                        graph[node1] = set()
                    graph[node].add(node1)
                    if pos not in data.seen:
                        items.append(pos)
            data.seen[start_pos] = True

    def shortest_path(self, graph, node1, node2):
        path_list = deque()
        path_list.append([node1])
        # To keep track of previously visited nodes
        previous_nodes = {node1}
        if node1 == node2:
            return path_list[0]

        while len(path_list) > 0:
            current_path = path_list.popleft()
            last_node = current_path[-1]
            next_nodes = graph[last_node]
            # Search goal node
            if node2 in next_nodes:
                current_path.append(node2)
                return current_path
            # Add new paths
            for next_node in next_nodes:
                if next_node in previous_nodes:
                    continue
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # No path is found
        return []

    def calc_1(self, data: HillMap) -> int:
        data.distance[data.start] = 0
        start = deque()
        start.append(data.start)
        graph = {}
        name = data.start[0] * len(data.input[0]) + data.start[1]
        name_end = data.end[0] * len(data.input[0]) + data.end[1]
        graph[name] = set()
        self.build_graph(data, start, graph)
        x = self.shortest_path(graph, name, name_end)

        return len(x) - 1

    def build_graph2(self, data, items, graph, seen, x_max, y_max):
        x_limit = x_max*y_max - y_max
        y_limit = y_max - 1
        while len(items) > 0:
            node = items.pop()
            if node in seen:
                continue
            height = data[node]
            y_node = node % y_max
            if node >= y_max:
                pos = node - y_max
                self.add_item(data, graph, height, items, node, pos, seen)
            if node < x_limit:
                pos = node + y_max
                self.add_item(data, graph, height, items, node, pos, seen)
            if y_node > 0:
                pos = node - 1
                self.add_item(data, graph, height, items, node, pos, seen)
            if y_node < y_limit:
                pos = node + 1
                self.add_item(data, graph, height, items, node, pos, seen)
            seen[node] = True

    def add_item(self, data, graph, height, items, node, pos, seen):
        if data[pos] >= height-1:
            node1 = pos
            if node1 not in graph:
                graph[node1] = set()
            graph[node].add(node1)
            if pos not in seen:
                items.append(pos)

    def calc_2(self, data ) -> int:
        input_data, end, x_max, y_max = data
        graph = {}
        queue = deque()
        queue.append(end)
        seen = {}
        graph[end] = set()
        self.build_graph2(input_data, queue, graph, {}, x_max, y_max)

        seen = {end: True}
        length = 0
        queue = deque()
        queue.append((0, end))
        done = False
        heights = input_data
        while len(queue) > 0 and not done:
            steps, node_index = queue.popleft()
            index_ = graph[node_index]
            for node in index_:
                if node not in seen:
                    height = heights[node]
                    if height == 1:
                        length = steps + 1
                        done = True
                        break
                    queue.append((steps + 1, node))
                seen[node] = True

        return length

    def load_handler_part1(self, data: [str]) -> HillMap:
        rows, cols = (len(data), len(data[0]))
        new_data = np.zeros((rows, cols))
        row_pos = 0
        max_height = 0
        for row in data:
            col_pos = 0
            for col in row:
                if col == 'S':
                    value = 200
                    start = (row_pos, col_pos)
                elif col == 'E':
                    value = 99
                    end = (row_pos, col_pos)
                else:
                    value = ord(col) - ord('a') + 1
                    if value > max_height:
                        max_height = value
                new_data[row_pos, col_pos] = value
                col_pos += 1
            row_pos += 1
        new_data[end] = max_height
        hill_map = HillMap(new_data, np.full((rows, cols),  np.inf), start, end)
        return hill_map

    def load_handler_part2(self, data: [str]) -> [str]:
        new_data = {}
        row_pos = 0
        pos = 0
        for row in data:
            col_pos = 0
            for col in row:
                if col == 'S':
                    value = 1
                elif col == 'E':
                    value = 26
                    end = pos
                else:
                    value = ord(col) - ord('a') + 1
                new_data[pos] = value
                col_pos += 1
                pos += 1
            row_pos += 1
        return new_data, end, row_pos, col_pos

    def load_handler_part2x(self, data: [str]) -> [str]:
        rows, cols = (len(data), len(data[0]))
        new_data = np.zeros((rows, cols), dtype=np.int)
        row_pos = 0
        max_height = 0
        for row in data:
            col_pos = 0
            for col in row:
                if col == 'S':
                    value = 1
                    start = (row_pos, col_pos)
                elif col == 'E':
                    value = 26
                    end = (row_pos, col_pos)
                else:
                    value = ord(col) - ord('a') + 1
                new_data[row_pos, col_pos] = value
                col_pos += 1
            row_pos += 1
        hill_map = HillMap(new_data, np.full((rows, cols), np.inf), start, end)
        return hill_map


if __name__ == '__main__':
    configure()
    aoc = Aoc202212()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        exit(1)
