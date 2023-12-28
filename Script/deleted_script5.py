'''
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

import requests
from script2 import *

access_token = access_token()

def get_artist_genres(artist_id):

    headers = {'Authorization': 'Bearer ' + access_token}

    # Endpoint pour obtenir les informations sur un artiste
    endpoint = f"https://api.spotify.com/v1/artists/{artist_id}"

    # Faire la requête GET à l'API Spotify
    response = requests.get(endpoint, headers=headers)

    # Vérifier si la requête a réussi (statut 200 OK)
    if response.status_code == 200:
        # Analyser la réponse JSON
        data = response.json()

        # Obtenir les genres de l'artiste s'ils existent
        genres = data.get("genres", [])
        print("ok")
        return genres
    else:
        # Afficher un message d'erreur si la requête a échoué
        print(f"Erreur {response.status_code}: Impossible d'obtenir les genres de l'artiste.")
        return None

import requests
'''

import requests

def get_artists_genres(artist_ids, headers):
    # Convertir la liste d'IDs d'artistes en une chaîne séparée par des virgules
    artists_str = ",".join(artist_ids)

    # Endpoint pour obtenir les informations sur plusieurs artistes
    endpoint = f"https://api.spotify.com/v1/artists?ids={artists_str}"

    # Faire la requête GET à l'API Spotify
    response = requests.get(endpoint, headers=headers)

    # Vérifier si la requête a réussi (statut 200 OK)
    if response.status_code == 200:
        # Analyser la réponse JSON
        data = response.json()

        # Récupérer les genres de chaque artiste
        all_genres = []
        for artist_data in data["artists"]:
            genres = artist_data.get("genres", [])
            all_genres.append(genres)

        return all_genres
    else:
        # Afficher un message d'erreur si la requête a échoué
        print(f"Erreur {response.status_code}: Impossible d'obtenir les genres des artistes.")
        return [None]*len(artist_ids)

