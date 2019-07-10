#!/usr/bin/python3
import spotipy
import spotipy.util as util
import sys
from spotifyconfig import *
from spotifysyncutils import *

scope = 'user-library-read playlist-modify-public playlist-modify-private'
print(sys.argv)
if len(sys.argv) is 3:
    usernametocopy = sys.argv[1].split(':')[2]
    playlisttocopy = sys.argv[1].split(':')[4]
    usernametarget = sys.argv[2].split(':')[2]
    playlisttarget = sys.argv[2].split(':')[4]
elif len(sys.argv) < 5:
    print("Not enough arguments.")
    exit(0)
else:
    usernametocopy = sys.argv[1]
    playlisttocopy = sys.argv[2]
    usernametarget = sys.argv[3]
    playlisttarget = sys.argv[4]
token = util.prompt_for_user_token(usernametocopy, scope, client_id=CLIENT_ID,
                                   client_secret=CLIENT_SECRET, redirect_uri='https://stoicatedy.ovh')

if token:
    sp = spotipy.Spotify(auth=token)
    playlist = get_playlist_tracks(sp, usernametocopy, playlisttocopy)
    sync_playlist(sp, usernametarget, playlisttarget, [])
    while len(playlist):
        sp.user_playlist_add_tracks(
            usernametarget, playlisttarget, playlist[0:99])
        playlist = playlist[100:]
else:
    print("No token given.")
