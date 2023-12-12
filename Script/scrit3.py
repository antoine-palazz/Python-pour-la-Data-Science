#%%

import matplotlib.pyplot as plt


#juste un exemple

df ={}
df['genre']=[['rock','rap'],['rap'],['pop'],['classique'],['pop'],['pop']]


#création d'un dictionnaire des genres

genres = {}
for genre_artiste in df['genre']:
    for genre in genre_artiste:
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
