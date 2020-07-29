import argparse
import sched
import time
from datetime import datetime

import psutil
import requests

parser = argparse.ArgumentParser(
    description='This is an application that sends a list of currently running processes to a specified server every '
                'five seconds.'
)
parser.add_argument(
    '-t', '--target-server',
    help="The server we want to send the information to",
    required=True,
    action='store'
)
args = parser.parse_args()


def get_processes():
    scheduler.enter(5, 1, get_processes)

    requests.post(
        args.target_server,
        json={
            'running_processes': list({proc.name() for proc in psutil.process_iter()}),
            'timestamp': str(datetime.now())
        }
    )


if __name__ == '__main__':
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(0, 1, get_processes)
    scheduler.run()
