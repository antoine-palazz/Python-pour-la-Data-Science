import matplotlib.pyplot as plt
import pandas as pd

path = '/Users/clementgadeau/Python pour la DATA/Sauvegarde Git/Python-pour-la-Data-Science/Data/data/'
file = 'Titles2.csv'

df = pd.read_csv(path+file)

# Count the occurrences of each genre
genres_counts = df['genres'].str.split(', ').explode().value_counts()

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(genres_counts, labels=genres_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Genres')
plt.show()