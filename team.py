# --- Team Class ---
from player import Player
class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        if len(self.players) < 11:
            self.players.append(player)

    def display_team(self):
        print(f"\nTeam: {self.name}")
        for player in self.players:
            print(player)
