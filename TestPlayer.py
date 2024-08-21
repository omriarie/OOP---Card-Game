from unittest import TestCase
import random
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
from Domino import Domino
from Exceptions import InvalidNumberException, FullBoardException
from Board import Board
from Game import Game
from Hand import Hand
from NaivePlayer import NaivePlayer
from Team import Team
from unittest.mock import *

class TestPlayer(TestCase):

    @patch("Player.Player.__abstractmethods__", set())
    def test_score(self):
        d = Domino(1,1)
        h = Hand([d])
        p = Player("omri", 23, h)
        self.assertEqual(p.score(),2)

    @patch("Player.Player.__abstractmethods__", set())
    def test_has_dominoes(self):
        h = Hand([])
        p = Player("omri", 23, h)
        self.assertFalse(p.has_dominoes())

    @patch("Player.Player.__abstractmethods__", set())
    def test_str(self):
        h = Hand([])
        p = Player("omri", 23, h)
        self.assertEqual(str(p),"Name: omri, Age: 23, Hand: , Score: 0")

