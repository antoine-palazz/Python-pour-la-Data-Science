import pandas as pd
import matplotlib.pyplot as plt
import ast

Titles_en_csv = '/home/onyxia/work/Python-pour-la-Data-Science/Data/data/Titles2.csv'

# Lire le fichier CSV avec des options supplémentaires
Titles = pd.read_csv(Titles_en_csv, delimiter=',')

#création d'un dictionnaire des genres
genres_list = Titles['genres'].tolist()
genres = {}
for genre_artist in genres_list:
    if type(genre_artist) == str:
        test = ast.literal_eval(genre_artist)
        for genre in test:
            if genre in genres.keys():
                genres[genre] += 1
            else:
                genres[genre] = 1

liste_des_genres = []
nb_pour_chaque_genre = []
for cle,valeur in genres.items():
    liste_des_genres.append((valeur,cle))
    nb_pour_chaque_genre.append(valeur)
liste_des_genres.sort(key=lambda x: x[0])
print(liste_des_genres[-10:])
