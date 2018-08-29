from threading import Thread
from threading import RLock

bank_account = 1000
count = 1000000
rlock = RLock()

# Increment the bank account balance
def increment_account():
    global bank_account
    for i in range(count):
        # Acquire the lock
        with rlock:
            bank_account = bank_account + 1

# Decrement the bank account balance
def decrement_account():
    global bank_account
    for i in range(count):
        # Acquire the lock
        with rlock:
            bank_account = bank_account - 1

# Instantiate the threads.
thread1 = Thread(target=increment_account)
thread2 = Thread(target=decrement_account)

# Start the thread.
thread1.start()
thread2.start()

# Wait for the threads to finish.
thread1.join()
thread2.join()

print("bank account: {}".format(bank_account))

