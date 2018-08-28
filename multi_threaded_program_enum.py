import threading
import time
import random

# Create a function that will be executed by a thread.
def work_for_thread(thread_id):
    print("Thread {} is doing some work.".format(thread_id))
    sleep = random.randint(1,2)
    time.sleep(sleep)
    print("Thread {} has finished work.".format(thread_id))

# Initialize the threads.
for currentThread in range(5):
    thread = threading.Thread(target=work_for_thread, args=(currentThread,))
    # Start the thread.
    thread.start()