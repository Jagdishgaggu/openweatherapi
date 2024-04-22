import requests
from pprint import pprint

city = input('Enter the city:')

base_url = 'http://api.openweathermap.org/data/2.5/forecast'

payload = {
    'id': '524901',
    'appid': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'q': city
}

response = requests.get(base_url,params=payload)

print('Status Code:', response.status_code)

if response.status_code == 200:

    j = response.json()

    for w in j['list']:

        weather_info = {
        'temp': w['main']['temp'],
        'pressure': w['main']['pressure'],
        'humidity': w['main']['humidity'],
        'weather': w['weather'][0]['main'] if len(w['weather']) == 1 else "Unavailable",
        'weather_desc':w['weather'][0]['description'] if len(w['weather']) == 1 else "Unavailable",
        'datetime': w['dt_txt']
        }
        pprint(weather_info)
        break
    
else:
    pprint(response.content)