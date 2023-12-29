import matplotlib.pyplot as plt
import pandas as pd

path = '/Users/clementgadeau/Python pour la DATA/Sauvegarde Git/Python-pour-la-Data-Science/Data/data/'
file = 'df.csv'

df = pd.read_csv(path+file)
variables = ['danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo','type','id','uri','track_href','analysis_url','duration_ms','time_signature','genre']

# Count the occurrences of each genre
genres_counts = df['genres'].str.split(', ').explode().value_counts()

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(genres_counts, labels=genres_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Genres')
plt.show()