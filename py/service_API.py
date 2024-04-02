import requests
from py.config import Config

config=Config()

#API 통신 클래스
class CtprvnRltmMesureDnstyService:
    def __init__(self):
        self.url=(
            f"{config.LINK}?"
            f"serviceKey={config.SECRET_KEY}&"
            f"returnType={config.RETURN_TYPE}&"
            f"numOfRows={config.NUMOFROWS}"
        )
    def request_getCtprvnRltmMesureDnsty(self,city):
        url = f"{self.url}&sidoName={city}"
        response = requests.get(url)
        return response.json()
