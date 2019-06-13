#!/usr/bin/env python3
from dotenv import load_dotenv
import os
import requests
import json

def get_info_search(search: str):
  artists = get_artists(search)
  locations = get_locations(search)

def get_artists(artist: str):
  request_url = 'https://api.songkick.com/api/3.0/search/artists.json?query=' + artist + '&apikey=' + os.getenv("songkick_token")
  response = requests.get(request_url)
  artists = json.loads(response.content.decode('utf-8'))

  if artists.get('resultsPage').get('totalEntries') > 0:
    print(artists.get('resultsPage').get('results').get('artist')[0])
    return artists.get('resultsPage').get('results').get('artist')[0]
  else:
    return []

def get_locations(location: str):
  request_url = 'https://api.songkick.com/api/3.0/search/locations.json?query=' + location + '&apikey=' + os.getenv("songkick_token")
  response = requests.get(request_url)
  locations = json.loads(response.content.decode('utf-8'))

  if locations.get('resultsPage').get('totalEntries') > 0:
    print(locations.get('resultsPage').get('results').get('location')[0])
    return locations.get('resultsPage').get('results').get('location')[0]
  else:
    return []
