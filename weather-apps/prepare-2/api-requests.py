import requests
import json

def weather_api(city):
    api_key = '1187ffc7690886f66d0589689f2a01f0'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = json.loads(response.text)
    results = {}
    results['lon'] = data['coord']['lon']
    results['lat'] = data['coord']['lat']
    results['name'] =data['name']
    results['temp'] =data['main']['temp']
    results['humidity'] =data['main']['humidity']
    return results

print(weather_api('London'))