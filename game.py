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
    def __init__(self, home_team:Team, away_team:Team, home_score:int=0, away_score:int=0, month:int=0, day:int=0):
        self.home_team = home_team
        self.away_team = away_team
        self.score = {home_team: home_score, away_team: away_score}
        self.month = month
        self.day = day
    def result(self) -> GameResult:
        return ""


arsenal_vs_chelsea_316 = Game(arsenal, chelsea, 1,0, 3,16)
