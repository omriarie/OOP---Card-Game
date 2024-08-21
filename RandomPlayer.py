import random
import copy
from Player import Player

"""
this class is a player with sertent way of playing
"""
class RandomPlayer(Player):
    """
    this class will inherit all of her fathers methods and will implement only her play method
    """

    """
    the founction will try to make a play by a copy of the original hand after shuffeling it.
    it will make a copy, shuffle it and try to play with the shuffled hand, when it can add to the board it will remove from the original hand the tile
    that has been played
    """
    def play(self, board):
        # Don't change this line and don't move it!
        random.seed(12)  # You can read about seed here: https://en.wikipedia.org/wiki/Random_seed
        temp = copy.deepcopy(self.hand.array)
        random.shuffle(temp)
        for domino in temp:
            if (board.add_right(domino) == True):
                self.hand.remove_domino(domino)
                return True
            if (board.add_left(domino) == True):
                self.hand.remove_domino(domino)
                return True
        return False
