#!/usr/bin/python3
import spotipy
import sys
import logging as log
from .utils import initSpotifyAPI, get_playlist_tracks, clear_playlist

if __name__ == "__main__":
    if len(sys.argv) is 3:
        usernametocopy = sys.argv[1].split(':')[2]
        playlisttocopy = sys.argv[1].split(':')[4]
        usernametarget = sys.argv[2].split(':')[2]
        playlisttarget = sys.argv[2].split(':')[4]
    elif len(sys.argv) < 5:
        usernametocopy = input("Enter your user ID: ")
        playlisttocopy = input(
            "Enter the ID of the playlist that you want to copy: ")
        usernametarget = input(
            "Enter the user ID of the owner of the playlist that you want to copy to: ")
        playlisttarget = input(
            "Enter the ID of the playlist that you want to copy to: ")
    else:
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
