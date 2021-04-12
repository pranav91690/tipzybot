import requests
from bs4 import BeautifulSoup
from fantasy.db.mongo import addPlayers


links = {
    "RCB" : "https://www.cricbuzz.com/cricket-team/royal-challengers-bangalore/59/players",
    "MI" : "https://www.cricbuzz.com/cricket-team/mumbai-indians/62/players",
    "KKR" : "https://www.cricbuzz.com/cricket-team/kolkata-knight-riders/63/players",
    "CSK" : "https://www.cricbuzz.com/cricket-team/chennai-super-kings/58/players",
    "SRH" : "https://www.cricbuzz.com/cricket-team/sunrisers-hyderabad/255/players",
    "DC" : "https://www.cricbuzz.com/cricket-team/delhi-capitals/61/players",
    "RR" : "https://www.cricbuzz.com/cricket-team/rajasthan-royals/64/players",
    "KXIP" : "https://www.cricbuzz.com/cricket-team/kings-xi-punjab/65/players"
}

playersList = []


for team,link in links.items():
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')
    a_tags = soup.find_all("a")

    for a_tag in a_tags:
        if 'href' in a_tag.attrs and '/profiles' in a_tag.attrs["href"]:
            # print(a_tag.attrs["href"], a_tag.attrs["title"])
            profile_num = a_tag.attrs["href"].strip().split("/")[2]
            player_name = a_tag.attrs["title"].strip()
            playersList.append({
                "_id" : int(profile_num),
                "team" : team,
                "name" : player_name
            })

print(playersList)

addPlayers(playersList)


