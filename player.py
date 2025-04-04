# --- Player Class ---
class Player:
    def __init__(self, name, position, price, rating):
        self.name = name
        self.position = position  # "GK", "DEF", "MID", "FWD"
        self.price = price
        self.rating = rating

    def __str__(self):
        return f"{self.name} ({self.position}) - ${self.price}M, Rating: {self.rating}"
