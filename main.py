#!/usr/bin/python3
import spotipy
import sys
import logging as log
import re
from spotifysyncplaylist.utils import initSpotifyAPI, get_playlist_tracks, clear_playlist


def main():
    if len(sys.argv) is 3:
        # In case we get two spotify URIs in sys.argv
        usernametocopy = sys.argv[1].split(':')[2]
        playlisttocopy = sys.argv[1].split(':')[4]
        usernametarget = sys.argv[2].split(':')[2]
        playlisttarget = sys.argv[2].split(':')[4]
    elif len(sys.argv) < 5:
        URI = input(
            "Enter the URI of the playlist that you want to copy: ")
        # This makes the program compatible with open.spotify.com links
        URI = 'spotify:' + \
            re.sub(r'(http[s]?:\/\/)?(open.spotify.com)\/',
                   '', URI).replace('/', ':')
        URI = re.sub(r'\?.*', '', URI)

        usernametocopy = URI.split(":")[2]
        playlisttocopy = URI.split(":")[4]

        # This makes the program compatible with open.spotify.com links
        URI = input(
            "Enter the URI of the target playlist: ")
        URI = 'spotify:' + \
            re.sub(r'(http[s]?:\/\/)?(open.spotify.com)\/',
                   '', URI).replace('/', ':')
        URI = re.sub(r'\?.*', '', URI)

        usernametarget = URI.split(':')[2]
        playlisttarget = URI.split(':')[4]

    else:
        # In case we get four IDs in sys.argv
        usernametocopy = sys.argv[1]
        playlisttocopy = sys.argv[2]
        usernametarget = sys.argv[3]
        playlisttarget = sys.argv[4]

    sp = initSpotifyAPI(usernametocopy)
    playlist = get_playlist_tracks(sp, usernametocopy, playlisttocopy)
    # This sets the playlist to nothing
    clear_playlist(sp, usernametarget, playlisttarget)
    # This adds the song in order to the target playlist
    while len(playlist):
        sp.user_playlist_add_tracks(
            usernametarget, playlisttarget, playlist[0:99])
        playlist = playlist[100:]


if __name__ == "__main__":
    main()
