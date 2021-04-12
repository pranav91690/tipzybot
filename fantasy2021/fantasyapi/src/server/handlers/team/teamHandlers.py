from aiohttp import web
from bson.objectid import ObjectId
from bson import json_util

async def teams(request):
    mongo_client = request.app['mongoclient']
    teams_collection = mongo_client["fantasy2021"]["teams"]
    query = request.query
    league_id = str(query.get("league_id"))

    ## The teams are part of the leagues!!

    list_of_teams = []
    async for document in teams_collection.find({'league_id': {'$eq': league_id}}):
        list_of_teams.append(document)

    return web.Response(text=json_util.dumps(list_of_teams),content_type="application/json")

async def team(request):
    id = request.match_info['team_id']
    mongo_client = request.app['mongoclient']
    teams_collection = mongo_client["fantasy2021"]["teams"]
    document = await teams_collection.find_one({'_id' : ObjectId(id)})

    return web.Response(text=json_util.dumps(document), content_type="application/json")

async def post_team(request):
    request_body = await request.json()
    mongo_client = request.app['mongoclient']
    teams_collection = mongo_client["fantasy2021"]["teams"]
    result = await teams_collection.insert_one(request_body)

    return web.json_response({'success' : result.acknowledged, '_id' : str(result.inserted_id)})

async def put_team(request):
    id = request.match_info['team_id']
    request_body = await request.json()
    mongo_client = request.app['mongoclient']
    teams_collection = mongo_client["fantasy2021"]["teams"]
    result = await teams_collection.update_one({'_id': ObjectId(id)}, {'$set': request_body})
    return web.json_response({'success' : result.acknowledged})
