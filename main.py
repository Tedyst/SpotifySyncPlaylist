#!/usr/bin/python3
import spotipy
import sys
import logging as log
import re
import time
from spotifysyncplaylist.utils import initSpotifyAPI, get_playlist_tracks, clear_playlist
from spotifysyncplaylist.config import AUTO, TIMEOUT

usernametocopy = ""
playlisttocopy = ""
usernametarget = ""
playlisttarget = ""
sp = ""


def main():
    if len(sys.argv) is 3:
        # In case we get two spotify URIs in sys.argv
        URI = sys.argv[1]
        URI = 'spotify:' + \
            re.sub(r'(http[s]?:\/\/)?(open.spotify.com)\/',
                   '', URI).replace('/', ':')
        URI = re.sub(r'\?.*', '', URI)
        usernametocopy = URI.split(':')[2]
        playlisttocopy = URI.split(':')[4]

        URI = sys.argv[1]
        URI = 'spotify:' + \
            re.sub(r'(http[s]?:\/\/)?(open.spotify.com)\/',
                   '', URI).replace('/', ':')
        URI = re.sub(r'\?.*', '', URI)
        usernametarget = URI.split(':')[2]
        playlisttarget = URI.split(':')[4]
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
    if sp:
        pass
    else:
        log.error("Spotify API not working.")


def get_playlists():
    playlist = get_playlist_tracks(sp, usernametocopy, playlisttocopy)
    # This sets the playlist to nothing
    clear_playlist(sp, usernametarget, playlisttarget)
    # This adds the song in order to the target playlist
    while len(playlist):
        sp.user_playlist_add_tracks(
            usernametarget, playlisttarget, playlist[0:99])
        playlist = playlist[100:]


if __name__ == "__main__":
    if AUTO == True:
        while True:
            main()
            log.log(
                "INFO", "We ran main(), and copied the playlist. Next run in 60 seconds.")
            time.sleep(TIMEOUT)
    else:
        main()
        get_playlists()
