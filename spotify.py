import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from flask import Flask, render_template, request
import openai

app = Flask(__name__, template_folder="templates")

#authentication stuff
openai.api_key = "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"

spotify_client_id = "e68285acd05e49bb9134e5bcc2622778"
spotify_client_secret = "9c30bbe0f3ed49ae83dab84643141535"

scope = "user-library-read"

spotify_client_credentials_manager = SpotifyClientCredentials(
    client_id=spotify_client_id,
    client_secret=spotify_client_secret
)

def app_Authorization():
    REDIRECT_URI = get_redirect_uri()
    auth_query_parameters = {
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "scope": SCOPE,
        # "state": STATE,
        # "show_dialog": SHOW_DIALOG_str,
        "client_id": CLIENT_ID
    }
    url_args = "&".join(["{}={}".format(key, urllib.parse.quote(val)) for key,val in auth_query_parameters.items()])
    auth_url = f"{SPOTIFY_AUTH_URL}/?{url_args}"
    return auth_url

@app.route("/")
def home():
    
    return render_template("index.html")



@app.route("/callback")
def callback():
    spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(scope=scope, client_id=spotify_client_id, client_secret=spotify_client_secret, redirect_uri="http://localhost:8888/callback")
    )
    result = spotify.current_user_saved_tracks(scope=scope)
    return result


