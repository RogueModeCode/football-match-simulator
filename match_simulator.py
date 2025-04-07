import random
from player import Player
from team import Team
from collections import Counter

from teams_database import plymouth_argyle, famalicao, chelsea, arsenal

SCORE_PER_MIN_PROB = 0.05
CARD_PER_MIN_PROB = 0.036

FORWARD_SCORING_PROB = 0.60
MIDFIELD_SCORING_PROB = 0.30
DEFENDER_SCORING_PROB = 0.099

def simulate_match(team1, team2):

    score1 = 0
    score2 = 0
    yellow_cards = 0
    red_cards = 0
    events = []

    for second in range(1, 90 * 60):
        # scoring event
        if random.random() < SCORE_PER_MIN_PROB/60:  
            if random.random() < team1.team_strength() / (team1.team_strength() + team2.team_strength()):

                scoring_probabilty = random.random() 
                if scoring_probabilty < FORWARD_SCORING_PROB:
                    scorer = team1.random_player_by_position("FWD")
                elif scoring_probabilty < FORWARD_SCORING_PROB + MIDFIELD_SCORING_PROB:
                    scorer = team1.random_player_by_position("MID")
                elif scoring_probabilty < FORWARD_SCORING_PROB + MIDFIELD_SCORING_PROB + DEFENDER_SCORING_PROB:
                    scorer = team1.random_player_by_position("DEF")
                else:
                    scorer = team1.random_player_by_position("GK")

                goalie = team2.random_player_by_position("GK")

                if random.random()*goalie.rating > random.random()*scorer.rating:
                    #shot saved
                    events.append((round(second/60), f"{goalie.name} saved {scorer.name}'s shot"))
                else: 
                    #shot scored   
                    score1 += 1
                    assister = random.choice([p for p in team1.players])
                    if assister == scorer:
                        events.append((round(second/60), f"{scorer.name} scored for {team1.name}"))
                    else:
                        events.append((round(second/60), f"{scorer.name} scored for {team1.name} and was assisted by {assister.name}"))

            else:
                goalie = team1.random_player_by_position("GK")

                #goalie = random.choice([p for p in team1.players if p.position == "GK"])
                scoring_weight = []
                for p in team2.players:
                    if p.position == "FWD":
                        scoring_weight.extend([p] * 5)
                    elif p.position == "MID":
                        scoring_weight.extend([p] * 4)
                    elif p.position == "DEF":
                        scoring_weight.append(p)
                scorer = random.choice(scoring_weight)
                if random.random()*goalie.rating > random.random()*scorer.rating:
                    #shot saved
                    events.append((round(second/60), f"{goalie.name} saved {scorer.name}'s shot"))
                else: 
                    #shot scored   
                    score2 += 1
                    assister = random.choice([p for p in team2.players])
                    if assister == scorer:
                        events.append((round(second/60), f"{scorer.name} scored for {team2.name}"))
                    else:
                        events.append((round(second/60), f"{scorer.name} scored for {team2.name} and was assisted by {assister.name}"))
                    

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
    if score1 + score2 == 0:
        mvp = random.choice([p for p in team1.players or team2.players])
        return mvp
    else:
        scorers = [event.split()[0] for _, event in events if "scored" in event]
        mvp, _ = Counter(scorers).most_common(1)[0]
        return mvp



# --- Example Usage ---
if __name__ == "__main__":

    team1 = plymouth_argyle
    team2 = chelsea
    league_array = [plymouth_argyle, arsenal, chelsea, famalicao]

    for team in league_array:
        if team == team1 or team == team2:
            team.display_team()
            print(team.display_team)

    # Simulate match
    score1, score2, events = simulate_match(team1, team2)
    generate_match_report(team1, team2, score1, score2, events)
