"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure


class Aoc201900(AocBase):
    """
    AOC Day 10 Class
    """

    direction = {'>': complex(1, 0), '<': complex(-1, 0), '^': complex(0, -1), 'v': complex(0, 1),
                 complex(1, 0): '>', complex(-1, 0): '<', complex(0, -1): '^', complex(0, 1): 'v'}

    turns = {
        complex(1, 0): {'S': complex(1, 0), 'L': complex(0, -1), 'R': complex(0, 1), '\\': complex(0, 1), '/': complex(0, -1) },
        complex(-1, 0): {'S': complex(-1, 0), 'L': complex(0, 1), 'R': complex(0, -1), '\\': complex(0, -1), '/': complex(0, 1)},
        complex(0, 1): {'S': complex(0, 1), 'L': complex(1, 0), 'R': complex(-1, 0), '\\': complex(1, 0), '/': complex(-1, 0) },
        complex(0, -1): {'S': complex(0, -1), 'L': complex(-1, 0), 'R': complex(1, 0), '\\': complex(-1, 0), '/': complex(1, 0)},
        'S':'R','R':'L', 'L':'S'
    }

    def calc_1(self, data: dict) -> int:
        result = 0
        mine, carts = data
        # self.draw_mine(mine, carts)
        cart:complex = 0 + 0j
        while True:
            new_carts = {}
            odered_carts =  sorted(carts.keys(), key = lambda x: (x.real, x.imag))
            for cart in odered_carts:
                direction = carts[cart][0]
                turn = carts[cart][1]
                cart += carts[cart][0]
                if cart in new_carts:
                    return f'{int(cart.real)},{int(cart.imag)}'
                match (mine[cart]):
                    case '+':
                        direction = self.turns[direction][turn]
                        turn = self.turns[turn]
                    case '-':
                        pass
                    case '|':
                        pass
                    case _:
                        direction = self.turns[direction][mine[cart]]

                new_carts[cart] = (direction, turn )
            carts = new_carts
            # self.draw_mine(mine, carts)

    def calc_2(self, data: [str]) -> int:
        result = 0
        mine, carts = data
        # self.draw_mine(mine, carts)
        cart:complex = 0 + 0j
        while True:
            new_carts = {}
            ordered_carts =  sorted(carts.keys(), key = lambda x: (x.real, x.imag))
            for cart in ordered_carts:
                if cart not in carts:
                    continue

                current_cart = carts.pop(cart)

                direction = current_cart[0]
                turn = current_cart[1]
                cart += current_cart[0]
                if cart in carts :
                    carts.pop(cart)
                    continue
                match (mine[cart]):
                    case '+':
                        direction = self.turns[direction][turn]
                        turn = self.turns[turn]
                    case '-':
                        pass
                    case '|':
                        pass
                    case _:
                        direction = self.turns[direction][mine[cart]]

                carts[cart] = (direction, turn )
            if len(carts) == 1:
                cart = list(carts.keys())[0]
                return f'{int(cart.real)},{int(cart.imag)}'
            # self.draw_mine(mine, carts)




    def load_handler_part1(self, data: [str]) -> tuple[dict, dict]:
        mapping = {'>':'-', '<':'-', '^':'|', 'v':'|'}

        mine = {}
        y = 0
        carts ={}
        for row in data:
            x = 0
            for c in row:
                if c in mapping:
                    carts[complex(x,y)] = (self.direction[c], 'L')
                    c = mapping[c]
                mine[complex(x,y)] = c
                x+=1
            y += 1

        return mine, carts


    def load_handler_part2(self, data: [str]) -> tuple[dict, dict]:
        return self.load_handler_part1(data)

    def draw_mine(self, mine, carts ):
        pos = 0 + 0j
        line = ""
        while pos in mine:
            c = mine[pos]
            if pos in carts:
                line += self.direction[carts[pos][0]]
            else:
                line += c
            pos += 1
            if pos not in mine:
                print(line)
                line = ""
                pos = complex(0,int(pos.imag) +1)





if __name__ == '__main__':
    configure()
    aoc = Aoc201900()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-2]+.txt")
    if failed:
        sys.exit(1)
