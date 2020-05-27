# web_app\services\spotify_service.py

import os
from dotenv import load_dotenv
import spotipy
from spotipy import oauth2

load_dotenv()

cid = os.getenv("SPOTIPY_CLIENT_ID", default="OOPS")
secret = os.getenv("SPOTIPY_CLIENT_SECRET", default="OOPS")

credentials = oauth2.SpotifyClientCredentials(client_id=cid,
                                              client_secret=secret)
spot = spotipy.Spotify(client_credentials_manager=credentials)

# artist_name = "queen"
# track_name = "bohemian rhapsody"
# song_info = spot.search(q=f'artist:{artist_name} track:{track_name}')
# breakpoint()
# track_id = song_info['tracks']['items'][0]['id']
# print(track_id)
