# --- Player Class ---
class Player:
    def __init__(self, name, position, rating):
        self.name = name
        self.position = position  # "GK", "DEF", "MID", "FWD"
        self.rating = rating

    def __str__(self):
        return f"{self.name} ({self.position}), Rating: {self.rating}"
