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


def sync_playlist(client, username, target, playlist):
    client.user_playlist_replace_tracks(username, target, playlist)
