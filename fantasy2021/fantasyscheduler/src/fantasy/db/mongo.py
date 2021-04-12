from pymongo import MongoClient, UpdateOne
client = MongoClient('mongodb://mongo:27017/')
fantasy = client["fantasy2021"]

def addMatches(matches):
    operations = []
    for match in matches:
        operations.append(UpdateOne({"_id" : match["_id"]},{"$set" : match}, upsert=True))

    fantasy.matches.bulk_write(operations)

def addPlayers(players):
    fantasy.players.insert_many(players)

def searchPlayerRegex(playerName):
    return fantasy.players.find_one({
        'name' : {'$regex': playerName}
    })

def searchPlayer(playerName):
    return fantasy.players.find_one({
        'name' : playerName
    })

def addTeams(teams):
    fantasy.teams.insert_many(teams)

def getMatches():
    return fantasy.matches.find({})

def getMatchesBetweenDates(start,end):
    return fantasy.matches.find({
        'time' : {
            '$gte' : start,
            '$lte' : end
        }
    })

def addScores(scores):
    operations = []
    for score in scores:
        operations.append(UpdateOne({"_id" : score["_id"]},{"$set" : score}, upsert=True))

    fantasy.scores.bulk_write(operations)