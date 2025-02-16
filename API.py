import requests
from Custom_decorator import timer

class API:
    def __init__(self, base_url, headers=None, timeout=30, max_retries=3):

        self.base_url = base_url
        self.headers = headers or {}
        self.timeout = timeout
        self.max_retries = max_retries

    # GET and POST methods with Error handling
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

    