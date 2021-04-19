/*
    Hover effect for spotify login button
    changes the spotify logo color depending on the hover
*/
const spotify_login_button = document.getElementById("spotify-login-btn");

spotify_login_button.addEventListener("mouseover", hover);
spotify_login_button.addEventListener("mouseout", unhover);

function hover(){
    var img = document.getElementById("spotify-logo");
    var new_src = img.getAttribute("src").replace("light", "dark");
    img.setAttribute("src", new_src);
}
function unhover(){
    var img = document.getElementById("spotify-logo");
    var new_src = img.getAttribute("src").replace("dark","light");
    img.setAttribute("src", new_src);
}


/*
  ----SPOTIFY AUTHORIZATION----
  Use authorization data from index view to authenticate user
*/

// Spotify login button on click - begins authorization
spotify_login_button.addEventListener("click", spotifyAuth);

// Convert auth data to JSON for easy acces
const auth_data = JSON.parse(spotify_login_button.getAttribute("value"));

// GET request sent here
const SPOTIFY_AUTHORIZE_URL = "https://accounts.spotify.com/authorize";

function spotifyAuth(){
    let request = SPOTIFY_AUTHORIZE_URL;
    request += "?client_id=" + auth_data['CLIENT_ID'];
    request += "&response_type=code";
    request += "&redirect_uri=" + auth_data['REDIRECT_URI'];
    request += "&show_dialog=true";
    request += "&scope=" + auth_data['SCOPE'];
    
    window.open(request);
}