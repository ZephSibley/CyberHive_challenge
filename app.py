import psutil
import sched
import time


def get_processes():
    print('*** Running Processes ***')

    for proc in psutil.process_iter():
        try:
            # Get process name & pid from process object.
            process_name = proc.name()
            process_id = proc.pid
            print(process_name, ' ::: ', process_id)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    s.enter(5, 1, get_processes)


if __name__ == '__main__':
    s = sched.scheduler(time.time, time.sleep)
    s.enter(5, 1, get_processes)
    s.run()
