#!/usr/bin/env python3
from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, executor, types
import info
from concert import Concert

load_dotenv()

bot = Bot(token=os.getenv("telegram_token"))
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hello I am My Concerts Bot and I am here to help you in knowing the concerts you are intereted in.")


@dispatcher.message_handler()
async def echo(search: types.Message):
    await bot.send_message(search.chat.id, 'Analyzing concerts of ' + search.text + '.')
    concerts = info.get_info_search(search.text)
    concerts_counter = 0

    for typed_concerts in concerts:
        for concert in typed_concerts:
            await bot.send_message(search.chat.id, format_message(concert))
            concerts_counter += 1

    if concerts_counter == 0:
        await bot.send_message(search.chat.id, 'No results for ' + search.text + '.')


def format_message(concert: Concert):
    artists_separator = ', '
    return artists_separator.join(concert.artists) + '\n' + concert.date + \
        ' @ ' + concert.venue + '\n(' + concert.city + ', ' + concert.country + ')\n' + \
        'http://www.google.com/maps/place/' + concert.latitude + ',' + concert.longitude


def poll():
    executor.start_polling(dispatcher, skip_updates=True)
