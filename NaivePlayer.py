from Player import Player

"""
this class is a player with sertent way of playing
"""
class NaivePlayer(Player):
    """
    the class will inherit all of her methods from Player and will make only the play method
    """

    """
    the method will try to play by the order od her tiles in her hand
    if it works then it will return true
    after going all over his hand and none of the card are matchong it will return False
    """
    def play(self, board):
        for domino in self.hand.array:
            if (board.add_right(domino) == True):
                self.hand.remove_domino(domino)
                return True
            if (board.add_left(domino) == True):
                self.hand.remove_domino(domino)
                return True
        return False
