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

class DoublyLinkedCircularList:
    def __init__(self):
        """
        Create a new doubly linked list.
        Takes O(1) time.
        """
        self.curr = None


    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        curr = self.curr
        start = self.curr
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
            if curr == start:
                break
        return '[' + ', '.join(nodes) + ']'

    def to_list(self, start_from = None):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        curr = self.curr
        if start_from:
            curr = start_from
        start = curr
        while curr:
            nodes.append(curr.data)
            curr = curr.next
            if curr == start:
                break
        return nodes

    def insert(self, data):
        if self.curr:
            new_curr = DListNode(data=data, next=self.curr.next, prev=self.curr)
        else:
            new_curr = DListNode(data=data)
            new_curr.prev = new_curr
            new_curr.next = new_curr

        self.curr = new_curr
    #
    # def prepend(self, data):
    #     """
    #     Insert a new element at the beginning of the list.
    #     Takes O(1) time.
    #     """
    #     new_head = DListNode(data=data, next=self.head)
    #     if self.head:
    #         self.head.prev = new_head
    #     self.head = new_head
    #
    # def append(self, data):
    #     """
    #     Insert a new element at the end of the list.
    #     Takes O(n) time.
    #     """
    #     if not self.head:
    #         self.head = DListNode(data=data)
    #         return
    #     curr = self.head
    #     while curr.next:
    #         curr = curr.next
    #     curr.next = DListNode(data=data, prev=curr)

    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """
        curr = self.curr
        while curr and curr.data != key:
            curr = curr.next
        return curr  # Will be None if not found

    def remove_elem(self, node):
        """
        Unlink an element from the list.
        Takes O(1) time.
        """
        if node.next == node:
            self.curr = None
        else:
            self.curr = node.next

        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev



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

    def next(self, moves = 1):
        for i in range(moves):
            self.curr = self.curr.next

    def previous(self, moves = 1):
        for i in range(moves):
            self.curr = self.curr.prev


