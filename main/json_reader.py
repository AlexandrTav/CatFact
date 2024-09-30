import requests

"""
Reads data from free Cat facts API
"""
class JsonReader:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def cityWeather(self, city="Moscow"):
        self.base_url = f"http://api.weatherapi.com/v1/current.json?key={self.api_key}&q={city}"
        response = requests.get(self.base_url)
        return response.json()

    def TempData(self):
        response = requests.get(self.base_url)
        data = response.json()
        return data["current"]["temp_c"]

    def get_response_json(self):
        response = requests.get(self.base_url)
        return response.json()