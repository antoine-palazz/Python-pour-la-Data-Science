"""
Run this file to create your data base
"""
from _0_init import token, headers
from script4 import get_all_playlist_tracks, get_track_id_and_artist
playlist_id = '04ZwFco4KsjgPlVMtzwfgS'

playlist_tracks = get_all_playlist_tracks(playlist_id, token)
Titles = get_track_id_and_artist(playlist_tracks)

print(Titles.heas())