import random
import copy
from collections import Counter
from teams_database import plymouth_argyle, famalicao, chelsea, arsenal, liverpool, real_madrid, manchester_city, manchester_united, tottenham, newcastle, nottingham_forest, aston_villa, bournemouth, fulham, brighton, brentford, crystal_palace, everton, wolverhampton, west_ham, leichester, southampton
from game import Game, GameResult
from games_database import season2024_25

SCORE_PER_MIN_PROB = 0.05
CARD_PER_MIN_PROB = 0.036
SUB_PER_MIN_PROB = 0.036

FORWARD_SCORING_PROB = 0.60
MIDFIELD_SCORING_PROB = 0.30
DEFENDER_SCORING_PROB = 0.099


def simulate_match(home_team, away_team):

    score1 = 0
    score2 = 0
    yellow_cards = 0
    carded_players = []
    events = []


    for second in range(1, 90 * 60):
        # scoring event
        if random.random() < SCORE_PER_MIN_PROB/60:
            if random.random() < home_team.team_strength() / (home_team.team_strength() + away_team.team_strength()):
                score1 = simulate_scoring_event(home_team, away_team, second, events, score1)
            else:
                score2 = simulate_scoring_event(away_team, home_team, second, events, score2)
        
        # card event    
        if random.random() < CARD_PER_MIN_PROB/60:
            if random.random() < 0.50:
                carded_player = random.choice([p for p in home_team.players if p.position == "FWD" or p.position == "MID" or p.position == "DEF"])
            else:
                carded_player = random.choice([p for p in away_team.players if p.position == "FWD" or p.position == "MID" or p.position == "DEF"])
            if carded_player in carded_players or random.random() < .05:
                carded_player.team.red_cards += 1
                events.append((round(second/60), f"{carded_player.name} ({carded_player.team.abbr}) was given a red card"))
                carded_player.team.remove_player(carded_player)
            else:
                yellow_cards += 1
                events.append((round(second/60), f"{carded_player.name} ({carded_player.team.abbr}) was given a yellow card"))
                carded_players.append(carded_player)
        # forfeit  
        if home_team.red_cards == 5:
            events.append((round(second/60), f"{away_team.name} forfeit due to recieving five red cards"))
            game = Game(home_team, away_team, score1, score2, events, 0,00) 
            return game
        if away_team.red_cards == 5:
            events.append((round(second/60), f"{away_team.name} forfeit due to recieving five red cards"))
            game = Game(home_team, away_team, score1, score2, events, 0,00) 
            return game

        if second > 60 * 60:
            if random.random() < SUB_PER_MIN_PROB/60:
                if random.random() < 0.50:
                    pass
                # sub on sub one
                # else
                # sub on team two
        
    game = Game(home_team, away_team, score1, score2, events, 0,00) 
    return game

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
        if scorer == None:
            #shot never happened
            pass
        elif random.random()*goalie.rating > random.random()*scorer.rating:
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

def generate_match_report(game):
    print(f"\n🏁 Final Score: {game.team1.name} {game.score1} - {game.score2} {game.team2.name}")
    print("📜 Match Events:")
    for minute, event in game.events:
        print(f"  {minute}' - {event}")

    if game.events:
        mvp = find_mvp(game.events)
        print(f"\n🌟 Man of the Match: {mvp}")
    else:
        print("\nNo goals were scored.")

def find_mvp(game):
    if game.score1 + game.score2 == 0:
        mvp = random.choice([p for p in game.team1.players or game.team2.players])
        return mvp
    else:
        scorers = [event.split()[0] for _, event in game.events if "scored" in event]
        mvp, _ = Counter(scorers).most_common(1)[0]
        return mvp



# --- Example Usage ---
if __name__ == "__main__":

    # team1 = arsenal
    # team2 = real_madrid
    # league_array = [plymouth_argyle, famalicao, chelsea, arsenal, liverpool, real_madrid, man_city, man_utd, tottenham, newcastle, nottingham_forest, aston_villa, bournemouth, fulham, brighton, brentford, crystal_palace, everton, wolves, west_ham, leicester_city, southampton]

    # for team in league_array:
    #     if team == team1 or team == team2:
    #         team.display_team()
    #         print(team.display_team)

    # # Simulate match
    # current_game = simulate_match(team1, team2)
    # generate_match_report(current_game)

    number_of_game_results_correct = 0
    number_of_home_wins = 0
    number_of_home_wins_correct = 0

    number_of_away_wins = 0
    number_of_away_wins_correct = 0
    
    number_of_draws = 0
    number_of_draws_correct = 0

    for actual_game in season2024_25:
        
        print(f"\nActual Result:")
        print(f"{actual_game.home_team.name} vs {actual_game.away_team.name}: {actual_game.score[actual_game.home_team.abbr]} - {actual_game.score[actual_game.away_team.abbr]}")
        print(f"{actual_game.result()}")

        home_team_copy = copy.deepcopy(actual_game.home_team)
        away_team_copy = copy.deepcopy(actual_game.away_team)

        # Simulate match
        predited_game = simulate_match(home_team_copy, away_team_copy)

        print(f"Predicted Result:")
        print(f"{predited_game.home_team.name} vs {predited_game.away_team.name}: {predited_game.score[predited_game.home_team.abbr]} - {predited_game.score[predited_game.away_team.abbr]}")
        print(f"{predited_game.result()}")

        sse_home = (predited_game.score[actual_game.home_team.abbr] - actual_game.score[actual_game.home_team.abbr])**2
        sse_away = (predited_game.score[actual_game.away_team.abbr] - actual_game.score[actual_game.away_team.abbr])**2
        print(f"SSE Home: {sse_home}")
        print(f"SSE Away: {sse_away}")
        print(f"SSE Total: {sse_home + sse_away}")
        print(f"-----------------------------------")
        # print(f"Predicted Result: {predicted_result}")
        # print(f"Actual Result: {actual_game.result()}")
        # print(f"Score: {predicted_score} - {actual_game.score}")
        if predited_game.result() == actual_game.result():
            number_of_game_results_correct += 1
        
        if actual_game.result() == GameResult.HOME_WIN:
            number_of_home_wins += 1
            if predited_game.result() == actual_game.result():
                number_of_home_wins_correct += 1
        
        if actual_game.result() == GameResult.AWAY_WIN:
            number_of_away_wins += 1
            if predited_game.result() == actual_game.result():
                number_of_away_wins_correct += 1
        
        if actual_game.result() == GameResult.DRAW:
            number_of_draws += 1
            if predited_game.result() == actual_game.result():
                number_of_draws_correct += 1

    print(f"Home wins correct {number_of_home_wins_correct} out of {number_of_home_wins}.")
    print(f"Away wins correct {number_of_away_wins_correct} out of {number_of_away_wins}.")
    print(f"Draws correct {number_of_draws_correct} out of {number_of_draws}.")


    print(f"Number of game results correct: {number_of_game_results_correct} out of {len(season2024_25)}")
    print(f"Percentage of game results correct: {number_of_game_results_correct/len(season2024_25)*100}%")
    