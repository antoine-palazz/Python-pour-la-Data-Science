import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = "b6871ef2f14a4b60888a32454862b876"
client_secret = "3a5d22aa09434e32a9760159ca3bb234"

# Shows a user's playlists

from spotipy.oauth2 import SpotifyOAuth

scope = 'playlist-read-private'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,client_id=client_id,client_secret=client_secret))

results = sp.current_user_playlists(limit=50)
for i, item in enumerate(results['items']):
    print("%d %s" % (i, item['name']))
