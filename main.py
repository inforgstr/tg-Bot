import requests
from config import API
import datetime


def get_weather(city, open_weather_token):

    code_to_smile = {
        "Clear": "Clear \U00002600",
        "Clouds": "Cloudy \U00002601",
        "Rain": "Rain \U00002614",
        "Drizzle": "Drizzle \U00002614",
        "Thunderstorm": "Thunderstorm \U000026A1",
        "Snow": "Snow \U0001F328",
        "Mist": "Mist \U0001F32B",
    }

    try:
        req = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        weather = req.json()
        description = weather["weather"][0]["main"]

        if description in code_to_smile:
            wd = code_to_smile[description]


        city = weather["name"]
        temp = f'{weather["main"]["temp"]:.1f}°C'
        humidity = f'{weather["main"]["humidity"]} %'
        pressure = weather["main"]["pressure"]
        feels = f"{weather['main']['feels_like']:.1f}"


        code = weather["sys"]["country"]
        sunrise = datetime.datetime.fromtimestamp(weather["sys"]["sunrise"]).strftime(
            "%d.%m.%Y  at  %H: %M"
        )
        sunset = datetime.datetime.fromtimestamp(weather["sys"]["sunset"]).strftime(
            "%d.%m.%Y  at  %H: %M"
        )

        wind = f'{weather["wind"]["speed"]:.1f} m/s'


        print(f"******{datetime.datetime.now().strftime('%h %m    %H:%M ')}******\n\n"
            f"In {city}  temperature  {temp} (feels {feels}) {wd}\n\nHumidity:\t{humidity}\n\nCountry code:\t{code}\n\n"
            f"Pressure:\t{pressure}\n\nWind:\t\t{wind}\n\nSunrise:\t{sunrise}\n\nSunset:\t\t{sunset}"
        )

    except Exception as ex:
        print("Error ", ex)
        print("Please, try again!")


def main():
    city = input("City: ")
    get_weather(city, API)


if __name__ == "__main__":
    main()
