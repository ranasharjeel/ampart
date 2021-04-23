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
    Hamburger menu toggle
*/
let toggle = 0;
document.getElementById("ham").addEventListener("click", openMenu);

function openMenu(){
    
    if(toggle==0){
        document.getElementById("mainmenu").style.display = "block";
        document.getElementById("backdrop").style.display = "block"
        var ham = document.getElementById("ham-img");
        var new_src = ham.getAttribute("src").replace("menu","cross");
        ham.setAttribute("src", new_src)
        toggle=1;
    }
    else{
        document.getElementById("mainmenu").style.display = "none";
        document.getElementById("backdrop").style.display = "none";
        var ham = document.getElementById("ham-img");
        var new_src = ham.getAttribute("src").replace("cross","menu");
        ham.setAttribute("src", new_src)
        toggle=0;
    }
}


/* Display error if failed to login */
const error_msg = document.getElementById("login-fail-msg");
const error_code = error_msg.getAttribute("value");

if(error_code!=0){
    error_msg.style.visibility = 'visible';
}
else{
    error_msg.style.visibility = 'hidden';
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
const AUTH_ENDPOINT = "https://accounts.spotify.com/authorize";


// Send request and get auth code
function spotifyAuth(){
    let request = AUTH_ENDPOINT;
    request += "?client_id=" + auth_data['CLIENT_ID'];
    request += "&response_type=code";
    request += "&redirect_uri=" + auth_data['REDIRECT_URI'];
    request += "&show_dialog=true";
    request += "&scope=" + auth_data['SCOPE'];
    
    //window.open(request, "_self");
    location.href = request;
}
