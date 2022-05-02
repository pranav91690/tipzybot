import requests
from bs4 import BeautifulSoup
import time
import re
import editdistance
import json

matchPattern = r"\/cricket-stats\/player\/(\d+)\/(.+)"
matchPattern2 = r"https://www\.cricbuzz\.com\/profiles\/(\d+)\/(.+)"

with open(r"C:\Users\pachanta\tipzybot\tipzybot\fantasy2021\fantasyscheduler\ipl2022teams.csv") as file:
    lines = file.readlines()
    teams = {}
    for line in lines[1:]:
        data = line.split(",")
        owner = data[8].strip()
        if owner:
            if not owner in teams:
                teams[owner] = []
            teams[owner].append(data)
        # else:
        #     if not "free" in teams:
        #         teams["free"] = []
        #
        #     teams["free"].append(data)

    players_with_ids_and_teams = []



playerMasterListMap = {}
with open("playerMasterList.csv","r") as file:
    for line in file:
        data = line.split(",")

        playerMasterListMap[data[1].rstrip()] = data[0]


finalPlayersList = []
soldPlayers = set()

for k, v in teams.items():
    for player in v:
        finalPlayer = []
        name = str(player[1]).strip()
        lowerCaseName = [x.lower() for x in name.split(" ")]
        cbSearchName = "+".join(lowerCaseName)
        cbMatchName = "-".join(lowerCaseName)
        if cbMatchName in playerMasterListMap:

            finalPlayer.extend(player[:9])
            finalPlayer.append(cbMatchName)
            finalPlayer.append(playerMasterListMap[cbMatchName])
            soldPlayers.add(int(playerMasterListMap[cbMatchName]))

        else:
            if name == "J Suchith":
                finalPlayer.extend(player[:9])
                finalPlayer.append("jagadeesha-suchith")
                finalPlayer.append("10357")
                soldPlayers.add(int("10357"))

            elif name == "K Gowtham":
                finalPlayer.extend(player[:9])
                finalPlayer.append("krishnappa-gowtham")
                finalPlayer.append("8925")
                soldPlayers.add(int("8925"))
            else:
                minDistance = None
                minKey = ""
                for key in playerMasterListMap.keys():
                    distance = editdistance.eval(cbMatchName,key)
                    # print(distance,cbMatchName,key)
                    if not minDistance:
                        minDistance = distance
                    if distance < minDistance:
                        minDistance = distance
                        minKey = key

                finalPlayer.extend(player[:9])
                finalPlayer.append(minKey)
                finalPlayer.append(playerMasterListMap[minKey])
                soldPlayers.add(int(playerMasterListMap[minKey]))

            # print(finalPlayer)

        finalPlayersList.append(finalPlayer)
        # print(finalPlayer)

print("Sold Players")
# print(len(soldPlayers))


for k,v in playerMasterListMap.items():
    if not int(v) in soldPlayers:
        # print(k,v)
        name = " ".join([x.title() for x in k.split("-")])
        # print("(((((((((")
        # print(name)
        finalPlayersList.append(["",name,"","","","","","","Open",k,v])


print(len(finalPlayersList))
# with open(r"players_with_ids_and_teams.csv","w") as outputfile:
#     for player in finalPlayersList:
#         print(player)
#         outputfile.write(",".join(player) + "\n")

with open(r"players_with_ids_and_teams.json","w") as outputfile:
    players = {}
    for player in finalPlayersList:
        # print(player[8])
        if not player[8] in players:
            players[player[8]] = []
        finalPlayer = []
        finalPlayer.extend(player)
        finalPlayer.append(0)
        finalPlayer.append(100)

        players[player[8]].append(finalPlayer)

        # print(finalPlayer)



    '''
        Serial Number
        Name
        Team
        Type
        Tier
        Base Price
        Sold Price
        Owner
        cbName
        id
        start
        end
    '''
    playersPlus = {}
    playersPlus["name"] = "How the fuck did we pick 15 players from SRH"
    playersPlus["teams"] = []
    playersPlus["open"] = []

    for k,v in players.items():
        if k == "Open":

            for player in v:
                playerplus = {
                    "snum" : player[0],
                    "name" : player[1],
                    "team" : player[2],
                    "nationality": player[3],
                    "type" : player[4],
                    "tier" : player[5],
                    "base_price" : player[6],
                    "sold_price" : player[7],
                    "owner" : player[8],
                    "cbName" : player[9],
                    "id" : player[10],
                    "start" : 0,
                    "end" : 100,
                }

                playersPlus["open"].append(playerplus)
        else:

            teamtemp = {}
            teamtemp["name"] = k
            teamtemp["players"] = []

            for player in v:
                playerplus = {
                    "snum" : player[0],
                    "name" : player[1],
                    "team" : player[2],
                    "nationality": player[3],
                    "type" : player[4],
                    "tier" : player[5],
                    "base_price" : player[6],
                    "sold_price" : player[7],
                    "owner" : player[8],
                    "cbName" : player[9],
                    "id" : player[10],
                    "start" : 0,
                    "end" : 100,
                    "active" : 1
                }

                teamtemp["players"].append(playerplus)

            playersPlus["teams"].append(teamtemp)

    print(playersPlus["open"])

    outputfile.write(json.dumps(playersPlus,indent=4, sort_keys=True))




