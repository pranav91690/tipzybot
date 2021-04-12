import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["fantasy2021"]
mycol = mydb["teams"]


with open('/Users/pranav/fantasy2021/fantasy2021/team.json') as json_file:
    data = json.load(json_file)

teamNames = []
for team in data:
    teamNames.append({
        "name" : str(team)
    })

x = mycol.insert_many(teamNames)

print(x)
