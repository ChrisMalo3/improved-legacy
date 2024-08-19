# synchronous function

from tornado.httpclient import HTTPClient
key = 'my_secret_key'

def get_weather():
    city = 'london'
    url = 'https://api.weatherapi.com/v1/current.json?key=' + key + '&q=' + city + '&aqi=no'
    print(url)
    http_client = HTTPClient()
    response = http_client.fetch(url)
    return (response.body)

# Asynchronous function
from tornado.httpclient import AsyncHTTPClient
secret_key = 'my_secret_key'

async def get_weather():
    city = 'london'
    url = 'http://api.weatherapi.com/v1/current.json?key=' + key + '&q=' + city + '&aqi=no'
    print(url)
    http_client = AsyncHTTPClient()
    response = await http_client.fetch(url)
    return (response.body)
