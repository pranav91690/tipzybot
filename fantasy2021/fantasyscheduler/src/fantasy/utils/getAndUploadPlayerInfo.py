import requests
from bs4 import BeautifulSoup

players = []
urls = [16266,16271,16276,16281,16286,16291,16296,16301,16306,16311]
for url in urls:
    final_url = "https://www.cricbuzz.com/cricket-series/squads/4061/players/{}".format(str(url))
    print(final_url)
    r = requests.get(final_url)
    soup = BeautifulSoup(r.content, "html.parser")
    a_tags = soup.find_all("a")
    for tag in a_tags:
        attrs = tag.attrs
        if "href" in attrs and "/profiles/" in attrs["href"]:
            data = str(attrs["href"]).strip().split("/")
            cbPlayerId = str(data[2])
            cbName = str(data[3])
            players.append([cbPlayerId,cbName])

with open("playerMasterList.csv","w") as file:
    for player in players:
        file.write(",".join(player) + "\n")








