from django.http import Http404, HttpResponse
from django.shortcuts import render
from . import spotify_auth, errors

'''
    ----Views----
'''


# Index page
def index(request):
    # Spotify data
    sp = spotify_auth.getSpotifyObj()

    # Get top tracks of the user 
    top_artists_list = []
    if(sp != errors.couldNotAuthenticate()):
        top_artists = sp.current_user_top_artists(20).get('items')

        for i in top_artists:
            
            top_artists_list.append(i['name'])
    
    return render(request, 'index.html', {'top_artists_list' : top_artists_list})


# Playback page
def play(request):
    
    return render(request, 'play.html', {})