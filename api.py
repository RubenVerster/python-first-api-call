from nis import match
from unittest import case
import requests

class APICall:
    '''Base class to make a basic API call with requests'''

    def call(self, method, api_url):
        if method.lower() == 'get':
            r =  requests.get(api_url)

        match r.status_code:
            case 200 | 201 | 202:
                return r.json("value")
            case _:
                raise TypeError("API Error")

class ChuckNorris(APICall):
    '''This is the Chuck Norris API'''
    url = 'https://api.chucknorris.io/jokes/random?category='
    categories = ['dev', 'explicit', 'fashion', 'food', 'history', 'movie', 'music', 'political', 'science', 'sport', 'travel']

    def __init__(self, category):
        self.category = category
        if not self.category in self.categories:
            raise TypeError("Invalid category")
    
    def get(self):
        api_url = f'{self.url}{self.category}'
        return self.call('get', api_url)