import os
from django.http import Http404, HttpResponse
from django.shortcuts import render
from . import spotify_auth, errors, cloud

'''
    ----Views----
'''


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

    # Pass data required for authorization if user wants to login
    CLIENT_ID = os.environ.get('AMPART_CLIENT_ID')
    CLIENT_SECRET = os.environ.get('AMPART_CLIENT_SECRET')
    REDIRECT_URI = "http://127.0.0.1:8000/auth.html"
    SCOPE = "user-library-read user-top-read"

    auth_data = {
        "CLIENT_ID" : CLIENT_ID,
        "CLIENT_SECRET" : CLIENT_SECRET,
        "REDIRECT_URI" : REDIRECT_URI,
        "SCOPE" : SCOPE
    }

    return render(request, 'index.html', auth_data)


# Authorization page
def auth(request):
    
    return render(request, 'auth.html', {})