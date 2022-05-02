import requests
from bs4 import BeautifulSoup
import re
from collections import OrderedDict
import pytz



india = pytz.timezone('Asia/Calcutta')


def updateFieldingInfo(playerId, type, profileMap):
    if playerId in profileMap:
        new_val = 1
        if type in profileMap[playerId]:
            new_val = profileMap[playerId][type] + new_val
        profileMap[playerId].update({
            type : new_val
        })

def updateBattingInfo(playerId, battingInfo,profileMap):
    if playerId in profileMap:
        profileMap[playerId].update(battingInfo)

def updateBowlingInfo(playerId, bowlingInfo,profileMap):
    if playerId in profileMap:
        profileMap[playerId].update(bowlingInfo)

def extractFieldingData(dismissal,profileMap,fullNames,fLastNames,lastNames,firstNames):
    re_run_out = "run out \((.+\/?)\)"
    # re_catch = "c (.+) b .+"
    re_catch = "c (?:\(sub\))?(.+) b .+"
    re_stump = "st (.+) b .+"
    re_cbolwed = "c and b (.+)"


    res = OrderedDict()
    res["cbowled"] = re_cbolwed
    res["run_out"] = re_run_out
    res["catch"] = re_catch
    res["stump"] = re_stump


    for k, r in res.items():
        m = re.search(r, dismissal)
        try:
            fielders = m.group(1)
            players = list(fielders.split('/'))

            for player in players:
                if "sub" in player:
                    player = player.split("[")[1].split("]")[0]

                p = player.strip().lower()
                if p in fullNames:
                    updateFieldingInfo(fullNames[p],k,profileMap)
                elif p in fLastNames:
                    updateFieldingInfo(fLastNames[p], k, profileMap)
                elif p in lastNames:
                    updateFieldingInfo(lastNames[p], k, profileMap)
                elif p in firstNames:
                    updateFieldingInfo(firstNames[p], k, profileMap)
                else:
                    # print("No Match",p)
                    continue
            break
        except:
            continue

def extractBattingInfo(batting_tag, profileMap,fullNames,fLastNames,lastNames,firstNames):
    meta = list(filter(lambda x: x != ' ', list(batting_tag.children)))
    try:
        batting_stats = [[meta[0].a.attrs['href'], meta[0].a.string.strip()], meta[1].span.string.strip(),
                         meta[2].string.strip(), meta[3].string.strip(), meta[4].string.strip(), meta[5].string.strip()]

        # name = batting_stats[0][1].strip()
        profile_num = batting_stats[0][0].split("/")[2].strip()
        dismissal = batting_stats[1].strip()
        runs = batting_stats[2].strip()
        bowls_faced = batting_stats[3].strip()
        fours = batting_stats[4].strip()
        sixes = batting_stats[5].strip()


        extractFieldingData(dismissal,profileMap,fullNames,fLastNames,lastNames,firstNames)

        stats = {}
        # stats["profile_num"] = profile_num
        # stats["name"] = name
        stats["runs"] = runs
        stats["balls"] = bowls_faced
        stats["4s"] = fours
        stats["6s"] = sixes
        stats["dismissal"] = dismissal

        updateBattingInfo(profile_num,stats, profileMap)

    except:
        return

def extractBowlingInfo(bowling_tag, profileMap):
    meta1 = list(filter(lambda x: x != ' ', list(bowling_tag.children)))
    try:
        bowling_stats = [[meta1[0].a.attrs['href'].strip(), meta1[0].a.string.strip()], meta1[1].string.strip(),
                         meta1[2].string.strip(), meta1[3].string.strip(), meta1[4].string.strip(),
                         meta1[5].string.strip(), meta1[6].string.strip()]

        # name = bowling_stats[0][1]
        profile_num = bowling_stats[0][0].split("/")[2].strip()
        overs = bowling_stats[1].strip()
        maidens = bowling_stats[2].strip()
        runs_conceded = bowling_stats[3].strip()
        wickets = bowling_stats[4].strip()

        r = overs.split(".")
        if len(r) > 1:
            balls = int(r[0]) * 6 + int(r[1])
        else:
            balls = int(r[0]) * 6

        stats = {}
        # stats["profile_num"] = profile_num
        # stats["name"] = name
        stats["balls_bowled"] = str(balls)
        stats["maidens"] = maidens
        stats["runs_given"] = runs_conceded
        stats["wickets"] = wickets

        updateBowlingInfo(profile_num ,stats, profileMap)
    except:
        return

def extractInningsData(innings_tag,profileMap,fullNames,fLastNames,lastNames,firstNames):
    # Get the Batting, Bowling,Fielding Info
    batting_tags = [] # This will contain the fielding tags as well! <--- cool
    bowling_tags = []
    div_tags = innings_tag.find_all("div")
    for div_tag in div_tags:
        attrs = div_tag.attrs
        if "class"  in attrs and "cb-scrd-itms" in attrs["class"]:
            length = len(list(div_tag.children))

            if length == 15:
                batting_tags.append(div_tag)
            elif length == 17:
                bowling_tags.append(div_tag)

    for batting_tag in batting_tags:
        extractBattingInfo(batting_tag,profileMap,fullNames,fLastNames,lastNames,firstNames)

    for bowling_tag in bowling_tags:
        extractBowlingInfo(bowling_tag,profileMap)

def updateMom(playerId,profileMap):
    profileMap[playerId].update({
        "mom": 1
    })

def getMom(url, profileMap):
    r1 = requests.get(url)
    soup1 = BeautifulSoup(r1.content, 'html.parser')
    div_tags = soup1.find_all("div")
    for tag in div_tags:
        attrs = tag.attrs
        if "class" in attrs and "cb-mom-itm" in attrs["class"]:
            a_tag = tag.a
            attrs_2 = a_tag.attrs
            player_id = attrs_2["href"].split("/")[2].strip()
            updateMom(player_id, profileMap)

def getScores(match_id,scores_url,mom_url):
    print("Getting Score")

    profileMap = {}
    fullNames = {}
    fLastNames = {}
    lastNames = {}
    firstNames = {}

    try:
        r = requests.get(scores_url)
        soup = BeautifulSoup(r.content, 'html.parser')

        playing_tags = []
        first_innings_tag = None
        second_innings_tag = None
        bench_tags = []

        div_tags = soup.find_all("div")
        for tag in div_tags:
            try:
                attrs = tag.attrs
                if tag.contents[0].strip() == "Playing":
                    playing_tags.append(tag)
                elif tag.contents[0].strip() == "Bench":
                    bench_tags.append(tag)
                elif 'id' in attrs and 'innings_1' in attrs["id"]:
                    first_innings_tag = tag
                elif 'id' in attrs and 'innings_2' in attrs["id"]:
                    second_innings_tag = tag
            except:
                continue

        for playing_tag in playing_tags:
            playersList = playing_tag.next_sibling.next_sibling
            a_tags = playersList.find_all("a")

            for tag in a_tags:
                attrs = tag.attrs
                if 'href' in attrs  and 'profiles' in attrs["href"]:
                    player_id = attrs["href"].split("/")[2].strip()
                    # name = tag.contents[0].strip().lower()
                    name = " ".join(attrs["href"].split("/")[3].split("-")).strip().lower()
                    fullNames[name] = player_id
                    # Well Consider only 1 and rest names for now!!
                    names = name.split(" ")
                    if len(names) > 1:
                        fname = names[0].strip()
                        lname = " ".join(names[1:]).strip()

                        fLastNames[fname[0] + ' ' + lname] = player_id
                        lastNames[lname] = player_id
                        firstNames[fname] = player_id

        for bench_tag in bench_tags:
            playersList = bench_tag.next_sibling.next_sibling
            a_tags = playersList.find_all("a")

            for tag in a_tags:
                attrs = tag.attrs
                if 'href' in attrs  and 'profiles' in attrs["href"]:
                    player_id = attrs["href"].split("/")[2].strip()
                    # name = tag.contents[0].strip().lower()
                    name = " ".join(attrs["href"].split("/")[3].split("-")).strip().lower()
                    fullNames[name] = player_id
                    # Well Consider only 1 and rest names for now!!
                    names = name.split(" ")
                    if len(names) > 1:
                        fname = names[0].strip()
                        lname = " ".join(names[1:]).strip()

                        fLastNames[fname[0] + ' ' + lname] = player_id
                        lastNames[lname] = player_id
                        firstNames[fname] = player_id


        for name,profileNumber in fullNames.items():
            profileMap[profileNumber] = {
                "name" : name
            }


        if first_innings_tag:
            extractInningsData(first_innings_tag,profileMap,fullNames,fLastNames,lastNames,firstNames)

        if second_innings_tag:
            # Get the Batting, Bowling,Fielding Info
            extractInningsData(second_innings_tag,profileMap,fullNames,fLastNames,lastNames,firstNames )

        getMom(mom_url, profileMap)

        scores = []

        for k,v in profileMap.items():
            v.update({
                "match_id" : match_id,
                "player_id" : k,
            })
            v["_id"] = int(str(match_id) + str(k))

            scores.append(v)

        # if insert:
        #     addScores(scores)

        print("Got " + str(len(scores)))

        return scores
    except Exception as e:
        print("Received Exception")
        print(str(e))