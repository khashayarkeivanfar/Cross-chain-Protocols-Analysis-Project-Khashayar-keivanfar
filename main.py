import requests
import sys
import urllib3
import queue
from API import *
from Configuration import *
from parse import *
import os
import concurrent.futures
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
    "USDTETH_USDTARO": [LiFiAPI(base_url_LiFi, headers),ConfigLiFi(fromChain=1, toChain=42161, fromAmount=str(1000000),
                                  fromToken="USDT", toToken="USDT")],
    "USDCBASE_ETHETH": [LiFiAPI(base_url_LiFi, headers),ConfigLiFi(fromChain=8453, toChain=1, fromAmount=str(1000000),
                                  fromToken="USDC", toToken="USDC")],
    "USDCSOL_USDCARO": [LiFiAPI(base_url_LiFi, headers),ConfigLiFi(fromChain=1, toChain=42161, fromAmount=str(1000000),
                                  fromToken="USDC", toToken="USDC")]
}

# Bungee API Instances
api_Bungee_instances = {
    "USDTETH_USDTARO": [BungeeAPI(base_url_Bungee, headers), ConfigBungee(fromChainId=1, toChainId=42161, fromAmount=str(1000000),
                                    fromTokenAddress="0xdac17f958d2ee523a2206206994597c13d831ec7",
                                    toTokenAddress="0xfd086bc7cd5c481dcc9c85ebe478a1c0b69fcbb9")],
    "USDCBASE_ETHETH": [BungeeAPI(base_url_Bungee, headers), ConfigBungee(fromChainId=8453, toChainId=1, fromAmount=str(1000000),
                                    fromTokenAddress="0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
                                    toTokenAddress="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48")],
    "USDCSOL_USDCARO": [BungeeAPI(base_url_Bungee, headers), ConfigBungee(fromChainId=1, toChainId=42161, fromAmount=str(1000000),
                                    fromTokenAddress="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
                                    toTokenAddress="0xaf88d065e77c8cC2239327C5EDb3A432268e5831")],
}



plot_queue = queue.Queue()
def fetch_and_write(values, output_dir, prefix):

    try:
        response = values[0].get("", values[1])
        if prefix == "bungee":
            plot_queue.put(("bungee", response))  
        elif prefix == "lifi":
            plot_queue.put(("lifi", response))
            LiFi_analysis(json.dumps(response))
    except Exception as e:
        print(f"Error processing {prefix} with values {values}: {e}")

def process_instances(instances, output_dir, prefix):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {
            executor.submit(fetch_and_write, values, output_dir, prefix): values
            for values in instances.values()
        }
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()  
            except Exception as e:
                print(f"Error in processing {prefix}: {e}")
output_dir = os.getcwd()

def main(): 
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future1 = executor.submit(process_instances, api_lifi_instances, output_dir, "lifi")
        future2 = executor.submit(process_instances, api_Bungee_instances, output_dir, "bungee")

    
        for future in concurrent.futures.as_completed([future1, future2]):
            try:
                future.result()
            except Exception as e:
                print(f"Critical error in one of the main tasks: {e}")
    while not plot_queue.empty():
        prefix, data = plot_queue.get()
        if prefix == "bungee":
            Bungee_analytics(data)  
        elif prefix == "lifi":
            LiFi_analysis(data)
    print("All plots are displayed. Close them to exit.")
    plt.show()
if __name__ == "__main__":
    main()

