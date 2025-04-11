from player import Player 
from team import Team

# Logan's team
plymouth_argyle = Team("Plymouth Argyle FC", "PAFC")
plymouth_players = [
    Player("Whittaker", "FWD", 74, plymouth_argyle),
    Player("Forshaw", "MID", 71, plymouth_argyle),
    Player("Mumba", "DEF", 71, plymouth_argyle),
    Player("Hardie", "FWD", 70, plymouth_argyle),
    Player("Pálsson", "DEF", 70, plymouth_argyle),
    Player("Tijani", "FWD", 70, plymouth_argyle),
    Player("Gibson", "DEF", 69, plymouth_argyle),
    Player("Hazard", "GK", 68, plymouth_argyle),
    Player("Randell", "Mid", 68, plymouth_argyle),
    Player("Pleguezuelo", "DEF", 68, plymouth_argyle),
    Player("Houghton", "MID", 67, plymouth_argyle),
]

for player in plymouth_players:
    plymouth_argyle.add_player(player)

#Cael's Team
chelsea = Team("Chelsea FC", "CFC")
chelsea_players = [
    Player("Jackson", "FWD", 82),
    Player("Palmer", "MID", 86),
    Player("Caicedo", "MID", 80),
    Player("Fernandez", "MID", 82),
    Player("Neto", "MID", 82),
    Player("Madueke", "MID", 80),
    Player("Fofana", "DEF", 79),
    Player("Gusto", "DEF", 80),
    Player("Cucurella", "DEF", 84),
    Player("Colwill", "DEF", 79),
    Player("Sanchez", "GK", 79),
]
for player in  chelsea_players:
    chelsea.add_player(player)

 #Jonahs Team
arsenal = Team("Arsenal FC", "AFC")
arsenal_players = [
        Player("Saka", "FWD", 87),
        Player("Havertz", "FWD", 83),
        Player("Martinelli", "FWD", 83),
        Player("Ødegaard", "MID", 89),
        Player("Rice", "MID", 87),
        Player("Nwaneri", "MID", 76),
        Player("Lewis-Skelly", "DEF", 81),
        Player("Gabriel", "DEF", 86),
        Player("Saliba", "DEF", 87),
        Player("Timber", "DEF", 84),
        Player("Raya", "GK", 83),
]
for player in arsenal_players:
    arsenal.add_player(player)

#Levis Team
famalicao = Team("FC Famalicao", "FAM")
famalicao_players = [
        Player("Youssouf", "FWD", 76),
        Player("Rochinha", "FWD", 74),
        Player("Gonzalez", "FWD", 71),
        Player("Sa", "MID", 72),
        Player("Topic", "MID", 70),
        Player("Aranda", "MID", 68),
        Player("de Haas", "DEF", 69),
        Player("Soares", "DEF", 70),
        Player("Mihaj", "DEF", 70),
        Player("Riccieli", "DEF", 72),
        Player("Zlobin", "GK", 67),
]
for player in famalicao_players:
    famalicao.add_player(player)