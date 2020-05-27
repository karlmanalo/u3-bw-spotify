# web_app/routes/suggestion_routes.py

from flask import Blueprint, render_template, request
from web_app.services.spotify_service import spot
import requests


suggestion_routes = Blueprint("suggestion_routes", __name__)


@suggestion_routes.route("/suggest/<artist_name>/<track_name>", methods=["GET"])
def suggest_songs(artist_name, track_name):

    artist_name = artist_name  # TODO: ENCODE SPACES? str.replace(" ", "%20")?
    track_name = track_name  # TODO: ENCODE SPACES? str.replace(" ", "%20")?
    print(artist_name)
    print(track_name)

    user_query = artist_name + ' ' + track_name
    
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer BQCzLNEJZst0KzIJSmiKHFqFtlCWoO8NBo9DJwD7HgKuOxTuwZCqUWx2_TOUYn0uqzAFPLP-TUX49YBgyIEZUucFBEtabumCn4ukykdgjwJwCzapKHCUvlVEWQWELfEYOLLP1WY1XLlh_BsfglV_9m0',
    }

    params = (
        ('q', user_query), #  TODO: replace second item in tuple with user_query
        ('type', 'track,artist'),
    )

    song_info = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params)

    breakpoint()
    # breakpoint()
    # song_info = spot.search(q=f'artist:{artist_name} track:{track_name}')

    track_id = song_info.json()['tracks']['items'][0]['id']

    # TODO: INCORPORATE PICKLED MODEL HERE. EXPECTED INPUT SONG ID?, EXPECTED
    # OUTPUT 10 RECOMMENDED SONGS
    return render_template("suggestion_results.html",
                           title=track_name, #  TODO: replace with track_name
                           artist=artist_name #  TODO: replace with artist_name AND output model's results
                           )
