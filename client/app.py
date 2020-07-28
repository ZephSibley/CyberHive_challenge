import sched
import time

import psutil
import requests


def get_processes():
    scheduler.enter(5, 1, get_processes)

    requests.post(
        'http://localhost:8000',
        json=list({proc.name() for proc in psutil.process_iter()})
    )


if __name__ == '__main__':
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(0, 1, get_processes)
    scheduler.run()
