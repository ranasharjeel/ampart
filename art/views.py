import os, json
from django.http import Http404, HttpResponse
from django.shortcuts import render


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

    # base 64 encoded client id/secret
    creds = f"{CLIENT_ID}:{CLIENT_SECRET}"
    creds.encode();


    # Package data to JSON and send to auth template
    # (to get access and refresh tokens + additional tokeninfo)
    token_data = {
        'CODE' : auth_code,
        'REDIRECT_URI' : REDIRECT_URI,
        'ENCODED_CREDS' : creds 
    }
    token_data = json.dumps(token_data)


    return render(request, 'auth.html', {'token_data' : token_data})