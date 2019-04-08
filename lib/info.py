from dotenv import load_dotenv
import os
import requests
import json

def get_info_search(search: str):
  artist = get_artist(search)

def get_artist(artist: str):
  request_url = 'https://api.songkick.com/api/3.0/search/artists.json?query=' + artist + '&apikey=' + os.getenv("songkick_token")
  response = requests.get(request_url)
  artist = json.loads(response.content.decode('utf-8'))

  if artist.get('resultsPage').get('totalEntries') > 0:
    print(artist.get('resultsPage').get('results').get('artist')[0])
    return artist.get('resultsPage').get('results').get('artist')[0]
  else:
    return []
