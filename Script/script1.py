from collections import OrderedDict
path = '/home/onyxia/work/Python-pour-la-Data-Science/playlist.txt'
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