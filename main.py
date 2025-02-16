import requests
import sys
import urllib3
import time 

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)     # In case of any SSL/TLS certification verification warnings


"""""
In case that we want to intercept the request via burpsuit or any other method 
proxies = {'http':' http://127.0.0.1:8080' , 'https':'https://127.0.0.1:8080'} 
"""""


def main():
    if len(sys.argv) != 2:
        print("Error in Usage %s <url>" % sys.argv[0])
        sys.argv[0]
        sys.exit(-1)
    url = sys.argv[1]
    print("Awating connection to %s" % url)

if __name__ == "__main__":
    main()
#timer decorator
def timer(func):
    def wrapper():
        start = time.time()
        func()
        elapsed = time.time() - start
        print ('took {} to retrieve the data'.format(elapsed))
    return wrapper




