from flask import Flask, render_template, request, redirect
from spotify import app_Authorization, user_Authorization, get_user_liked_songs, Profile_Data

app = Flask(__name__, template_folder="templates")

#renders the web page
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    auth_url = app_Authorization()
    return redirect(auth_url)

@app.route("/callback")
def callback():
    authorization_header = user_Authorization()

    profile_data = Profile_Data(authorization_header)
    user_id = profile_data["id"]
    user_name = profile_data["display_name"]

    user_liked_songs = get_user_liked_songs(authorization_header)
    return user_liked_songs

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)

# #returns the playlist
# @app.route("/song", methods=["POST","GET"])
# def get_input():
#     formattedPlaylist = ""
#     real_songs = []
#     song = request.form["song"]
#     tags = get_song_tags(song)
#     playlist = generate_playlist(tags)

#     for song in playlist.split("\n"):
#         result = spotify.search(q=song, type="track", limit=1)
#         if len(result["tracks"]["items"]) > 0:
#             track_id = result["tracks"]["items"][0]["id"]
#             track_url = result["tracks"]["items"][0]["external_urls"]["spotify"]
#             real_songs.append(result["tracks"]["items"][0]["name"] + " \n" + track_url)

#     if len(real_songs) > 0:
#         formattedPlaylist += "Here's your playlist:\n"
#         for song1 in real_songs:
#             formattedPlaylist+= f"- {song1}\n"

#     return formattedPlaylist

# if __name__ == '__main__':
#     app.run(host='localhost', port=5000, debug=True)



# #console version
# print("Welcome to SpotifAI.")
# #Asks user to put in their favorite song, generates tags and then uses the tags to generate a playlist
# song = input("Input a song to get started: ")
# tags = get_song_tags(song)
# print(f"Here are some tags for the song '{song}': {tags}")
# playlist = generate_playlist(tags)

# #Uses spotify to check if the songs that were generated were real and not just made up by the AI.
# #Gets the full name of the song and a playable link.
# real_songs = []

# for song in playlist.split("\n"):
#     result = spotify.search(q=song, type="track", limit=1)
#     if len(result["tracks"]["items"]) > 0:
#         track_id = result["tracks"]["items"][0]["id"]
#         track_url = result["tracks"]["items"][0]["external_urls"]["spotify"]
#         real_songs.append(result["tracks"]["items"][0]["name"] + " \n" + track_url)

# if len(real_songs) > 0:
#     print("Here's your playlist:")
#     for song in real_songs:
#         print(f"- {song}")
# else:
#     print("")