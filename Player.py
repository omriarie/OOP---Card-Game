from abc import ABC,abstractmethod

"""
this class is going to represent the base of all the players and will contain their basic methods.

"""

class Player(ABC):

    """
    this founction will make an appirance of Player with his age name and hand of tiles
    """

    def __init__(self, name, age, hand):
        self.name = name
        self.age = age
        self.hand = hand
    """
    this founction will sum up all of the dominos value and return it
    """
    def score(self):
        temp = 0
        for index in range(len(self.hand)):
            temp += self.hand[index].get_left() + self.hand[index].get_right()
        return temp
    """
    this founction will check if there are dominos in the players hand or not
    and return a boolian value 
    """
    def has_dominoes(self):
        return len(self.hand) > 0
    """
    this founction will not be implemented in here, if user will try runing it it will raise an error
    """

    @abstractmethod
    def play(self, board):
        pass

    """
    this founction will return a string that is going to represent the player
    """
    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, Hand: {self.hand}, Score: {self.score()}'
    """
    the founction will return a string of the player so it could be printed.
    """
    def __repr__(self):
        return str(self)
