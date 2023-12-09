from collections import OrderedDict

path = '/home/onyxia/work/Python-pour-la-Data-Science/playlist.txt'

def playlist_txt_to_list(path):
    """"
    Summary:
        créer une liste de chansons(str) à partir d'un fichier txt
    Args:
        path (_str_): chemin du ficher txt où se trouvent les titres
    """
    fichier = open(path, "r")
    playlist = fichier.read()
    fichier.close()
    playlist= playlist.split("\n")
    playlist = list(OrderedDict.fromkeys(playlist))
    nb_titres = len(playlist)
    for k in range(nb_titres):
        song = playlist[k]
        ind = 0
        size = len(song)
        while ind < size and song[ind] != "-":
            ind += 1
        playlist[k] = song[ind+2:]
    return(playlist)

#print(playlist_txt_to_list(path))