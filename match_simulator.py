import random
from collections import Counter
from teams_database import plymouth_argyle, famalicao, chelsea, arsenal

SCORE_PER_MIN_PROB = 0.05
CARD_PER_MIN_PROB = 0.036
SUB_PER_MIN_PROB = 0.036

FORWARD_SCORING_PROB = 0.60
MIDFIELD_SCORING_PROB = 0.30
DEFENDER_SCORING_PROB = 0.099


def simulate_match(team1, team2):

    score1 = 0
    score2 = 0
    yellow_cards = 0
    red_cards = 0
    carded_players = []
    events = []


    for second in range(1, 90 * 60):
        # scoring event
        if random.random() < SCORE_PER_MIN_PROB/60:
            if random.random() < team1.team_strength() / (team1.team_strength() + team2.team_strength()):
                score1 = simulate_scoring_event(team1, team2, second, events, score1)
            else:
                score2 = simulate_scoring_event(team2, team1, second, events, score2)
        
        # card event    
        if random.random() < CARD_PER_MIN_PROB/60:
            if random.random() < 0.50:
                carded_player = random.choice([p for p in team1.players if p.position == "FWD" or p.position == "MID" or p.position == "DEF"])
            else:
                carded_player = random.choice([p for p in team2.players if p.position == "FWD" or p.position == "MID" or p.position == "DEF"])
            if carded_player in carded_players or random.random() < .05:
                red_cards += 1
                events.append((round(second/60), f"{carded_player.name} ({carded_player.team.abbr}) was given a red card"))
                carded_player.team.remove(carded_player)
            else:
                yellow_cards += 1
                events.append((round(second/60), f"{carded_player.name} ({carded_player.team.abbr}) was given a yellow card"))
                carded_players.append(carded_player)

        if second > 60 * 60:
            if random.random() < SUB_PER_MIN_PROB/60:
                if random.random() < 0.50:
                    pass
                # sub on sub one
                # else
                # sub on team two
            
    return score1, score2, events 


def simulate_scoring_event(attacking_team, defending_team, second, events, attacking_team_score): 

        scoring_probabilty = random.random() 
        if scoring_probabilty < FORWARD_SCORING_PROB:
            scorer = attacking_team.random_player_by_position("FWD")
        elif scoring_probabilty < FORWARD_SCORING_PROB + MIDFIELD_SCORING_PROB:
            scorer = attacking_team.random_player_by_position("MID")
        elif scoring_probabilty < FORWARD_SCORING_PROB + MIDFIELD_SCORING_PROB + DEFENDER_SCORING_PROB:
            scorer = attacking_team.random_player_by_position("DEF")
        else:
            scorer = attacking_team.random_player_by_position("GK")

        goalie = defending_team.random_player_by_position("GK")

        if random.random()*goalie.rating > random.random()*scorer.rating:
            #shot saved
            events.append((round(second/60), f"{goalie.name} ({defending_team.abbr}) saved {scorer.name}'s ({attacking_team.abbr}) shot"))
        else: 
            #shot scored   
            attacking_team_score += 1
            assister = random.choice([p for p in attacking_team.players])
            if assister == scorer:
                events.append((round(second/60), f"{scorer.name} scored for {attacking_team.name}"))
            else:
                events.append((round(second/60), f"{scorer.name} scored for {attacking_team.name} and was assisted by {assister.name}"))

        
        return attacking_team_score

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
    team2 = famalicao
    league_array = [plymouth_argyle, arsenal, chelsea, famalicao]

    for team in league_array:
        if team == team1 or team == team2:
            team.display_team()
            print(team.display_team)

    # Simulate match
    score1, score2, events = simulate_match(team1, team2)
    generate_match_report(team1, team2, score1, score2, events)
