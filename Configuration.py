class Param:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def ParamConfig(self, **kwargs):
        try:
            token_dict = {
                "fromChain": getattr(self, "fromChain", None),
                "toChain": getattr(self, "toChain", None),
                "fromToken": getattr(self, "fromToken", None),
                "toToken": str(getattr(self, "toToken", 0) * (10**18)),
                "fromAddress": "0x0000000000000000000000000000000000000000",
                "includeDEXs": "true",
            }
            return token_dict
        except AttributeError as e:
            print(f"Error: {e}")
            return {}
    

        
        
