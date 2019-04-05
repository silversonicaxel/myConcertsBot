#!/usr/bin/env python3
from dotenv import load_dotenv
import os
import telepot

__author__ = "Alessandro Rabitti"
__version__ = "0.0.1"
__license__ = "MIT"

def main():
    load_dotenv()
    telegram_token = os.getenv("telegram_token")
    print(telegram_token)

    bot = telepot.Bot(telegram_token)
    print(bot.getMe())

if __name__ == "__main__":
    main()
