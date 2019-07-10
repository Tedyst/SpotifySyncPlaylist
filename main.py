import spotipy
import spotipy.util as util
import sys
from spotifysyncutils import *

scope = 'user-library-read'
username = "spotify:user:vq0u2761le51p2idib6f89y78"
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    playlist = get_playlist_tracks(sp, username, sys.argv[1])
    target = sys.argv[2]
    sync_playlist(sp, username, target, playlist)
else:
    print("No token given.")
