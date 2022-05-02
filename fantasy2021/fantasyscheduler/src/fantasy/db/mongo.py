from pymongo import MongoClient, UpdateOne
client = MongoClient('mongodb://mongo:27017/')
fantasy = client["ipl2022"]

def addMatches(matches):
    operations = []
    for match in matches:
        operations.append(UpdateOne({"_id" : match["_id"]},{"$set" : match}, upsert=True))

    fantasy.matches.drop()
    fantasy.matches.bulk_write(operations)

def addPlayers(players):
    operations = []
    for player in players:
        operations.append(UpdateOne({"_id": player["_id"]}, {"$set": player}, upsert=True))

    fantasy.players.bulk_write(operations)


def getMatches():
    return fantasy.matches.find({})

def addScores(scores):
    operations = []
    for score in scores:
        operations.append(UpdateOne({"_id" : score["_id"]},{"$set" : score}, upsert=True))

    fantasy.scores.bulk_write(operations)