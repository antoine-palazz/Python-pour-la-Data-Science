import pandas as pd
import matplotlib.pyplot as plt
Titles_en_csv = '/home/onyxia/work/Python-pour-la-Data-Science/Data/data/Titles2.csv'

# Lire le fichier CSV avec des options supplémentaires
Titles = pd.read_csv(Titles_en_csv, delimiter=',')
Titles = Titles.drop(['type','uri','id','track_href','analysis_url','artist','artist_id','genres','Title','track_id'], axis = 1)

path = '/home/onyxia/work/Python-pour-la-Data-Science/Data/data/Titles3.csv'
Titles.to_csv(path, index=False)
