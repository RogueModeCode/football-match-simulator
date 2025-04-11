from player import Player
import random 

POSITION_STRENGTH = { "GK": 1.2, "DEF": 1.0, "MID":1.1, "FWD": 1.2 }

# --- Team Class ---
class Team:
    def __init__(self, name, abbr):
        self.name = name
        self.abbr = abbr
        self.players = []

    def add_player(self, player):
        if len(self.players) < 11:
            self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def display_team(self):
        print(f"\nTeam: {self.name}")
        for player in self.players:
            print(player)

    def __str__(self):
        result = f"\nTeam: {self.name}"
        for player in self.players:
            result+= str(player) +"\n"

        return result

    def team_strength(self):
        total = 0
        for player in self.players:
            total += player.rating * POSITION_STRENGTH[player.position.upper()] 
        
        return total
    
    def random_player_by_position(self, position):
        random_player = random.choice([p for p in self.players if p.position == position])
        return random_player

