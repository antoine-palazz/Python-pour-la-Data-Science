import requests
import pandas as pd
from base64 import b64encode
import matplotlib.pyplot as plt


def get_access_token():
    """
    Returns the access token for Spotify API
    """
    logins = "Data/data/logins.txt"
    with open(logins, "r") as file:
        client_id = str(file.readline().strip())
        client_secret = str(file.readline())
    file.close()

    token_url = "https://accounts.spotify.com/api/token"

    # Concatenates client-id and client_secret, then encodes them in base64
    credentials = b64encode(f"{client_id}:{client_secret}".encode()).decode("utf-8")

    # Requests headers
    headers = {
        "Authorization": f"Basic {credentials}",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    # Requests body
    data = {
        "grant_type": "client_credentials",
    }

    # Does the Request
    response = requests.post(token_url, headers=headers, data=data)

    # Makes sure the response does not mean error.
    if response.status_code == 200:
        # We obtain the access token
        access_token = response.json().get("access_token")
        return access_token
    else:
        print(
            f"Error during the token request : {response.status_code} - {response.text}"
        )
        return None


def access_API():
    # Access to the API
    token = get_access_token()

    # Request with the access token :
    headers = {
        "Authorization": f"Bearer {token}",
    }
    return (token, headers)


def get_track_id(track, headers):
    # We make sure track is a string
    track = str(track)

    # Request for the track
    search_url = "https://api.spotify.com/v1/search"
    search_params = {
        "q": track,
        "type": "track",
        "limit": 1,
    }

    # Search
    search_response = requests.get(search_url, params=search_params, headers=headers)
    search_data = search_response.json()
    # Verify if there are results
    if (
        "tracks" in search_data
        and "items" in search_data["tracks"]
        and search_data["tracks"]["items"]
    ):
        # We take the ID of the first song found.
        track_id = search_data["tracks"]["items"][0]["id"]
        return track_id

    else:
        print("Aucun résultat trouvé pour la chanson " + track)
        return None


def get_track_details(track_ids, headers):
    tracks_url = "https://api.spotify.com/v1/tracks"
    params = {"ids": ",".join(track_ids)}

    response = requests.get(tracks_url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()["tracks"]
    else:
        print(
            f"Erreur lors de la récupération des détails des pistes. Code d'erreur : {response.status_code}"
        )
        return None


def get_audio_features(track_id, headers):
    """
    Return a dictionnary for the track.
    track_id must be just a string for one single track.
    """
    audio_features_url = f"https://api.spotify.com/v1/audio-features/{track_id}"

    response = requests.get(audio_features_url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(
            f"Erreur lors de la récupération des caractéristiques audio de la piste. Code d'erreur : {response.status_code}"
        )
        return None


def get_track_features(track_id, headers):
    """
    Return a dictionnary for the track features.
    track_id my be a list of under 100 tracks or just a string for one single track.
    """

    str_track_id = ",".join(track_id)

    params = {"ids": str_track_id}
    features_url = "https://api.spotify.com/v1/audio-features"
    response = requests.get(features_url, headers=headers, params=params)
    print(response)

    # Verify the response:
    if response.status_code == 200:
        # La réponse est au format JSON, imprimez toutes les caractéristiques
        data = response.json()
        return data["audio_features"]
    else:
        print(f"Erreur lors de la requête : {response.status_code} - {response.text}")
        return [None] * len(track_id)


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
        return data
    else:
        print(f"Erreur lors de la requête : {response.status_code} - {response.text}")
        return None


def get_features_labels(headers):
    """
    Returns the list of the features labels the spotify API gives us
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


# Obtenez les pistes de la playlist avec gestion de la pagination
def get_all_playlist_tracks(playlist_id, access_token):
    playlist_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = {"Authorization": "Bearer " + access_token}
    params = {"offset": 0, "limit": 100}  # Limits the response to 100 each time.

    all_tracks = []

    while True:
        response = requests.get(playlist_url, headers=headers, params=params)

        if response.status_code == 200:
            playlist_data = response.json()
            tracks = playlist_data["items"]
            all_tracks.extend(tracks)

            # Check if there are other tracks to recover
            if playlist_data["next"]:
                # Update the offset to get the following page.
                params["offset"] += params["limit"]
            else:
                break
        else:
            print(
                f"Error retrieving tracks from playlist. Error code : {response.status_code}"
            )
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
            title.append(track["track"]["name"])
            track_id.append(track["track"]["id"])
            artist.append(track["track"]["artists"][0]["name"])
            artist_id.append(track["track"]["artists"][0]["id"])
        df = pd.DataFrame({"Title": title})
        df["track_id"] = track_id
        df["artist"] = artist
        df["artist_id"] = artist_id
        return df
    else:
        print("No track found.")
        return None


def get_artists_genres(artist_ids, headers):
    # Convert the list of artist IDs to a comma-separated string
    artists_str = ",".join(artist_ids)

    # Endpoint to obtain information on several artists
    endpoint = f"https://api.spotify.com/v1/artists?ids={artists_str}"

    # Make a GET request to the Spotify API
    response = requests.get(endpoint, headers=headers)

    # Check if request was successful (status 200 OK)
    if response.status_code == 200:
        # Analyze the JSON response
        data = response.json()

        # Recover each artist's genre
        all_genres = []
        for artist_data in data["artists"]:
            genres = artist_data.get("genres", [])
            all_genres.append(genres)

        return all_genres
    else:
        # Display error message if query failed
        print(
            f"Erreur {response.status_code}: Impossible d'obtenir les genres des artistes."
        )
        return [None] * len(artist_ids)


# The four following functions are used to reorganize the 'genres' column in our dataset.


def reduce_genres_list(list_of_genres):
    sorted_list = sorted(list_of_genres, key=lambda x: len(x))
    visited_words = []
    dict = {}
    for genre in sorted_list:
        dict[genre] = [genre]
        c = 0
        for word in visited_words:
            if word in genre and word != genre:
                dict[genre] += [word]
                c += 1
        if c > 0:
            dict[genre].remove(genre)
        visited_words += [genre]
    return dict


def get_genres_list(data_set):
    union_genres = set()
    for genre_str in data_set["genres"]:
        if pd.notna(genre_str):
            # We use ast.literal_eval to get a list from a string of a list
            genre_list = ast.literal_eval(genre_str)
            union_genres = union_genres.union(set(genre_list))
    return list(union_genres)


def remake_genre_list(genre_list, dict):
    new_list = []
    for genre in genre_list:
        new_list += dict[genre]
    most_frequent_genre = max(set(new_list), key=new_list.count)
    return most_frequent_genre
