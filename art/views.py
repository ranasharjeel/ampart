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
    top_tracks_list = []
    if(sp != errors.couldNotAuthenticate()):
        top_tracks = sp.current_user_top_tracks(10).get('items')

        for i in top_tracks:
            top_tracks_list.append(i['name'])
    
    return render(request, 'index.html', {'top_tracks_list' : top_tracks_list})


# Playback page
def play(request):
    
    return render(request, 'play.html', {})