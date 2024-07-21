import time
import logging

from aiogram import Bot, Dispatcher, types


TOKEN = "7228537802:AAHc4PSiL4DTCIRKlgDM05vsWuKFW1sFTxk"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands="start")
def start_handler(message: types.Message):
    pass



