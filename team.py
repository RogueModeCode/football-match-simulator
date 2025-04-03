# --- Team Class ---
from player import Player
class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players

    def add_player(self, player):
        if len(self.players) < 11:
            self.players.append(player)

    def display_team(self):
        print(f"\nTeam: {self.name}")
        for player in self.players:
            print(player)


Team("Arsenal", [Player("Saka", "FWD", 12, 87),
            Player("Havertz", "FWD", 12, 83),
            Player("Martinelli", "FWD", 12, 83),
            Player("Ødegaard", "MID", 12, 89),
            Player("Rice", "MID", 12, 87),
            Player("Nwaneri", "MID", 12, 76),
            Player("Lewis-Skelly", "DEF", 12, 81),
            Player("Gabriel", "DEF", 12, 86),
            Player("Saliba", "DEF", 12, 87),
            Player("Timber", "DEF", 12, 84),
            Player("Raya", "GK", 12, 83)]
)
print(Team("Arsenal", [Player("Saka", "FWD", 12, 87),
            Player("Havertz", "FWD", 12, 83),
            Player("Martinelli", "FWD", 12, 83),
            Player("Ødegaard", "MID", 12, 89),
            Player("Rice", "MID", 12, 87),
            Player("Nwaneri", "MID", 12, 76),
            Player("Lewis-Skelly", "DEF", 12, 81),
            Player("Gabriel", "DEF", 12, 86),
            Player("Saliba", "DEF", 12, 87),
            Player("Timber", "DEF", 12, 84),
            Player("Raya", "GK", 12, 83)]))
