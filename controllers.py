from flask import Flask, render_template, request, redirect, session
from spotify import app_Authorization, user_Authorization, Profile_Data, get_user_liked_songs, search_song
from openaiapi import get_song_tags, generate_playlist

app = Flask(__name__, template_folder="templates")
app.secret_key = 'david'

#renders the web page
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    auth_url = app_Authorization()
    session["spotify"] = auth_url
    return redirect(auth_url)

@app.route("/callback")
def callback():
    spotify = session.get("spotify")
    user = user_Authorization()
    session["user"] = user

    return redirect("/song")

@app.route("/song", methods=["POST","GET"])
def get_input():
    header = session.get("user")
    formattedPlaylist = ""
    real_songs = []
    playlist_dict ={}
    # song = request.form["song"]
    song = "lo que hay x aqui"
    tags = get_song_tags(song)
    playlist = generate_playlist(tags)

    for song in playlist.split("\n"):
        result = search_song(header = header, song_name = song)
        if len(result["tracks"]["items"]) > 0:
            track_id = result["tracks"]["items"][0]["id"]
            track_url = result["tracks"]["items"][0]["external_urls"]["spotify"]
            real_songs.append(result["tracks"]["items"][0]["name"] + " \n" + track_url)
            playlist_dict[result["tracks"]["items"][0]["name"]] = track_url

    return playlist_dict

if __name__ == '__main__':
    app.run(host='localhost', port=2000, debug=True)