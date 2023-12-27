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

def access_API():
    # Access to the API
    token = access_token()

    # Request with the access token :
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return (token, headers)


def get_track_id(track, headers):
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

def get_track_details(track_ids, headers):
    tracks_url = 'https://api.spotify.com/v1/tracks'
    params = {'ids': ','.join(track_ids)}

    response = requests.get(tracks_url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()['tracks']
    else:
        print(f"Erreur lors de la récupération des détails des pistes. Code d'erreur : {response.status_code}")
        return None

def get_audio_features(track_id, headers):
    """
    Return a dictionnary for the track.
    track_id must be just a string for one single track.
    """
    audio_features_url = f'https://api.spotify.com/v1/audio-features/{track_id}'

    response = requests.get(audio_features_url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erreur lors de la récupération des caractéristiques audio de la piste. Code d'erreur : {response.status_code}")
        return None



def get_track_features(track_id, headers):
    """
    Return a dictionnary for the track features.
    track_id my be a list of under 100 tracks or just a string for one single track.
    """
    if type(track_id) == list:
        track_id = ','.join(track_id)

    params = {'ids': track_id}
    features_url = "https://api.spotify.com/v1/audio-features"
    response = requests.get(features_url, headers=headers,params=params)
    print(response)

    # Verify the response: 
    if response.status_code == 200:
        # La réponse est au format JSON, imprimez toutes les caractéristiques
        data = response.json()
        return(data['audio_features'])
    else:
        print(f"Erreur lors de la requête : {response.status_code} - {response.text}")
        return(None)



def get_track_analysis(track_id, headers):
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


def get_features_labels(headers):
    """
    Returns a list of the features labels the spotify API gives us
    """
    track_id = get_track_id("Lose Yourself", headers)
    data_features = get_audio_features(track_id, headers)

    df = pd.DataFrame([data_features])
    features = df.columns.tolist()

    return features


def get_analysis_labels(headers):
    """
    Returns a list of the features labels the spotify API gives us
    """
    track_id = get_track_id("Lose Yourself", headers)
    data_analysis = get_track_analysis(track_id, headers)

    df = pd.DataFrame([data_analysis])
    analysis = df.columns.tolist()

    return analysis
