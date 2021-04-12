from aiohttp import web
from bson import json_util
from server.points.calculatePoints import calculatePoints

async def getScores(request):
    print("Got Request to Get Score")
    try:
        mongo_client = request.app['mongoclient']
        players_collection = mongo_client["fantasy2021"]["players"]
        scores_collection = mongo_client["fantasy2021"]["scores"]

        owners = ["Ram", "Pranav", "Avadesh", "Sauri", "Sree", "Sheky"]
        cumulative_points = {}

        for owner in owners:
            owner_players = []
            async for player in players_collection.find({"owner": owner}):
                owner_players.append(str(player["_id"]))

            async for score in scores_collection.find({"player_id": {"$in": owner_players}}):
                points = calculatePoints(score)

                if not owner in cumulative_points:
                    cumulative_points[owner] = {}

                if not "players" in cumulative_points[owner]:
                    cumulative_points[owner]["players"] = {}

                if not score["player_id"] in cumulative_points[owner]["players"]:
                    cumulative_points[owner]["players"][score["player_id"]] = {}

                current_points = cumulative_points[owner]["players"][score["player_id"]]

                for k, v in points.items():
                    if not k in current_points:
                        current_points[k] = v
                    else:
                        if k == "points":
                            current_points[k] += v
                        elif k == "categories":
                            for category in v:
                                current_points[k][category] += category

                cumulative_points[owner]["players"][score["player_id"]] = current_points

        scores_list = []

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


