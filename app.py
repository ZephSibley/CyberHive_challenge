import sched
import time

import psutil
import requests


def get_processes():
    running_processes = {proc.name() for proc in psutil.process_iter()}

    requests.post('http://localhost:8080', data=running_processes)

    # Schedule another run
    s.enter(5, 1, get_processes)


if __name__ == '__main__':
    s = sched.scheduler(time.time, time.sleep)
    s.enter(5, 1, get_processes)
    s.run()
