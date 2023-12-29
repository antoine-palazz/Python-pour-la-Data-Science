import pandas as pd
import ast

path = '/Users/clementgadeau/Python pour la DATA/Sauvegarde Git/Python-pour-la-Data-Science/Data/data/'

data_set = pd.read_csv(path + 'Titles2.csv')
union_genres = []

# Makes a list of all genres
for genre_str in data_set['genres']:
    if pd.notna(genre_str):
        # Utilisez ast.literal_eval pour évaluer la chaîne comme une liste
        genre_list = ast.literal_eval(genre_str)
        union_genres = union_genres + genre_list

union_genres_set = set(union_genres)

"""
with open(path + "Genres_Musicaux.txt", 'w') as file:
    file.write(f"Il y a {len(union_genres_set)} genres nommés différemment\n")
    for element in union_genres_set:
        file.write(f"{element}\n")
"""


def count_occurrence(list):
    """Returns a dictionnary of the occurrences of each genre."""
    occurrences = {}
    for element in list:
        occurrences[element] = occurrences.get(element, 0) + 1
    return occurrences

def sorting_by_occurrence(list):
    """Returns a sorted list of genres from most to least frequent, and the dictionnary of occurences."""
    occurrences = count_occurrence(list)
    sorted_list = sorted(occurrences.keys(), key=lambda x: occurrences[x], reverse=True)
    return sorted_list, occurrences

sorted_genres = sorting_by_occurrence(union_genres)
liste_finale = [[i, sorted_genres[1][i]] for i in sorted_genres[0]]

#sorting_by_occurrence(union_genres)
"""
with open(path + "Genres_Musicaux_multiplicité.txt", 'w') as file:
    file.write(f"Il y a {len(set(union_genres))} genres nommés différemment\n")
    for element in liste_finale:
        file.write(f"{element}\n")
"""


def divide_str(string):
    """
    Returns a list of each words of a string.
    A word is considered to be something
    """
    # Utiliser la méthode split pour diviser la chaîne en mots
    words = string.split()  # Divise automatiquement en utilisant l'espace comme séparateur
    # Diviser également en utilisant le tiret comme séparateur
    for word in words[:]:  # Utiliser une copie de la liste pour éviter les problèmes de modification pendant l'itération
        if '-' in word:
            words.remove(word)
            words.extend(word.split('-'))
    return words

# Appliquer la fonction à chaque élément de la liste
different_words = set([word for string in union_genres_set for word in divide_str(string)])
#print(different_words)

genre_list = []
encountered_words = set()
"""
for genre, occurence in liste_finale:
    words = divide_str(genre)
    if set(words) & encountered_words == set():
        if len(words) == 1:
            genre_list.append(genre)
    else:
"""

# Étape 1 : Créez une liste des genres à un seul mot  
genres_un_mot = []
genres_deux_mots = []
genres_trois_mots = []
autres_genres = []

for genre in liste_finale : 
    # Étape 1 : Créez une liste des genres à un seul mot  
    if len(divide_str(genre[0])) == 1 :
        genres_un_mot += [genre[0]]
    # Étape 2 : Créez une liste des genres à deux mots
    elif len(divide_str(genre[0])) == 2:
        genres_deux_mots += [genre[0]]
    # Étape 3 : Créez une liste des genres à trois mots
    elif len(divide_str(genre[0])) == 3:
        genres_trois_mots += [genre[0]]
    else :
        autres_genres += [genre[0]]


#print("Les autres genres sont ", autres_genres, len(autres_genres))

#print(liste_finale)
# Étape 4 : Itérez sur la liste initiale et remplacez les genres
nouvelle_liste_finale = []
for genre in union_genres:
    mots = divide_str(genre)

    # Cas 1 : Genre à un mot
    if len(mots) == 1 and mots[0] in genres_un_mot:
        nouvelle_liste_finale.append(mots[0])

    # Cas > 1 : Genre à deux mots
    elif len(mots) > 1 and set(mots) & set(genres_un_mot) != set():
        nouvelle_liste_finale.append(next(word for word in mots if word in genres_un_mot))

    # Cas par défaut : Aucun changement
    else:
        nouvelle_liste_finale.append(genre)


nouvelle_liste_finale_finale = []
for genre in nouvelle_liste_finale:
    mots = divide_str(genre)
    if len(mots) > 2 and set(mots) & set(genres_deux_mots) != set():
        i = 0
        for word1 in mots:
            for word2 in mots:
                if word2 != word1:
                    if word1 + ' ' + word2 in genres_deux_mots:
                        nouvelle_liste_finale_finale.append(word1 + ' ' + word2)
                        i += 1
                        break
                    elif word2 + ' ' + word1 in genres_deux_mots:
                        nouvelle_liste_finale_finale.append(word2 + ' ' + word1)
                        i += 1
                        break
            if i == 1:
                break

    else :
        nouvelle_liste_finale_finale.append(genre)




new_list = sorting_by_occurrence(nouvelle_liste_finale_finale)
new_list = [[i, new_list[1][i]] for i in new_list[0]]

somme1 = 0
somme2 = 0
for i in new_list :
    somme1 += i[1]
for j in liste_finale:
    somme2 += j[1]

"""
with open(path + "Genres_Musicaux_simplifiés.txt", 'w') as file:
    file.write(f"Il y a {len(new_list)} genres nommés différemment\n")
    for element in new_list:
        file.write(f"{element}\n")
"""

genres_par_occurrences = [i[0] for i in new_list]



tracks_genre = []
for genre_list in data_set['genres'].tolist():
    if isinstance(genre_list, str) or isinstance(genre_list, list):
        tracks_genre.append(ast.literal_eval(genre_list))
    else:
        tracks_genre.append(['Pas de genre'])

#print(tracks_genre, tracks_genre.count(['Pas de genre']))

tracks_genre_simplified = []
j, h = 0, 0
for genre_list_init in tracks_genre:
    i = 0
    genre_list = [i for i in genre_list_init]
    for genre in genre_list_init :
        genre_list = genre_list + [i for i in divide_str(genre)]
    for genre in new_list:
        if genre[0] in genre_list:
            tracks_genre_simplified.append(genre[0])
            i += 1
            h += 1
            break
    if i == 0:
        tracks_genre_simplified.append('Sans genre')
        j += 1

print(j, h, j+h)

#print(tracks_genre_simplified, len(tracks_genre_simplified))

tracks_genre_simplified_per_occurrence = sorting_by_occurrence(tracks_genre_simplified)
tracks_genre_simplified_per_occurrence = [[i, tracks_genre_simplified_per_occurrence[1][i]] for i in tracks_genre_simplified_per_occurrence[0]]

somme3 = 0
for i in tracks_genre_simplified_per_occurrence :
    somme3 += i[1]


with open(path + "Genres_Musicaux_data.txt", 'w') as file:
    file.write(f"On obtient {len(tracks_genre_simplified_per_occurrence)} genres différents\n")
    file.write(f"Il y a {len(tracks_genre_simplified)} morceaux différents\n")
    file.write(f"Je compte {somme3} morceaux différents avec mon alogrithme\n")
    for element in tracks_genre_simplified_per_occurrence:
        file.write(f"{element}\n")


# Let put that into functions : 
def delete_nan(df):
    return(df.dropna(subset=['genres']))

"""
def find_genres_by_words(genres_list, nb_words = 1):
    for genre in genres_list:
        if genre 
    return
"""



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

#Let's clean our genres column.
#data_set['Sorted_genres'] = data_set