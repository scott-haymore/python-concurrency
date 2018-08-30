from threading import Thread
from threading import Condition
import random
import time

count = 10

class Consumer(Thread):
    def __init__(self, cond_var, list_items):
        # The consumer will acquire the lock using this condition variable.
        self.cond_var = cond_var
        # List of items
        self.list_items = list_items
        Thread.__init__(self)

    def run(self):
        # Iterate over some finite range.
        for x in range(count):
            # Acquire the lock.
            with self.cond_var:
                # Wait for notification that the item is ready.
                self.cond_var.wait()
                # Pop the item off the list.
                some_item = self.list_items.pop()
                # Finally consume the item in some way.
                print("Consuming: {}".format(some_item))

class Producer(Thread):

    def __init__(self, cond_var, list_items):
        # The consumer will acquire the lock using this condition variable.
        self.cond_var = cond_var
        # List of items
        self.list_items = list_items
        Thread.__init__(self)
        
    def run(self):
        # Iterate over some finite range.
        for x in range(count):
            # Acquire the lock.
            with self.cond_var:
                # Generate some random integer between one and ten.
                some_item = random.randint(1,10)
                print("Producing: {}".format(some_item))
                # Append the item to the list.
                self.list_items.append(some_item)
                # Notify consumers that the item is ready.
                self.cond_var.notify()
            # This timer is here to ensure the producer doesn't produce faster
            # than the consumer consumes.
            time.sleep(1)

# Shared resource between the consumer and producer.
list_items = []
# Shared conditional variable between the consumer and producer.
cond_var = Condition()

# Instantiate the producer and consumer objects.
producer = Producer(cond_var, list_items)
consumer = Consumer(cond_var, list_items)

# Start the threads.
consumer.start()
producer.start()

# Wait for the threads to finish.
producer.join()
consumer.join()