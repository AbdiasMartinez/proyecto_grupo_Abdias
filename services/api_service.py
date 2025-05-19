import requests

class APIClient:
    def __init__(self, url):
        self.url = url

    def obtener_datos(self, limite=10):
        params = {'$limit': limite}
        res = requests.get(self.url, params=params)
        res.raise_for_status()
        return res.json()