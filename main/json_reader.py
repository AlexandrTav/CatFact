import requests

from datetime import datetime

"""
Reads data from free Cat facts API
"""
class JsonReader:
    def __init__(self, base_url, api_key):
        self.url = base_url + f"?key={api_key}"
        self.api_key = api_key

    def cityWeather(self, city="Moscow"):
        self.url = self.url + f"&q={city}"
        response = requests.get(self.url)
        return response.json()

    def H_Time(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    def TempData(self, city="Moscow"):
        response = requests.get(self.url)
        data = self.cityWeather(city)
        temp = data["current"]["temp_c"]
        cond = data["current"]["condition"]["text"]
        return temp, cond

    def HistoryInfo(now, city, data):
        {
            "time": now,
            "city": city,
            "temperature": data,
            #"condition": cond
        }

    def get_response_json(self):
        return self.cityWeather()