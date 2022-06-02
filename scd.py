import schedule
import time
def job():
    print("hello world")

def jib():
    print("hello")
schedule.every(1).seconds.do(jib)
schedule.every(3).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)