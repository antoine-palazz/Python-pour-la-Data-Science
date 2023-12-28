import tarfile
import os
import pandas as pd
import h5py
import hdf5_getters  # Assurez-vous que ce module est dans le même répertoire que votre script

def extract_info_recursive(metadata):
    track_info = []
    for key, value in metadata.items():
        if isinstance(value, dict):
            track_info.extend(extract_info_recursive(value))
        else:
            track_info.append(hdf5_getters.get_info(value))
    return track_info

def get_track_info(h5):
    track_info = extract_info_recursive(h5.root.metadata.songs)
    df = pd.DataFrame(track_info, columns=['Title', 'Artist', 'Genre'])
    return df

def process_hdf5_file(hdf5_file_path):
    h5 = hdf5_getters.open_h5_file_read(hdf5_file_path)
    df = get_track_info(h5)
    h5.close()
    return df

def process_subset_tar(tar_file_path):
    df_list = []
    with tarfile.open(tar_file_path, 'r:gz') as tar:
        for member in tar.getmembers():
            if member.isfile() and member.name.endswith('.h5'):
                member_file = tar.extractfile(member)
                member_path = os.path.join(os.getcwd(), member.name)
                with open(member_path, 'wb') as f:
                    f.write(member_file.read())
                df_list.append(process_hdf5_file(member_path))
                os.remove(member_path)
    result_df = pd.concat(df_list, ignore_index=True)
    return result_df

# Example usage
subset_tar_path = 'chemin_vers_votre_subset_tar.tgz'
result_dataframe = process_subset_tar(subset_tar_path)
print(result_dataframe)
