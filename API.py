import requests
from Custom_decorator import timer
import jason 

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

    def __str__(self):
        return "Object of {} class with the {} being the parent class".format(self.__class__.__name__ , self.__class__.__bases__[0].__name__)
