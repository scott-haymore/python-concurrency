from threading import Thread

bank_account = 1000
count = 100000

# Increment the bank account balance
def increment_account():
    global bank_account
    for i in range(count):
        bank_account = bank_account + 1

# Decrement the bank account balance
def decrement_account():
    global bank_account
    for i in range(count):
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

