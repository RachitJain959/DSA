# In a tournament teams are marked from a to z We are given a sequence of winning teams in a tournament.
# Find the team with just one win in the entire tournament and return its index.
# If there are multiple such teams, return the one with the earliest win Le occurring first, if no such team, return-1,
#
# Example 1:
# Input: s="acabsecs"
# Output: 3
#
# Example 2:
# Input: s= "finse"
# Output: 0
#
# Example 3:
# Input: s="aabb"
# Output: -1

def findTeamWithOneWin(s):
    team_wins = {}  # Dictionary to store the number of wins for each team
    team_order = []  # List to store the order of appearance of teams

    for i, team in enumerate(s):
        if team in team_wins:
            team_wins[team] += 1
        else:
            team_wins[team] = 1
            team_order.append((team, i))

    for team, wins in team_wins.items():
        if wins == 1:
            # Find the first team with one win
            return min(team_order, key=lambda x: x[1] if x[0] == team else float('inf'))[1]

    return -1  # No team with one win found


# Test cases
print(findTeamWithOneWin("acabsecs"))  # Output: 3
print(findTeamWithOneWin("finse"))  # Output: 0
print(findTeamWithOneWin("aabb"))  # Output: -1
