
class EmptyBoardException(Exception):

    def __init__(self, massage):
        self.massage = massage

    def __str__(self):
        return f'ERROR {self.massage}'


class FullBoardException(Exception):

    def __init__(self, massage):
        self.massage = massage

    def __str__(self):
        return f'ERROR {self.massage}'


class NoSuchDominoException(Exception):

    def __init__(self, massage):
        self.massage = massage

    def __str__(self):
        return f'ERROR {self.massage}'


class InvalidNumberException(Exception):

    def __init__(self, massage):
        self.massage = massage

    def __str__(self):
        return f'ERROR {self.massage}'
