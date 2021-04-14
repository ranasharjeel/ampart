import os
import spotipy
from spotipy import oauth2
from . import errors

CLIENT_ID = os.environ.get('AMPART_CLIENT_ID')
CLIENT_SECRET = os.environ.get('AMPART_CLIENT_SECRET')
REDIRECT_URI = "http://localhost:8888/"
CACHE = ".ampartcache"
SCOPE = "user-library-read user-top-read user-read-currently-playing"



'''
    Attempts to authorize user and getting access token
    Access token will allow access to spotify user data (within scopes)
    Caches the access token, if not already cached
'''
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
        return access_token
        
    else:
        return errors.noAccessToken(True)


'''
    Authorize user and return spotify data access object
'''
def getSpotifyObj():
    # Return spotify obj if authorization is successful
    access_token = attemptAuth()
    if access_token != errors.noAccessToken():
        return spotipy.Spotify(access_token)

    else:
        return errors.couldNotAuthenticate(True)
