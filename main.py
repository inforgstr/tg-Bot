import requests
from config import TOKEN, API


def get_weather(city, open_weather_token):
    try:
        req = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        weather = req.json()
        city = weather["name"]

    except Exception as ex:
        print("Please, try again!")


def main():
    city = input("City: ")
    get_weather(city, API)


if __name__ == "__main__":
    main()
