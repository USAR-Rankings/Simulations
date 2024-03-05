import math
import random as random



bracket_keys={
    "Open":["A1","C4","B2","D3","D1","A4","C2","B3","B1","D4","A2","C3","C1","B4","A3","D2"],
    "A":["A1","BYE","B3","C3","A2","BYE","C2","B4","B1","BYE","A3","C4","C1","BYE","B2","A4"],
    "B":["A1","BYE","B3","C3","B2","BYE","C2","A4","B1","BYE","A3","C4","C1","BYE","A2","B4"],
    "C":["A1","BYE","B3","C3","C2","BYE","B2","A4","B1","BYE","A3","C4","C1","BYE","A2","B4"],
    "8":['1', '8', '4', '5', '2', '7', '3', '6'],
    "16":['1', '16', '8', '9', '4', '13', '5', '12', '2', '15', '7', '10', '3', '14', '6', '11'],
    "32":['1', '32', '16', '17', '8', '25', '9', '24', '4', '29', '13', '20', '5', '28', '12', '21', '2', '31', '15', '18', '7', '26', '10', '23', '3', '30', '14', '19', '6', '27', '11', '22']
}


def calc_prob(score1, score2):
    """
    Calculates the probability of team 2 winning the match based on a rating system.

    Parameters:
    - score1 (float): Rating score of team 1.
    - score2 (float): Rating score of team 2.

    Returns:
    - float: Probability of team 2 winning.
    """
    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (score1 - score2) / 25))


def play_game(team1, team2, team_dict):
    """
    Simulates a single game between two teams.

    Parameters:
    - team1 (str): Name of team 1.
    - team2 (str): Name of team 2.
    - team_dict (dict): Dictionary containing team ratings.

    Returns:
    - str: Name of the winning team.
    """
    cutoff = calc_prob(team_dict[team1], team_dict[team2])
    result = random.uniform(0, 1)
    if result > cutoff:
        return team1
    else:
        return team2


def best_of_3(team_1, team_2, td):
    """
    Simulates a best-of-3 series between two teams.

    Parameters:
    - team_1 (str): Name of team 1.
    - team_2 (str): Name of team 2.
    - td (dict): Dictionary containing team ratings.

    Returns:
    - str: Name of the winning team.
    """
    w_d = {team_1: 0, team_2: 0}
    while w_d[team_1] < 2 and w_d[team_2] < 2:
        winner = play_game(team_1, team_2, team_dict=td)
        w_d[winner] += 1
    if w_d[team_1] == 2:
        return team_1
    else:
        return team_2