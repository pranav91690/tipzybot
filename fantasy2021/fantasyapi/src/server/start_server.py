from aiohttp import web
from server.handlers.league.leagueHandlers import leagues,getLeagueScores
from server.handlers.scores.scoresHandlers import getScores
from server.handlers.genericHandlers import addPlayers,addLeagues,addMatches
from server.utils.utils import getLeagues,getPlayers,getMatches
import motor.motor_asyncio

async def create_app():
    app = web.Application()

    client = motor.motor_asyncio.AsyncIOMotorClient('mongo', 27017)

    app['mongoclient'] = client

    app.add_routes([
        web.get('/leagues',leagues),

        ## Not usin the below route for now -- so commnting them out!!
        # web.get('/league/{league_id}',league),
        # web.post('/league',post_league),
        # web.put('/league/{league_id}',put_league),
        # web.post('/team/{league_id}',post_team),
        # web.put('/team/{league_id}/{team_id}',put_team),

        #### <<< --- These are actual endpoints for now!!!
        web.get('/addplayers',addPlayers),
        web.get('/addleagues',addLeagues),
        web.get('/addmatches',addMatches),
        web.get('/league/{league_id}/getscores',getLeagueScores),
        web.get('/getscores',getScores)

        ## We shoud have more routes here -- can be grouped under scores handlers for now!!
        ## addPLayers, addMatches, addLeagues, tradePlayer,
    ])

    app['state'] = {}
    return app

if __name__ == '__main__':
    web.run_app(create_app())




