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


print("Les autres genres sont ", autres_genres, len(autres_genres))

print(liste_finale)
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


with open(path + "Genres_Musicaux_simplifiés.txt", 'w') as file:
    file.write(f"Il y a {len(new_list)} genres nommés différemment\n")
    for element in new_list:
        file.write(f"{element}\n")

print(somme1, somme2)
print(divide_str('rock'))