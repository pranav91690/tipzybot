from fantasy.cricbuzz.parseScores import getScores

scores_url = "https://www.cricbuzz.com/live-cricket-scorecard/35617/csk-vs-dc-2nd-match-indian-premier-league-2021"
mom_url = "https://www.cricbuzz.com/live-cricket-scores/35617/csk-vs-dc-2nd-match-indian-premier-league-2021"
match_id = "35617"
scores = getScores(match_id,scores_url,mom_url,False)
print(scores)
