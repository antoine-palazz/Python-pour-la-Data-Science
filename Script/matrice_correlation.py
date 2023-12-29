#%%
#Créer database numerale
import pandas as pd
import matplotlib.pyplot as plt
import ast

df_str = '/home/onyxia/work/Python-pour-la-Data-Science/Data/data/df.csv'



# Lire le fichier CSV avec des options supplémentaires
df = pd.read_csv(df_str, delimiter=',')
df = df.drop(['type','uri','id','track_href','analysis_url','artist','artist_id','genre','Title','track_id'], axis = 1)

path = '/home/onyxia/work/Python-pour-la-Data-Science/Data/data/df_numeral.csv'
df.to_csv(path, index=False)

#%%
#Matrice des corrélations
import pandas as pd
import matplotlib.pyplot as plt
f = plt.figure()
df_numeral_str = '/home/onyxia/work/Python-pour-la-Data-Science/Data/data/df_numeral.csv'

# Lire le fichier CSV avec des options supplémentaires
df_numeral = pd.read_csv(df_numeral_str, delimiter=',')

plt.matshow(df_numeral.corr())
plt.xticks(range(df_numeral.shape[1]), df_numeral.columns, rotation=45)
plt.yticks(range(df_numeral.shape[1]), df_numeral.columns)

cb = plt.colorbar()
cb.ax.tick_params()
plt.title('Matrice de corrélation')


# Calcul de la variance des colonnes
variance_per_column = df_numeral.var()

# Affichage de la variance des colonnes
print("\nVariance des colonnes:")
print(variance_per_column)