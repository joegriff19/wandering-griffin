import requests
import pandas as pd
import dash
from dash import html
from dash_iconify import DashIconify
import os
import dash_extensions as de
from app import server
from flask import send_from_directory

options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))


def update_weather(location):
    request_str = 'http://api.weatherstack.com/current?access_key=d779aff91a964382a38b84e587262b7c&query={}&units=f'.format(location)
    weather_requests = requests.get(request_str)
    json_data = weather_requests.json()
    weather_df = pd.DataFrame(json_data)
    # print(weather_df)
    for i in range(len(weather_df)):
        temp = weather_df.current['temperature']
        # precip = weather_df.current['precip']
        # cloudcover = weather_df.current['cloudcover']
        weather_descriptions = weather_df.current['weather_descriptions']
        weather_code = weather_df.current['weather_code']
        is_day = weather_df.current['is_day']

    # print(weather_code)
    # print(is_day)

    c_temp = int((temp-32) / 1.8)

    weather_descriptions = str(weather_descriptions)
    weather_descriptions = weather_descriptions.strip("[]")
    weather_descriptions = weather_descriptions.strip("'")
    weather_descriptions = weather_descriptions.lower()

    # weather_icons = str(weather_icons)
    # weather_icons = weather_icons.strip("[]")
    # print(weather_icons)

    weather_str = 'Current weather: ', weather_descriptions, ', '
    weather_str1 = temp, '°F ('
    weather_str2 = c_temp, '°C)'
    final_weather_str = weather_str + weather_str1 + weather_str2

    # weather_icon = html.Img(src=dash.get_asset_url(weather_icons))
    # print(weather_icon)
    # weather_image_name = get_weather_image(weather_code)
    # weather_image_name = 'line-md:github-loop'

    global json_path
    # json_path = 'snowman.json'
    json_path = get_weather_image(weather_code)
    if is_day == 'no':
        if json_path == 'sun.json':
            json_path = 'moon.json'
        if json_path == 'partly_cloudy.json':
            json_path = 'moon_cloudy.json'
        if json_path == 'sun_snow.json':
            json_path = 'snow_night.json'

    return (html.Div(final_weather_str),
            html.Div(de.Lottie(options=options, width="10vh", height="10vh", url="/loader2", speed=1,
                               isClickToPauseDisabled=True)))


@server.route("/loader2", methods=['GET'])
def serving_lottie_loader2():
    directory = os.path.join(os.getcwd(), "assets/lottie")
    return send_from_directory(directory, json_path)


def get_weather_image(code):
    weather_images = [[395, 'snowman.json'], [392, 'sun_snow.json'], [389, 'lightning.json'],
                      [386, 'lightning.json'], [377, 'rain.json'], [374, 'rain.json'],
                      [371, 'snowman.json'], [368, 'sun_shower.json'], [365, 'rain.json'],
                      [362, 'rain.json'], [359, 'rain.json'], [356, 'rain.json'],
                      [353, 'sun_shower.json'], [350, 'rain.json'], [338, 'snowman.json'],
                      [335, 'snowman.json'], [332, 'snowman.json'], [329, 'sun_snow.json'],
                      [326, 'sun_snow.json'], [323, 'sun_snow.json'], [320, 'rain.json'],
                      [317, 'rain.json'], [314, 'rain.json'], [311, 'sun_shower.json'],
                      [308, 'rain.json'], [305, 'rain.json'], [302, 'rain.json'],
                      [299, 'rain.json'], [296, 'sun_shower.json'], [293, 'rain.json'],
                      [284, 'rain.json'], [281, 'rain.json'], [266, 'rain.json'],
                      [263, 'sun_shower.json'], [260, 'fog.json'], [248, 'fog.json'],
                      [230, 'snowman.json'], [227, 'sun_snow.json'], [200, 'lightning.json'],
                      [185, 'rain.json'], [182, 'rain.json'], [179, 'sun_snow.json'],
                      [176, 'sun_shower.json'], [143, 'cloudy.json'], [122, 'cloudy.json'],
                      [119, 'cloudy.json'], [116, 'partly_cloudy.json'],
                      [113, 'sun.json']]

    weather_code_df = pd.DataFrame(weather_images, columns=['code', 'image'])
    for i in range(len(weather_code_df)):
        if code == weather_code_df.code[i]:
            weather_image_name = weather_code_df.image[i]

    return weather_image_name

# df_region_level = pd.DataFrame(region_level_mapping, columns=['Entity', 'Region_Level'])
#
# for i in range(len(df_region_level)):
#     if self.analysis_parameters.entity == df_region_level.Entity[i]:
#         dwh_region_level = df_region_level.Region_Level[i]
#
# return dwh_region_level

def get_lat_lon(gj_file):
    coordinates_str = str(gj_file['features'][0]['geometry']['coordinates'])
    coordinates_str = coordinates_str[1:]
    coordinates_str = coordinates_str[:-1]
    coordinates_str = coordinates_str.split(", ")
    lat = coordinates_str[1]
    lon = coordinates_str[0]
    lat = str(lat)
    lon = str(lon)
    lat_lon_str = lat + ',' + lon

    return lat_lon_str
