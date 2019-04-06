from dotenv import load_dotenv
import os
import requests
import json

def get():
    response = requests.get(os.getenv("songkick_url"))
    print(json.loads(response.content.decode('utf-8')))
