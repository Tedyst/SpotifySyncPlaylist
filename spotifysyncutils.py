def get_playlist_tracks(client, username, uri):
    results = client.user_playlist_tracks(username, uri)
    tracks = results['items']
    while results['next']:
        results = client.next(results)
        tracks.extend(results['items'])
    return tracks


def sync_playlist(client, username, target, playlist):
    client.user_playlist_replace_tracks(username, target, playlist)
