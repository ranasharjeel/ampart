'''
    Custom error messages
'''


# User authentication access token didnt return
def noAccessToken(call_error=False):
    if call_error:
        print("[ERROR] No access token found")
    return 1101


# User authentication failed due to various reasons
def couldNotAuthenticate(call_error=False):
    if call_error:
        print("[ERROR] Could not authorize user")
    return 1102