#!/usr/bin/env python3
from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, executor, types

load_dotenv()
telegram_token = os.getenv("telegram_token")

bot = Bot(token=telegram_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hello I am My Concerts Bot and I am here to help you in knowing the concert around your town.")

@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.chat.id, 'You said: ' + message.text)

def poll():
  executor.start_polling(dp, skip_updates=True)
