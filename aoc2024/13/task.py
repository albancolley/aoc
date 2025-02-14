"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure


class Aoc202413(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: []) -> int:
        result = 0
        tries = 100
        # print(data)
        for claw in data:
            button_a, button_b, target = claw
            a_x = button_a[0]
            a_y = button_a[1]
            b_x = button_b[0]
            b_y = button_b[1]
            t_x =  target[0]
            t_y =  target[1]
            x = 0
            y = 0
            for i in range(1, tries + 1):
                x += a_x
                y += a_y
                if (t_x - x) % b_x != 0:
                    continue
                if (t_y - y) % b_y != 0:
                    continue
                if int((t_x - x) / b_x) == int((t_y - y) / b_y):
                    price = 3 * i + int((t_x - x) / b_x)
                    result += price
                    break

        return result

    def calc_2(self, data: [str]) -> int:
        result = 0
        for claw in data:
            button_a, button_b, target = claw
            a_x = button_a[0]
            a_y = button_a[1]
            b_x = button_b[0]
            b_y = button_b[1]
            t_x = target[0]
            t_y = target[1]
            b_bottom = a_x*b_y - b_x*a_y
            b_top = a_x*t_y - t_x*a_y
            if b_top % b_bottom == 0:
                b_clicks = int(b_top / b_bottom)
                if (t_x -b_clicks*b_x) % a_x == 0 :
                    a_clicks = int((t_x - b_clicks * b_x) / a_x)
                    price = 3 * a_clicks + b_clicks
                    result += price

        return result



    def load_handler_part1(self, data: [str]) -> [str]:
        i = 0
        result = []
        while i < len(data):
            button_a = self.getButton(data[i])
            button_b = self.getButton(data[i+1])
            t = data[i+2].split(': X=')[1].split(", Y=")
            target = (int(t[0]), int(t[1]))
            result += [(button_a, button_b, target)]
            i+=4
        return result

    def getButton(self, ba):
        ba2 = ba.split(': X+')
        ba3 = ba2[1].split(", Y+")
        button_a = (int(ba3[0]), int(ba3[1]))
        return button_a

    def load_handler_part2(self, data: [str]) -> [str]:
        i = 0
        result = []
        while i < len(data):
            button_a = self.getButton(data[i])
            button_b = self.getButton(data[i + 1])
            t = data[i + 2].split(': X=')[1].split(", Y=")
            extra = 10000000000000
            target = (int(t[0]) + extra, int(t[1]) + extra)
            result += [(button_a, button_b, target)]
            i += 4
        return result


if __name__ == '__main__':
    configure()
    aoc = Aoc202413()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
