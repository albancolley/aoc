import os.path
import string
from dataclasses import dataclass

from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
import re
from collections import deque
import heapq as heap

logger = logging.getLogger("ACO2022-14")


# class definition
class Entry:

    # constructor
    def __init__(self, flow, m_time, e_time, m_node_name, e_node_name, opened, m_path, e_path):
        self.flow = flow
        self.m_time = m_time
        self.e_time = e_time
        self.m_node_name = m_node_name
        self.e_node_name = e_node_name
        self.opened = opened
        self.m_path = m_path
        self.e_path = e_path

    def __lt__(self, nxt):
        if self.flow == nxt.flow:
            if self.opened == nxt.opened:
                return self.m_time + self.e_time > nxt.m_time + nxt.e_time
            return self.opened > nxt.opened

        return self.flow > nxt.flow
    #
    # def __lt__(self, nxt):
    #         return self.distance + len(self.path) < nxt.distance + len(nxt.path)


class Aoc202212(AocBase):

    def calc_1(self, data) -> int:
        total = 0
        graph, rated_nodes = data
        rooms = deque()
        to_visit = []
        results = []
        for key in rated_nodes:
            to_visit.append(key)
        rooms.append(('AA', 0, to_visit[:], 30, ['AA']))
        while len(rooms) > 0:
            room_name, flow, seen_valves, time, path = rooms.popleft()
            if time <= 0:
                continue
            all_node_visited = True
            for node in graph[room_name]:
                node, distance, node_score = node
                if (time - distance) <= 0:
                    continue
                if node in seen_valves:
                    all_node_visited = False
                    new_score = (time - distance) * node_score
                    remaining_valves = seen_valves[:]
                    remaining_valves.remove(node)
                    new_path = path[:]
                    new_path.append(node)
                    rooms.append((node, flow + new_score, remaining_valves, time - distance, new_path))
            if all_node_visited:
                results.append((flow, path))
        results.sort()
        row = results[-1]
        total = row[0]
        return total

    def calc_2(self, data) -> int:
        total = 0
        graph, rated_nodes = data
        rooms = deque()
        # to_visit = []
        results = []
        # for key in rated_nodes:
        #     to_visit.append(key)
        rooms.append(('AA', 0, [], 26, ['AA']))
        while len(rooms) > 0:
            room_name, flow, seen_valves, time, path = rooms.popleft()
            if time < 0:
                continue
            results.append((flow, set(seen_valves), 26 - time))
            for node in graph[room_name]:
                node, distance, node_score = node
                if (time - distance) <= 0:
                    continue
                if node not in seen_valves:
                    new_score = (time - distance) * node_score
                    new_seen_valves = seen_valves[:]
                    new_seen_valves.append(node)
                    new_path = path[:]
                    new_path.append(node)
                    rooms.append((node, flow + new_score, new_seen_valves, time - distance, new_path))

        max_flow = 0
        print('got lists')
        for r in results:
            for r2 in results:
                if r[0] + r2[0] > max_flow:
                    if len(r[1].intersection(r2[1])) == 0:
                        max_flow = r[0] + r2[0]
                        print(max_flow)
        return max_flow

    def calc_2nope(self, data: [str]) -> int:
        total = 0
        graph, rated_nodes = data
        pq = []
        heap.heappush(pq, Entry(0, 26, 26, 'AA', 'AA', set(), ['AA'], ['AA']))
        max_flow = 0
        min_distance = 1000
        for g in graph:
            nodes = graph[g]
            for node in nodes:
                min_distance = min(min_distance, node[1])
        while pq:
            entry = heap.heappop(pq)
            if entry.m_time < 0 or entry.e_time < 0:
                continue

            if (len(entry.opened) >= len(rated_nodes)) or (entry.m_time < min_distance and entry.e_time < min_distance):
                if entry.flow > max_flow:
                    print(entry.flow, len(pq))
                max_flow = max(max_flow, entry.flow)
                continue

            for m_node in graph[entry.m_node_name]:
                m_next_node_name, m_next_distance, m_next_node_score = m_node
                m_time_remaining, m_new_score, m_new_opened, m_new_path = self.buld_next(m_next_distance,
                                                                                         m_next_node_name,
                                                                                         m_next_node_score,
                                                                                         entry.m_time, entry.opened,
                                                                                         entry.m_path)

                for e_node in graph[entry.e_node_name]:
                    if m_node in entry.opened and e_node in entry.opened:
                        continue
                    if m_node in entry.opened:
                        m_node = entry.m_node_name
                    if m_node in entry.opened:
                        m_node = entry.m_node_name

                    e_next_node_name, e_next_distance, e_next_node_score = e_node
                    e_time_remaining, e_new_score, e_new_opened, e_new_path = self.buld_next(e_next_distance,
                                                                                             e_next_node_name,
                                                                                             e_next_node_score,
                                                                                             entry.e_time, m_new_opened,
                                                                                             entry.e_path)
                    heap.heappush(pq,
                                  Entry(entry.flow + m_new_score + e_new_score,
                                        m_time_remaining, e_time_remaining,
                                        m_next_node_name, e_next_node_name,
                                        e_new_opened,
                                        m_new_path, e_new_path
                                        ))
        return max_flow


    def buld_next(self, next_distance, next_node_name, next_node_score, time, opened: set, path):
        new_opened = opened.copy()
        time_remaining = time
        new_score = (time - next_distance) * next_node_score
        if next_node_name in opened:
            new_score = 0
        else:
            time_remaining = (time - next_distance)
            new_opened.add(next_node_name)
            new_path = path[::-1]
            new_path.append(next_node_name)

        return time_remaining, new_score, new_opened, new_path

    def calc_2almost(self, data: [str]) -> int:
        total = 0
        graph, rated_nodes = data
        rooms = deque()
        to_visit = []
        results = []
        for key in rated_nodes:
            to_visit.append(key)
        rooms.append(('AA', 'AA', 0, to_visit[:], 26, 26, [('AA', 'AA')], [], []))
        count = 1
        max_score = 0
        while len(rooms) > 0:
            room_name, elephant_room_name, flow, visited_values, time, elephant_time, path, p_path, e_path = rooms.popleft()
            # if count % 10000 == 0:
            #     print(count, len(rooms))
            count = count + 1
            next_rooms = []
            next_elephant_rooms = []

            for room in graph[room_name]:
                node, distance, node_score = room
                if node not in visited_values:
                    new_score = (time - distance) * 0
                    time_remaining = (time - distance + 1)
                    next_rooms.append((node, new_score, time_remaining))
                if time - distance > 0:
                    new_score = (time - distance) * node_score
                    time_remaining = (time - distance)
                    next_rooms.append((node, new_score, time_remaining))

            for room in graph[elephant_room_name]:
                node, distance, node_score = room
                if node not in visited_values:
                    elephant_new_score = (elephant_time - distance) * 0
                    elephant_time_remaining = (elephant_time - distance + 1)
                    next_elephant_rooms.append((node, elephant_new_score, elephant_time_remaining))
                if elephant_time - distance > 0:
                    elephant_new_score = (elephant_time - distance) * node_score
                    elephant_time_remaining = (elephant_time - distance)
                    next_elephant_rooms.append((node, elephant_new_score, elephant_time_remaining))

            if len(next_rooms) == 0 and len(next_elephant_rooms) == 0:
                if flow > max_score:
                    print(flow)
                    max_score = flow
                # results.append((flow, path))
                continue

            if len(next_rooms) == 0:
                new_flow = flow + next_elephant_rooms[0][1]
                if new_flow > max_score:
                    print(new_flow)
                    max_score = new_flow
                # results.append((new_flow, path))
                continue

            if len(next_elephant_rooms) == 0:
                new_flow = flow + next_rooms[0][1]
                if new_flow > max_score:
                    print(new_flow)
                    max_score = new_flow
                # results.append((new_flow, path))
                continue

            for room in next_rooms:
                new_room_name, new_room_score, new_room_time_remaining = room
                for elephant_room in next_elephant_rooms:
                    elephant_new_room_name, elephant_new_room_score, elephant_new_room_time_remaining = elephant_room
                    if new_room_name == elephant_new_room_name:
                        continue
                    remaining_valves = visited_values[:]
                    if new_room_name in remaining_valves:
                        remaining_valves.remove(new_room_name)
                    if elephant_new_room_name in remaining_valves:
                        remaining_valves.remove(elephant_new_room_name)
                    new_path = path[:]
                    new_path.append((new_room_name, elephant_new_room_name, flow, new_room_score,
                                     elephant_new_room_score, flow + new_room_score + elephant_new_room_score
                                     , new_room_time_remaining,
                                     elephant_new_room_time_remaining))
                    new_p_path = p_path[:]
                    new_p_path.append((new_room_name, new_room_score, new_room_time_remaining))
                    new_e_path = e_path[:]
                    new_e_path.append(
                        (elephant_new_room_name, elephant_new_room_score, elephant_new_room_time_remaining))
                    # print((new_room_name, elephant_new_room_name, flow + new_room_score + elephant_new_room_score,
                    #               remaining_valves, new_room_time_remaining,
                    #               elephant_new_room_time_remaining, new_path, p_path, e_path))
                    rooms.appendleft(
                        (new_room_name, elephant_new_room_name, flow + new_room_score + elephant_new_room_score,
                         remaining_valves, new_room_time_remaining,
                         elephant_new_room_time_remaining, new_path, new_p_path, new_e_path))

        # results.sort()
        # row = results[-1]
        # total = row[0]
        return max_score

    def calc_2x(self, data: [str]) -> int:
        total = 0
        graph, rated_nodes = data
        rooms = deque()
        to_visit = []
        results = []
        for key in rated_nodes:
            to_visit.append(key)
        rooms.append(('AA', 'AA', 0, to_visit[:], 26, 26, [('AA', 'AA')]))
        while len(rooms) > 0:
            room_name, elephant_room_name, flow, not_visited, time, elephant_time, path = rooms.popleft()
            if time <= 0 and elephant_time <= 0:
                continue
            all_node_visited = True
            for room in graph[room_name]:
                node, distance, node_score = room
                if node in not_visited:
                    all_node_visited = False
                    remaining_valves = not_visited[:]
                    if time - distance < 0:
                        new_score = time * node_score
                        time_remaining = 0
                    else:
                        new_score = (time - distance) * node_score
                        time_remaining = (time - distance)
                    remaining_valves.remove(node)
                    for elephant_room in graph[elephant_room_name]:
                        elephant_node, elephant_distance, elephant_node_score = elephant_room
                        if elephant_node == node or elephant_node not in remaining_valves:
                            continue
                        elephant_remaining_valves = remaining_valves[:]
                        if time - elephant_distance < 0:
                            elephant_new_score = elephant_time * elephant_node_score
                            elephant_time_remaining = 0
                        else:
                            elephant_new_score = (elephant_time - elephant_distance) * elephant_node_score
                            elephant_time_remaining = (elephant_time - elephant_distance)
                        elephant_remaining_valves.remove(elephant_node)
                        new_path = path[:]
                        new_path.append((node, elephant_node))
                        rooms.insert(0, (node, elephant_node, flow + new_score + elephant_new_score,
                                         elephant_remaining_valves, time_remaining,
                                         elephant_time_remaining, new_path))
            if all_node_visited:
                results.append((flow, path))
        results.sort()
        row = results[-1]
        total = row[0]
        return total

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

    def load_handler_part1(self, data: [str]) -> {}:
        graph = {}
        rated_nodes = {}
        p = re.compile(F'Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.*)')
        for row in data:
            m = re.match(p, row)
            if m:
                valve = m.group(1)
                rate = int(m.group(2))
                if rate > 0:
                    rated_nodes[valve] = rate
                tunnels = m.group(3)
                connected_valves = []
                for connected_valve in tunnels.split(','):
                    connected_valves.append(connected_valve.strip())
                graph[valve] = connected_valves

        new_graph = {}
        verts = []
        for valve in rated_nodes:
            path = self.shortest_path(graph, 'AA', valve)
            verts.append((valve, len(path), rated_nodes[valve]))
        new_graph['AA'] = verts
        for valve in rated_nodes:
            verts = []
            for valve2 in rated_nodes:
                if valve2 != valve:
                    path = self.shortest_path(graph, valve, valve2)
                    verts.append((valve2, len(path), rated_nodes[valve2]))
            new_graph[valve] = verts
        return new_graph, rated_nodes

    def load_handler_part2(self, data: [str]) -> [str]:
        graph = {}
        rated_nodes = {}
        p = re.compile(F'Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.*)')
        for row in data:
            m = re.match(p, row)
            if m:
                valve = m.group(1)
                rate = int(m.group(2))
                if rate > 0:
                    rated_nodes[valve] = rate
                tunnels = m.group(3)
                connected_valves = []
                for connected_valve in tunnels.split(','):
                    connected_valves.append(connected_valve.strip())
                graph[valve] = connected_valves

        new_graph = {}
        verts = []
        for valve in rated_nodes:
            path = self.shortest_path(graph, 'AA', valve)
            verts.append((valve, len(path), rated_nodes[valve]))
        new_graph['AA'] = verts
        for valve in rated_nodes:
            verts = []
            for valve2 in rated_nodes:
                if valve2 != valve:
                    path = self.shortest_path(graph, valve, valve2)
                    verts.append((valve2, len(path), rated_nodes[valve2]))
            new_graph[valve] = verts
        return new_graph, rated_nodes


if __name__ == '__main__':
    configure()
    aoc = Aoc202212()
    failed, results = aoc.run("part1x_[0-9]+.txt", "part2_[1-2]+.txt")
    if failed:
        exit(1)
