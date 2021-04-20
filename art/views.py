import os, json, requests
from django.shortcuts import render
from . import errors, spotify

'''
    ----Views----
'''


# Data required for authorization if user wants to login
CLIENT_ID = os.environ.get('AMPART_CLIENT_ID')
CLIENT_SECRET = os.environ.get('AMPART_CLIENT_SECRET')
REDIRECT_URI = "http://127.0.0.1:8000/art/auth"
SCOPE = "user-library-read user-top-read"


# Index page
def index(request):
    '''
    # Spotify data
    sp = spotify_auth.getSpotifyObj()

    # Get data from user
    top_artists_list = []
    top_genres_list = []
    if(sp != errors.couldNotAuthenticate()):
        
        top = sp.current_user_top_artists(200).get('items')

        # Top artists
        for i in top:
            top_artists_list.append(i['name'])
    

        # Top genres
        for i in top:
            for j in i['genres']:
                top_genres_list.append(j)
        


    # Generate word cloud from top artist/genres names
    cloud.generateWordCloud(top_artists_list, "note", "artists")
    cloud.generateWordCloud(top_genres_list, "single", "genres")
    '''



    # Package data to JSON and send to index template
    # (to get authorization code)
    auth_data = {
        'CLIENT_ID' : CLIENT_ID,
        'CLIENT_SECRET' : CLIENT_SECRET,
        'REDIRECT_URI' : REDIRECT_URI,
        'SCOPE' : SCOPE
    }
    auth_data = json.dumps(auth_data)


    return render(request, 'index.html', {'auth_data' : auth_data})


# Authorization page
def auth(request):

    # authorization code
    auth_code = request.GET['code'] 

    # Create and send post request for access/refresh tokens
    endpoint = "https://accounts.spotify.com/api/token"

    body = {
        "grant_type" : "authorization_code",
        "code" : auth_code,
        "redirect_uri" : REDIRECT_URI
    }

    r = requests.post(endpoint, data=body, auth=(CLIENT_ID,CLIENT_SECRET))
    

    if r.status_code == 200:
        # Get response and set access/refresh tokens
        content = r.json()
        spotify.ACCESS_TOKEN = content['access_token']
        spotify.REFRESH_TOKEN = content['refresh_token']
        
    else:
        errors.badRequest(True)
        

    # TEMP - Testing out web API queries
    print(spotify.getTopArtists())

    return render(request, 'auth.html', {})