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

    # Get top artist of the user 
    top_artists_list = []
    if(sp != errors.couldNotAuthenticate()):
        top_artists = sp.current_user_top_artists(50).get('items')

        for i in top_artists:
            top_artists_list.append(i['name'])
    
    # Generate word cloud from top artist names
    cloud.generateWordCloud(top_artists_list)

    return render(request, 'index.html', {'top_artists_list' : top_artists_list})


# Playback page
def play(request):
    
    return render(request, 'play.html', {})