'''
    Custom error messages
'''

def noAccessToken(call_error=False):
    if call_error:
        print("[ERROR] No access token found")
    return 1101


def couldNotAuthenticate(call_error=False):
    if call_error:
        print("[ERROR] Could not authorize user")

    return 1102