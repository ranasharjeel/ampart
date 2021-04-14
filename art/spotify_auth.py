import spotipy
from spotipy import oauth2
import os

CLIENT_ID = os.environ.get('AMPART_CLIENT_ID')
CLIENT_SECRET = os.environ.get('AMPART_CLIENT_SECRET')
REDIRECT_URI = "http://localhost:8888/"
CACHE = ".ampartcache"
SCOPE = "user-library-read user-top-read"



def attemptAuth():
        
    # Create authorization request
    sp = oauth2.SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE,
        cache_path=CACHE
    )

    access_token = ""

    # Get cached token if it exists
    token_info = sp.get_cached_token()

    # Get access token from cached token
    if token_info:
        print("Cached token exists.")
        access_token = token_info['access_token']

    # Cached token doesn't exist:
    # Get access token and cache it
    else:
        print("No cached token...creating one.")
        code = sp.get_authorization_code()
        token_info = sp.get_access_token(code, as_dict=False)
        access_token = token_info
        

    # Return access token if it's available
    if access_token != "":
        print("Access token available.")
        
        return spotipy.Spotify(access_token)
        
    
    else:
        return "[ERROR] Access token unavailable."
