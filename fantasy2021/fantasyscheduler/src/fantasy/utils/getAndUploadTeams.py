import pytz
from fantasy.db.mongo import searchPlayer,addTeams
file = r"C:\Users\pachanta\fantasy\parseCode\teams.csv"
teamsList = {}
india = pytz.timezone('Asia/Calcutta')

def parseTeamInfo(teamInfo):
    info = teamInfo.split(",")
    name = info[0].strip()
    team = info[1].strip()
    nationality = info[2].strip()
    type = info[3].strip()
    base_price = info[4].strip()
    sold_price = info[5].strip()
    owner = info[6].strip()

    _id = searchPlayer(name)["_id"]


    player =  {
        # "profile_num": profile_num,
        "name": name,
        "team": team,
        "nationality": nationality,
        "type": type,
        "base_price": base_price,
        "sold_price": sold_price,
        "owner": owner
    }

    if not owner in teamsList:
        teamsList[owner] = {
            "team_name" : owner,
            "players" : [],
            "purse" : 45,
            "purse_remaining" : 45
        }

    # start = india.localize(datetime.strptime('2020-09-18 00:00:00.000000', '%Y-%m-%d %H:%M:%S.%f'))
    # end = india.localize(datetime.strptime('2020-11-12 23:59:00.000000', '%Y-%m-%d %H:%M:%S.%f'))

    start_match = 1
    end_match = 56

    teamsList[owner]["players"].append({
        "_id" : _id,
        "start_match" : start_match,
        "end_match" : end_match,
        "info" : player
    })
    teamsList[owner]["purse_remaining"] = teamsList[owner]["purse_remaining"] - float(sold_price)


for line in open(file, 'r', encoding='utf8').readlines():
    parts = line.split(",,")
    parseTeamInfo(parts[0].strip())
    parseTeamInfo(parts[1].strip())


teams = []
count = 1
for k,v in teamsList.items():
    v.update({
        '_id' : count
    })
    teams.append(v)
    count = count + 1

addTeams(teams)

