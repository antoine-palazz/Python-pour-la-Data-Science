"""
Run this file to create your data base
"""
from _0_init import token, headers
from deleted_script4 import get_all_playlist_tracks, get_track_id_and_artist
import pandas as pd
from delated_script2 import get_track_features, get_features_labels

def add_track_feature_to_a_dataset(sub_df,headers):
    #We now request the track features of our tracks.
    track_list = sub_df['track_id'].tolist()
    nb_musiques = len(track_list)
    print("il y a", nb_musiques, "musiques")
    nb_utilisation_token_track = nb_musiques // 100 + int(nb_musiques % 100 != 0)
    track_features_list = []
    for k in range(nb_utilisation_token_track-1):
        track_features_list = track_features_list + get_track_features(track_list[100*k:100*(k+1)],headers)
    track_features_list = track_features_list + get_track_features(track_list[(nb_utilisation_token_track-1)*100:],headers)
    sub_df['track_features'] = track_features_list
    Features = get_features_labels(headers)
    #print(Features)

    for feature in Features:
        sub_df[feature] = sub_df['track_features'].apply(lambda x: x.get(feature))
    sub_df.drop(columns=['track_features'], inplace = True)
    return sub_df

list_sub_df = []
playlist_id_list_2 = [('7CI3NR7rvCkgiLhch1qprf','r&b',),('5n9btvMZ52rxwozhQdKU7v','classical music'),('79Bcltku1dcD08JcAM29kL','jazz'),('7gqtGYFoCR3tAqTtEUQZTw','pop')]

for playlist_id, genre_playlist in playlist_id_list_2:
    playlist_tracks = get_all_playlist_tracks(playlist_id, token)
    sub_df = get_track_id_and_artist(playlist_tracks)
    sub_df = add_track_feature_to_a_dataset(sub_df,headers)
    sub_df['genre'] = genre_playlist
    list_sub_df.append(sub_df)

df_2 = pd.concat(list_sub_df, axis = 0)

path = '/home/onyxia/work/Python-pour-la-Data-Science/Data/data/df_2.csv'
df_2.to_csv(path, index=False)