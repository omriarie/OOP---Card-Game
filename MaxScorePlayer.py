import copy
from Player import Player

"""
this class is a player with sertent way of playing
"""
class MaxScorePlayer(Player):
    """
    this class will inherit her methods from her father except from play, str and repr
    """

    """
    the founction will make a deep copy of the players hand, sort if by value of Dominos 
    and check if the dominos can be played by order, if it finds a domino that it can play with then it will remove it
    from the original hand and return True
    if it cant play with the original domino it will try flipping it and try again.
    """
    def play(self, board):### check if sort is working here
        temp = copy.deepcopy(self.hand.array)
        temp.sort(reverse=True)
        for domino in temp:
            if (board.add_right(domino) == True):
                self.hand.remove_domino(domino)
                return True
            if (board.add_left(domino) == True):
                self.hand.remove_domino(domino)
                return True
        return False
    """
    the founction will return a string that is representing the Max Score Player
    """
    def __str__(self):
        return f"{super().__str__()}, I can win the game!"
    """
    the founction will return a string of the player so i can be printed
    """
    def __repr__(self):
        return str(self)
