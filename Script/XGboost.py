import pandas as pd # Pour le dataframe
import numpy as np # Pour la normalisation et calculs de moyenne
import matplotlib.pyplot as plt # Pour la visualisation
import seaborn as sns

from PIL import Image


import os # C'est ce qui va nous permettre d'itérer sur les fichiers de l'environnement de travail

from sklearn.feature_selection import VarianceThreshold
from sklearn.model_selection import train_test_split, GridSearchCV, validation_curve, RandomizedSearchCV # Split de dataset et optimisation des hyperparamètres
from sklearn.ensemble import RandomForestClassifier # Random forest
from sklearn.ensemble import GradientBoostingClassifier # XGBoost
from sklearn.neighbors import KNeighborsClassifier # k-NN
from sklearn.svm import SVC # SVM
from sklearn.metrics import accuracy_score, confusion_matrix, recall_score, f1_score, zero_one_loss, classification_report # Métriques pour la mesure de performances
from sklearn.preprocessing import normalize, StandardScaler
from xgboost import XGBClassifier
from pprint import pprint

df_str = '/home/onyxia/work/Python-pour-la-Data-Science/Data/data/df.csv'
df = pd.read_csv(df_str, delimiter=',')
df = df.drop(['type','uri','id','track_href','analysis_url','artist','artist_id','Title','track_id'], axis = 1)

def genre_to_num(genre):
    if genre == 'rock':
        return 8
    if genre == 'rap':
        return 7
    if genre == 'r&b':
        return 6
    if genre == 'pop':
        return 5
    if genre == 'metal':
        return 4
    if genre == 'jazz':
        return 3
    if genre == 'country':
        return 2
    if genre == 'classical music':
        return 1
    if genre == 'blues':
        return 0
df['genre'] = df['genre'].apply(genre_to_num)

features = df.copy()
# valeurs à prédire
genres = np.array(features['genre'])
# supprime les labels des données
features = features.drop('genre', axis = 1)
# sauvegarde le nom de features
feature_list = list(features.columns)
# conversion en numpy array
features = np.array(features)


# séparer les données en training and testing sets
train_features, test_features, train_genres, test_genres = train_test_split(features, genres, test_size = 0.25, random_state = 0, shuffle = True)
print('Training Features Shape:', train_features.shape)
print('Training Genres Shape:', train_genres.shape)
print('Testing Features Shape:', test_features.shape)
print('Testing Genres Shape:', test_genres.shape)

clf = XGBClassifier(objective= 'multi:softprob', random_state = 42)
print('Parameters currently in use:\n')
pprint(clf.get_params())

random_grid = {
    "colsample_bylevel" : [1],
    "colsample_bytree" : [1],
    "gamma" : [0],
    "max_delta_step" : [0],
    "min_child_weight" : [1],
    "learning_rate" : [0.1],
    "max_depth" : [20, None],
    "n_estimators" : [100, 200, 300, 400, 500], 
    "subsample" : [0.8]}

pprint(random_grid)

# création du modèle
clf = XGBClassifier(objective= 'multi:softprob', random_state=42)

# random search
clf_random = RandomizedSearchCV(estimator = clf, param_distributions = random_grid, n_iter = 10, cv = 3, verbose=2, random_state=0, n_jobs = -1)

# fit le modèle
clf_random.fit(train_features, train_genres)

pd_res = pd.concat([pd.DataFrame(clf_random.cv_results_["params"]),pd.DataFrame(clf_random.cv_results_["mean_test_score"], columns=["Accuracy"])],axis=1)
pd_res = pd_res.sort_values('Accuracy', ascending=False)
print(pd_res)

param_grid = {
    "learning_rate" : [0.1], #d0.3
    "max_depth"        : [20], #d6
    "n_estimators" : [300, 350, 450], #d100
    "subsample" : [0.8], #d1
}

pprint(param_grid)

# création du modèle
clf = XGBClassifier(objective= 'multi:softprob', random_state = 0)

grid = GridSearchCV(clf, param_grid = param_grid, n_jobs=-1, scoring="accuracy", cv=3) #scoring="neg_log_loss"
grid.fit(train_features, train_genres)

pd_res = pd.concat([pd.DataFrame(grid.cv_results_["params"]),pd.DataFrame(grid.cv_results_["mean_test_score"], columns=["Accuracy"])],axis=1)
pd_res = pd_res.sort_values('Accuracy', ascending=False)
print(pd_res)

# model
model_xgb = XGBClassifier(objective='multi:softprob', colsample_bylevel=1, colsample_bytree=1, gamma=0, learning_rate=0.1, max_delta_step=0, max_depth=20, min_child_weight=1, n_estimators=300, subsample=0.8, random_state = 42)

# fit the model with the training data
model_xgb.fit(train_features, train_genres)

# predict the target on the test dataset
predict_test = model_xgb.predict(test_features)
 
# Accuracy Score on test dataset
accuracy_test = accuracy_score(test_genres, predict_test)
print('\naccuracy_score on test dataset : ', accuracy_test)
