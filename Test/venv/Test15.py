from apscheduler.schedulers.background import BlockingScheduler

def test():
    print('123123123')

scheduler = BlockingScheduler()
scheduler.add_job(test, 'interval', seconds=3)
scheduler.start()