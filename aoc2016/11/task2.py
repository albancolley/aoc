from itertools import combinations
import heapq

# hardcoded input
polonium, thulium, promethium, ruthenium, cobalt, elerium, dilithium ,curium, plutonium= 1, 2, 3, 4, 5, 6, 7,8,9
# initial = (0, (
# 	tuple(sorted((promethium, -promethium))),
# 	tuple(sorted((cobalt, curium,ruthenium,plutonium))),
#     tuple(sorted((-cobalt,-curium,-ruthenium,-plutonium))),
#     ()
# ))

initial = (0, (
	tuple(sorted((promethium, -promethium, -elerium, elerium, dilithium ,-dilithium  ))),
	tuple(sorted((cobalt, curium,ruthenium,plutonium))),
    tuple(sorted((-cobalt,-curium,-ruthenium,-plutonium))),
    ()
))


# The first floor contains a promethium generator and a promethium-compatible microchip.
# The second floor contains a cobalt generator, a curium generator, a ruthenium generator, and a plutonium generator.
# The third floor contains a cobalt-compatible microchip, a curium-compatible microchip, a ruthenium-compatible microchip, and a plutonium-compatible microchip.
# The fourth floor contains nothing relevant.

def correct(floor):
	if not floor or floor[-1] < 0: # no generators
		return True
	return all(-chip in floor for chip in floor if chip < 0)

frontier = []
heapq.heappush(frontier, (0, initial))
cost_so_far = {initial: 0}

while frontier:
	_, current = heapq.heappop(frontier)
	floor, floors = current

	# print(current)

	if floor == 3 and all(len(f) == 0 for f in floors[:-1]): # goal!
		break

	directions = [dir for dir in (-1, 1) if 0 <= floor + dir < 4]
	moves = list(combinations(floors[floor], 2)) + list(combinations(floors[floor], 1))
	pair = False
	for move in moves:
		if pair:
			continue
		if len(move) == 2:
			if move[0] == move[1]:
				pair = True
			# else:
			# 	if move[0] > 0 > move[1]:
			# 		continue
			# 	elif move[0] < 0 < move[1]:
			# 		continue

		for direction in directions:
			new_floors = list(floors)
			new_floors[floor] = tuple(x for x in floors[floor] if x not in move)
			new_floors[floor+direction] = tuple(sorted(floors[floor+direction] + move))

			if not correct(new_floors[floor]) or not correct(new_floors[floor+direction]):
				continue

			next = (floor+direction, tuple(new_floors))
			new_cost = cost_so_far[current] + 1
			if next not in cost_so_far or new_cost < cost_so_far[next]:
				cost_so_far[next] = new_cost
				priority = new_cost - len(new_floors[3])*10 # silly manually tweakable heuristic factor
				heapq.heappush(frontier, (priority, next))

print(cost_so_far[current], current)