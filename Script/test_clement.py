import tarfile
import os
import pandas as pd
import h5py

# Chemin vers le fichier tar
path_tar = "/Users/clementgadeau/Python pour la DATA/DATA_SET/millionsongsubset.tar"

# Répertoire où extraire les fichiers
path_extract = "/Users/clementgadeau/Python pour la DATA/DATA_SET/Extraction/"

# Extraire le contenu du fichier tar
with tarfile.open(path_tar, 'r') as tar:
    tar.extractall(path=path_extract)

# Fonction pour rechercher récursivement le fichier HDF5 dans les sous-dossiers
def search_hdf5_file(big_file):
    for sub_file, _, files in os.walk(big_file):
        for file in files:
            if file.endswith('.h5'):
                return os.path.join(sub_file, file)
    return None

# Choisissez le fichier HDF5 parmi les fichiers extraits
hdf5_file = search_hdf5_file(path_extract)

# Vérifier si le fichier HDF5 a été trouvé
if hdf5_file:
    # Afficher la structure du fichier HDF5
    with h5py.File(hdf5_file, 'r') as fichier:
        def afficher_structure(groupe, indent=0):
            for cle, valeur in groupe.items():
                if isinstance(valeur, h5py.Group):
                    print("  " * indent + f"Group: {cle}")
                    afficher_structure(valeur, indent + 1)
                elif isinstance(valeur, h5py.Dataset):
                    print("  " * indent + f"Dataset: {cle}")

        afficher_structure(fichier)

        # Fonction pour extraire les informations du fichier HDF5
        def get_info(track):
            return {
                'Titre': str(track['title'][0]),  # Convertir en chaîne de caractères
                'Artiste': str(track['artist_name'][0]),  # Convertir en chaîne de caractères
                'Genre': track['genre'][0].decode('utf-8') if 'genre' in track and len(track['genre']) > 0 else None,
            }

        # Extraire les données pour chaque chanson sous le groupe 'metadata'
        track_info = [get_info(track) for track in fichier['metadata']['songs']]

    # Créer un DataFrame avec les données extraites
    df = pd.DataFrame(track_info)

    # Afficher les premières lignes du DataFrame
    print(df.head())
else:
    print("Aucun fichier avec l'extension '.h5' trouvé dans les sous-dossiers du répertoire d'extraction.")
