import requests
import pandas as pd


def update_weather(location):
    print(location)
    request_str = 'http://api.weatherstack.com/current?access_key=d779aff91a964382a38b84e587262b7c&query={}&units=f'.format(location)
    weather_requests = requests.get(request_str)
    json_data = weather_requests.json()
    weather_df = pd.DataFrame(json_data)
    for i in range(len(weather_df)):
        temp = weather_df.current['temperature']
        # precip = weather_df.current['precip']
        # cloudcover = weather_df.current['cloudcover']
        weather_descriptions = weather_df.current['weather_descriptions']

    weather_descriptions = str(weather_descriptions)
    weather_descriptions = weather_descriptions.strip("[]")
    weather_descriptions = weather_descriptions.strip("'")
    weather_descriptions = weather_descriptions.lower()

    weather_str = 'Current weather: ', weather_descriptions, ', '
    weather_str1 = temp, '°F\n'
    # weather_str2 = 'The cloudcover is ', cloudcover, '%\n'
    # weather_str3 = 'The chance of precipitation is ', precip, '%\n'

    return weather_str + weather_str1