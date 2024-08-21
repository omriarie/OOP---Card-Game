from abc import ABC,abstractmethod
"""
this class s going to contain a list of cards
"""

class Collection(ABC):

    """
    the founction will make an appirance of the class collection, with the list of tiles it gets
    """
    def __init__(self, array):
        self.array = array
    """
    the founction will return a pointer to the collection's list
    """
    def get_collection(self):
        return self.array
    """
    this founction will not be  Implemented in here so it will raise an error
    """
    @abstractmethod
    def add(self, item, option=True):
        pass
    """
    the founction will return the varible in the right place
    if it cants it will return None
    """
    def __getitem__(self, i):
        if not type(i) == int:
            return None
        if 0 <= i < len(self.array):
            return self.array[i]
        else:
            return None
    """
    the founction will check if the second varible is a collection too, if not it will will return False
    if it does  it will check if the arrays are the same
    """
    def __eq__(self, other):
        if not type(self) == type(other):
            return False
        if self.array == other.get_collection():
            return True
        else:
            return False

    """
    the founction will check if the collections are not the same . returns a boolian answer
    """
    def __ne__(self, other):
        if not type(self) == type(other):
            return True
        if self == other:
            return False
        else:
            return True
    """
    the founction will return the len of the array of the board
    """
    def __len__(self):
        return len(self.array)
    """
    the founction will return if the collection has a sertent tile or not
    """
    def __contains__(self, item):
        for i in self.array:
            if i == item:
                return True
        return False
    """
    the founction will return a string that will represent the collection making str of all the dominos and combining them
    """
    def __str__(self):
        return ''.join([str(domino) for domino in self.array])
    """
    the founction will return a string of the collection
    """
    def __repr__(self):
        return str(self)
