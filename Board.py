from Exceptions import EmptyBoardException, InvalidNumberException
from Exceptions import FullBoardException
from Collection import *

"""
the class will inherit from class collection,
this class will contain maximum capasity variable with is between 1-28
and a collection varible that will contain a domino array but at the biggining will be empty
"""

class Board(Collection):
    """
    the init will make a appirance of board with correct value of max_capacity
    and make an empty list of domino
    """
    def __init__(self, max_capacity):
        if not 1 <= max_capacity <= 28:
            raise InvalidNumberException("value must be between 1 and 28!")
        self.max_capacity = max_capacity
        super(Board, self).__init__(array=[])

    """
    the founction will send the left number on the left tile on the board
    """
    def in_left(self):
        if len(self.array) == 0:
            raise EmptyBoardException("the board is empty!")
        return self[0].get_left()

    """
        the founction will send the right number on the right tile on the board
    """
    def in_right(self):
        if len(self.array) == 0:
            raise EmptyBoardException("the board is empty!")
        return self[len(self.array) - 1].get_right()

    """
        the founction will first check if the board is full or not, then if its empty it will add the tile 
        then if its niether then according to the boolian varible it will try to add to the right side of the board.
        if it doesnt match then it will try to add the fliped domino, at the end it will send boolian answer if it worked or not.
    """
    def add(self, domino, add_to_right=True):
        if len(self.array) == self.max_capacity:
            raise FullBoardException("the board is full!")
        if len(self.array) == 0:
            self.array.append(domino)
            return True
        flipped = domino.flip()
        if add_to_right:
            if self.in_right() == domino.get_left():
                self.array.append(domino)
                return True
            elif self.in_right() == flipped.get_left():
                self.array.append(flipped)
                return True
        else:
            if self.in_left() == domino.get_right():
                self.array.insert(0, domino)
                return True
            elif self.in_left() == flipped.get_right():
                self.array.insert(0, flipped)
                return True
        return False

    """
        the founction will try to add to left with the founction "add" by sending the correct varibles
        sends the boolian answer of add
        """
    def add_left(self, domino):
        return self.add(domino, add_to_right=False)

    """
        the founction will try to add to right with the founction "add" by sending the correct varibles
        sends the boolian answer of add
    """
    def add_right(self, domino):
        return self.add(domino, add_to_right=True)

    """
        the founction will check if the board contains a tile or not, returns a 
    """
    def __contains__(self, key):
        for i in self.array:
            if i == key:
                return True
        return False

    """
    the founction will check if tow boards are equal acording to the dimndes 

    """

    def __eq__(self, other):
        if not type(self) == type(other):
            return False
        if self.max_capacity == other.max_capacity and len(self.array) == len(other.array):
            for i in range(0, len(self.array)):
                if (self.array[i].get_left() != other.array[i].get_left() or (
                        self.array[i].get_right() != other.array[i].get_right())):
                    return False
            return True
        return False
    """
    the founction will check if tow boards are not equal acording to their array
    """
    def __ne__(self, other):
        if not type(self) == type(other):
            return False
        return not self == other
    """
    the founction will send the len of the board array 
    """
    def __len__(self):
        return len(self.array)
