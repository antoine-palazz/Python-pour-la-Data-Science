"""
Run this file if you want to get the access token and the headers.
"""
from functions import get_access_token


# Access to the API
token = get_access_token()

# Request with the access token :
headers = {
    'Authorization': f'Bearer {token}',
}

