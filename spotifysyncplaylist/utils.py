from .config import CLIENT_ID, CLIENT_SECRET
import spotipy.util as util
import spotipy


def get_playlist_tracks(client, username, uri):
    results = client.user_playlist_tracks(username, playlist_id=uri)
    tracks = []
    for i in results['items']:
        tracks.append(i['track']['id'])
    while results['next']:
        results = client.next(results)
        for i in results['items']:
            tracks.append(i['track']['id'])
    return tracks


def clear_playlist(client, username, target):
    client.user_playlist_replace_tracks(username, target, [])


def initSpotifyAPI(username, scope="user-library-read playlist-modify-public playlist-modify-private", client_id=CLIENT_ID,
                   client_secret=CLIENT_SECRET, redirect_uri='https://stoicatedy.ovh'):
    token = util.prompt_for_user_token(username, scope, client_id,
                                       client_secret, redirect_uri='https://stoicatedy.ovh')
    if token:
        return spotipy.Spotify(auth=token)
    else:
        raise Exception("No token provided.")
