#!/usr/bin/env python3
from dotenv import load_dotenv
import os

__author__ = "Alessandro Rabitti"
__version__ = "0.0.1"
__license__ = "MIT"

def main():
    load_dotenv()
    telegram_token = os.getenv("telegram_token")
    print(telegram_token)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
