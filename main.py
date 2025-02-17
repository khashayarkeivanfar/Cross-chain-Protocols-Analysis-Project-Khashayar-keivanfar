import requests
import sys
import urllib3
from API import *
from Configuration import *

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)     # In case of any SSL/TLS certification verification warnings


"""""
In case that we want to intercept the request via burpsuit or any other application
proxies = {'http':' http://127.0.0.1:8080' , 'https':'https://127.0.0.1:8080'} 
"""""
# LiFi API initialization
base_url_LiFi  = "https://li.quest/v1/quote"
headers = {"accept": "application/json"}
fromChain = 1
toChain = 42161
fromAmount =  str(1000000)
fromToken ="USDT" #"0xdac17f958d2ee523a2206206994597c13d831ec7"
toToken ="USDT"       #"0xfd086bc7cd5c481dcc9c85ebe478a1c0b69fcbb9"

# Bungee API initialization
#base_url = 
def main():

    params = LifiConfig(fromChain, toChain , fromAmount , fromToken, toToken)
    api = LiFiAPI(base_url_LiFi , headers)
    try:
        response = api.get("", params)  
        print(json.dumps(response, indent=4))  
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    


if __name__ == "__main__":
    main()



