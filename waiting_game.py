# Print a message to the user indicating that they should wait random amount of time between 2 to 4 seconds.
# Player can press enter to start the timer
# Player presses enter again to stop the timer
# Finally show the elapsed time and how close the player got to the actual duration.

import random
import time


def waiting_game():
    random_wait_duration = random.randint(2, 4)
    print(f'Your target time is {random_wait_duration} seconds.')
    input("--- Press Enter to Begin ---")
    start = time.time()
    input(f'...Press enter again after {random_wait_duration} seconds...')
    end = time.time()
    elapsed_time = end - start
    time_difference = elapsed_time - random_wait_duration
    elapsed_time_output = f'Elapsed time: {elapsed_time:.3f} seconds.'
    if time_difference > 0:
        print(f'{elapsed_time_output} ({abs(time_difference):.3f} seconds too slow)')
    elif time_difference < 0:
        print(f'{elapsed_time_output} ({abs(time_difference):.3f} seconds too fast)')
    else:
        print(f'{elapsed_time_output} (Right on point)')



