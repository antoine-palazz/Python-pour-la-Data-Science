import pandas as pd
import matplotlib.pyplot as plt
import ast

Titles_en_csv = '/home/onyxia/work/Python-pour-la-Data-Science/Data/data/Titles2.csv'


'''
# Lire le fichier CSV avec des options supplémentaires
Titles = pd.read_csv(Titles_en_csv, delimiter=',')
Titles = Titles.drop(['type','uri','id','track_href','analysis_url','artist','artist_id','genres','Title','track_id'], axis = 1)

path = '/home/onyxia/work/Python-pour-la-Data-Science/Data/data/Titles3.csv'
Titles.to_csv(path, index=False)







#Matrice des corrélations
import pandas as pd
import matplotlib.pyplot as plt
f = plt.figure()
Titles_en_csv = '/home/onyxia/work/Python-pour-la-Data-Science/Data/data/Titles3.csv'

# Lire le fichier CSV avec des options supplémentaires
Titles = pd.read_csv(Titles_en_csv, delimiter=',')

plt.matshow(Titles.corr())
plt.xticks(range(Titles.shape[1]), Titles.columns, rotation=45)
plt.yticks(range(Titles.shape[1]), Titles.columns)

cb = plt.colorbar()
cb.ax.tick_params()
plt.title('Matrice de corrélation')


# Calcul de la variance des colonnes
variance_per_column = Titles.var()

# Affichage de la variance des colonnes
print("\nVariance des colonnes:")
print(variance_per_column)

'''