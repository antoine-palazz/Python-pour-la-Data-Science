import requests
import pandas as pd
from base64 import b64encode

client_id = "b6871ef2f14a4b60888a32454862b876"
client_secret = "3a5d22aa09434e32a9760159ca3bb234"

def access_token():
    """
    Return the access token for Spotify API
    """
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

access_token = access_token()

# Remplacez 'YOUR_PLAYLIST_ID' par l'ID de la playlist que vous souhaitez récupérer
playlist_id = '37i9dQZF1DX69KJk2S04Hp'

# Obtenez les pistes de la playlist avec gestion de la pagination
def get_all_playlist_tracks(playlist_id, access_token):
    playlist_url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
    headers = {'Authorization': 'Bearer ' + access_token}
    params = {'offset': 0, 'limit': 100}  # Limitez la réponse à 100 pistes à la fois

    all_tracks = []

    while True:
        response = requests.get(playlist_url, headers=headers, params=params)

        if response.status_code == 200:
            playlist_data = response.json()
            tracks = playlist_data['items']
            all_tracks.extend(tracks)

            # Vérifiez s'il y a plus de pistes à récupérer
            if playlist_data['next']:
                # Mettez à jour l'offset pour obtenir la page suivante
                params['offset'] += params['limit']
            else:
                break
        else:
            print(f"Erreur lors de la récupération des pistes de la playlist. Code d'erreur : {response.status_code}")
            return None

    return all_tracks

# Affichez les titres des pistes
def print_track_titles(tracks):
    if tracks:
        for track in tracks:
            print(track['track']['name'])
    else:
        print("Aucune piste trouvée.")

# Obtenez toutes les pistes de la playlist
playlist_tracks = get_all_playlist_tracks(playlist_id, access_token)

# Affichez les titres des pistes
print_track_titles(playlist_tracks)