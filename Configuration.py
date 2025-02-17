from API import *
def ConfigLiFi(fromChain, toChain , fromAmount, fromToken, toToken):

    params = {
        "fromChain": fromChain,
        "toChain": toChain,
        "fromToken": fromToken,
        "toToken": toToken,
        "fromAmount": fromAmount,
        "fromAddress": "0x1111111111111111111111111111111111111111",
        "includeDEXs": "true",
                }
    return params
def ConfigBungee(fromChain, toChain , fromAmount, fromToken, toToken):

    params = {
        "fromChain": fromChain,
        "toChain": toChain,
        "fromToken": fromToken,
        "toToken": toToken,
        "fromAmount": fromAmount,
        "fromAddress": "0x1111111111111111111111111111111111111111",
        "uniqueRoutesPerBridge": "true",
        "sort": "output"
                }
    return params
    
def fetch_data(api_obj, endpoint, params):
    
    return api_obj.get(endpoint, params)

    

        
        
