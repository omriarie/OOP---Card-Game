from copy import deepcopy
from Exceptions import InvalidNumberException

"""
this class is going to represent a tile of domino in the game
"""
class Domino:
    """
    the founction will make an appirance of the class Domino, placing the varibles of right and left in thier places.
    checking if the values of the varibles are according to the dimends
    """
    def __init__(self, left, right):

        if (0 <= left <= 6 and 0 <= right <= 6):  ##### check if parivate or not
            self.__left = left
            self.__right = right
        else:
            raise InvalidNumberException('numbers can be only between 0 and 6')
    """
    the founction will return the value of the left side of the domino
    """
    def get_left(self):
        return deepcopy(self.__left)
    """
    the founction will return the right value of the domino
    """
    def get_right(self):
        return deepcopy(self.__right)
    """
    the founction will make an str of the domino and its values according to the dimends
    """
    def __str__(self):
        return '[' + str(self.__left) + '|' + str(self.__right) + ']'
    """
    the founction will return a string of the domino so it could be printed
    """
    def __repr__(self):
        a = str(self)
        return a
    """
    the founction will return a boolian answer if the tow dominos are the same or not.
    """
    def __eq__(self, other):
        if not type(other) == Domino:
            return False
        return (self.__left == other.get_left() and self.__right == other.get_right()) or (self.__left == other.get_right() and self.__right == other.get_left())
    """
    the founction will return a boolian aswer if tow dominos are not alike
    """
    def __ne__(self, other):
        if not type(other) == Domino:
            return False
        return not self == other
    """
    the founction will return a boolian answer if the domino value is bigger then the other or not
    """
    def __gt__(self, other):
        if not type(other) == Domino:
            return False
        temp_self = self.__left + self.__right
        temp_other = other.get_left() + other.get_right()
        if (temp_self > temp_other):
            return True
        return False
    """
    the founction will check if the key is in the board array or not, returns a boolian answer
    """
    def __contains__(self, key):
        if (self.__right == key or self.__left == key):
            return True
        return False
    """
    the founction will make a domino that is the same as the one that it gets but swaps the vaues of the varibles 
    returns the new domino
    """
    def flip(self):
        return Domino(left=self.__right, right=self.__left)
