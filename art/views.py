import os, json, requests
from django.shortcuts import render, redirect, reverse
from . import errors, spotify, cloud



# Data required for authorization if user wants to login
CLIENT_ID = os.environ.get('AMPART_CLIENT_ID')
CLIENT_SECRET = os.environ.get('AMPART_CLIENT_SECRET')
REDIRECT_URI = "http://127.0.0.1:8000/art/auth"
#REDIRECT_URI = "http://192.168.10.28:8000/art/auth"
SCOPE = "user-library-read user-top-read"


# Index page
def index(request):
    
    error = 0 # No errors logged initially
    # Check for session errors, set and delete if present
    try:
        error = request.session['err']
        del request.session['err']
    
    except:
        pass
    print("ERROR CODE: ", error)
    
    # Package data to JSON and send to index template
    # (to get authorization code on login click)
    auth_data = {
        'CLIENT_ID' : CLIENT_ID,
        'CLIENT_SECRET' : CLIENT_SECRET,
        'REDIRECT_URI' : REDIRECT_URI,
        'SCOPE' : SCOPE
    }
    auth_data = json.dumps(auth_data)


    return render(request, 'index.html', {'auth_data' : auth_data, 'error' : error})


# Authorization page
def auth(request):
    

    auth_code = ""
    
    try:
        # authorization code
        auth_code = request.GET['code'] 
    except:
        request.session['err'] = errors.couldNotAuthenticate()
        return redirect('art:index')


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
        
    else: # failed to get access/refresh tokens
        errors.badRequest(True)
        return redirect('/art/')
        
        


    # Generate and save artists and genres cloud arts
    top_artists = spotify.getTopArtists()
    top_genres = spotify.getTopGenres()

    # Generate word cloud from top artist/genres names
    cloud.generateWordCloud(top_artists, "n", "artists")
    cloud.generateWordCloud(top_genres, "s", "genres")
    


    return render(request, 'auth.html', {'status' : r.status_code})
