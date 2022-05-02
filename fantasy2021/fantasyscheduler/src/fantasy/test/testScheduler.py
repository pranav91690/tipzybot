import pytz
from datetime import datetime,timedelta
from fantasy.db.mongo import getMatches

india = pytz.timezone('Asia/Calcutta')
matches = getMatches()
for match in matches:
    # print(match)
    ts = int(match["timestamp"])
    dt_start = india.localize(datetime.fromtimestamp(int(match["timestamp"]) / 1000))
    dt_end = dt_start + timedelta(hours = 5)
    now = india.localize(datetime.now())

    if (dt_start < now < dt_end):
        print(match)