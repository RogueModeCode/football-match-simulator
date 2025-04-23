from team import Team
from teams_database import plymouth_argyle, famalicao, chelsea, arsenal, liverpool, real_madrid

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
        self.score = {home_team: home_score, away_team: away_score}
        self.events = events
        self.month = month
        self.day = day

    def result(self) -> GameResult:
        if self.score[self.home_team] == self.score[self.away_team]:
            return GameResult.DRAW
        elif self.score[self.home_team] < self.score[self.away_team]:
            return GameResult.AWAY_WIN
        else:
            return GameResult.HOME_WIN 


season = [ 
            Game(arsenal, chelsea, 1,0, 3,16),
            Game(arsenal, famalicao, 2,0, 3,23),
            Game(arsenal, liverpool, 1,1, 3,30),
            Game(arsenal, real_madrid, 2,1, 4,6),
            Game(arsenal, plymouth_argyle, 3,0, 4,13),
            Game(arsenal, famalicao, 2,0, 4,20),
            Game(arsenal, chelsea, 1,0, 4,27),
            Game(arsenal, liverpool, 1,1, 5,4),
            Game(arsenal, real_madrid, 2,1, 5,11),
            Game(arsenal, plymouth_argyle, 3,0, 5,18)
        ]
