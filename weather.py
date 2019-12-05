import requests
from pprint import pprint

city = input('Enter your city: ')

url='https://weather.cit.api.here.com/weather/1.0/report.json?product=alerts&name={}&app_id=DemoAppId01082013GAL&app_code=AJKnXv84fjrb0KIHawS0Tg'.format(city)

res = requests.get(url)

data = res.json()

pprint(data)

print('alert :' , data['alerts']['alerts'][0]['description'],'. Stay safe')