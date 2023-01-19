import requests
from config import API, TOKEN
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def get_city(message: types.Message):
    await message.answer(
        "Hi there!\nSend me correct city to see the weather of the place.\nGood luck!"
    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
