import requests
from Custom_decorator import timer
import json

class API:
    def __init__(self, base_url, headers=None, timeout=30):

        self.base_url = base_url
        self.headers = headers or {}
        self.timeout = timeout

    # GET method with timer decorator
    @timer
    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(
                url,
                headers=self.headers,
                params=params,
                timeout=self.timeout
            )

        return response.json()
    def __str__(self):
        return self.__class__.__name__

class LiFiAPI(API):
    def __str__(self):
         return "Object of {} class with the {} being the parent class".format(self.__class__.__name__ , self.__class__.__bases__[0].__name__)
       

class BungeeAPI(API):
    def __init__(self, base_url, headers=None, timeout=30):
        
        bungee_specific_headers = {
            'API-KEY': '72a5b4b0-e727-48be-8aa1-5da9d62fe635' , 
        }
        merged_headers = {**bungee_specific_headers, **(headers or {})}
        super().__init__(base_url, headers=merged_headers, timeout=timeout)
    def __str__(self):
        return "Object of {} class with the {} being the parent class".format(self.__class__.__name__ , self.__class__.__bases__[0].__name__)
