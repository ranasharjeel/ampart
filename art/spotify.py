'''
    Spotify web API query script
    Methods return data for quick access
'''

import requests

# Tokens for queries
ACCESS_TOKEN = ""
REFRESH_TOKEN = ""



# Get top artists as JSON object
def getTopArtistsJSON(limit):
    endpoint = "https://api.spotify.com/v1/me/top/artists"
    header = {
        "Authorization" : "Bearer {token}".format(token=ACCESS_TOKEN)
    }

    r = requests.get(endpoint, headers=header, params={'limit' : limit})
    r = r.json()

    return r


# Get top artists as a list
def getTopArtists(limit=200):
    top_artists = []
    top = getTopArtistsJSON(limit).get('items')

    for i in top:
        top_artists.append(i['name'])

    return top_artists


# Get top genres as a list
def getTopGenres(limit=200):
    top_genres = []
    top = getTopArtistsJSON(limit).get('items')

    for i in top:
        for j in i['genres']:
            top_genres.append(j)

    return top_genres