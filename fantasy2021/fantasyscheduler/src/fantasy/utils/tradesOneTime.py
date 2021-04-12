from fantasy.db.mongo import searchPlayer,addTeams,searchPlayerRegex


file = r"C:\Users\pachanta\fantasy\parseCode\trade1.txt"
lines = []
team = []
for line in open(file, 'r').readlines():

        mod = line[:-1]

        if mod == "":
            lines.append(team)
            team = []
        else:
            team.append(mod)

if len(team) > 0:
    lines.append(team)

updates = []

for team in lines:
    update = {}
    update["team"] = team[0][:-1]
    trades = []
    injuries = []

    addArray = None

    for line in team[1:]:
        if line == "Injury":
            addArray = injuries
        elif line == "Trade":
            addArray = trades
        else:
            addArray.append(line)

    update["trades"] = trades
    update["injuries"] = injuries

    updates.append(update)

for update in updates:
    trades = update["trades"]
    for info in trades:
        name = info.split(",")[0]
        if "." in name:
            name = name.split(".")[1].strip()
        print(name)
        print(searchPlayerRegex(name))