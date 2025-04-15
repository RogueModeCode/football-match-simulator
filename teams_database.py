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
    Player("Randell", "MID", 68, plymouth_argyle),
    Player("Pleguezuelo", "DEF", 68, plymouth_argyle),
    Player("Houghton", "MID", 67, plymouth_argyle),
    #subs
    Player("Edwards", "DEF", 67, plymouth_argyle),
    Player("Gyabi", "MID", 66, plymouth_argyle),
    Player("Cissoko", "FWD", 69, plymouth_argyle),
]

for player in plymouth_players:
    plymouth_argyle.add_player(player)

liverpool = Team("Liverpool FC", "LFC")
liverpool_players = [
    Player("Alisson", "GK", 89, liverpool),
    Player("van Dijk", "DEF", 89, liverpool),
    Player("Salah", "FWD", 89, liverpool),
    Player("Mac Allister", "MID", 86, liverpool),
    Player("Alexander-Arnold", "DEF", 86, liverpool),
    Player("Robertson", "DEF", 85, liverpool),
    Player("Jota", "FWD", 85, liverpool),
    Player("Chiesa", "FWD", 84, liverpool),
    Player("Diaz", "FWD", 84, liverpool),
    Player("Konaté", "DEF", 83, liverpool),
    Player("Szoboszlai", "MID", 81, liverpool),
    #subs
    Player("Endo", "MID", 80, liverpool),
    Player("Gakpo", "FWD", 83, liverpool),
    Player("Gomex", "DEF", 80, liverpool),
]

for player in liverpool_players:
    liverpool.add_player(player)

#Cael's Team
chelsea = Team("Chelsea FC", "CFC")
chelsea_players = [
    Player("Jackson", "FWD", 82, chelsea),
    Player("Palmer", "MID", 86, chelsea),
    Player("Caicedo", "MID", 80, chelsea),
    Player("Fernandez", "MID", 82, chelsea),
    Player("Neto", "MID", 82, chelsea),
    Player("Madueke", "MID", 80, chelsea),
    Player("Fofana", "DEF", 79, chelsea),
    Player("Gusto", "DEF", 80, chelsea),
    Player("Cucurella", "DEF", 84, chelsea),
    Player("Colwill", "DEF", 79, chelsea),
    Player("Sanchez", "GK", 79, chelsea),
]
for player in  chelsea_players:
    chelsea.add_player(player)

 #Jonahs Team
arsenal = Team("Arsenal FC", "AFC")
arsenal_players = [
        Player("Saka", "FWD", 87, arsenal),
        Player("Havertz", "FWD", 83, arsenal),
        Player("Martinelli", "FWD", 83, arsenal),
        Player("Ødegaard", "MID", 89, arsenal),
        Player("Rice", "MID", 87, arsenal),
        Player("Nwaneri", "MID", 76, arsenal),
        Player("Lewis-Skelly", "DEF", 81, arsenal),
        Player("Gabriel", "DEF", 86, arsenal),
        Player("Saliba", "DEF", 87, arsenal),
        Player("Timber", "DEF", 84, arsenal),
        Player("Raya", "GK", 83, arsenal),
]
for player in arsenal_players:
    arsenal.add_player(player)

#Levis Team
famalicao = Team("FC Famalicao", "FAM")
famalicao_players = [
        Player("Youssouf", "FWD", 76, famalicao),
        Player("Rochinha", "FWD", 74, famalicao),
        Player("Gonzalez", "FWD", 71, famalicao),
        Player("Sa", "MID", 72, famalicao),
        Player("Topic", "MID", 70, famalicao),
        Player("Aranda", "MID", 68, famalicao),
        Player("de Haas", "DEF", 69, famalicao),
        Player("Soares", "DEF", 70, famalicao),
        Player("Mihaj", "DEF", 70, famalicao),
        Player("Riccieli", "DEF", 72, famalicao),
        Player("Zlobin", "GK", 67, famalicao),
]
for player in famalicao_players:
    famalicao.add_player(player)