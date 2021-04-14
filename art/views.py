from django.http import Http404, HttpResponse
from django.shortcuts import render
from . import spotify_auth

# Views
def index(request):
    sp = spotify_auth.attemptAuth()
    print(sp)
    return render(request, 'index.html', {})