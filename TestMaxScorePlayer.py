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

class TestMaxScorePlayer(TestCase):
    def test_play(self):
        d = Domino(1, 2)
        d2 = Domino(2, 3)
        d3 = Domino(1, 1)
        h = Hand([d, d2, d3])
        b = Board(5)
        player = MaxScorePlayer("omri", 23, h)
        player.play(b)
        player.play(b)
        player.play(b)
        self.assertEqual(b.get_collection(), [d3, d, d2])
        self.assertFalse(player.play(b))

    def test_str(self):
        d = Domino(1, 2)
        d2 = Domino(2, 3)
        d3 = Domino(1, 1)
        h = Hand([d, d2, d3])
        b = Board(5)
        player = MaxScorePlayer("omri", 23, h)
        self.assertEqual(str(player),"Name: omri, Age: 23, Hand: [1|2][2|3][1|1], Score: 10, I can win the game!")
