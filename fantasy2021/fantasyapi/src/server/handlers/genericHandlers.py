from aiohttp import web
from bson import json_util
from server.utils.utils import getLeagues,getPlayers
from pymongo import UpdateOne

async def addPlayers(request):
    try:
        mongo_client = request.app['mongoclient']
        players_collection = mongo_client["fantasy2021"]["players"]
        players = getPlayers()
        operations = []
        for player in players:
            operations.append(UpdateOne({"_id": player["_id"]}, {"$set": player}, upsert=True))

        await players_collection.bulk_write(operations)

        response = {
            "status" : "Inserted {} records".format(len(players))
        }

        return web.Response(text=json_util.dumps(response),content_type="application/json")

    except Exception as e:
        error_message = {"error": str(e)}
        return web.HTTPInternalServerError(text=json_util.dumps(error_message), content_type="application/json")


async def addLeagues(request):
    try:
        mongo_client = request.app['mongoclient']
        leagues_collection = mongo_client["fantasy2021"]["leagues"]
        leagues = getLeagues()
        operations = []

        for owner in leagues:
            operations.append(UpdateOne({"_id": owner["_id"]}, {"$set": owner}, upsert=True))

        await leagues_collection.bulk_write(operations)

        response = {
            "status": "Inserted {} records".format(len(leagues))
        }

        return web.Response(text=json_util.dumps(response), content_type="application/json")

    except Exception as e:
        error_message = {"error": str(e)}
        return web.HTTPInternalServerError(text=json_util.dumps(error_message), content_type="application/json")


async def addMatches(request):
    try:
        print("Adding Matches")

        mongo_client = request.app['mongoclient']
        matches_collection = mongo_client["fantasy2021"]["matches"]
        matches = []

        operations = []
        for match in matches:
            operations.append(UpdateOne({"_id": match["_id"]}, {"$set": match}, upsert=True))

        await matches_collection.bulk_write(operations)

        response = {
            "status" : "Inserted {} records".format(len(matches))
        }

        return web.Response(text=json_util.dumps(response),content_type="application/json")

    except Exception as e:
        error_message = {"error": str(e)}
        return web.HTTPInternalServerError(text=json_util.dumps(error_message), content_type="application/json")

async def get_matches(request):
    try:
        print("Getting Matches")
        mongo_client = request.app['mongoclient']
        matches_collection = mongo_client["ipl2022"]["matches"]
        matches =  []
        async for match in matches_collection.find():
            matches.append(match)

        return web.Response(text=json_util.dumps(matches), content_type="application/json")
    except Exception as e:
        error_message = {"error": str(e)}
        return web.HTTPInternalServerError(text=json_util.dumps(error_message), content_type="application/json")


async def addPlayer(request):
    try:
        pass
    except Exception as e:
        pass

