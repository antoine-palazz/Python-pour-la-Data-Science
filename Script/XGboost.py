import pandas as pd # Pour le dataframe
import numpy as np # Pour la normalisation et calculs de moyenne
import matplotlib.pyplot as plt # Pour la visualisation
from sklearn.feature_selection import VarianceThreshold
from sklearn.model_selection import train_test_split, GridSearchCV, validation_curve, RandomizedSearchCV # Split de dataset et optimisation des hyperparamètres
from sklearn.ensemble import RandomForestClassifier # Random forest
from sklearn.ensemble import GradientBoostingClassifier # XGBoost
from xgboost import XGBClassifier
from pprint import pprint

#model = XGBClassifier(objective='multi:softprob', colsample_bylevel=1, colsample_bytree=1, gamma=0, learning_rate=0.1, max_delta_step=3, max_depth=10, min_child_weight=1, n_estimators=300, subsample=0.8, random_state = 0)
model = XGBClassifier(objective='multi:softprob', colsample_bylevel=1, colsample_bytree=1, gamma=0, learning_rate=0.1, max_delta_step=0, max_depth=10, min_child_weight=1, n_estimators=300, subsample=0.8, random_state = 0)

# fit the model with the training data
model.fit(train_features, train_labels)
 
# predict the target on the test dataset
predict_test = model.predict(test_features)
 
# Accuracy Score on test dataset
accuracy_test = accuracy_score(test_labels, predict_test)
print('\naccuracy_score on test dataset : ', accuracy_test)