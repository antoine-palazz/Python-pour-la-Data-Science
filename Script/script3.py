#%%
import pandas as pd
import matplotlib.pyplot as plt
Titles_en_csv = '/home/onyxia/work/Python-pour-la-Data-Science/Data/data/df.csv'

# Lire le fichier CSV avec des options supplémentaires
df = pd.read_csv(Titles_en_csv, delimiter=',')

# Afficher les premières lignes du DataFrame
print(df.head())
#création d'un dictionnaire des genres
genres_list = df['genre'].tolist()
genres = {}
for genre in genres_list:
    if genre in genres.keys():
        genres[genre] += 1
    else:
        genres[genre] = 1

liste_des_genres = []
nb_pour_chaque_genre = []
for cle,valeur in genres.items():
    liste_des_genres.append(cle)
    nb_pour_chaque_genre.append(valeur)


#représentation graphique des genres

labels = liste_des_genres
sizes = nb_pour_chaque_genre
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  
plt.tight_layout()
plt.show()

'''
#Matrice des corrélations

f = plt.figure()

plt.matshow(Titles.corr())
plt.xticks(range(Titles.shape[1]), Titles.columns, rotation=45)
plt.yticks(range(Titles.shape[1]), Titles.columns)

cb = plt.colorbar()
cb.ax.tick_params()
plt.title('Matrice de corrélation')

'''
# %%
