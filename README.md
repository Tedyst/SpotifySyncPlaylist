# SpotifySyncPlaylist

A short Python script that copies one playlist to another playlist.

## Usage

Firstly you need to get credientials from Spotify, to use their API.

Create a file named spotifyconfig.py and populate it with:

```python
CLIENT_ID = ""
CLIENT_SECRET = ""
```

Then open a terminal and type:

```sh
main.py [playlist to copy] [target playlist]
```

You need to use the playlist's URI or playlist's `open.spotify.com` URL.

## Example

```sh
main.py spotify:user:vq0u2761le51p2idib6f89y78:playlist:1In3jsElefKy433ezeoZAG spotify:user:vq0u2761le51p2idib6f89y78:playlist:6KUpozVNQ4qdyIHuRtMtjF
```
