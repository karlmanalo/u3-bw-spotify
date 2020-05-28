# web_app/routes/suggestion_routes.py

from flask import Blueprint, render_template, request
# from web_app.services.spotify_service import spot
import requests
from dotenv import load_dotenv
import os

load_dotenv()

SPOTIFY_AUTHORIZATION = os.getenv("SPOTIFY_SECRET")

suggestion_routes = Blueprint("suggestion_routes", __name__)


@suggestion_routes.route("/suggest/<artist_name>/<track_name>",
                         methods=["GET"])
def suggest_songs(artist_name, track_name):

    """Gets access token utilizing client credentials"""
    headers = {
        'Authorization': f"Basic {SPOTIFY_AUTHORIZATION}"
    }

    data = {
        'grant_type': 'client_credentials'
    }

    response = requests.post('https://accounts.spotify.com/api/token',
                             headers=headers,
                             data=data)

    access_token = response.json()['access_token']

    artist_name = artist_name
    track_name = track_name
    # artist_name = request.form["artist"]
    # track_name = request.form["title"]

    user_query = artist_name + ' ' + track_name

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {access_token}",
    }

    params = (
        ('q', user_query),
        ('type', 'track,artist'),
    )

    song_info = requests.get('https://api.spotify.com/v1/search',
                             headers=headers,
                             params=params)

    track_id = song_info.json()['tracks']['items'][0]['id']  # TODO: remove .json() depending output of Erick's code

    print(track_id)

    # TODO: INCORPORATE PICKLED MODEL HERE. EXPECTED INPUT SONG ID?, EXPECTED
    # OUTPUT 10 RECOMMENDED SONGS
    return render_template("suggestion_results.html",
                           title=track_name,
                           artist=artist_name  # TODO: replace with model's results
                           )
