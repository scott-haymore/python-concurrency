from threading import Thread
from threading import Semaphore
import time

# Maximum number of connections allowed to the database.
MAX_CONNECTIONS = 2

# Instantiate the Semaphore object
sem = Semaphore(MAX_CONNECTIONS)

# Function that is to access the database.
def access_database(thread_id):
    print("Thread: {} attempting to acquire the lock at:\t{}"
          .format(thread_id, time.ctime()))
    # Attempt to acquire the lock.
    with sem:
        print("Thread: {} acquired the lock at:\t\t\t{}"
              .format(thread_id, time.ctime()))
        print("Thread: {} accessing the database.".format(thread_id))
        time.sleep(5)

for x in range(0,3):
    # Instantiate the thread objects.
    thread = Thread(target=access_database, args=(x,))
    # Start the threads.
    thread.start()
    
    