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


# En-tête de la requête avec le jeton d'accès
headers = {
    'Authorization': f'Bearer {token}',
}


def get_track_id(track):
    # We make sure track is a string
    track = str(track)

    # Request for the track
    search_url = "https://api.spotify.com/v1/search"
    search_params = {
        'q': track,
        'type': 'track',
        'limit': 1,
    }

    # Search
    search_response = requests.get(search_url, params=search_params, headers=headers)
    search_data = search_response.json()

    # Verify if there are results
    if 'tracks' in search_data and 'items' in search_data['tracks'] and search_data['tracks']['items']:
        # We take the ID of the first song found.
        track_id = search_data['tracks']['items'][0]['id']
        return (track_id)

    else:
        print("Aucun résultat trouvé pour la chanson " + track)
        return(None)



"""
    # Request the caracteristics
    features_url = f"https://api.spotify.com/v1/audio-features/{track_id}"
    features_response = requests.get(features_url, headers=headers)
    features_data = features_response.json()

    # Vérifier si des résultats ont été trouvés pour les caractéristiques de la piste
    if features_data:
        print("Caractéristiques de la piste " + track + " de Muse :")
        print(f"Clé: {features_data['key']}")
        print(f"Tempo: {features_data['tempo']}")
        print(f"Énergie: {features_data['energy']}")
        # Ajoutez d'autres caractéristiques selon vos besoins
    else:
        print("Aucun résultat trouvé pour les caractéristiques de la piste " + track + " de Muse")
"""

print(get_track_id("Verona"))

"""
# URL de l'endpoint pour obtenir les caractéristiques de la piste
features_url = f"https://api.spotify.com/v1/audio-features/{track_id}"

# En-tête de la requête avec le jeton d'accès
headers = {
    'Authorization': f'Bearer {token}',
}

# Effectuer la requête GET
response = requests.get(features_url, headers=headers)

# Vérifier la réponse
if response.status_code == 200:
    # La réponse est au format JSON, imprimez toutes les caractéristiques
    features_data = response.json()
    print("Caractéristiques de la piste :")
    for key, value in features_data.items():
        print(f"{key}: {value}")
else:
    print(f"Erreur lors de la requête : {response.status_code} - {response.text}")







# URL de l'endpoint pour obtenir les caractéristiques de la piste
analysis_url = f"https://api.spotify.com/v1/audio-analysis/{track_id}"

# En-tête de la requête avec le jeton d'accès
headers = {
    'Authorization': f'Bearer {token}',
}

# Effectuer la requête GET
response = requests.get(analysis_url, headers=headers)

# Vérifier la réponse
if response.status_code == 200:
    # La réponse est au format JSON, imprimez toutes les caractéristiques
    analysis_data = response.json()
    print("Caractéristiques de la piste :")
    i = 0
    for key, value in analysis_data.items():
        print(f"{key}: {value}", i, "\n \n \n")
        i += 1
    print(len(analysis_data.items()))
else:
    print(f"Erreur lors de la requête : {response.status_code} - {response.text}")

"""