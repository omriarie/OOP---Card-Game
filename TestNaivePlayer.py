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

class TestNaivePlayer(TestCase):

    def test_play(self):
        d = Domino(1, 2)
        d2 = Domino(2, 3)
        d3 = Domino(1, 1)
        h = Hand([d,d2, d3])
        b = Board(5)
        player = NaivePlayer("omri", 23,h)
        player.play(b)
        player.play(b)
        player.play(b)
        self.assertEqual(b.get_collection(), [d3, d, d2])
        self.assertFalse(player.play(b))

