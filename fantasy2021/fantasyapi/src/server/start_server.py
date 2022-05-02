from aiohttp import web
from server.handlers.league.leagueHandlers import get_league,post_league,put_league,leagues,getLeagueScores
from server.handlers.points.pointsHandlers import get_points
from server.handlers.genericHandlers import addPlayers,addLeagues,addMatches,get_matches

import motor.motor_asyncio

async def create_app():
    app = web.Application()

    client = motor.motor_asyncio.AsyncIOMotorClient('mongo', 27017)

    app['mongoclient'] = client

    app.add_routes([
        web.get('/leagues',leagues),

        # Adding a comment because why  not

        ## Not using the below route for now -- so commnting them out!!
        web.get('/league',get_league),
        web.get('/league/{league_id}',get_league),
        web.post('/league',post_league),
        web.put('/league/{league_id}',put_league),
        web.get('/match',get_matches),
        # web.post('/team/{league_id}',post_team),
        # web.put('/team/{league_id}/{team_id}',put_team),

        #### <<< --- These are actual endpoints for now!!!
        web.get('/addplayers',addPlayers),
        web.get('/addleagues',addLeagues),
        web.get('/addmatches',addMatches),
        web.get('/league/{league_id}/getscores',getLeagueScores),
        web.get('/points',get_points)

        ## We shoud have more routes here -- can be grouped under points handlers for now!!
        ## addPLayers, addMatches, addLeagues, tradePlayer,
    ])

    app['state'] = {}
    return app

if __name__ == '__main__':
    web.run_app(create_app())




