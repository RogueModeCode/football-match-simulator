import random
from player import Player
from team import Team
from collections import Counter

# --- Helper Functions ---
def calculate_team_strength(team):
    total = 0
    for player in team.players:
        if player.position == "GK":
            total += player.rating * 0.9
        elif player.position == "DEF":
            total += player.rating * 1.0
        elif player.position == "MID":
            total += player.rating * 1.1
        elif player.position == "FWD":
            total += player.rating * 1.2
    return total


def simulate_match(team1, team2):
    team1_strength = calculate_team_strength(team1)
    team2_strength = calculate_team_strength(team2)

    score1 = 0
    score2 = 0
    events = []

    for minute in range(1, 91):
        if random.random() < 0.05:  # 5% chance per minute of a scoring event
            if random.random() < team1_strength / (team1_strength + team2_strength):
                scorer = random.choice([p for p in team1.players if p.position == "FWD" or p.position == "MID"])
                score1 += 1
                events.append((minute, f"{scorer.name} scored for {team1.name}"))
            else:
                scorer = random.choice([p for p in team2.players if p.position == "FWD" or p.position == "MID"])
                score2 += 1
                events.append((minute, f"{scorer.name} scored for {team2.name}"))

    return score1, score2, events


def generate_match_report(team1, team2, score1, score2, events):
    print(f"\n🏁 Final Score: {team1.name} {score1} - {score2} {team2.name}")
    print("📜 Match Events:")
    for minute, event in events:
        print(f"  {minute}' - {event}")

    if events:
        mvp = find_mvp(events)
        print(f"\n🌟 MVP of the Match: {mvp}")
    else:
        print("\nNo goals were scored.")


def find_mvp(events):
    scorers = [event.split()[0] for _, event in events if "scored" in event]
    mvp, _ = Counter(scorers).most_common(1)[0]
    return mvp



# --- Example Usage ---
if __name__ == "__main__":

    
    # Logan's team
    plymouth_argyle = Team("Plymouth Argyle FC")
    plymouth_players = [
        Player("Whittaker", "FWD", 74),
        Player("Forshaw", "MID", 71),
        Player("Mumba", "DEF", 71),
        Player("Hardie", "FWD", 70),
        Player("Pálsson", "DEF", 70),
        Player("Tijani", "FWD", 70),
        Player("Gibson", "DEF", 69),
        Player("Hazard", "GK", 68),
        Player("Randell", "Mid", 68),
        Player("Pleguezuelo", "DEF", 68),
        Player("Houghton", "MID", 67),
    ]
    for player in plymouth_players:
        plymouth_argyle.add_player(player)

    plymouth_argyle.display_team()
    print (calculate_team_strength(plymouth_argyle))

    #Jonahs Team
    arsenal = Team("Arsenal FC")
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
            Player("Raya", "GK", 83)
    ]
    for player in arsenal_players:
        arsenal.add_player(player)

    arsenal.display_team()
    print (calculate_team_strength(arsenal))

    #Cael's Team
    chelsea = Team("Chelsea FC")
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
        Player("Sanchez", "GK", 79)
    ]
    for player in  chelsea_players:
        chelsea.add_player(player)

    chelsea.display_team()
    print (calculate_team_strength(chelsea))

    # Create some sample players
    players_pool = [
        Player("Messi", "FWD", 95),
        Player("Ronaldo", "FWD", 93),
        Player("Modric", "MID", 90),
        Player("De Bruyne", "MID", 92),
        Player("Van Dijk", "DEF", 89),
        Player("Alisson", "GK", 90),
        Player("Hakimi", "DEF", 86),
        Player("Kante", "MID", 88),
        Player("Kane", "FWD", 91),
        Player("Neuer", "GK", 88),
        Player("Walker", "DEF", 85),
    ]

    # Create teams
    team_a = Team("Thunder FC")
    team_b = Team("Dragon United")

    # Assign players (randomly or manually)
    for i in range(11):
        team_a.add_player(random.choice(players_pool))
        team_b.add_player(random.choice(players_pool))

    # team_a.display_team()
    # team_b.display_team()

    # Simulate match
    score1, score2, events = simulate_match(arsenal, chelsea)
    generate_match_report(arsenal, chelsea, score1, score2, events)