from delated_script2 import *

access_token = access_token()

#playlist_id = '04ZwFco4KsjgPlVMtzwfgS'

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

# Affichez les ids et les titres des musiques ainsin que les ids et les noms des artistes
def get_track_id_and_artist(tracks):
    if tracks:
        title = []
        track_id = []
        artist = []
        artist_id = []
        for track in tracks:
            title.append(track['track']['name'])
            track_id.append(track['track']['id'])
            artist.append(track['track']['artists'][0]['name'])
            artist_id.append(track['track']['artists'][0]['id'])
        df = pd.DataFrame({'Title':title})
        df['track_id'] = track_id
        df['artist'] = artist
        df['artist_id'] = artist_id
        return df
    else:
        print("Aucune piste trouvée.")
        return None

'''
playlist_tracks = get_all_playlist_tracks(playlist_id, access_token)
Titles = get_track_id_and_artist(playlist_tracks)
print(Titles.head())
'''