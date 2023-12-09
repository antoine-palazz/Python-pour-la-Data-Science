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

track_id = get_track_id("Verona")
print(track_id)

def get_track_features(track_id):
    track_id = str(track_id)
    # Request the caracteristics
    features_url = f"https://api.spotify.com/v1/audio-features/{track_id}"
    features_response = requests.get(features_url, headers=headers)
    features_data = features_response.json()

    # Vérifier la réponse
    if features_response.status_code == 200:
        # La réponse est au format JSON, imprimez toutes les caractéristiques
        features_data = features_response.json()
        print("Caractéristiques de la piste :")
        for key, value in features_data.items():
            print(f"{key}: {value}")
    else:
        print(f"Erreur lors de la requête : {features_response.status_code} - {features_response.text}")

print(get_track_features(track_id))

def get_track_features(track_id):
    """
    Renvoie le dictionnaire des features du morceau.
    """
    track_id = str(track_id)
    # Request the caracteristics
    features_url = f"https://api.spotify.com/v1/audio-features/{track_id}"
    response = requests.get(features_url, headers=headers)

    # Vérifier la réponse
    if response.status_code == 200:
        # La réponse est au format JSON, imprimez toutes les caractéristiques
        data = response.json()
        return(data)
    else:
        print(f"Erreur lors de la requête : {response.status_code} - {response.text}")
        return(None)

print(get_track_features(track_id))



def get_track_analysis(track_id):
    """
    Renvoie le dictionnaire des features du morceau.
    """
    track_id = str(track_id)
    # Request the caracteristics
    analysis_url = f"https://api.spotify.com/v1/audio-analysis/{track_id}"
    response = requests.get(analysis_url, headers=headers)

    # Vérifier la réponse
    if response.status_code == 200:
        # La réponse est au format JSON, imprimez toutes les caractéristiques
        data = response.json()
        return(data)
    else:
        print(f"Erreur lors de la requête : {response.status_code} - {response.text}")
        return(None)

data_analysis = get_track_analysis(track_id)
data_features = get_track_features(track_id)
df1 = pd.DataFrame([data_analysis])
df2 = pd.DataFrame([data_features])
print(df1)
print(df2)

from script1 import playlist
playlist0 = playlist[:5]
print(playlist0)
Titles = pd.DataFrame({'Title': playlist0})
print(Titles)
print(data_features)
Features = list(data_features.keys())
print(Features)

Titles['track_id'] = Titles['Title'].apply(get_track_id)
Titles['track_features'] = Titles['track_id'].apply(get_track_features)
print(Titles.info)
for feature in Features:
    Titles[feature] = Titles['track_features'].apply(lambda x: x.get(feature))
Titles.drop(columns=['track_features'], inplace = True)

print(Titles)
"""
path = '/home/onyxia/work/Python-pour-la-Data-Science/Data/data/Titles.csv'
Titles.to_csv(path, index=False)
"""