import requests

class APIClient:
    URL = "https://www.datos.gov.co/resource/w2ub-ctmm.json"

    def obtener_datos(self, limite=100):
        try:
            params = {"$limit": limite}
            response = requests.get(self.URL, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error al conectar con la API: {e}")
            return None
