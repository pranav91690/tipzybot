from fantasy.cricbuzz.parseScores import getScores

scores_url = "https://www.cricbuzz.com/live-cricket-scorecard/35627/kkr-vs-mi-5th-match-indian-premier-league-2021"
mom_url = "https://www.cricbuzz.com/live-cricket-scores/35627/kkr-vs-mi-5th-match-indian-premier-league-2021"
match_id = "35627"
scores = getScores(match_id,scores_url,mom_url,False)
for score in scores:
    print(score)
