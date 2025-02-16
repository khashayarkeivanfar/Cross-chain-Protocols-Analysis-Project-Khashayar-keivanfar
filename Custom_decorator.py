import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs) 
        elapsed = time.time() - start
        print(f'Took {elapsed:.4f} seconds to retrieve the data')
        return result 
    return wrapper