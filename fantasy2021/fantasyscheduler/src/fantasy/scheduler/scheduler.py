from datetime import datetime,timedelta
import pytz
from apscheduler.schedulers.background import BlockingScheduler

from fantasy.db.mongo import addMatches,addScores
from fantasy.cricbuzz.parseScores import getScores
from fantasy.utils.utils import getMatchInfo
india = pytz.timezone('Asia/Calcutta')

def start(sched):
    print("Getting Match Info")
    matches = getMatchInfo()
    print("Got : " + str(len(matches)) + " matches")
    print("Uploading Match Information to the Db")
    addMatches(matches)
    print("Getting Job List")
    jobList = getJobList(matches)
    print("Length of Job List is " + str(len(jobList)))

    for job in jobList:
        args = [job[0],job[1],job[2]]

        start = india.localize(datetime.strptime(job[3],'%Y-%m-%d %H:%M:%S'))
        end = india.localize(datetime.strptime(job[4],'%Y-%m-%d %H:%M:%S'))
        now = india.localize(datetime.now())


        if (end > now):
            if start < now < end:
                sched.add_job(getAndAddScores,'interval', args=args, seconds=15,end_date=job[4])
            else:
                sched.add_job(getAndAddScores,'interval', args=args, seconds=15,
                              start_date=job[3], end_date=job[4])
        else:
            getAndAddScores(job[0],job[1],job[2])

    print("Length of Scheduled Jobs")
    print(len(sched.get_jobs()))

    sched.start()


def getJobList(matches):
    india = pytz.timezone('Asia/Calcutta')
    jobList = []
    for match in matches:
        ts = int(match["timestamp"])
        dt_start = datetime.fromtimestamp(ts / 1000)
        dt_end = dt_start + timedelta(hours=5)
        start = dt_start.strftime('%Y-%m-%d %H:%M:%S')
        end = dt_end.strftime('%Y-%m-%d %H:%M:%S')
        job = [match["_id"],match["scorecard"],match["mom"],start,end]
        jobList.append(job)

    return jobList

def getAndAddScores(match_id,scores_url,mom_url):
    scores = getScores(match_id,scores_url,mom_url)
    addScores(scores)

if __name__ == '__main__':
    print("Starting Scheduler")
    sched = BlockingScheduler()
    start(sched)






