"""
AOC Day X
"""
import sys
from common import AocBase
from common import configure


class Aoc201600(AocBase):
    """
    AOC Day 10 Class
    """


    def check(self, last):
        for i in range(len(last)):
            tls = last[i:i+4]
            if len(tls) != 4:
                continue
            if tls[0] == tls[1]:
                continue
            if tls[0] == tls[3] and tls[1] == tls[2]:
                return True
        return False

    def calc_1(self, data: dict) -> int:
        result = 0
        for d in data:
            mode = True
            ok1 = False
            ok2 = True
            last = ""
            for c in d:
                if c == "[":
                    if self.check(last):
                        ok1 = True
                    last = ""
                if c == "]":
                    if self.check(last):
                        ok2 = False
                    last = ""

                last += c

            if self.check(last):
                if mode:
                    ok1 = True
                else:
                    ok2 = False

            if ok1 and ok2:
                result += 1

        return result


    def three_char_seq(self, last):
        result = []
        for i in range(len(last)):
            tls = last[i:i + 3]
            if len(tls) != 3:
                continue
            if tls[0] == tls[1]:
                continue
            if tls[0] == tls[2]:
                result += [tls]
        return result

    def calc_2(self, data: [str]) -> int:
        result = 0
        for d in data:
            aba_codes = []
            bab_codes = []
            last = ""
            for c in d:
                if c == "[":
                    aba_codes += self.three_char_seq(last)
                    last = ""
                if c == "]":
                    bab_codes += self.three_char_seq(last)
                    last = ""

                last += c

            if len(last) > 0:
                aba_codes += self.three_char_seq(last)

            for aba_code in aba_codes:
                if ''.join([aba_code[1], aba_code[0], aba_code[1]]) in bab_codes:
                    result += 1
                    break


        return result

    def load_handler_part1(self, data: [str]) -> [str]:
       return data

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)



if __name__ == '__main__':
    configure()
    aoc = Aoc201600()
    failed, results = aoc.run("part1_[0-2]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
