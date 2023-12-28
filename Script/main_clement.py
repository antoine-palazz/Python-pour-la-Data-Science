import pandas as pd
import ast

path = '/Users/clementgadeau/Python pour la DATA/Sauvegarde Git/Python-pour-la-Data-Science/Data/data/'

data_set = pd.read_csv(path + 'Titles2.csv')

union_genres = []

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
    occurrences = {}
    for element in list:
        occurrences[element] = occurrences.get(element, 0) + 1
    return occurrences


def sorting_by_occurrence(list):
    occurrences = count_occurrence(list)
    sorted_list = sorted(occurrences.keys(), key=lambda x: occurrences[x], reverse=True)
    return sorted_list, occurrences

sorted_genres = sorting_by_occurrence(union_genres)
liste_finale = [[i, sorted_genres[1][i]] for i in sorted_genres[0]]

sorting_by_occurrence(union_genres)
"""
with open(path + "Genres_Musicaux_multiplicité.txt", 'w') as file:
    file.write(f"Il y a {len(set(union_genres))} genres nommés différemment\n")
    for element in liste_finale:
        file.write(f"{element}\n")
"""


def divide_str(string):
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
print(different_words)

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
genres_un_mot = [genre[0] for genre in liste_finale if len(divide_str(genre[0])) == 1]
# Étape 2 : Créez une liste des genres à deux mots
genres_deux_mots = [genre[0] for genre in liste_finale if len(divide_str(genre[0])) == 2]
# Étape 3 : Créez une liste des genres à trois mots
genres_trois_mots = [genre[0] for genre in liste_finale if len(divide_str(genre[0])) == 3]

autres_genres = [genre[0] for genre in liste_finale if genre[0] not in genres_un_mot + genres_deux_mots + genres_trois_mots]
print("Les autres genres sont ", autres_genres, len(autres_genres))

# Étape 4 : Itérez sur la liste initiale et remplacez les genres
nouvelle_liste_finale = []
for genre, occurrence in liste_finale:
    mots = divide_str(genre)

    # Cas 1 : Genre à un mot
    if len(mots) == 1 and mots[0] in genres_un_mot:
        nouvelle_liste_finale.append((mots[0], occurrence))

    # Cas 2 : Genre à deux mots
    elif len(mots) == 2 and any(word in genres_un_mot for word in mots):
        nouvelle_liste_finale.append((next(word for word in mots if word in genres_un_mot), occurrence))

    # Cas 3 : Genre à trois mots
    elif len(mots) == 3 and any(word in genres_un_mot for word in mots):
        nouvelle_liste_finale.append((next(word for word in mots if word in genres_un_mot), occurrence))
    
    # Ajoutez d'autres cas au besoin pour les genres composés de plus de trois mots

    # Cas par défaut : Aucun changement
    else:
        nouvelle_liste_finale.append((genre, occurrence))
    


print(nouvelle_liste_finale)

