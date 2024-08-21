from unittest import TestCase
from Collection import *
from Board import *
from Domino import *
from Exceptions import *
from Game import *
from Hand import *
from MaxScorePlayer import *
from NaivePlayer import *
from Player import *
from RandomPlayer import *

class TestHand(TestCase):

    def test_add(self):
        d = Domino(1,2)
        d2 = Domino(2,3)
        h = Hand([])
        h.add(d)
        h.add(d2,1)
        self.assertEqual(h.array,[d,d2])

    def test_remove_domino(self):
        d = Domino(1, 2)
        h = Hand([])
        h.add(d)
        h.remove_domino(d)
        h2 = Hand([])
        self.assertRaises(NoSuchDominoException, h2.remove_domino, d)

    def test_len(self):
        h = Hand([])
        self.assertEqual(len(h),0)

    def test_ne(self):
        d = Domino(1, 2)
        h = Hand([])
        h2 = Hand([])
        h2.add(d)
        self.assertTrue(h != h2,False)

    def test_getitem(self):
        d = Domino(1, 2)
        h = Hand([d])
        self.assertEqual(h.__getitem__(2), None)
        self.assertEqual(h.__getitem__(0), d)

    def test_eq(self):
        d = Domino(1, 2)
        d2 = Domino(2, 1)
        h = Hand([d])
        h2 = Hand([d2])
        self.assertEqual(h == h2,True)


    def test_cont(self):
        d = Domino(1, 2)
        d2 = Domino(4,5)
        h = Hand([d])
        self.assertTrue(d in h)
        self.assertFalse(d2 in h)