# Python-pour-la-Data-Science

Vous trouverez dans ce répertoire le projet réalisé par Valentin Smague et Clément Gadeau, qui essaie de donner une réponse à la question suivante : *Peut-on à partir de données quantitatives sur un morceau, prédire le genre musical auquel il appartient ?*

  - follow_me.ipynb est le notebook qui présente l'intégralité de notre projet. Tout le contenu du projet est accessible depuis le notebook.

  - function.py est un fichier python qui répertorie toutes les fonctions utilisés au cours du projet. Le code de chaque fonctions est retranscrit dans le notebook, à l'exception de get_features_labels. Ce fichier est un simple répertoire de fonctions et n'apporte pas plus d'informations que le notebook n'en contient.

  - df_init.csv est le data set initial assemblé de façon expérimental par notre première méthode.

  - Dataset_Genres.csv est le data set final sur lequel nous travaillerons.


Voici le plan de notre projet :
#### __I. Récupérer et traiter les données__
  - Requêter l'API Spotify pour constituer un premier dataset
  - Nettoyer le dataset : identifier un genre unique pour chaque morceau
  - Constituer un dataset muris de nos réflexions

#### __II. Visualiser pour comprendre les données__
  - Vérifier la bonne répartition des genres musicaux
  - Comprendre le lien entre les variables et les genres
  - Mettre en évidence ces relations

#### __III. Modéliser la prédiction du genre__
  - Random Forest
  - XGBoost

### __Conclusion__