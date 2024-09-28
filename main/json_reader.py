import requests

class JsonReader:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def get_response_json(self):
        return requests.get(self.base_url).json();