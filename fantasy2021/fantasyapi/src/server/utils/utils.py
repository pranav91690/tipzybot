import json
import os
import requests
from bs4 import BeautifulSoup

def getPlayers():
    players = []
    with open('server/utils/data/players.json') as json_file:
        players = json.load(json_file)
    return players

def getLeagues():
    leagues = []
    for filename in os.listdir("server/utils/data/leagues"):
        if filename.endswith("json"):
            owners = []
            with open(os.path.join("server/utils/data/leagues",filename),'r') as file:
                owners = json.load(file)

            for owner in owners:
                leagues.append(owner)

    return leagues

def getMatches():
    r = requests.get("https://www.cricbuzz.com/cricket-series/3472/indian-premier-league-2021/matches")
    soup = BeautifulSoup(r.content, "html.parser")

    div_tags = soup.find_all("div")
    match_tags = []
    for tag in div_tags:
        attrs = tag.attrs
        if 'class' in attrs and 'cb-srs-mtchs-tm' in attrs["class"]:
            match_tags.append(tag)

    matches = []
    match_number = 1
    for i in range(0, len(match_tags), 2):
        link_tag = match_tags[i]
        time_tag = match_tags[i + 1]

        a_tags = link_tag.find_all("a")
        span_tags = time_tag.find_all("span")

        match = {}

        for tag in a_tags:
            if "class" in tag.attrs and "text-hvr-underline" in tag.attrs["class"]:
                link = tag["href"]
                parts = link.split("/")
                match["_id"] = str(parts[2])
                match["scorecard"] = "https://www.cricbuzz.com" + "/live-cricket-scorecard/" + "/".join(parts[2:])
                match["mom"] = "https://www.cricbuzz.com" + "/live-cricket-scores/" + "/".join(parts[2:])

        for tag in span_tags:
            if "class" in tag.attrs and "schedule-date" in tag.attrs["class"]:
                match["timestamp"] = tag["timestamp"]

        if "scorecard" in match:
            match["number"] = match_number
            match_number += 1
            matches.append(match)

    return matches