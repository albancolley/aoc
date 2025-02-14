"""
AOC Day X
"""
import sys

from common import AocBase
from common import configure


class Aoc202400(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: dict) -> int:
        wires: dict[str, int]
        wires, inputs, tree = data
        # print(wires, inputs)

        new_wires = self.compute(inputs, wires)

        result = self.get_integer(new_wires, "z")
        return result

    def get_integer(self, wires, value):
        keys = [x for x in wires.keys() if x.startswith(value)]
        keys.sort()
        keys.reverse()
        r = [str(wires[x]) for x in keys]
        result = int("".join(r), 2)
        return result

    def compute(self, inputs, original_wires) -> dict:
        queue: list = inputs.copy()
        wires = original_wires.copy()
        last_length = len(queue)
        while len(queue) > 0:
            new_queue = []
            while len(queue) > 0:
                inp = queue.pop()
                left, cond, right, out = inp
                if left in wires and right in wires:
                    match cond:
                        case 'AND':
                            wires[out] = wires[left] & wires[right]
                        case 'OR':
                            wires[out] = wires[left] | wires[right]
                        case 'XOR':
                            wires[out] = wires[left] ^ wires[right]
                else:
                    new_queue.append(inp)

            queue = new_queue
            if last_length == len(queue):
                break
            last_length = len(queue)
        return wires

    def calc_2(self, data: [str]) -> str:
        wires: dict[str, int]
        wires, inputs, tree = data
        # print(wires, inputs)
        # print(len(inputs))

        # all_intrsections = self.do_run(inputs, wires)

        # did ny hand with output from self.do_run(inputs, wires)
        # Basically looked at the growth of the number of steps at each binary digit and work out what term was wrong.


        results = []
        new_inputs: list = inputs.copy()

        p = ('y05', 'AND', 'x05', 'svm')
        i = ('y05', 'XOR', 'x05', 'nbc')
        results += [p[3], i[3]]
        new_inputs.remove(p)
        new_inputs.remove(i)
        new_inputs.append((p[0], p[1], p[2], i[3]))
        new_inputs.append((i[0], i[1], i[2], p[3]))

        p = ('dkk', 'OR', 'pbd', 'z15')
        i = ('fwr', 'XOR', 'cpv', 'kqk')
        results += [p[3], i[3]]

        new_inputs.remove(p)
        new_inputs.remove(i)
        new_inputs.append((p[0], p[1], p[2], i[3]))
        new_inputs.append((i[0], i[1], i[2], p[3]))

        p = ('x23', 'AND', 'y23', 'z23')
        i = ('kph', 'XOR', 'hpw', 'cgq')
        results += [p[3], i[3]]

        new_inputs.remove(p)
        new_inputs.remove(i)
        new_inputs.append((p[0], p[1], p[2], i[3]))
        new_inputs.append((i[0], i[1], i[2], p[3]))

        p= ('bdr', 'XOR', 'fsp', 'fnr')
        i = ('fsp', 'AND', 'bdr', 'z39')
        results += [p[3], i[3]]

        new_inputs.remove(p)
        new_inputs.remove(i)
        new_inputs.append((p[0], p[1], p[2], i[3]))
        new_inputs.append((i[0], i[1], i[2], p[3]))

        # all_intrsections = self.do_run(new_inputs, wires)
        new_wires = self.compute(new_inputs, wires)
        x = self.get_integer(new_wires, "x")
        y = self.get_integer(new_wires, "y")
        z = self.get_integer(new_wires, "z")
        expected = x + y
        if z != expected:
            return "Failed"

        results.sort()
        return ",".join(results)

    def do_run(self, inputs, wires):
        new_wires = self.compute(inputs, wires)
        x = self.get_integer(new_wires, "x")
        y = self.get_integer(new_wires, "y")
        z = self.get_integer(new_wires, "z")
        expected = x + y
        difference = format(z ^ expected, 'b')
        print(f'x {x:>050b}')
        print(f'y {y:>050b}')
        print(f'z {z:>050b}')
        print(f'e {expected:>050b}')
        print(f'd {z ^ expected:>050b}')
        print(x, y, z, x + y)
        changed_bits = []
        for i in range(50):
            pos = 50 - i - 1
            if pos < len(difference) and difference[pos] == '1':
                changed_bits.append(f'z{i:0>2}')
        all_bits = []
        for i in range(50):
            pos = 50 - i - 1
            all_bits.append(f'z{i:0>2}')
        # print(changed_bits)
        all_changes = {}

        tree={}
        for temp in inputs:
            tree[temp[3]] = (temp[0], temp[1], temp[2], temp[3])
        for changed_bit in all_bits:
            if not changed_bit in tree:
                break
            possibles = set()
            queue = [tree[changed_bit]]
            while len(queue) > 0:
                t = queue.pop()
                possibles.add(t)
                if t[0] in tree:
                    queue.append(tree[t[0]])
                if t[2] in tree:
                    queue.append(tree[t[2]])
            all_changes[changed_bit] = possibles

        all_intrsections = set()
        if len(changed_bits) > 0 :
            all_intrsections = all_changes[changed_bits[0]]
            for bit in all_changes:
                possibles = all_changes[bit]
                print(bit, len(possibles), possibles)
                all_intrsections = all_intrsections.intersection(possibles)

        for bit in all_changes:
            possibles = all_changes[bit]
            found = False
            for p in possibles:
                x = 'x' + bit[1:]
                y = 'y' + bit[1:]
                if p[1] == 'XOR':
                    if not((p[0] == x and p[1] == y) or (p[1] == y and p[0] ==x)):
                        found = True
            if not found:
                print(bit, len(possibles), possibles)

        last_match = all_changes["z00"]
        for bit in all_changes:
            possibles = all_changes[bit]
            print(bit, sorted(possibles.difference(last_match)))
            last_match = possibles



        # check = -1
        # for bit in all_changes:
        #     possibles = all_changes[bit]
        #     if len(possibles) != check:
        #         print(bit, check,  len(possibles), possibles)
        #     check += 4

            # for bit2 in all_changes:
            #     possibles2 = all_changes[bit2]
            #     inter = possibles2.intersection(possibles)
            #     print('I', bit, bit2, len(inter), inter )
            #     diff = possibles2.difference(possibles)
            #     print('D', bit, bit2, len(diff), diff )
        return all_intrsections

    def load_handler_part1(self, data: [str]) -> [str]:
        wires = {}
        inputs = []
        tree = {}
        line = 0
        while True:
            d = data[line]
            line += 1
            if d == '':
                break
            temp = d.split(": ")
            wires[temp[0]] = int(temp[1])

        while line < len(data):
            d = data[line]
            temp = d.split(' ')
            inputs.append((temp[0],temp[1], temp[2], temp[4]))
            tree[temp[4]] = (temp[0],temp[1], temp[2], temp[4])
            line += 1

        return wires, inputs, tree

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


if __name__ == '__main__':
    configure()
    aoc = Aoc202400()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
