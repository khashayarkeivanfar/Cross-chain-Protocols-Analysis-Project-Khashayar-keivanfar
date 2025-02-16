import requests
import sys
import urllib3



urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)     # In case of any SSL/TLS certification verification warnings


"""""
In case that we want to intercept the request via burpsuit or any other application
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



