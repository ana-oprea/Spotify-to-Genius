from pprint import pprint
import requests
import time
from googlesearch import search
import lyricsgenius

genius = lyricsgenius.Genius('put your genius token here')
SPOTIFY_ACCESS_TOKEN = 'put your spotify token here'
SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
def get_current_track(access_token):
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
    )
    resp_json = response.json()

    track_id = resp_json['item']['id']
    track_name = resp_json['item']['name']
    artists = resp_json['item']['artists']
    artists_names = ', '.join(
        [artist['name'] for artist in artists])

    current_track_info = {
        "id": track_id,
        "name": track_name,
        "artists": artists_names,
    }
    return current_track_info

def main():
    current_track_id = None
    while True:
        current_track_info = get_current_track(
        SPOTIFY_ACCESS_TOKEN
        )
        if current_track_info['id'] != current_track_id:
            pprint(current_track_info, indent = 4)
            current_track_id = current_track_info['id']
            query = current_track_info['name'] + " " + current_track_info['artists'] + " genius"
            for j in search(query, tld = "co.in", num = 1, stop = 1, pause = 2):
                print(j)
                song = genius.search_song(current_track_info['name'], current_track_info['artists'])
                print(song.lyrics)
        
        time.sleep(1)

if __name__ == '__main__':
    main()