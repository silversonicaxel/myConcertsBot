#!/usr/bin/env python3
from dotenv import load_dotenv
from datetime import datetime, timedelta
from concert import Concert
import os
import requests
import json


today = datetime.now()
range_days = timedelta(days=7)
future_day = today + range_days
max_date = future_day.strftime('%Y-%m-%d')


def get_info_artist(artist_search: str):
    artist_concerts = []

    artists = get_artists(artist_search)
    if len(artists):
        artist_id = str(artists[0]['id'])
        artist_concerts_data = get_concerts_via_artist(artist_id)

        for concert in artist_concerts_data:
            artist_concerts.append(parse_concert(concert))

    return artist_concerts


def get_info_city(city_search: str):
    location_concerts = []

    locations = get_locations(city_search)
    if len(locations):
        location_id = str(locations[0]['metroArea']['id'])
        location_concerts_data = get_concerts_via_location(location_id)

        for concert in location_concerts_data:
            location_concerts.append(parse_concert(concert))

    return location_concerts


def get_info_search(search: str):
    artist_concerts = get_info_artist(search)
    location_concerts = get_info_city(search)
    return (artist_concerts, location_concerts)


def parse_concert(concert: object):
    artists = []
    for artist in concert.get('performance'):
        artists.append(artist.get('artist').get('displayName'))
    date_raw = concert.get('start').get('date')
    date = datetime.strptime(date_raw, '%Y-%m-%d').strftime('%d %B %Y')
    venue = concert.get('venue').get('displayName')
    latitude = concert.get('venue').get('lat')
    longitude = concert.get('venue').get('lng')
    city = concert.get('venue').get('metroArea').get('displayName')
    country = concert.get('venue').get(
        'metroArea').get('country').get('displayName')

    return Concert(artists, date, venue, latitude, longitude, city, country)


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
