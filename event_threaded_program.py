from threading import Event
from threading import Thread
import time

# Instantiate the event object.
event = Event()

# Function that will be called by a thread.
def work_for_thread():
    # Wait for the event to be set.
    while not event.is_set():
        print("Waiting for notification")
        time.sleep(1)
    # Once the event has been set, perform the work.
    print("Thread is doing some work.")
    print("Thread has finished work.")

# Instantiate the thread object.
thread = Thread(target=work_for_thread)
# Start the thread
thread.start()
# Make the thread wait before being able to work.
time.sleep(3)
# Set the event.
print("Setting the event.")
event.set()