import time
import os


def set_alarm(alarm_time, sound_file, message):
    time_to_wait = alarm_time - time.time()
    time.sleep(time_to_wait)
    print(message)
    os.system(f'afplay {sound_file}')
