from utils.utils import getMatchInfo
from db.mongo import addMatches
matches = getMatchInfo()
addMatches(matches)


