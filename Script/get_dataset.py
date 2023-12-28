from functions import *


# Access to the API
access_token = get_access_token()
headers = {'Authorization': f'Bearer {access_token}',}


playlist_id = '04ZwFco4KsjgPlVMtzwfgS'
playlist_tracks = get_all_playlist_tracks(playlist_id, access_token)
Dataset = get_track_id_and_artist(playlist_tracks)
# Now we have a dataset of the title, the artist name, the artist id.



#We now request the track features of our tracks.
track_list = Dataset['track_id'].tolist()
nb_musiques = len(track_list)
print("il y a", nb_musiques, "musiques")
nb_utilisation_token_track = nb_musiques // 100 + int(nb_musiques % 100 != 0)
track_features_list = []

for k in range(nb_utilisation_token_track-1):
    track_features_list = track_features_list + get_track_features(track_list[100*k:100*(k+1)],headers)
track_features_list = track_features_list + get_track_features(track_list[(nb_utilisation_token_track-1)*100:],headers)
Dataset['track_features'] = track_features_list


Features = get_features_labels(headers)
#print(Features)

for feature in Features:
    Dataset[feature] = Dataset['track_features'].apply(lambda x: x.get(feature))
Dataset.drop(columns=['track_features'], inplace = True)




#We now request the artist genre for our tracks.
artist_list = Dataset['artist_id'].tolist()
nb_artist = len(artist_list)
print("il y a", nb_artist, "artistes")
nb_utilisation_token_artist = nb_artist // 50 + int(nb_artist % 50 != 0)
artist_genres_list = []

for k in range(nb_utilisation_token_artist-1):
    artist_genres_list = artist_genres_list + get_artists_genres(artist_list[50*k:50*(k+1)], headers)
    print(k/nb_utilisation_token_artist)
artist_genres_list = artist_genres_list + get_artists_genres(artist_list[(nb_utilisation_token_artist-1)*50:], headers)
Dataset['genres'] = artist_genres_list

print(Dataset.head())




#We now save our dataset to csv file.
#path = '/home/onyxia/work/Python-pour-la-Data-Science/Data/data/Titles3.csv'
#path = "/Users/clementgadeau/Python pour la DATA/DATA_SET/Our DATA_SET/"
Dataset.to_csv(path, index=False)