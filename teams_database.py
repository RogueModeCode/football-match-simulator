from player import Player 
from team import Team

# Logan's team
plymouth_argyle = Team("Plymouth Argyle FC")
plymouth_players = [
    Player("Whittaker", "FWD", 74, "(PAFC)"),
    Player("Forshaw", "MID", 71, "(PAFC)"),
    Player("Mumba", "DEF", 71, "(PAFC)"),
    Player("Hardie", "FWD", 70, "(PAFC)"),
    Player("Pálsson", "DEF", 70, "(PAFC)"),
    Player("Tijani", "FWD", 70, "(PAFC)"),
    Player("Gibson", "DEF", 69, "(PAFC)"),
    Player("Hazard", "GK", 68, "(PAFC)"),
    Player("Randell", "Mid", 68, "(PAFC)"),
    Player("Pleguezuelo", "DEF", 68, "(PAFC)"),
    Player("Houghton", "MID", 67, "(PAFC)"),
]

for player in plymouth_players:
    plymouth_argyle.add_player(player)

#Cael's Team
chelsea = Team("Chelsea FC")
chelsea_players = [
    Player("Jackson", "FWD", 82, "(CFC)"),
    Player("Palmer", "MID", 86, "(CFC)"),
    Player("Caicedo", "MID", 80, "(CFC)"),
    Player("Fernandez", "MID", 82, "(CFC)"),
    Player("Neto", "MID", 82, "(CFC)"),
    Player("Madueke", "MID", 80, "(CFC)"),
    Player("Fofana", "DEF", 79, "(CFC)"),
    Player("Gusto", "DEF", 80, "(CFC)"),
    Player("Cucurella", "DEF", 84, "(CFC)"),
    Player("Colwill", "DEF", 79, "(CFC)"),
    Player("Sanchez", "GK", 79, "(CFC)"),
]
for player in  chelsea_players:
    chelsea.add_player(player)

 #Jonahs Team
arsenal = Team("Arsenal FC")
arsenal_players = [
        Player("Saka", "FWD", 87, "(AFC)"),
        Player("Havertz", "FWD", 83, "(AFC)"),
        Player("Martinelli", "FWD", 83, "(AFC)"),
        Player("Ødegaard", "MID", 89, "(AFC)"),
        Player("Rice", "MID", 87, "(AFC)"),
        Player("Nwaneri", "MID", 76, "(AFC)"),
        Player("Lewis-Skelly", "DEF", 81, "(AFC)"),
        Player("Gabriel", "DEF", 86, "(AFC)"),
        Player("Saliba", "DEF", 87, "(AFC)"),
        Player("Timber", "DEF", 84, "(AFC)"),
        Player("Raya", "GK", 83, "(AFC)"),
]
for player in arsenal_players:
    arsenal.add_player(player)

#Levis Team
famalicao = Team("FC Famalicao")
famalicao_players = [
        Player("Youssouf", "FWD", 76, "(FAM)"),
        Player("Rochinha", "FWD", 74, "(FAM)"),
        Player("Gonzalez", "FWD", 71, "(FAM)"),
        Player("Sa", "MID", 72, "(FAM)"),
        Player("Topic", "MID", 70, "(FAM)"),
        Player("Aranda", "MID", 68, "(FAM)"),
        Player("de Haas", "DEF", 69, "(FAM)"),
        Player("Soares", "DEF", 70, "(FAM)"),
        Player("Mihaj", "DEF", 70, "(FAM)"),
        Player("Riccieli", "DEF", 72, "(FAM)"),
        Player("Zlobin", "GK", 67, "(FAM)"),
]
for player in famalicao_players:
    famalicao.add_player(player)