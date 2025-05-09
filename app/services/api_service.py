#services/api_service.py
import requests

class APIClient:
  def obtener_datos(self, limite=100):
    response = requests.get("https://www.datos.gov.co/resource/w2ub-ctmm.json?$limit={limite}")