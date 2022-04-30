from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


class Crypto:

    def get_crypto(self):

        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        
        parameters = {
            'start':'1',
            'limit':'10',
            'convert':'USD'
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': '21557255-0dcd-40f1-8cb8-1680fd50aaad'
        }

        session = Session()
        session.headers.update(headers)
       
        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            return data['data']
            
          
        except (ConnectionError, Timeout, TooManyRedirects) as erreur:
            print(erreur)