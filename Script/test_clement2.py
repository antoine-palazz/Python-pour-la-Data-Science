import tarfile
import os
import pandas as pd
import h5py
import numpy as np


# Chemin vers le fichier tar
path_tar = "/Users/clementgadeau/Python pour la DATA/DATA_SET/millionsongsubset.tar"

# Répertoire où extraire les fichiers
path_extract = "/Users/clementgadeau/Python pour la DATA/DATA_SET/Extraction/"

# Extraire le contenu du fichier tar
with tarfile.open(path_tar, 'r') as tar:
    tar.extractall(path=path_extract)

# Fonction récursive pour extraire les informations du fichier HDF5
def extract_info_recursive(group):
    track_info = []
    
    for key, value in group.items():
        if isinstance(value, h5py.Group):
            # Si c'est un groupe, appel récursif
            track_info.extend(extract_info_recursive(value))
        elif isinstance(value, h5py.Dataset):
            # Si c'est un dataset, extraire les informations
            if key == 'songs':
                track_info.append(get_info(value))
    
    return track_info

# Fonction pour extraire les informations du fichier HDF5
def get_info(track):
    title_data = track['title'][0]
    if isinstance(title_data, np.ndarray):
        title_value = ''.join([char.decode('utf-8') for char in title_data])
    else:
        title_value = str(title_data)

    return {
        'Titre': title_value,
        'Artiste': str(track['artist_name'][0][0]),
        'Genre': track['genre'][0].decode('utf-8') if 'genre' in track and len(track['genre']) > 0 else None,
    }



# Liste pour stocker les informations extraites
all_track_info = []

# Parcourir tous les fichiers HDF5 dans le répertoire d'extraction
for root, dirs, files in os.walk(path_extract):
    for file in files:
        if file.endswith('.h5'):
            file_path = os.path.join(root, file)
            with h5py.File(file_path, 'r') as fichier:
                # Vérifier si le groupe 'metadata' existe
                if 'metadata' in fichier:
                    # Appeler la fonction récursive pour extraire les informations
                    track_info = extract_info_recursive(fichier['metadata'])
                    all_track_info.extend(track_info)

df = pd.DataFrame(all_track_info)
print(df.head())
