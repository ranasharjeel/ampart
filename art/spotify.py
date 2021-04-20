'''
    Spotify web API query script
    Methods return JSON data for quick access
'''

import requests

# Tokens for queries
ACCESS_TOKEN = ""
REFRESH_TOKEN = ""



# Get top artists
def getTopArtists():
    endpoint = "https://api.spotify.com/v1/me/top/artists"
    header = {
        "Authorization" : "Bearer {token}".format(token=ACCESS_TOKEN)
    }

    r = requests.get(endpoint, headers=header)
    r = r.json()

    return r
