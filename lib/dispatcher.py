#!/usr/bin/env python3
from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, executor, types
import info

load_dotenv()

bot = Bot(token=os.getenv("telegram_token"))
dispatcher = Dispatcher(bot)

@dispatcher.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hello I am My Concerts Bot and I am here to help you in knowing the concert around your town.")

@dispatcher.message_handler()
async def echo(message: types.Message):
    info.get()
    await bot.send_message(message.chat.id, 'You said: ' + message.text)

def poll():
    executor.start_polling(dispatcher, skip_updates=True)
