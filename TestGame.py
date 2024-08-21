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


class TestGame(TestCase):

    def test_play(self):
        d = Domino(1, 1)
        h1 = Hand([d, d])
        p1 = NaivePlayer('player1', 20, h1)
        t1 = Team('team1', [p1])

        h2 = Hand([d, d, d])
        p2 = MaxScorePlayer('player2', 20, h2)
        t2 = Team('team1', [p2])

        b = Board(10)

        g = Game(b, t1, t2)
        # t1 has only 2 domino, and t2 has 3 dominos, so t1 will win
        self.assertEqual(g.play(), f'Team {t1.name} wins Team {t2.name}')


        h1 = Hand([d, d])
        p1 = NaivePlayer('player1', 20, h1)
        t1 = Team('team1', [p1])

        h2 = Hand([d, d, d])
        p2 = MaxScorePlayer('player2', 20, h2)
        t2 = Team('team1', [p2])
        b = Board(3)
        g = Game(b, t1, t2)
        self.assertEqual(g.play(), f'Team {t1.name} wins Team {t2.name}')

        h1 = Hand([d, d])
        p1 = NaivePlayer('player1', 20, h1)
        t1 = Team('team1', [p1])

        h2 = Hand([d, d])
        p2 = MaxScorePlayer('player2', 20, h2)
        t2 = Team('team1', [p2])
        b = Board(2)
        g = Game(b, t1, t2)
        self.assertEqual(g.play(), f'Draw!')

        h1 = Hand([d, d])
        p1 = NaivePlayer('player1', 20, h1)
        t1 = Team('team1', [p1])

        h2 = Hand([d])
        p2 = MaxScorePlayer('player2', 20, h2)
        t2 = Team('team1', [p2])
        b = Board(10)
        g = Game(b, t1, t2)
        self.assertEqual(g.play(), f'Team {t2.name} wins Team {t1.name}')


