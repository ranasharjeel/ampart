from django.http import Http404, HttpResponse
from django.shortcuts import render
from . import spotify_auth, errors, cloud

'''
    ----Views----
'''


# Index page
def index(request):
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
    cloud.generateWordCloud(top_artists_list, "note", 0)
    #cloud.generateWordCloud(top_genres_list, "note", 0)

    return render(request, 'index.html', {'top_artists_list' : top_artists_list})


# Playback page
def play(request):
    
    return render(request, 'play.html', {})