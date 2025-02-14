"""
AOC Day X
"""
import sys
from collections import Counter

from common import AocBase
from common import configure


class Aoc201905(AocBase):
    """
    AOC Day 10 Class
    """

    def calc_1(self, data: str) -> int:
        ll = DoublyLinkedList()
        for d in reversed(data):
            ll.prepend(d)

        removed = 0
        while True:
            match:bool = False
            cur: DListNode = ll.head
            while cur.next:
                first = cur.data
                second = cur.next.data
                new_cur = cur.next
                if first.upper() == second.upper() and first != second:
                    new_cur = cur.next.next
                    ll.remove_elem(cur.next)
                    ll.remove_elem(cur)
                    removed += 2
                    match = True
                cur = new_cur
                if cur is None:
                    break
            if not match:
                return len(data) - removed

        # data = np.array(data)
        # while True:
        #     match:bool = False
        #     for i in range(len(data)-1):
        #         cur:str = data[i]
        #         cur1:str = data[i+1]
        #         if cur.upper() == cur1.upper() and cur != cur1:
        #             del data[i]
        #             del data[i]
        #             match = True
        #             break
        #     if not match:
        #         return len(data)


    def calc_2(self, data: str) -> int:
        c = Counter(data.upper())
        totals = []
        for k in c.keys():
            totals.append(self.calc_1(data.replace(k, ''). replace(k.lower(),'')))
        total = min(totals)
        return total

    def load_handler_part1(self, data: [str]) -> [str]:
       return data[0]

    def load_handler_part2(self, data: [str]) -> [str]:
        return self.load_handler_part1(data)


class DListNode:
    """
    A node in a doubly-linked list.
    """
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

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

if __name__ == '__main__':
    configure()
    aoc = Aoc201905()
    failed, results = aoc.run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed:
        sys.exit(1)
