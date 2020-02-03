'''
From: Apple
Difficulty: Medium

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
'''

import time

def job_scheduler(f, n):
    def start():
        time.sleep(n/1000)
        f()
    return {"start": start}
    

def rf():
    print("Hello");

scheduled_job = job_scheduler(rf, 2000)
scheduled_job.start()
