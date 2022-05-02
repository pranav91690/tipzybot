from aiohttp import web
from bson.objectid import ObjectId
from bson import json_util

async def tournaments(request):
    pass

async def post_tournament(request):
    request_body = await request.json()
    mongo_client = request.app['mongoclient']
    tournament_collection = mongo_client["fantasy"]["tournaments"]
    result = await tournament_collection.insert_one(request_body)