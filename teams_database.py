from player import Player 
from team import Team

# Premier league

# liverpool
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

#chelsea
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

 #arsenal
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
        #subs
        Player("Trossard", "FWD", 83, arsenal),
        Player("Zinchenko", "MID", 79, arsenal),
        Player("White", "DEF", 84, arsenal),
]
for player in arsenal_players:
    arsenal.add_player(player)
    
# ipswitch
ipswich = Team("Ipswich Town", "IFC")
ipswich_players = [
        Player("Delap", "FWD", 71, ipswich),
        Player("Clarke", "FWD", 75, ipswich),
        Player("Hutchinson", "FWD", 74, ipswich),
        Player("Phillips", "MID", 77, ipswich),
        Player("Chaplin", "MID", 75, ipswich),
        Player("Morsey", "MID", 76, ipswich),
        Player("Davis", "DEF", 76, ipswich),
        Player("Greaves", "DEF", 75, ipswich),
        Player("O'Shea", "DEF", 74, ipswich),
        Player("Johnson", "DEF", 73, ipswich),
        Player("Muric", "GK", 75, ipswich),
        #subs
        Player("Szmodics", "MID", 75, ipswich),
        Player("Ogbene", "DEF", 73, ipswich),
        Player("Broadhead", "FWD", 72, ipswich),
]
for player in ipswich_players:
    ipswich.add_player(player)

#man city
man_city = Team("Manchester City", "MCI")
man_city_players = [
    Player("Ederson", "GK", 88, man_city),
    Player("Rúben Dias", "DEF", 88, man_city),
    Player("Kyle Walker", "DEF", 85, man_city),
    Player("Joško Gvardiol", "DEF", 82, man_city),
    Player("Nathan Aké", "DEF", 81, man_city),
    Player("Rodri", "MID", 91, man_city),
    Player("Kevin De Bruyne", "MID", 90, man_city),
    Player("Bernardo Silva", "MID", 88, man_city),
    Player("Erling Haaland", "FWD", 91, man_city),
    Player("Phil Foden", "FWD", 88, man_city),
    Player("Juack Grealish", "FWD", 84, man_city),
    # Substitutes
    Player("Matheus Nunes", "MID", 83, man_city),
    Player("Manuel Akanji", "DEF", 83, man_city),
    Player("Stefan Ortega", "GK", 80, man_city),
]

for player in man_city_players:
    man_city.add_player(player)

#man U
man_utd = Team("Manchester United FC", "MUN")
man_utd_players = [
    Player("André Onana", "GK", 83, man_utd),
    Player("Diogo Dalot", "DEF", 82, man_utd),
    Player("Matthijs de Ligt", "DEF", 84, man_utd),
    Player("Lisandro Martínez", "DEF", 84, man_utd),
    Player("Luke Shaw", "DEF", 82, man_utd),
    Player("Bruno Fernandes", "MID", 87, man_utd),
    Player("Casemiro", "MID", 84, man_utd),
    Player("Kobbie Mainoo", "MID", 77, man_utd),
    Player("Hojlund", "FWD", 78, man_utd),
    Player("Alejandro Garnacho", "FWD", 79, man_utd),
    Player("Scott McTominay", "FWD", 80, man_utd),
    # Substitutes
    Player("Harry Maguire", "DEF", 80, man_utd),
    Player("Mason Mount", "MID", 78, man_utd),
    Player("Altay Bayındır", "GK", 76, man_utd),
]

for player in man_utd_players:
    man_utd.add_player(player)

#Spurs
tottenham = Team("Tottenham Hotspur FC", "TOT")
tottenham_players = [
    Player("Guglielmo Vicario", "GK", 84, tottenham),
    Player("Cristian Romero", "DEF", 84, tottenham),
    Player("Micky van de Ven", "DEF", 81, tottenham),
    Player("Pedro Porro", "DEF", 83, tottenham),
    Player("Ben Davies", "DEF", 79, tottenham),
    Player("James Maddison", "MID", 85, tottenham),
    Player("Yves Bissouma", "MID", 79, tottenham),
    Player("Pape Matar Sarr", "MID", 78, tottenham),
    Player("Heung Min Son", "FWD", 87, tottenham),
    Player("Dejan Kulusevski", "FWD", 81, tottenham),
    Player("Richarlison", "FWD", 80, tottenham),
    # Substitutes
    Player("Giovani Lo Celso", "MID", 79, tottenham),
    Player("Emerson Royal", "DEF", 78, tottenham),
    Player("Fraser Forster", "GK", 75, tottenham),
]

for player in tottenham_players:
    tottenham.add_player(player)

#newcastle
newcastle = Team("Newcastle United FC", "NEW")
newcastle_players = [
    Player("Nick Pope", "GK", 83, newcastle),
    Player("Kieran Trippier", "DEF", 83, newcastle),
    Player("Fabian Schär", "DEF", 82, newcastle),
    Player("Sven Botman", "DEF", 82, newcastle),
    Player("Dan Burn", "DEF", 78, newcastle),
    Player("Bruno Guimarães", "MID", 85, newcastle),
    Player("Sandro Tonali", "MID", 85, newcastle),
    Player("Joelinton", "MID", 82, newcastle),
    Player("Alexander Isak", "FWD", 85, newcastle),
    Player("Anthony Gordon", "FWD", 83, newcastle),
    Player("Miguel Almirón", "FWD", 80, newcastle),
    # Substitutes
    Player("Joe Willock", "MID", 79, newcastle),
    Player("Tino Livramento", "DEF", 78, newcastle),
    Player("Martin Dúbravka", "GK", 76, newcastle),
]

for player in newcastle_players:
    newcastle.add_player(player)

#Nott'm
nottingham_forest = Team("Nottingham Forest FC", "NFO")
nottingham_forest_players = [
    Player("Matt Turner", "GK", 77, nottingham_forest),
    Player("Álex Moreno", "DEF", 79, nottingham_forest),
    Player("Nikola Milenković", "DEF", 79, nottingham_forest),
    Player("Murillo", "DEF", 78, nottingham_forest),
    Player("Willy Boly", "DEF", 77, nottingham_forest),
    Player("Morgan Gibbs-White", "MID", 79, nottingham_forest),
    Player("James Ward-Prowse", "MID", 79, nottingham_forest),
    Player("Ryan Yates", "MID", 75, nottingham_forest),
    Player("Taiwo Awoniyi", "FWD", 77, nottingham_forest),
    Player("Chris Wood", "FWD", 76, nottingham_forest),
    Player("Jota Silva", "FWD", 77, nottingham_forest),
    # Substitutes
    Player("Danilo", "MID", 76, nottingham_forest),
    Player("Ola Aina", "DEF", 75, nottingham_forest),
    Player("Keylor Navas", "GK", 81, nottingham_forest),
]

for player in nottingham_forest_players:
    nottingham_forest.add_player(player)

#aston villa
aston_villa = Team("Aston Villa FC", "AVL")
aston_villa_players = [
    Player("Emiliano Martínez", "GK", 87, aston_villa),
    Player("Matty Cash", "DEF", 80, aston_villa),
    Player("Ezri Konsa", "DEF", 81, aston_villa),
    Player("Tyrone Mings", "DEF", 80, aston_villa),
    Player("Lucas Digne", "DEF", 79, aston_villa),
    Player("Boubacar Kamara", "MID", 83, aston_villa),
    Player("John McGinn", "MID", 81, aston_villa),
    Player("Philippe Coutinho", "MID", 81, aston_villa),
    Player("Leon Bailey", "FWD", 81, aston_villa),
    Player("Ollie Watkins", "FWD", 85, aston_villa),
    Player("Jhon Durán", "FWD", 74, aston_villa),
    # Substitutes
    Player("Alex Moreno", "DEF", 79, aston_villa),
    Player("Emiliano Buendía", "MID", 80, aston_villa),
    Player("Robin Olsen", "GK", 77, aston_villa),
]

for player in aston_villa_players:
    aston_villa.add_player(player)

#bournmouth
bournemouth = Team("AFC Bournemouth", "BOU")
bournemouth_players = [
    Player("Kepa Arrizabalaga", "GK", 79, bournemouth),
    Player("Milos Kerkez", "DEF", 81, bournemouth),
    Player("Illia Zabarnyi", "DEF", 78, bournemouth),
    Player("Dean Huijsen", "DEF", 77, bournemouth),
    Player("Adam Smith", "DEF", 73, bournemouth),
    Player("Lewis Cook", "MID", 79, bournemouth),
    Player("Tyler Adams", "MID", 78, bournemouth),
    Player("Philip Billing", "MID", 77, bournemouth),
    Player("Evanilson", "FWD", 80, bournemouth),
    Player("Enes Ünal", "FWD", 78, bournemouth),
    Player("Justin Kluivert", "FWD", 76, bournemouth),
    # Substitutes
    Player("Dango Ouattara", "FWD", 75, bournemouth),
    Player("Marcos Senesi", "DEF", 78, bournemouth),
    Player("Neto", "GK", 78, bournemouth),
]

for player in bournemouth_players:
    bournemouth.add_player(player)

#Fulham
fulham = Team("Fulham FC", "FUL")
fulham_players = [
    Player("Bernd Leno", "GK", 81, fulham),
    Player("Antonee Robinson", "DEF", 79, fulham),
    Player("Joachim Andersen", "DEF", 79, fulham),
    Player("Calvin Bassey", "DEF", 77, fulham),
    Player("Timothy Castagne", "DEF", 76, fulham),
    Player("Sander Berge", "MID", 78, fulham),
    Player("Saša Lukić", "MID", 78, fulham),
    Player("Emile Smith Rowe", "MID", 78, fulham),
    Player("Ryan Sessegnon", "FWD", 77, fulham),
    Player("Raúl Jiménez", "FWD", 77, fulham),
    Player("Alex Iwobi", "FWD", 80, fulham),
    # Substitutes
    Player("Andreas Pereira", "MID", 78, fulham),
    Player("Harry Wilson", "FWD", 76, fulham),
    Player("Neto", "GK", 77, fulham),
]

for player in fulham_players:
    fulham.add_player(player)

#Brighton
brighton = Team("Brighton & Hove Albion FC", "BHA")
brighton_players = [
    Player("Bart Verbruggen", "GK", 75, brighton),
    Player("Joel Veltman", "DEF", 78, brighton),
    Player("Jan Paul van Hecke", "DEF", 75, brighton),
    Player("Lewis Dunk", "DEF", 81, brighton),
    Player("Pervis Estupiñán", "DEF", 79, brighton),
    Player("Carlos Baleba", "MID", 79, brighton),
    Player("Mats Wieffer", "MID", 80, brighton),
    Player("Matt O'Riley", "MID", 79, brighton),
    Player("Kaoru Mitoma", "FWD", 81, brighton),
    Player("Ferdi Kadıoğlu", "FWD", 81, brighton),
    Player("Danny Welbeck", "FWD", 75, brighton),
    # Substitutes
    Player("Jack Hinshelwood", "MID", 74, brighton),
    Player("Valentín Barco", "DEF", 73, brighton),
    Player("Kjell Scherpen", "GK", 72, brighton),
]

for player in brighton_players:
    brighton.add_player(player)

#Brentford
brentford = Team("Brentford FC", "BRE")
brentford_players = [
    Player("Mark Flekken", "GK", 78, brentford),
    Player("Ethan Pinnock", "DEF", 78, brentford),
    Player("Ben Mee", "DEF", 77, brentford),
    Player("Nathan Collins", "DEF", 75, brentford),
    Player("Rico Henry", "DEF", 77, brentford),
    Player("Vitaly Janelt", "MID", 77, brentford),
    Player("Mathias Jensen", "MID", 79, brentford),
    Player("Mikkel Damsgaard", "MID", 76, brentford),
    Player("Bryan Mbeumo", "FWD", 80, brentford),
    Player("Yoane Wissa", "FWD", 79, brentford),
    Player("Kevin Schade", "FWD", 77, brentford),
    # Substitutes
    Player("Aaron Hickey", "DEF", 76, brentford),
    Player("Fábio Carvalho", "MID", 74, brentford),
    Player("Matthew Cox", "GK", 65, brentford),
]

for player in brentford_players:
    brentford.add_player(player)

#Crystal Palace
crystal_palace = Team("Crystal Palace FC", "CRY")
crystal_palace_players = [
    Player("Dean Henderson", "GK", 80, crystal_palace),
    Player("Joel Ward", "DEF", 75, crystal_palace),
    Player("Marc Guéhi", "DEF", 81, crystal_palace),
    Player("Chris Richards", "DEF", 78, crystal_palace),
    Player("Tyrick Mitchell", "DEF", 77, crystal_palace),
    Player("Jeffrey Schlupp", "MID", 77, crystal_palace),
    Player("Cheick Doucouré", "MID", 79, crystal_palace),
    Player("Eberechi Eze", "MID", 81, crystal_palace),
    Player("Jordan Ayew", "FWD", 77, crystal_palace),
    Player("Jean-Philippe Mateta", "FWD", 79, crystal_palace),
    Player("Odsonne Édouard", "FWD", 78, crystal_palace),
    # Substitutes
    Player("Matheus França", "MID", 75, crystal_palace),
    Player("Nathaniel Clyne", "DEF", 76, crystal_palace),
    Player("Remi Matthews", "GK", 72, crystal_palace),
]

for player in crystal_palace_players:
    crystal_palace.add_player(player)

#Everton
everton = Team("Everton FC", "EVE")
everton_players = [
    Player("Jordan Pickford", "GK", 83, everton),
    Player("Seamus Coleman", "DEF", 75, everton),
    Player("James Tarkowski", "DEF", 79, everton),
    Player("Jarrad Branthwaite", "DEF", 78, everton),
    Player("Vitalii Mykolenko", "DEF", 77, everton),
    Player("Idrissa Gueye", "MID", 77, everton),
    Player("Amadou Onana", "MID", 77, everton),
    Player("James Garner", "MID", 75, everton),
    Player("Jack Harrison", "FWD", 76, everton),
    Player("Dominic Calvert-Lewin", "FWD", 77, everton),
    Player("Dwight McNeil", "FWD", 77, everton),
    # Substitutes
    Player("Ashley Young", "DEF", 74, everton),
    Player("Tom Davies", "MID", 74, everton),
    Player("Asmir Begović", "GK", 74, everton),
]

for player in everton_players:
    everton.add_player(player)

#wolves
wolves = Team("Wolverhampton Wanderers FC", "WOL")
wolves_players = [
    Player("José Sá", "GK", 81, wolves),
    Player("Rayan Aït-Nouri", "DEF", 81, wolves),
    Player("Craig Dawson", "DEF", 79, wolves),
    Player("Santiago Bueno", "DEF", 78, wolves),
    Player("Emmanuel Agbadou", "DEF", 77, wolves),
    Player("Mario Lemina", "MID", 80, wolves),
    Player("João Gomes", "MID", 78, wolves),
    Player("Tommy Doyle", "MID", 76, wolves),
    Player("Matheus Cunha", "FWD", 81, wolves),
    Player("Hwang Hee-Chan", "FWD", 79, wolves),
    Player("Raúl Jiménez", "FWD", 78, wolves),
    # Substitutes
    Player("Daniel Bentley", "GK", 75, wolves),
    Player("Sam Johnstone", "GK", 77, wolves),
    Player("Bastien Meupiyou", "DEF", 74, wolves),
]

for player in wolves_players:
    wolves.add_player(player)

#West Ham
west_ham = Team("West Ham United FC", "WHU")
west_ham_players = [
    Player("Alphonse Areola", "GK", 81, west_ham),
    Player("Vladimír Coufal", "DEF", 76, west_ham),
    Player("Maximilian Kilman", "DEF", 77, west_ham),
    Player("Aaron Cresswell", "DEF", 73, west_ham),
    Player("Emerson Palmieri", "DEF", 78, west_ham),
    Player("Guido Rodríguez", "MID", 82, west_ham),
    Player("James Ward-Prowse", "MID", 78, west_ham),
    Player("Mohammed Kudus", "MID", 82, west_ham),
    Player("Jarrod Bowen", "FWD", 82, west_ham),
    Player("Niclas Füllkrug", "FWD", 82, west_ham),
    Player("Lucas Paquetá", "FWD", 82, west_ham),
    # Substitutes
    Player("Aaron Wan-Bissaka", "DEF", 80, west_ham),
    Player("Łukasz Fabiański", "GK", 77, west_ham),
    Player("Carlos Soler", "MID", 78, west_ham),
]

for player in west_ham_players:
    west_ham.add_player(player)

#leicster city
leicester_city = Team("Leicester City FC", "LCFC")
leicester_city_players = [
    Player("Mads Hermansen", "GK", 76, leicester_city),
    Player("Ricardo Pereira", "DEF", 78, leicester_city),
    Player("Wout Faes", "DEF", 77, leicester_city),
    Player("Harry Souttar", "DEF", 76, leicester_city),
    Player("Timothy Castagne", "DEF", 77, leicester_city),
    Player("Wilfred Ndidi", "MID", 78, leicester_city),
    Player("Oliver Skipp", "MID", 77, leicester_city),
    Player("Kiernan Dewsbury-Hall", "MID", 77, leicester_city),
    Player("Jamie Vardy", "FWD", 77, leicester_city),
    Player("Patson Daka", "FWD", 76, leicester_city),
    Player("Kelechi Iheanacho", "FWD", 77, leicester_city),
    # Substitutes
    Player("Hamza Choudhury", "MID", 72, leicester_city),
    Player("Jannik Vestergaard", "DEF", 75, leicester_city),
    Player("Daniel Iversen", "GK", 75, leicester_city),
]

for player in leicester_city_players:
    leicester_city.add_player(player)

#southampton
southampton = Team("Southampton FC", "SOU")
southampton_players = [
    Player("Aaron Ramsdale", "GK", 81, southampton),
    Player("Yukinari Sugawara", "DEF", 79, southampton),
    Player("Taylor Harwood-Bellis", "DEF", 77, southampton),
    Player("Jack Stephens", "DEF", 73, southampton),
    Player("Kyle Walker-Peters", "DEF", 76, southampton),
    Player("Flynn Downes", "MID", 77, southampton),
    Player("Joe Aribo", "MID", 75, southampton),
    Player("Will Smallbone", "MID", 75, southampton),
    Player("Ben Brereton Díaz", "FWD", 77, southampton),
    Player("Cameron Archer", "FWD", 76, southampton),
    Player("Adam Armstrong", "FWD", 75, southampton),
    # Substitutes
    Player("Charlie Taylor", "DEF", 75, southampton),
    Player("Nathan Wood", "DEF", 74, southampton),
    Player("Khiani Shombe", "GK", 65, southampton),
]

for player in southampton_players:
    southampton.add_player(player)

#----------------------------------------------------------------------------------------
# Other

# plymoth
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

# barsa
barcelona = Team("Barcelona", "BAR")
barcelona_players = [
    Player("Lewandowski", "FWD", 88, barcelona),
    Player("Raphinha", "FWD", 84, barcelona),
    Player("Yamal", "FWD", 86, barcelona),
    Player("De Jong", "MID", 88, barcelona),
    Player("Pedri", "MID", 86, barcelona),
    Player("Dani Olmo", "MID", 84, barcelona),
    Player("Araujo", "DEF", 85, barcelona),
    Player("Kounde", "DEF", 85, barcelona),
    Player("Christensen", "DEF", 83, barcelona),
    Player("Balde", "DEF", 81, barcelona),
    Player("Ter Stegen", "GK", 89, barcelona),
    #subs
    Player("Ferran Torres", "FWD", 80, barcelona),
    Player("Martinez", "DEF", 81, barcelona),
    Player("Gavi", "MID", 83, barcelona)
]
for player in barcelona_players:
    barcelona.add_player(player)

# madrid
real_madrid = Team("Real Madrid FC", "RMA")
real_madrid_players = [
        Player("Mbappe", "FWD", 91, real_madrid),
        Player("Vini Jr", "FWD", 90, real_madrid),
        Player("Rodrygo", "FWD", 86, real_madrid),
        Player("Bellingham", "MID", 90, real_madrid),
        Player("Valverde", "MID", 88, real_madrid),
        Player("Modric", "MID", 86, real_madrid),
        Player("Mendy", "DEF", 84, real_madrid),
        Player("Rudiger", "DEF", 88, real_madrid),
        Player("Alaba", "DEF", 85, real_madrid),
        Player("Carvajal", "DEF", 86, real_madrid),
        Player("Courtois", "GK", 89, real_madrid),
        #subs
        Player("Camavinga", "MID", 83, real_madrid),
        Player("Tchouameni", "DEF", 85, real_madrid),
        Player("Endrick", "FWD", 77, real_madrid),
]
for player in real_madrid_players:
    real_madrid.add_player(player)

# famalicao
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






