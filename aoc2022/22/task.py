import dataclasses
import os.path
import string

import numpy as np

from aoc2022.common.aocbase import AocBase
from aoc2022.common.setup import configure
import logging
from dataclasses import dataclass
import re
from collections import deque

logger = logging.getLogger("ACO2022-17")

class Aoc202212(AocBase):

    directions = {
        'R' : (0,1),
        'L': (0,-1),
        'U': (-1, 0),
        'D': (1, 0)
    }

    points = {
        'R': 0,
        'L': 2,
        'U': 3,
        'D': 1
    }

    anticlockwise = {
        'U': 'L',
        'L': 'D',
        'D': 'R',
        'R': 'U',
    }
    clockwise = {
        'U': 'R',
        'R': 'D',
        'D': 'L',
        'L': 'U',
    }

    def calc_1(self, data) -> int:
        board, instructions, width, height = data
        for i in range(0, width):
            if board[1, i] == 1:
                break
        position = (1, i)
        facing = 'R'
        for instruction in instructions:
            for i in range(0, instruction[0]):
                position =self.move(position, facing, board)
            if instruction[1] == 'R':
                facing = self.clockwise[facing]
            elif instruction[1] == 'L':
                facing = self.anticlockwise[facing]

        return 1000*position[0] + 4 * position[1] + self.points[facing]

    def move(self, position, facing, board):
        direction = self.directions[facing]
        height = board.shape[0]
        width = board.shape[1]
        next_position = (position[0] + direction[0], position[1] + direction[1])
        x, y = next_position
        if board[x, y] == 0:
            match facing:
                case 'R':
                    for i in range(y-1, -1, -1):
                        if board[x, i] == 0:
                            y = i + 1
                            break
                case 'L':
                    for i in range(y+1, width + 1):
                        if board[x, i] == 0:
                            y = i - 1
                            break
                case 'U':
                    for i in range(x+1, height + 1):
                        if board[i, y] == 0:
                            x = i - 1
                            break
                case 'D':
                    for i in range(x-1, -1, -1):
                        if board[i, y] == 0:
                            x = i + 1
                            break
        if board[x, y] == 2:
            return position
        else:
            return (x , y)

    def next_position(self, position, facing, side_width):
        x, y = position
        x_new = x
        y_new = y
        new_facing = facing
        if facing == 'U' and 2*side_width < x <= 3*side_width and y == 1:  # 1 top to 2 top
            #Working
            x_new = side_width - (x - (2*side_width)) + 1
            y_new = side_width + 1
            new_facing = 'D'
            # print("1-2", x, y, x_new, y_new, facing, new_facing)
        elif facing == 'L' and x == 2*side_width + 1 and 0 < y <= side_width :  # 1 left to 3 top
            x_new = side_width + y
            y_new = side_width + 1
            new_facing = 'D'
            # print("1-3", x, y, x_new, y_new, facing, new_facing)
        elif facing == 'R' and x == 3 * side_width and 0 < y <= side_width:  # 1 right to 6 right
            x_new = 4 * side_width
            y_new = (side_width - y) + 2*side_width + 1
            new_facing = 'L'
            # print("1-6", x, y, x_new, y_new, facing, new_facing)

        elif facing == 'U' and 0 < x <= side_width and y == side_width + 1:  # 2 top to 1 top
            # Working
            x_new = (side_width - x) + 1 + 2*side_width
            y_new = 1
            new_facing = 'D'
            # print("2-1", x, y, x_new, y_new, facing, new_facing)
        elif facing == 'L' and x == 1 and side_width < y <= side_width*2:  # 2 left to 6 bottom
            x_new = (side_width-(y - side_width )) + 3*side_width + 1
            y_new = side_width * 3
            new_facing = 'U'
            # print("2-6", x, y, x_new, y_new, facing, new_facing)
        elif facing == 'D' and 0 < x <= side_width and y == 2 * side_width:  # 2 bottom to 5 bottom
            x_new = (side_width - x) + 2 * side_width +1
            y_new = side_width * 3
            new_facing = 'U'
            # print("2-5", x, y, x_new, y_new, facing, new_facing)

        elif facing == 'U' and side_width < x <= side_width*2 and y == side_width + 1:  # 3 top to 1 left
            # working
            x_new = side_width * 2 + 1
            y_new = x - side_width
            new_facing = 'R'
            # print("3-1", x, y, x_new, y_new, facing, new_facing)
        elif facing == 'D' and side_width < x <= side_width*2 and y == 2 * side_width:  # 3 bottom to 5 left
            x_new = side_width * 2 + 1
            y_new = (2 * side_width - x) + 2*side_width + 1
            new_facing = 'R'
            # print("3-5", x, y, x_new, y_new, facing, new_facing)

        elif facing == 'R' and x == side_width * 3 and side_width < y <= side_width*2:  # 4 right to 6 top
            # Working
            x_new = 5 * side_width - y + 1
            y_new = 2 * side_width + 1
            new_facing = 'D'
            # print("4-6", x, y, x_new, y_new, facing, new_facing)

        elif facing == 'L' and x == side_width * 2 + 1 and 2*side_width < y <= 3*side_width:  # 5 left to 3 bottom
            x_new = (3*side_width - y) + side_width + 1
            y_new = 2 * side_width
            new_facing = 'U'
            # print("5-3", x, y, x_new, y_new, facing, new_facing)
        elif facing == 'D' and 2*side_width < x <= 3*side_width and y == side_width * 3:  # 5 bottom to 2 bottom
            # working
            x_new = side_width - (x - 2*side_width) + 1
            y_new = 2 * side_width
            new_facing = 'U'
            # print("5-2", x, y, x_new, y_new, facing, new_facing)

        elif facing == 'U' and 3*side_width < x <= 4*side_width and y == side_width * 2 + 1:  # 6 top to 4 right
            x_new = 3 * side_width
            y_new = (side_width - (x - 3*side_width)) + side_width + 1
            new_facing = 'L'
            # print("6-4", x, y, x_new, y_new, facing, new_facing)
        elif facing == 'R' and x == 4*side_width and side_width*2 < y <= side_width*3:  # 6 right to 1 left
            x_new = 3 * side_width
            y_new = (side_width - (y - 2* side_width)) + 1
            new_facing = 'L'
            # print("6-1", x, y, x_new, y_new, facing, new_facing)
        elif facing == 'D' and 3*side_width < x <= 4*side_width and y == side_width * 3:  # 6 bottom to 2 right
            x_new = 1
            y_new = (side_width -(x - 3*side_width)) + side_width + 1
            new_facing = 'R'
            # print("6-2", x, y, x_new, y_new, facing, new_facing)
        else:
            direction = self.directions[new_facing]
            x_new = x + direction[1]
            y_new = y + direction[0]

        next_position = (int(x_new), int(y_new))
        return next_position, new_facing


    def move2(self, position, facing, board):
        # direction = self.directions[facing]
        height = board.shape[0]
        width = board.shape[1]
        next_position, new_facing = self.next_position(position, facing, (width -2) / 4)
        x, y = next_position
        if board[y, x][0] == 0:
            match facing:
                case 'R':
                    for i in range(y-1, -1, -1):
                        if board[i, x][0] == 0:
                            y = i + 1
                            break
                case 'L':
                    for i in range(y+1, width + 1):
                        if board[i, x][0] == 0:
                            y = i - 1
                            break
                case 'U':
                    for i in range(x+1, height + 1):
                        if board[y,i][0]==0:
                            x = i - 1
                            break
                case 'D':
                    for i in range(x-1, -1, -1):
                        if board[y,i][0] == 0:
                            x = i + 1
                            break
        if board[y, x][0] == 2:
            return position, facing
        else:
            return (x , y), new_facing


    def calc_2(self, data: []) -> int:
        board, instructions, width, height, start, facing = data
        position = start
        facing = facing
        for instruction in instructions:
            # print(position, facing)
            # print(instruction)
            for i in range(0, instruction[0]):
                position, facing = self.move2(position, facing, board)
            if instruction[1] == 'R':
                facing = self.clockwise[facing]
            elif instruction[1] == 'L':
                facing = self.anticlockwise[facing]
        _, x, y = board[position[1], position[0]]
        # return 1000 * x + 4 * y + self.points[facing]
        if width > 100:
            # hack to rotate facing back
            facing = self.clockwise[facing]
        result = int(1000 * x + 4 * y + self.points[facing])
        return result
        # 169, 116, R

    def load_handler_part1(self, data: [(int, int)]) -> {}:

        result = []
        width = 0
        height = 0
        for row in data:
            if len(row) == 0:
                break
            width = max(len(row), width)
            height += 1
        board = np.zeros((width + 2) * (height + 2))
        pos = width + 3
        for x in range(0, height):
            row = data[x]
            for y in range(0, width):
                if y < len(row):
                    match row[y]:
                        case '.':
                            board[pos] = 1
                        case '#':
                            board[pos] = 2
                pos = pos + 1
            pos += 2
        board = board.reshape(height+ 2, width + 2)
        instruction_info = data[height+1]
        next_instruction = ''
        instructions = []
        for c in instruction_info:
            if c.isnumeric():
                next_instruction += c
            else:
                instructions.append((int(next_instruction), c))
                next_instruction = ''
        instructions.append((int(next_instruction), ''))
        return board, instructions, width+2, height+2

    def load_handler_part2(self, data: [str]) -> [str]:
        width = 0
        height = 0
        for row in data:
            if len(row) == 0:
                break
            width = max(len(row), width)
            height += 1
        board = np.zeros((width + 2) * (height + 2), dtype=[('tile', 'i4'), ('x', 'i4'), ('u', 'i4')])
        pos = width + 3
        start = None
        for x in range(0, height):
            row = data[x]
            for y in range(0, width):
                if y < len(row):
                    match row[y]:
                        case '.':
                            if not start:
                                start = (y+1, x+1)
                            board[pos] = (1, x+1, y+1)
                        case '#':
                            board[pos] = (2, x+1, y+1)
                pos = pos + 1
            pos += 2
        board = board.reshape(height + 2, width + 2)
        instruction_info = data[height + 1]
        next_instruction = ''
        instructions = []
        for c in instruction_info:
            if c.isnumeric():
                next_instruction += c
            else:
                instructions.append((int(next_instruction), c))
                next_instruction = ''
        instructions.append((int(next_instruction), ''))

        # return board, instructions, width, height, start, 'R'

        facing = 'R'
        new_board = board.copy()
        if width > 100:
            # hack to rotate to example cube layout
            new_board = np.rot90(new_board)
            top_corner = new_board[1:51,1:51]
            top_corner2 = np.rot90(top_corner,2)
            new_board[1:51, 101:151] = top_corner2
            new_board[1:51, 1:51] = 0
            start = (100, 1)
            facing = 'U'
        return new_board, instructions, width, height, start, facing

    def load_handler_part2a(self, data: [str]) -> [str]:
        cube = np.zeros((4, 4, 4))
        print(cube[:,:,0])
        sides = np.array([4, 4, 4])
        data2 = np.ones(sides)
        for i in range(0,4):
            cube[..., 0] = i
            cube = np.rot90(cube, 1)
        return None

if __name__ == '__main__':

    configure()
    aoc = Aoc202212()
    failed, results = aoc.run("part1_[1-2]+.txt", "part2_[1-2]+.txt")
    if failed:
        exit(1)
