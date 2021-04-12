def calculatePoints(stats):
    # Runs * 1
    # sr = runs - balls
    # 4s * 1
    # 6s * 3
    # duck * -10
    #     #
    #     # catches * 10
    #     # runs outs * 10
    #     # stumping * 10
    #     # mom * 50
    #     # wickets * 25
    #     # balls - runs

    runs, bat_milestone, fours, sixes, sr, duck, catches, runouts, stumpings, wickets, bowl_milestone, econ_rate, maidens, run_penalty, mom = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

    # print(stats)

    # batting
    if "runs" in stats:
        runs = int(stats["runs"]) * 1
        bat_milestone = 0
        if 25 <= runs < 50:
            bat_milestone = 5
        elif 50 <= runs < 75:
            bat_milestone = 15
        elif 75 <= runs < 100:
            bat_milestone = 25
        elif 100 <= runs < 125:
            bat_milestone = 40
        elif runs >= 125:
            bat_milestone = 75

        sr = runs - int(stats["balls"])

        if runs == 0 and stats["dismissal"] != "not out":
            duck = -10

    if "4s" in stats:
        fours = int(stats["4s"]) * 1

    if "6s" in stats:
        sixes = int(stats["6s"]) * 3


    # fielding
    if "catch" in stats:
        catches = int(stats["catch"]) * 10
    if "run_out" in stats:
        runouts = int(stats["run_out"]) * 10
    if "stumped" in stats:
        stumpings = int(stats["stumped"]) * 10
    if "cbowled" in stats:
        catches = catches + int(stats["cbowled"]) * 10


    # bowling
    if "wickets" in stats:
        wickets = int(stats["wickets"]) * 25
        wicks = int(stats["wickets"])
        bowl_milestone = 0
        if wicks == 2:
            bowl_milestone = 10
        elif  wicks == 3:
            bowl_milestone = 25
        elif  wicks == 4:
            bowl_milestone = 40
        elif  wicks == 5:
            bowl_milestone = 75
        elif wicks > 5:
            bowl_milestone = 100

    if "balls_bowled" in stats and "runs_given" in stats:
        erate = int(stats["balls_bowled"]) * 1.5 - int(stats["runs_given"])
        if erate >= 0:
            econ_rate = erate * 2
        else:
            econ_rate = erate

    if "maidens"  in stats:
        maidens = int(stats["maidens"]) * 30

    if "runs_given" in stats:
        if int(stats["runs_given"]) > 50:
            run_penalty  = -10

    if "mom" in stats:
        mom = 50

    final_points = {
        "runs" : runs,
        "bat_milestone" : bat_milestone,
        "fours" : fours,
        "sixes" : sixes,
        "sr" : sr,
        "duck" : duck,
        "catches" : catches,
        "runouts" : runouts,
        "stumpings" : stumpings,
        "wickets" : wickets,
        "bowl_milestone" : bowl_milestone,
        "econ_rate" : econ_rate,
        "maidens" : maidens,
        "run_penalty" : run_penalty,
        "mom" : mom
    }

    total = sum(final_points.values())
    non_zero_cats = dict(filter(lambda v : v[1] != 0, final_points.items()))


    return {
        "name" : stats["name"].strip(),
        "points" : total,
        "categories" : non_zero_cats
    }