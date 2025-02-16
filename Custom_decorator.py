import time
def timer(func):
    def wrapper():
        start = time.time()
        func()
        elapsed = time.time() - start
        print ('took {} to retrieve the data'.format(elapsed))
    return wrapper