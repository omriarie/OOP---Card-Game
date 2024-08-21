


"""
this class is going to represent a game of domino between tow teams and one board
"""
class Game:
    """
    the founction will make an appirence of the class board
    """
    def __init__(self, board, team1, team2):
        self.board = board
        self.team1 = team1
        self.team2 = team2
    """
    the founction will make a game with tow teams, and a board, it will let the first team play first and every time someone plays it will check if someone wins or
    not, the founction will save in varibles if someone played or not and if they both didnt play in a row then it will check the tow teams score
    then it will determ if someone wins or there is a Draw or not
    """
    def play(self):
        team2_played = False
        team1_played = False
        while True:
            if self.board.max_capacity != len(self.board):
                team1_played = self.team1.play(board=self.board)
                if team1_played:
                    if not self.team1.has_dominoes_team():
                        return f'Team {self.team1.name} wins Team {self.team2.name}'
            if self.board.max_capacity != len(self.board):
                team2_played = self.team2.play(board=self.board)
                if team2_played:
                    if not self.team2.has_dominoes_team():
                        return f'Team {self.team2.name} wins Team {self.team1.name}'

            if not team2_played and not team1_played or self.board.max_capacity == len(self.board):
                if self.team1.score_team() < self.team2.score_team():
                    return f'Team {self.team1.name} wins Team {self.team2.name}'
                elif self.team2.score_team() < self.team1.score_team():
                    return f'Team {self.team2.name} wins Team {self.team1.name}'
                else:
                    return 'Draw!'
