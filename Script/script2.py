import requests
import pandas as pd

url = "https://api.deezer.com/track/3135556"

req = requests.get(url)
wb = req.json()

print(type(req))
print(req.content[:5])
print(wb)
