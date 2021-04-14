from django.http import Http404, HttpResponse
from django.shortcuts import render
from . import spotify_auth, errors

# Views
def index(request):
    # Spotify data
    sp = spotify_auth.getSpotifyObj()
    if(sp != errors.couldNotAuthenticate()):
        print(sp.current_user())


    return render(request, 'index.html', {})