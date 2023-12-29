import pandas as pd # Pour le dataframe
import numpy as np # Pour la normalisation et calculs de moyenne
import matplotlib.pyplot as plt # Pour la visualisation
from sklearn.feature_selection import VarianceThreshold
from sklearn.model_selection import train_test_split, GridSearchCV, validation_curve, RandomizedSearchCV # Split de dataset et optimisation des hyperparamètres
from sklearn.ensemble import GradientBoostingClassifier # XGBoost
from xgboost import XGBClassifier
from pprint import pprint
from sklearn.metrics import accuracy_score, confusion_matrix, recall_score, f1_score, zero_one_loss, classification_report # Métriques pour la mesure de performances
from sklearn.preprocessing import normalize, StandardScaler

df_str = '/home/onyxia/work/Python-pour-la-Data-Science/Data/data/df.csv'
df = pd.read_csv(df_str, delimiter=',')
df = df.drop(['type','uri','id','track_href','analysis_url','artist','artist_id','Title','track_id'], axis = 1)
features = df
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

sc = StandardScaler()
train_features = sc.fit_transform(train_features)
test_features = sc.transform(test_features)

#model = XGBClassifier(objective='multi:softprob', colsample_bylevel=1, colsample_bytree=1, gamma=0, learning_rate=0.1, max_delta_step=3, max_depth=10, min_child_weight=1, n_estimators=300, subsample=0.8, random_state = 0)
model = XGBClassifier(objective='multi:softprob', colsample_bylevel=1, colsample_bytree=1, gamma=0, learning_rate=0.1, max_delta_step=0, max_depth=10, min_child_weight=1, n_estimators=300, subsample=0.8, random_state = 0)

# fit the model with the training data
model.fit(train_features, train_genres)
 
# predict the target on the test dataset
predict_test = model.predict(test_features)
 
# Accuracy Score on test dataset
accuracy_test = accuracy_score(test_genres, predict_test)
print('\naccuracy_score on test dataset : ', accuracy_test)