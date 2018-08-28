from threading import Thread

class my_threading_class(Thread):
    # Initializer
    def __init__(self):
        print("my_threading_class")
        Thread.__init__(self)
    
    # Function that is called when .start() is invoked.
    def run(self):
        print("Thread is doing some work.")

# Instantiate the object.
thread = my_threading_class()

# Start the thread.
thread.start()

# Block until thread finishes.
thread.join()

