from unittest import TestCase

from linked_list import DoublyLinkedCircularList

class TestDoublyLinkedCircularList(TestCase):
    def test_insert(self):

        dl = DoublyLinkedCircularList()

        dl.insert(0)
        start = dl.curr
        dl.insert(1)
        dl.insert(2)
        dl.insert(3)

        print(dl)

        self.assertListEqual(dl.to_list(start), [0, 1, 2, 3])

        dl.remove_elem(dl.curr)

        self.assertListEqual(dl.to_list(start), [0, 1, 2])

        dl.remove_elem(dl.curr)
        self.assertListEqual(dl.to_list(dl.find(1)), [1, 2])

        dl.next()

        self.assertEqual(dl.curr, dl.find(2))

        dl.next()

        self.assertEqual(dl.curr, dl.find(1))


        dl.previous()
        self.assertEqual(dl.curr, dl.find(2))

        dl.previous(2)
        self.assertEqual(dl.curr, dl.find(2))
