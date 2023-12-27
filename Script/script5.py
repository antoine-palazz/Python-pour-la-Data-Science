import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


client_id = "b6871ef2f14a4b60888a32454862b876"
client_secret = "3a5d22aa09434e32a9760159ca3bb234"


client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Fonction pour obtenir les genres d'un artiste
def get_artist_genres(artist_name):
    results = sp.search(q='artist:' + artist_name, type='artist')
    if results['artists']['items']:
        artist = results['artists']['items'][0]
        genres = artist['genres']
        return genres
    else:
        return None

# Exemple d'utilisation
artist_name = 'Bob Marley'
genres = get_artist_genres(artist_name)
if genres:
    print(f"Genres de l'artiste {artist_name}: {', '.join(genres)}")
else:
    print(f"Aucun résultat trouvé pour l'artiste {artist_name}")
