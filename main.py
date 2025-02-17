import requests
import sys
import urllib3
from API import *
from Configuration import *
from concurrent.futures import ThreadPoolExecutor, as_completed
from tokens import *
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)     # In case of any SSL/TLS certification verification warnings


"""""
In case that we want to intercept the request via burpsuit or any other application
proxies = {'http':' http://127.0.0.1:8080' , 'https':'https://127.0.0.1:8080'} 
"""""
# LiFi API initialization
base_url_LiFi = "https://li.quest/v1/quote"
base_url_Bungee = "https://api.socket.tech/v2/quote"
headers = {"accept": "application/json"}

# LiFi API Instances
api_lifi_instances = {
    "USDTETH_USDTARO": LiFiAPI(base_url_LiFi, headers),
    # "BNBBSC_AVAXC": LiFiAPI(base_url_LiFi, headers),
    "USDCBASE_ETHETH": LiFiAPI(base_url_LiFi, headers),
    "USDCSOL_USDCARO": LiFiAPI(base_url_LiFi, headers),
}

# Bungee API Instances
api_Bungee_instances = {
    "USDTETH_USDTARO": BungeeAPI(base_url_Bungee, headers),
    # "BNBBSC_AVAXC": BungeeAPI(base_url_Bungee, headers),
    "USDCBASE_ETHETH": BungeeAPI(base_url_Bungee, headers),
    "USDCSOL_USDCARO": BungeeAPI(base_url_Bungee, headers),
}

# LiFi API Parameters
api_LiFi_params = {
    "USDTETH_USDTARO": ConfigLiFi(fromChain=1, toChain=42161, fromAmount=str(1000000),
                                  fromToken="USDT", toToken="USDT"),
    # "BNBBSC_AVAXC": ConfigLiFi(fromChain=56, toChain=43114, fromAmount=str(100000000000000000000000000),
    #                            fromToken="BNB", toToken="AVAX"),
    "USDCBASE_ETHETH": ConfigLiFi(fromChain=8453, toChain=1, fromAmount=str(1000000),
                                  fromToken="USDC", toToken="USDC"),
    "USDCSOL_USDCARO": ConfigLiFi(fromChain=1, toChain=42161, fromAmount=str(1000000),
                                  fromToken="USDC", toToken="USDC"),
}

# Bungee API Parameters
api_Bungee_params = {
    "USDTETH_USDTARO": ConfigBungee(fromChainId=1, toChainId=42161, fromAmount=str(1000000),
                                    fromTokenAddress="0xdac17f958d2ee523a2206206994597c13d831ec7",
                                    toTokenAddress="0xfd086bc7cd5c481dcc9c85ebe478a1c0b69fcbb9"),
    # "BNBBSC_AVAXC": ConfigBungee(fromChain=56, toChain=43114, fromAmount=str(100000000),
    #                              fromToken="BNB",
    #                              toToken="FvwEAhmxKfeiG8SnEvq42hc6whRyY3EFYAvebMqDNDGCgxN5Z"),
    "USDCBASE_ETHETH": ConfigBungee(fromChainId=8453, toChainId=1, fromAmount=str(1000000),
                                    fromTokenAddress="0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
                                    toTokenAddress="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"),
    "USDCSOL_USDCARO": ConfigBungee(fromChainId=1, toChainId=42161, fromAmount=str(1000000),
                                    fromTokenAddress="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
                                    toTokenAddress="0xaf88d065e77c8cC2239327C5EDb3A432268e5831"),
}

# Function to Fetch Data
def fetch_data(api_obj, endpoint, params):
    return api_obj.get(endpoint, params)

# Main Execution
def main():
    api_list = []

    # Collect all API calls for LiFi
    for key in api_lifi_instances:
        api_list.append((api_lifi_instances[key], "", api_LiFi_params[key]))


    # Collect all API calls for Bungee
    for key in api_Bungee_instances:
        api_list.append((api_Bungee_instances[key], "", api_Bungee_params[key]))

    # Parallel Execution
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_api = {executor.submit(fetch_data, api, endpoint, params): api for api, endpoint, params in api_list}

        for future in as_completed(future_to_api):
            try:
                response = future.result()
                print(json.dumps(response, indent=4))
            except requests.exceptions.RequestException as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()

