import random
from player import Player
from team import Team
from collections import Counter

from teams_database import plymouth_argyle, famalicao, chelsea, arsenal

SCORE_PER_MIN_PROB = 0.05
CARD_PER_MIN_PROB = 0.036

POSITION_STRENGTH = { "GK": 1.2, "DEF": 1.0, "MID":1.1, "FWD": 1.2 }

# --- Helper Functions ---
def calculate_team_strength(team):
    total = 0
    for player in team.players:
        total += player.rating * POSITION_STRENGTH[player.position.upper()] 
        
    return total

def simulate_match(team1, team2):
    team1_strength = calculate_team_strength(team1)
    team2_strength = calculate_team_strength(team2)

    score1 = 0
    score2 = 0
    yellow_cards = 0
    red_cards = 0
    events = []

    for second in range(1, 90 * 60):
        # scoring event
        if random.random() < SCORE_PER_MIN_PROB/60:  
            if random.random() < team1_strength / (team1_strength + team2_strength):
                scorer = random.choice([p for p in team1.players if p.position == "FWD" or p.position == "MID"])
                score1 += 1
                events.append((round(second/60), f"{scorer.name} scored for {team1.name}"))
            else:
                scorer = random.choice([p for p in team2.players if p.position == "FWD" or p.position == "MID"])
                score2 += 1
                events.append((round(second/60), f"{scorer.name} scored for {team2.name}"))

        # card event    
        if random.random() < CARD_PER_MIN_PROB/60:
            carded = random.choice([p for p in team1.players or team2.players if p.position == "FWD" or p.position == "MID" or p.position == "DEF"])
            if random.random() < .95:
                yellow_cards += 1
                events.append((round(second/60), f"{carded.name} was given a yellow card"))
            else:
                red_cards += 1
                events.append((round(second/60), f"{carded.name} was given a red card"))
                
            

    return score1, score2, events



def generate_match_report(team1, team2, score1, score2, events):
    print(f"\n🏁 Final Score: {team1.name} {score1} - {score2} {team2.name}")
    print("📜 Match Events:")
    for minute, event in events:
        print(f"  {minute}' - {event}")

    if events:
        mvp = find_mvp(events)
        print(f"\n🌟 Man of the Match: {mvp}")
    else:
        print("\nNo goals were scored.")


def find_mvp(events):
    scorers = [event.split()[0] for _, event in events if "scored" in event]
    mvp, _ = Counter(scorers).most_common(1)[0]
    return mvp



# --- Example Usage ---
if __name__ == "__main__":

    plymouth_argyle.display_team()
    print (calculate_team_strength(plymouth_argyle))

    arsenal.display_team()
    print (calculate_team_strength(arsenal))
    
    chelsea.display_team()
    print (calculate_team_strength(chelsea))

    famalicao.display_team()
    print (calculate_team_strength(famalicao))

    # Simulate match
    score1, score2, events = simulate_match(arsenal, famalicao)
    generate_match_report(arsenal, famalicao, score1, score2, events)
