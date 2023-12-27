#from script1 import playlist
from script2 import *
from script4 import Titles
from script5 import get_artist_genres


# Access to the API
token = access_token()

# Request with the access token :
headers = {
    'Authorization': f'Bearer {token}',
}

track_list = Titles['track_id'].tolist()
nb_musiques = len(track_list)
print("il y a", nb_musiques, "différentes musiques")
nb_utilisation_token = nb_musiques // 100 + int(nb_musiques % 100 != 0)
track_features_list = []

for k in range(nb_utilisation_token-1):
    track_features_list = track_features_list + get_track_features(track_list[100*k:100*(k+1)],headers)
    print(k/nb_utilisation_token)
track_features_list = track_features_list + get_track_features(track_list[(nb_utilisation_token-1)*100:],headers)
Titles['track_features'] = track_features_list

Features = get_features_labels(headers)
#print(Features)

for feature in Features:
    Titles[feature] = Titles['track_features'].apply(lambda x: x.get(feature))
Titles.drop(columns=['track_features'], inplace = True)

Titles['genres'] = Titles['Artist'].apply(get_artist_genres)
print(Titles.head())

path = '/home/onyxia/work/Python-pour-la-Data-Science/Data/data/Titles2.csv'
Titles.to_csv(path, index=False)
