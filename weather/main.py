import requests
import os
from datetime import datetime

def question():
    country = input('Enter the country code: ')
    city = input('Enter the city name: ')
    return [country,city]

def main():
    answers = question()
    key = os.environ.get('WEATHER_KEY')
    try:
        query = {'q':f'{answers[1]},{answers[0]}' , 'units': 'imperial', 'appid':key}
        forecasturl = 'http://api.openweathermap.org/data/2.5/forecast/'
        forecastdata = requests.get(forecasturl,params=query).json()
        forecastitems = forecastdata['list']
        for forecast in forecastitems:
            timestamp = forecast['dt']
            date = datetime.fromtimestamp(timestamp)
            temp = forecast['main']['temp']
            description = forecast['weather'][0]['description']
            wind = forecast['wind']['speed']

            print(f'\nAt {date}, The temprature will be {temp} Farenheit, The weather description is {description}, The wind speed will be')
    except Exception as e:
        print('Error Occured: ',e)
if __name__ == '__main__':
    main()