from unittest import TestCase
from unittest.mock import *
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




class TestCollection(TestCase):

    @patch("Collection.Collection.__abstractmethods__", set())
    def test_get_collection(self):
        d = Domino(1,2)
        c = Collection([d])
        self.assertEqual(c.get_collection(),[d])

    @patch("Collection.Collection.__abstractmethods__", set())
    def test_getitem(self):
        d = Domino(1, 2)
        c = Collection([d])
        self.assertEqual(c.__getitem__(0),d)
        self.assertEqual(c.__getitem__(1), None)

    @patch("Collection.Collection.__abstractmethods__", set())
    def test_eq(self):
        d = Domino(1, 2)
        c = Collection([])
        c2 = Collection([])
        self.assertTrue(c == c2)
        self.assertFalse(c == 2)

    @patch("Collection.Collection.__abstractmethods__", set())
    def test_ne(self):
        d = Domino(1, 2)
        c = Collection([d])
        c2 = Collection([])
        self.assertTrue(c != c2)
        self.assertTrue(c != d)

    @patch("Collection.Collection.__abstractmethods__", set())
    def test_len(self):
        d = Domino(1, 2)
        c = Collection([d])
        self.assertEqual(len(c),1)

    @patch("Collection.Collection.__abstractmethods__", set())
    def test_cont(self):
        d = Domino(1, 2)
        c = Collection([d])
        self.assertIn(d, c.get_collection())
        self.assertTrue(d in c.get_collection())
        c2 = Collection([])
        self.assertFalse(d in c2.array,False)
        self.assertEqual(str(c.get_collection()), "[[1|2]]")

    @patch("Collection.Collection.__abstractmethods__", set())
    def test_str(self):
        d = Domino(1, 2)
        c = Collection([d])
        self.assertEqual(str(c),"[1|2]")

    @patch("Collection.Collection.__abstractmethods__", set())
    def test_repr(self):
        d = Domino(1, 2)
        c = Collection([d])
        self.assertEqual(c.__repr__(), "[1|2]")

    @patch("Collection.Collection.__abstractmethods__", set())
    def test_contains(self):
        d = Domino(1, 2)
        d2 = Domino(3, 4)
        c = Collection([d])
        self.assertTrue(d in c)
        self.assertFalse(d2 in c)