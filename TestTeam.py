from unittest import TestCase
import random

from Domino import Domino
from Board import Board
from Hand import Hand
from NaivePlayer import NaivePlayer
from Team import Team

class TestTeam(TestCase):
    def test_get_team(self):
        d = Domino(1, 1)
        h1 = Hand([d, d])
        p1 = NaivePlayer('player1', 20, h1)
        t1 = Team('team1', [p1])
        self.assertEqual(str(t1.get_team()),str([p1]))


    def test_score_team(self):
        d = Domino(1, 1)
        h1 = Hand([d, d])
        p1 = NaivePlayer('player1', 20, h1)
        t1 = Team('team1', [p1])
        self.assertEqual(t1.score_team(),4)

    def test_has_dominoes_team(self):
        d = Domino(1, 1)
        h1 = Hand([d, d])
        p1 = NaivePlayer('player1', 20, h1)
        t1 = Team('team1', [p1])
        self.assertTrue(t1.has_dominoes_team())
        h1 = Hand([])
        p1 = NaivePlayer('player1', 20, h1)
        t1 = Team('team1', [p1])
        self.assertFalse(t1.has_dominoes_team())

    def test_play(self):
        d = Domino(1, 1)
        h1 = Hand([d, d])
        p1 = NaivePlayer('player1', 20, h1)
        t1 = Team('team1', [p1])
        b = Board(1)
        self.assertTrue(t1.play(b))

    def test_str(self):
        d = Domino(1, 1)
        h1 = Hand([d, d])
        p1 = NaivePlayer('player1', 20, h1)
        t1 = Team('team1', [p1])
        self.assertEqual(str(t1),"Name: team1, Score team: 4, Players: Name: player1, Age: 20, Hand: [1|1][1|1], Score: 4")
