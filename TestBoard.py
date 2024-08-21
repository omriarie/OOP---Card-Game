from unittest import TestCase

from Board import *
from Domino import *
from Exceptions import *

class TestBoard(TestCase):
    def test_in_left(self):
        b = Board(10)
        self.assertRaises(EmptyBoardException, b.in_left)
        d = Domino(1, 2)
        d2 = Domino(2, 1)
        b.add(d,True)
        self.assertEqual(b.in_left(), 1)
        b.add(d2, True)
        self.assertEqual(b.in_right(),1)
        b.add(d2, True)
        self.assertEqual(b.in_right(), 2)

    def test_in_right(self):
        b = Board(10)
        self.assertRaises(EmptyBoardException, b.in_right)
        d = Domino(1, 2)
        d2 = Domino(2, 1)
        b.add(d, True)
        b.add(d2, True)
        b.add(d2, True)
        self.assertEqual(b.in_right(), 2)
    def test_add(self):
        b = Board(10)
        d = Domino(1, 2)
        d2 = Domino(2, 1)
        b.add(d, True)
        b.add(d2, True)
        b.add(d2, True)
        b.add(d, False)
        b2 = Board(1)
        b2.add(d, True)
        self.assertRaises(FullBoardException, b2.add, d, False)
        b.add(d, False)
        d3 = Domino(5, 5)
        self.assertFalse(b.add(d3), False)

    def test_add_left(self):
        d = Domino(1, 2)
        b = Board(10)
        b.add(d)
        self.assertTrue(b.add_left(d), True)

    def test_add_right(self):
        d = Domino(1, 2)
        b = Board(10)
        b.add(d)
        self.assertTrue(b.add_right(d), True)

    def test_get_item(self):
        b = Board(10)
        self.assertEqual(b[1],None)
        d = Domino(1, 2)
        b.add(d)
        self.assertEqual(b[4], None)

    def test_eq(self):
        b = Board(10)
        b2 = Board(10)
        d = Domino(1, 2)
        b.add(d)
        b2.add(d)
        i = 1
        self.assertTrue(b == b2, True)
        self.assertFalse(b == i)

    def test_ne(self):
        b = Board(10)
        b2 = Board(10)
        d = Domino(1, 2)
        b.add(d)
        self.assertTrue(b != b2)

    def test_len(self):
        b = Board(10)
        d = Domino(1, 2)
        b.add(d)
        self.assertEqual(len(b),1)

    def test_contains(self):
        b = Board(10)
        d = Domino(1, 2)
        b.add(d)
        d2 = Domino(4, 5)
        self.assertTrue(d in b)
        self.assertFalse(d2 in b)