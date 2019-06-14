#!/usr/bin/env python3
from dotenv import load_dotenv
from datetime import datetime, timedelta
import os
import requests
import json

today = datetime.now()
range_days = timedelta(days=7)
future_day = today + range_days
max_date = future_day.strftime("%Y-%m-%d")


def get_info_search(search: str):
    artists = get_artists(search)
    if len(artists):
        artists_concerts = get_concerts_via_artist(str(artists[0]['id']))
        print(artists_concerts)

    locations = get_locations(search)
    if len(locations):
        locations_concerts = get_concerts_via_artist(
            str(locations[0]['metroArea']['id']))
        print(locations_concerts)


def get_artists(artist: str):
    request_url = 'https://api.songkick.com/api/3.0/search/artists.json?query=' + \
        artist + '&apikey=' + os.getenv("songkick_token")
    response = requests.get(request_url)
    artists = json.loads(response.content.decode('utf-8'))

    if artists.get('resultsPage').get('totalEntries') > 0:
        return artists.get('resultsPage').get('results').get('artist')
    else:
        return []


def get_concerts_via_artist(artist_id: str):
    request_url = 'https://api.songkick.com/api/3.0/artists/' + artist_id + \
        '/calendar.json?max_date=' + max_date + '&apikey=' + os.getenv("songkick_token")
    response = requests.get(request_url)
    concerts = json.loads(response.content.decode('utf-8'))

    if concerts.get('resultsPage').get('totalEntries') > 0:
        return concerts.get('resultsPage').get('results').get('event')
    else:
        return []


def get_locations(location: str):
    request_url = 'https://api.songkick.com/api/3.0/search/locations.json?query=' + \
        location + '&apikey=' + os.getenv("songkick_token")
    response = requests.get(request_url)
    locations = json.loads(response.content.decode('utf-8'))

    if locations.get('resultsPage').get('totalEntries') > 0:
        return locations.get('resultsPage').get('results').get('location')
    else:
        return []


def get_concerts_via_location(location_id: str):
    request_url = 'https://api.songkick.com/api/3.0/metro_areas/' + location_id + \
        '/calendar.json?max_date=' + max_date + '&apikey=' + os.getenv("songkick_token")
    response = requests.get(request_url)
    concerts = json.loads(response.content.decode('utf-8'))

    if concerts.get('resultsPage').get('totalEntries') > 0:
        return concerts.get('resultsPage').get('results').get('event')
    else:
        return []
