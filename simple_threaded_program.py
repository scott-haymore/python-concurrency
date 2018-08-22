import threading

# Create a function that will be executed by a thread.
def work_for_thread(thread_id):
    print("Thread {} is doing some work.".format(thread_id))
    print("Thread {} has finished work.".format(thread_id))

# Initialize the thread.
thread = threading.Thread(target=work_for_thread, args=(1,))
# Start the thread.
thread.start()