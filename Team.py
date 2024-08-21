import copy
"""
this class is going to represent a team of player 
"""
class Team:
    """
    this method will make an appirence of team, it will get a name for the team and a list of players.
    """
    def __init__(self, name, players):
        self.name = name
        self.__players = players
    """
    this founction will return a deep copy of the players list so it will not be changed 
    """
    def get_team(self):
        return copy.deepcopy(self.__players)
    """
    this founction will return a sum of all the team's players score
    """
    def score_team(self):
        temp = 0
        for player in self.__players:
            temp += player.score()
        return temp
    """
    this founction will return boolian answer if any of the teams players has dominos or not
    """
    def has_dominoes_team(self):
        return any([player.has_dominoes() for player in self.__players])

    """
    the founction will let every player try to play at the order they are in the list
    if they can play it will return true
    else it will return False
    """
    def play(self, board):
        for player in self.__players:
            if player.play(board) == True:
                return True
        return False
    """
    the founction will make a str that represent the team and add up to it the player's str
    """
    def __str__(self):### making fist string red also
        string = "Name: " + str(self.name) + ", Score team: " + str(self.score_team()) + ", Players:"
        for player in self.__players:
            string += f' {player}'
        return string
    """
    the founction will make a string out of a team so it could be printed
    """
    def __repr__(self):
        return str(self)
