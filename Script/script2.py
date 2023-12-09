import requests
import pandas as pd
from base64 import b64encode


def access_token():
    """
    Return the access token for Spotify API
    """
    client_id = "b6871ef2f14a4b60888a32454862b876"
    client_secret = "3a5d22aa09434e32a9760159ca3bb234"
    token_url = "https://accounts.spotify.com/api/token"

    # Concatène client-id et client_secret, puis les encode en base64
    credentials = b64encode(f"{client_id}:{client_secret}".encode()).decode('utf-8')

    # En-têtes de la requête
    headers = {
        'Authorization': f'Basic {credentials}',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    # Corps de la requête
    data = {
        'grant_type': 'client_credentials',
    }

    # Effectuer la requête POST
    response = requests.post(token_url, headers=headers, data=data)

    # Vérifier la réponse
    if response.status_code == 200:
        # La réponse est au format JSON, vous pouvez extraire le jeton d'accès de cette façon
        access_token = response.json().get('access_token')
        return(access_token)
    else:
        print(f"Erreur lors de la demande du token : {response.status_code} - {response.text}")
        return(None)

token = access_token()




# ID Spotify du groupe Daft Punk
artist_id = "4tZwfgrHOc3mvqYlEYSvVi"  
# C'est l'ID de Daft Punk, vous pouvez obtenir l'ID d'un artiste en recherchant sur l'API Spotify.

# URL de l'endpoint pour obtenir des informations sur un artiste
artist_url = f"https://api.spotify.com/v1/artists/{artist_id}"

# En-tête de la requête avec le jeton d'accès
headers = {
    'Authorization': f'Bearer {token}',
}

# Effectuer la requête GET
response = requests.get(artist_url, headers=headers)

# Vérifier la réponse
if response.status_code == 200:
    # La réponse est au format JSON, vous pouvez extraire les informations de l'artiste de cette façon
    artist_info = response.json()
    print(f"Informations sur l'artiste Daft Punk :")
    print(f"Nom: {artist_info['name']}")
    print(f"Genres: {', '.join(artist_info['genres'])}")
    print(f"Popularité: {artist_info['popularity']}")
    print(f"URL Spotify: {artist_info['external_urls']['spotify']}")
else:
    print(f"Erreur lors de la requête : {response.status_code} - {response.text}")