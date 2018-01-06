import spotipy
import json
import pprint
sp = spotipy.Spotify()
from spotipy.oauth2 import SpotifyClientCredentials
cid ="29ed730a97614d47855056f3f71ff371"
secret = "f1656e76e32e4d3b922f23c1ee5416a4"
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False
artist = 'Paul Van Dyk'
artist = sp.search(q = artist)
