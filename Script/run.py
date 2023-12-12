from script1 import playlist
from script2 import *


# Access to the API
token = access_token()

# Request with the access token :
headers = {
    'Authorization': f'Bearer {token}',
}

ids = [get_track_id('Lose Yourself', headers), get_track_id('Verona', headers)]
print(ids)

print(get_track_features(ids, headers))
"""
playlist0 = playlist[:5]
print(playlist0)
Titles = pd.DataFrame({'Title': playlist0})
print(Titles)
print(data_features)
Features = list(data_features.keys())
print(Features)

Titles['track_id'] = Titles['Title'].apply(get_track_id)
Titles['track_features'] = Titles['track_id'].apply(get_track_features)
print(Titles.info)
for feature in Features:
    Titles[feature] = Titles['track_features'].apply(lambda x: x.get(feature))
Titles.drop(columns=['track_features'], inplace = True)
"""
#print(Titles)
"""
path = '/home/onyxia/work/Python-pour-la-Data-Science/Data/data/Titles.csv'
Titles.to_csv(path, index=False)
"""