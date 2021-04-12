import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["fantasy2021"]
mycol = mydb["players"]


with open('/Users/pranav/fantasy2021/fantasy2021/players.json') as json_file:
    data = json.load(json_file)

x = mycol.insert_many(data)

print(x)
