from API import *
def Config(fromChain, toChain , fromAmount, fromToken, toToken):

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
    
def fetch_data(api_obj, endpoint, params):
    
    return api_obj.get(endpoint, params)

    

        
        
