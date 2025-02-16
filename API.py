class API:
    def __init__(self, base_url, headers= None, timeout= 30, **kwargs):

        self.base_url = base_url
        self.headers = headers or {}
        self.timeout = timeout
        self.extra_params = kwargs 

        