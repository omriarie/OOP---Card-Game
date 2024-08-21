from Collection import Collection
from Exceptions import NoSuchDominoException

"""
this class is going to represent the deck in every player's hand by a list of dominos
"""
class Hand(Collection):
    """
    the founction will make an appirence of hand using its father's init founction, makeing a varible named array filled with
    a list of dominos
    """
    def __init__(self, dominoes):
        super(Hand, self).__init__(array=dominoes)
    """
    the founction will add a domino to the Hand, if the index is not sent then it will append to the end of the list the domino,
    if the index varivle gets a int then it will add to the corrrect palce the user wanted, else it will return None
    """
    def add(self, domino, index=None):
        if(index == None):
            self.array.append(domino)
        elif 0 <= index <= len(self.array):
            self.array.insert(index,domino)
        else:
            return None
    """
    the founction will remove a domino by getting the domino the user wants to remove , if it exist it will remove it and send back the place of the domino
    if it doesnt then if will raise an exception
    """
    def remove_domino(self, domino):
        for i in range(len(self.array)):
            if(self.array[i] == domino):
                self.array.pop(i)
                return i
        raise NoSuchDominoException("there is no such domino in hand")
    """
    the founction will check if there is such domino in the Hand, if there is it will return Treu
    else it will return False
    """
    def __contains__(self, key):
        for i in self.array:
            if i == key:
                return True
        return False
    """
    the founction will check if tow hand are the same or not by compering their arrays
    """
    def __eq__(self, other):
        if not type(self) == type(other):
            return False
        if self.array == other.array:
            return True
        return False
    """
    the founction will check if tow Hands are the same or not, returns a boolian answer
    """
    def __ne__(self, other):
        if not type(self) == type(other):
            return False
        return not self == other
    """
    the founction will return the len of the array of the Hand
    """
    def __len__(self):
        return len(self.array)


