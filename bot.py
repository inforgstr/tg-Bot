import requests
from config import API, TOKEN
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import datetime


bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def get_city(message: types.Message):
    await message.answer(
        "Hi there!\nSend me correct city to see the weather of the place.\nGood luck!"  # greeting
    )


@dp.message_handler(content_types=["text"])
async def get_weather(message: types.Message):
    code_to_smile = {
        "Clear": "Clear \U00002600",
        "Clouds": "Cloudy \U00002601",
        "Rain": "Rain \U00002614",
        "Drizzle": "Drizzle \U00002614",
        "Thunderstorm": "Thunderstorm \U000026A1",  # there are some emojies from unicode
        "Snow": "Snow \U0001F328",
        "Mist": "Mist \U0001F32B",
    }

    try:
        req = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={API}&units=metric"
        )
        # all information about weather
        weather = req.json()
        description = weather["weather"][0]["main"]

        if description in code_to_smile:
            wd = code_to_smile[description]

        # extracting some data from api
        city = weather["name"]
        temp = f'{weather["main"]["temp"]:.1f}°C'
        humidity = f'{weather["main"]["humidity"]} %'
        feels = f"{weather['main']['feels_like']:.1f}"

        code = weather["sys"]["country"]
        sunrise = datetime.datetime.fromtimestamp(weather["sys"]["sunrise"]).strftime(
            "%d.%m.%Y  at  %H: %M"
        )
        sunset = datetime.datetime.fromtimestamp(weather["sys"]["sunset"]).strftime(
            "%d.%m.%Y  at  %H: %M"
        )

        wind = f'{weather["wind"]["speed"]:.1f} m/s'

        await message.answer(
            f"---------------- {datetime.datetime.now().strftime('%h %m    %H:%M ')}-----------------\n\n"
            f"In {city}  temperature  {temp} (feels {feels}°C) \n{wd}\n\nSunset:\t\t{sunset}\n\n"
            f"Sunrise:\t{sunrise}\n\nHumidity:\t{humidity}\n\nWind:\t\t{wind}\n\nCountry code:\t{code}"
        )

    except Exception as ex:
        await message.reply("Please, try again!")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
