import sched
import time
from datetime import datetime

import psutil
import requests


def get_processes():
    scheduler.enter(5, 1, get_processes)

    requests.post(
        'http://localhost:8000',
        json={
            'running_processes': list({proc.name() for proc in psutil.process_iter()}),
            'timestamp': str(datetime.now())
        }
    )


if __name__ == '__main__':
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(0, 1, get_processes)
    scheduler.run()
