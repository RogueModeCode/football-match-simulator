from team import Team

from enum import Enum

class GameResult(Enum):
    HOME_WIN = 1
    AWAY_WIN = 2
    DRAW = 3

    def __str__(self):
        if self == GameResult.HOME_WIN:
            return "Home Win"
        elif self == GameResult.AWAY_WIN:
            return "Away Win"
        else:
            return "Draw"

class Game:
    def __init__(self, home_team:Team, away_team:Team, home_score:int=0, away_score:int=0, events:str="", month:int=0, day:int=0):
        self.home_team = home_team
        self.away_team = away_team
        self.score = {home_team.abbr: home_score, away_team.abbr: away_score}
        self.events = events
        self.month = month
        self.day = day

    def result(self) -> GameResult:
        if self.score[self.home_team.abbr] == self.score[self.away_team.abbr]:
            return GameResult.DRAW
        elif self.score[self.home_team.abbr] < self.score[self.away_team.abbr]:
            return GameResult.AWAY_WIN
        else:
            return GameResult.HOME_WIN 
