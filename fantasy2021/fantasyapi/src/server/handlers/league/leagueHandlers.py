from aiohttp import web
from bson.objectid import ObjectId
from bson import json_util
from server.points.calculatePoints import calculatePoints
import json

async def leagues(request):
    try:
        mongo_client = request.app['mongoclient']
        leagues_collection = mongo_client["ipl2022"]["league"]

        list_of_leagues = await leagues_collection.distinct()

        return web.Response(text=json_util.dumps(list_of_leagues),content_type="application/json")
    except Exception as e:
        error_message = {"error" : str(e)}
        return web.Response(text=json_util.dumps(error_message), content_type="application/json")


async def get_league(request):
    mongo_client = request.app['mongoclient']
    leagues_collection = mongo_client["ipl2022"]["league"]
    print(request.match_info)

    if 'league_id' not in request.match_info:

        leagues =  []
        async for match in leagues_collection.find():
            leagues.append(match)

        return web.Response(text=json_util.dumps(leagues), content_type="application/json")

    else:
        id = request.match_info['league_id']
        document = await leagues_collection.find_one({'_id' : ObjectId(id)})
        return web.Response(text=json_util.dumps(document), content_type="application/json")

async def post_league(request):
    request_body = await request.json()
    mongo_client = request.app['mongoclient']
    league_collection = mongo_client["ipl2022"]["league"]
    result = await league_collection.insert_one(request_body)
    return web.json_response({'success' : result.acknowledged, '_id' : str(result.inserted_id)})

async def put_league(request):
    id = request.match_info['league_id']
    request_body = await request.json()
    mongo_client = request.app['mongoclient']
    leagues_collection = mongo_client["ipl2022"]["league"]
    result = await leagues_collection.replace_one({'_id': ObjectId(id)}, request_body)
    return web.json_response({'success' : result.acknowledged})




async def getLeagueScores(request):
    id = request.match_info['league_id']

    print("Got Request to Get Score for league id {}".format(id))

    try:
        mongo_client = request.app['mongoclient']
        matches_collection = mongo_client["ipl2022"]["matches"]
        leagues_collection = mongo_client["ipl2022"]["league"]
        scores_collection = mongo_client["ipl2022"]["scores"]


        league = await leagues_collection.find_one({'_id' : ObjectId(id)})

        cumulative_points = {}
        scores_list = []

        matchesMap = {}
        async for match in matches_collection.find({}):
            matchesMap[match["_id"]] = match["number"]

        for team in league["teams"]:
            owner_name = team["name"]
            # scores_list.append(owner_name)

            players = list(map(lambda x : x["id"],team["players"]))
            playersMap = dict(map(lambda x : (x["id"],x),team["players"]))

            async for score in scores_collection.find({"player_id": {"$in": players}}):
                player_id = score["player_id"]
                start = int(playersMap[player_id]["start"])
                end = int(playersMap[player_id]["end"])
                match_num = int(matchesMap[score["match_id"]])

                if start <= match_num <= end:
                    points = calculatePoints(score)

                    if not owner_name in cumulative_points:
                        cumulative_points[owner_name] = {}

                    if not "players" in cumulative_points[owner_name]:
                        cumulative_points[owner_name]["players"] = {}

                    if not score["player_id"] in cumulative_points[owner_name]["players"]:
                        cumulative_points[owner_name]["players"][score["player_id"]] = {}

                    current_points = cumulative_points[owner_name]["players"][score["player_id"]]

                    for k, v in points.items():
                        if not k in current_points:
                            current_points[k] = v
                        else:
                            if k == "points":
                                current_points[k] += v
                            elif k == "categories":
                                for category, value in v.items():
                                    if not category in current_points[k]:
                                        current_points[k][category] = 0
                                    current_points[k][category] += int(value)

                    cumulative_points[owner_name]["players"][score["player_id"]] = current_points


        openPlayers = list(map(lambda x: x["id"], league["open"]))
        openPlayersMap = dict(map(lambda x: (x["id"], x), league["open"]))

        async for score in scores_collection.find({"player_id": {"$in": openPlayers}}):
            player_id = score["player_id"]
            start = int(openPlayersMap[player_id]["start"])
            end = int(openPlayersMap[player_id]["end"])
            match_num = int(matchesMap[score["match_id"]])

            if start <= match_num <= end:
                points = calculatePoints(score)

                if not "open" in cumulative_points:
                    cumulative_points["open"] = {}

                if not "players" in cumulative_points["open"]:
                    cumulative_points["open"]["players"] = {}

                if not score["player_id"] in cumulative_points["open"]["players"]:
                    cumulative_points["open"]["players"][score["player_id"]] = {}

                current_points = cumulative_points["open"]["players"][score["player_id"]]

                for k, v in points.items():
                    if not k in current_points:
                        current_points[k] = v
                    else:
                        if k == "points":
                            current_points[k] += v
                        elif k == "categories":
                            for category, value in v.items():
                                if not category in current_points[k]:
                                    current_points[k][category] = 0
                                current_points[k][category] += int(value)

                cumulative_points["open"]["players"][score["player_id"]] = current_points





        for k, v in cumulative_points.items():
            score = {}
            points = sum(list(map(lambda x: x["points"], list(v["players"].values()))))
            score["owner"] = k
            score["points"] = points
            score["players"] = v["players"]
            scores_list.append(score)



        print("Done Getting Score")
        return web.Response(text=json_util.dumps(scores_list), content_type="application/json")

    except Exception as e:
        print("Received an error while getting score -> " + str(e))
        error = {"error" : str(e)}
        return web.Response(text=json_util.dumps(error), content_type="application/json")





