from aiohttp import web
from bson.objectid import ObjectId
from bson import json_util

async def leagues(request):
    try:
        mongo_client = request.app['mongoclient']
        leagues_collection = mongo_client["fantasy2021"]["leagues"]

        list_of_leagues = []
        async for document in leagues_collection.find():
            list_of_leagues.append(document)

        return web.Response(text=json_util.dumps(list_of_leagues),content_type="application/json")
    except Exception as e:
        error_message = {"error" : str(e)}
        return web.Response(text=json_util.dumps(error_message), content_type="application/json")


async def league(request):
    id = request.match_info['league_id']
    mongo_client = request.app['mongoclient']
    leagues_collection = mongo_client["fantasy2021"]["leagues"]
    document = await leagues_collection.find_one({'_id' : ObjectId(id)})

    return web.Response(text=json_util.dumps(document), content_type="application/json")

async def post_league(request):
    request_body = await request.json()
    mongo_client = request.app['mongoclient']

    players_collection = mongo_client["fantasy2021"]["players"]
    list_of_players = []
    async for document in players_collection.find():
        list_of_players.append(document)



    request_body["playerpool"] = list_of_players
    request_body["teams"] = []

    leagues_collection = mongo_client["fantasy2021"]["leagues"]
    result = await leagues_collection.insert_one(request_body)

    return web.json_response({'success' : result.acknowledged, '_id' : str(result.inserted_id)})

async def put_league(request):
    id = request.match_info['league_id']
    request_body = await request.json()
    mongo_client = request.app['mongoclient']
    leagues_collection = mongo_client["fantasy2021"]["leagues"]
    result = await leagues_collection.update_one({'_id': ObjectId(id)}, {'$set': request_body})
    return web.json_response({'success' : result.acknowledged})





