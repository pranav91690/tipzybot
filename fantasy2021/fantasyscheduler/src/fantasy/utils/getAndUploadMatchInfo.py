import requests
from bs4 import BeautifulSoup
from fantasy.db.mongo import addMatches
import pytz

def addAllMatches():
    print("Adding Matches")
    india = pytz.timezone('Asia/Calcutta')

    r = requests.get("https://www.cricbuzz.com/cricket-series/3472/indian-premier-league-2021/matches")
    soup = BeautifulSoup(r.content, "html.parser")

    div_tags = soup.find_all("div")
    match_tags = []
    for tag in div_tags:
        attrs = tag.attrs
        if 'class' in attrs and 'cb-srs-mtchs-tm' in attrs["class"]:
            match_tags.append(tag)

    matches = []

    for i in range(0,len(match_tags),2):
        link_tag = match_tags[i]
        time_tag = match_tags[i+1]

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
            matches.append(match)

    addMatches(matches)