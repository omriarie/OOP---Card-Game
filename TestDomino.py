from unittest import TestCase

from Domino import *
from Exceptions import *


class TestDomino(TestCase):
    def test_get_left(self):
        d = Domino(1, 2)
        self.assertEqual(d.get_left(),1)

    def test_get_right(self):
        d = Domino(1, 2)
        self.assertEqual(d.get_right(), 2)

    def test_flip(self):
        d = Domino(1, 2)
        d2 = Domino(2, 1)
        self.assertEqual(d.flip(),d2)

    def test_str(self):
        d = Domino(1, 2)
        self.assertEqual(str(d),"[1|2]")

    def test_repe(self):
        d = Domino(1, 2)
        self.assertEqual(d.__repr__(), "[1|2]")

    def test_ne(self):
        d = Domino(1, 2)
        d2 = Domino(5,6)
        self.assertTrue(d != d2)

    def test_gt(self):
        d = Domino(1, 2)
        d2 = Domino(5, 6)
        self.assertFalse(d > d2,False)
        self.assertTrue(d2 > d)
        self.assertRaises(InvalidNumberException, Domino,8,5)
        self.assertFalse(d > 5, False)

    def test_eq(self):
        d = Domino(1, 2)
        self.assertFalse(d == 5, False)

    def test_contains(self):
        d = Domino(1, 2)
        self.assertFalse(3 in d)
        self.assertTrue(1 in d)
