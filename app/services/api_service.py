import requests

class APIClient:
    def obtener_datos(self, limit=100):
        response = requests.get(f"https://www.datos.gov.co/resource/w2ub-ctmm.json?$limit={limit}")
        return response.json()
