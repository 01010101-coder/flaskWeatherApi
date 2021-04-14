from flask import Flask, render_template, request
import requests
import json
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "POST":
        city = request.form['city']
        country = request.form['country']
        api_key = "4d4d08bad7dd93c879a6beba8309b357"
        weather_url = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units=imperial')

        weather_data = weather_url.json()

        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        response = requests.get(url).json()
        # 200, 300, 400, 500
        if response.get('cod') != 200:
            # если подключение не успешно
            message = response.get('message', '')
            return f'Error getting data for {city.title()}, Error message - {message}'

        temp_cel = round((weather_data['main']['temp']-32) /1.8, 2)
        max_temp_cel = round((weather_data['main']['temp_max']-32)/1.8, 2)
        min_temp_cel = round((weather_data['main']['temp_min']-32)/1.8, 2)
        pressure = weather_data['main']['pressure']
        status_weather = weather_data["weather"][0]["main"]

        return render_template("result.html", temp=temp_cel, max_temp=max_temp_cel, min_temp = min_temp_cel, pressure=pressure, main_weather=status_weather, city=city)

    return render_template("index.html")
