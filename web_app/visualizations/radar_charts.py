# web_app\visualizations\radar_charts.py

import pandas as pd
import spotipy
from spotipy import oauth2, Spotify
from dotenv import load_dotenv
import os
import plotly.express as px
import plotly.graph_objects as go

load_dotenv()

cid = os.getenv("SPOTIPY_CLIENT_ID")
secret = os.getenv("SPOTIPY_CLIENT_SECRET")

credentials = oauth2.SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=credentials)

def visualization(artist_name, track_name):
    """
    function to output radar graph for given artist name and track name
    """
    data = sp.search(q=f'artist:{artist_name} track:{track_name}')
    artist_name = data['tracks']['items'][0]['artists'][0]['name']
    track_name = data['tracks']['items'][0]['name']
    track_id = data['tracks']['items'][0]['id']   
    album_name = data['tracks']['items'][0]['album']['name']
    album_id = data['tracks']['items'][0]['album']['id']
    album_cover_link = data['tracks']['items'][0]['album']['images'][0]['url']
    track_sample = data['tracks']['items'][0]['preview_url']
    audio_features = sp.audio_features(track_id)
    audio_features = audio_features[0] # changes the provided list from spotify into a dictionary
    irrelevant = ["id", "uri", "analysis_url", "type", "track_href"]
    for key in irrelevant:
      del audio_features[key]
    #audio_features = jsonify(audio_features) in FLASK app
    song_info =  [track_name, artist_name, track_id, album_name, album_id, album_cover_link, track_sample, audio_features]

    song_info = song_info[7]
    for key in ['duration_ms', 'key', 'loudness', 'tempo', 'time_signature']:
        song_info.pop(key)
    keys = list(song_info.keys())
    values = list(song_info.values())

    fig = go.Figure(data=go.Scatterpolar(
    r=values,
    theta=keys,
    fill='toself'
    ))

    fig.update_layout(
    polar=dict(
        radialaxis=dict(
        visible=True
        ),
    ),
    title="Audio Features for {song_title} by {artist_name}",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="#7f7f7f"
        ),
    showlegend=False
    )

    return fig.show()
