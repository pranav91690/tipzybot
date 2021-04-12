from aiohttp import web
from server.handlers.league.leagueHandlers import leagues,league,post_league,put_league
from server.handlers.team.teamHandlers import teams,team,post_team,put_team
from server.handlers.scores.scoresHandlers import getScores
import motor.motor_asyncio

async def create_app():
    app = web.Application()

    client = motor.motor_asyncio.AsyncIOMotorClient('mongo', 27017)


    app['mongoclient'] = client

    app.add_routes([
        web.get('/leagues',leagues),
        web.get('/league/{league_id}',league),
        web.post('/league',post_league),
        web.put('/league/{league_id}',put_league),
        web.post('/team/{league_id}',post_team),
        web.put('/team/{league_id}/{team_id}',put_team),
        web.get('/getscores',getScores)
    ])

    app['state'] = {}
    return app

if __name__ == '__main__':
    web.run_app(create_app())




