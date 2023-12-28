#from script1 import playlist
from script2 import *
from script4 import Titles
from script5 import get_artists_genres


# Access to the API
token = access_token()

# Request with the access token :
headers = {
    'Authorization': f'Bearer {token}',
}

track_list = Titles['track_id'].tolist()
nb_musiques = len(track_list)
print("il y a", nb_musiques, "musiques")
nb_utilisation_token_track = nb_musiques // 100 + int(nb_musiques % 100 != 0)
track_features_list = []

for k in range(nb_utilisation_token_track-1):
    track_features_list = track_features_list + get_track_features(track_list[100*k:100*(k+1)],headers)
track_features_list = track_features_list + get_track_features(track_list[(nb_utilisation_token_track-1)*100:],headers)
Titles['track_features'] = track_features_list


Features = get_features_labels(headers)
#print(Features)

for feature in Features:
    Titles[feature] = Titles['track_features'].apply(lambda x: x.get(feature))
Titles.drop(columns=['track_features'], inplace = True)

artist_list = Titles['artist_id'].tolist()
nb_artist = len(artist_list)
print("il y a", nb_artist, "artistes")
nb_utilisation_token_artist = nb_artist // 50 + int(nb_artist % 50 != 0)
artist_genres_list = []

for k in range(nb_utilisation_token_artist-1):
    artist_genres_list = artist_genres_list + get_artists_genres(artist_list[50*k:50*(k+1)], headers)
    print(k/nb_utilisation_token_artist)
artist_genres_list = artist_genres_list + get_artists_genres(artist_list[(nb_utilisation_token_artist-1)*50:], headers)
Titles['genres'] = artist_genres_list

print(Titles.head())


path = '/home/onyxia/work/Python-pour-la-Data-Science/Data/data/Titles3.csv'
Titles.to_csv(path, index=False)
