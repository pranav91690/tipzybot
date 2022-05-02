from fantasy.cricbuzz.parseScores import getScores

scores_url = "https://www.cricbuzz.com/live-cricket-scorecard/45916/lsg-vs-csk-7th-match-indian-premier-league-2022"
mom_url = "https://www.cricbuzz.com/live-cricket-scores/45916/lsg-vs-csk-7th-match-indian-premier-league-2022"
match_id = "45916"
scores = getScores(match_id,scores_url,mom_url,False)
for score in scores:
    print(score)
