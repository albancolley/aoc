"""
AOC Day X
"""
import sys

from common import AocBase
from common import configure


class DListNode:
    """
    A node in a doubly-linked list.
    """
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
        if prev:
            prev.next = self
        if next:
            next.prev = self


    def __repr__(self):
        return repr(self.data)


class DoublyLinkedList:
    def __init__(self):
        """
        Create a new doubly linked list.
        Takes O(1) time.
        """
        self.head = None

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'

    def prepend(self, data):
        """
        Insert a new element at the beginning of the list.
        Takes O(1) time.
        """
        new_head = DListNode(data=data, next=self.head)
        if self.head:
            self.head.prev = new_head
        self.head = new_head

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        if not self.head:
            self.head = DListNode(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = DListNode(data=data, prev=curr)

    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr  # Will be None if not found

    def remove_elem(self, node):
        """
        Unlink an element from the list.
        Takes O(1) time.
        """
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node is self.head:
            self.head = node.next
        node.prev = None
        node.next = None

    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        elem = self.find(key)
        if not elem:
            return
        self.remove_elem(elem)

    def reverse(self):
        """
        Reverse the list in-place.
        Takes O(n) time.
        """
        curr = self.head
        prev_node = None
        while curr:
            prev_node = curr.prev
            curr.prev = curr.next
            curr.next = prev_node
            curr = curr.prev
        self.head = prev_node.prev

class Aoc202409(AocBase):
    """
    AOC Day 10 Class
    """
    def calc_1(self, data: [int]) -> int:
        result = 0
        disk = {}
        pos = 0
        file_id = 0
        for i in range(0, len(data),2):
            value = data[i]
            for x in range(value):
                disk[pos] = file_id
                pos += 1
            file_id += 1
            if i+1 < len(data):
                number_of_blanks = data[i+1]
                pos += number_of_blanks

        # self.print_disk(disk, pos)

        clean_disk = {}
        start = 0
        end = pos
        pos = 0
        while start <= end:
            while start in disk and start <=end:
                clean_disk[pos] = disk[start]
                start += 1
                pos += 1
            while start not in disk:
                while end not in disk:
                    end -= 1
                clean_disk[pos] = disk[end]
                pos += 1
                end -= 1
                start += 1

        # self.print_disk(clean_disk, pos)

        for i in range(len(clean_disk)):
            result += i * clean_disk[i]

        return result

# 0099811188827773336446555566
# 0099811188827773336446555566

    def print_disk(self, disk, pos):
        line = ""
        for i in range(pos):
            if i in disk:
                line += str(disk[i])
            else:
                line += "."
        print(line)

    def calc_2(self, data: DoublyLinkedList) -> int:

        # self.print_line(data)

        end_pos:DListNode  = data.head
        while end_pos.next:
            end_pos:DListNode  = end_pos.next

        # self.print_line(data)

        while end_pos:
            # print(data)
            # print(f'end_pos:{end_pos}')
            while end_pos and end_pos.data[1] == -1:
                end_pos = end_pos.prev

            if not end_pos:
                break

            start_pos: DListNode = data.head
            while start_pos != end_pos:
                if start_pos.data[1] == -1 and start_pos.data[0] >= end_pos.data[0]:
                    break
                start_pos = start_pos.next

            if start_pos != end_pos:
                if start_pos.data[0] > end_pos.data[0]:
                    blanks: DListNode = DListNode((start_pos.data[0] - end_pos.data[0], -1))
                    blanks.prev = start_pos
                    blanks.next = start_pos.next
                    start_pos.next = blanks
                    blanks.next.prev = blanks
                start_pos.data = end_pos.data
                end_pos.data = (end_pos.data[0], -1)

            end_pos = end_pos.prev

        # self.print_line(data)

        node: DListNode = data.head
        result = 0
        pos = 0
        while node:
            for i in range(node.data[0]):
                if node.data[1] != -1:
                    result += pos * node.data[1]
                pos += 1
            node = node.next

        return result

    def print_line(self, data):
        node: DListNode = data.head
        line = ""
        while node:
            if node.data[1] != -1:
                line += str(node.data[1]) * node.data[0]
            else:
                line += "." * node.data[0]
            node = node.next
        print(line)

    def load_handler_part1(self, data: [str]) -> [str]:
       return [int(d) for d in data[0]]

    def load_handler_part2(self, data: [str]) -> [str]:
        result = DoublyLinkedList()
        line = [int(d) for d in data[0]]
        file_id = int(len(line) / 2)
        for i in range(len(line) -1, -1, -1):
            if i % 2 == 0:
                result.prepend((line[i], file_id))
                file_id -= 1
            else:
                result.prepend((line[i], -1))
        return result




if __name__ == '__main__':
    configure()
    aoc = Aoc202409()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
