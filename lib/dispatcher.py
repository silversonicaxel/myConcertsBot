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
    await message.reply("Hello I am My Concerts Bot and I am here to help you in knowing the concerts you are intereted in.")


@dispatcher.message_handler()
async def echo(search: types.Message):
    await bot.send_message(search.chat.id, 'Analyzing concerts of ' + search.text + '.')
    info.get_info_search(search.text)


def poll():
    executor.start_polling(dispatcher, skip_updates=True)
